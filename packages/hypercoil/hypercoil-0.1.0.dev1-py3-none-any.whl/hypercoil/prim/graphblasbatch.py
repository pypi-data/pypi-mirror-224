#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
GraphBLAS batching
~~~~~~~~~~~~~~~~~~
Batching transformations and batched operations for GraphBLAS. Currently
this is a hacky proof of concept that only supports a small subset of
operators.
"""
from typing import (
    Any,
    Callable,
    Mapping,
    Optional,
    Tuple,
    Type,
    Union,
)

import graphblas as gb
import numba
import numpy as np
from graphblas import ffi, lib
from graphblas.dtypes import BOOL, INT8, UINT64, lookup_dtype
from graphblas.exceptions import check_status_carg
from graphblas.operator import (
    UNKNOWN_OPCLASS,
    BinaryOp,
    IndexUnaryOp,
    Monoid,
    OpBase,
    ParameterizedUdf,
    SelectOp,
    Semiring,
    TypedOpBase,
    TypedUserBinaryOp,
    TypedUserIndexUnaryOp,
    TypedUserMonoid,
    TypedUserSemiring,
    TypedUserUnaryOp,
    UnaryOp,
)
from graphblas.utils import libget


ffi_new = ffi.new


def batch_type(
    batch_shape: Tuple[int, ...],
    dtype: np.dtype = np.float32
) -> gb.dtypes.DataType:
    NP_Batched = np.dtype(
        ((dtype, batch_shape)),
    )
    dtype = np.dtype(dtype)
    batch_ident = 'x'.join([str(i) for i in batch_shape])
    dtype_ident = f"{dtype.char}{8 * dtype.itemsize}"
    ident = f"{batch_ident}_{dtype_ident}"
    Batched = gb.dtypes.register_new(
        f"Batched_{ident}", NP_Batched
    )

    zeros = np.zeros(batch_shape, dtype=dtype)

    @register_batched("unary", batch_shape, Batched, ident=ident)
    def exp(x):
        return np.exp(x)

    @register_batched("indexunary", batch_shape, gb.dtypes.BOOL, ident=ident)
    def allle(x, y, i, j):
        return (x <= y).all()

    @register_batched(
        "binary", batch_shape, Batched, ident=ident,
        monoid=True, identity=zeros
    )
    def plus(x, y):
        return x + y

    @register_batched(
        "binary", batch_shape, Batched, ident=ident,
        monoid=True, identity=zeros
    )
    def times(x, y):
        return x * y

    BatchedSemiring.register_new(
        f"plus_times_batched_{ident}", plus, times.binaryop)

    return Batched


def register_batched(
    opclass: str,
    batch_shape: Tuple[int, ...],
    return_type: gb.dtypes.DataType,
    nopython: bool = True,
    monoid: bool = False,
    fname: Optional[str] = None,
    ident: Optional[str] = None,
    identity: Optional[Any] = None,
) -> Callable:
    opclasses = {
        "unary": (BatchedUnaryOp, batch_unop),
        "binary": (BatchedBinaryOp, batch_binop),
        "indexunary": (BatchedIndexUnaryOp, batch_iuop),
    }
    opclass, batching_fn = opclasses[opclass]

    def register(f: Callable) -> Callable:
        fname_ = fname or f.__name__
        ident_ = ident or 'x'.join(batch_shape)

        f_batched = batching_fn(batch_shape, nopython=nopython)(f)
        f_batched = opclass.register_new(
            f'{fname_}_batched_{ident_}', f_batched, is_udt=True)
        f_batched.set_return_type(return_type)

        if monoid:
            return BatchedMonoid.register_new(
                f'{fname_}_batched_{ident_}',
                f_batched,
                identity=identity,
            )

        return f_batched

    return register


def batch_unop(
    batch_shape: Tuple[int, ...],
    nopython: bool = True,
) -> Callable:

    def batch_transform(f: Callable) -> Callable:
        f_compiled = numba.jit(f, nopython=nopython)

        def f_batched(
            z: numba.types.CPointer,
            x: numba.types.CPointer,
        ) -> numba.types.CPointer:
            x_ = numba.carray(x, batch_shape)
            z_ = numba.carray(z, batch_shape)
            n, = batch_shape
            for i in range(n):
                z_[i] = f_compiled(x_[i])
            return z_
        return f_batched

    return batch_transform


def batch_iuop(
    batch_shape: Tuple[int, ...],
    nopython: bool = True,
) -> Callable:

    def batch_transform(f: Callable) -> Callable:
        f_compiled = numba.jit(f, nopython=nopython)

        def f_batched(
            z: numba.types.CPointer,
            x: numba.types.CPointer,
            i: numba.types.uint64,
            j: numba.types.uint64,
            y: numba.types.Any,
        ) -> numba.types.Any:
            x_ = numba.carray(x, batch_shape)
            y_ = numba.carray(y, 1) # thunk
            z_ = numba.carray(z, 1)
            z_[0] = f_compiled(x_, y_, i, j)
            return z_[0]
        return f_batched

    return batch_transform


def batch_binop(
    batch_shape: Tuple[int, ...],
    nopython: bool = True,
) -> Callable:

    def batch_transform(f: Callable) -> Callable:
        f_compiled = numba.jit(f, nopython=nopython)

        def f_batched(
            z: numba.types.CPointer,
            x: numba.types.CPointer,
            y: numba.types.CPointer,
        ) -> numba.types.CPointer:
            x_ = numba.carray(x, batch_shape)
            y_ = numba.carray(y, batch_shape)
            z_ = numba.carray(z, batch_shape)
            n, = batch_shape
            for i in range(n):
                z_[i] = f_compiled(x_[i], y_[i])
            return z_
        return f_batched
    
    return batch_transform


def _get_udt_wrapper_batched(
    numba_func: Callable,
    return_type: gb.dtypes.DataType,
    dtype: gb.dtypes.DataType,
    dtype2: Optional[gb.dtypes.DataType] = None,
    *,
    include_indexes: bool = False,
) -> Tuple[Callable, Type]:
    ztype = INT8 if return_type == BOOL else return_type
    xtype = INT8 if dtype == BOOL else dtype
    nt = numba.types
    if include_indexes:
        ytype = INT8 if dtype2 == BOOL else dtype2
        wrapper_args = [
            nt.CPointer(ztype.numba_type),
            nt.CPointer(xtype.numba_type.dtype),
            UINT64.numba_type,
            UINT64.numba_type,
            nt.CPointer(ytype.numba_type.dtype),
        ]
    else:
        wrapper_args = [
            nt.CPointer(ztype.numba_type.dtype),
            nt.CPointer(xtype.numba_type.dtype)
        ]
        if dtype2 is not None:
            ytype = INT8 if dtype2 == BOOL else dtype2
            wrapper_args.append(nt.CPointer(ytype.numba_type.dtype))
    wrapper_sig = nt.void(*wrapper_args)

    BL = BR = yarg = yname = rcidx = ""

    if dtype2 is not None:
        yarg = ", y_ptr"
        yname = ", y_ptr"

    if include_indexes:
        rcidx = ", row, col"

    d = {"numba": numba, "numba_func": numba_func}
    text = (
        f"def wrapper(z_ptr, x_ptr{rcidx}{yarg}):\n"
        f"    {BL}numba_func(z_ptr, x_ptr{rcidx}{yname}){BR}\n"
    )
    exec(text, d)
    return d["wrapper"], wrapper_sig


def find_opclass_subclass_compat(gb_op):
    # We have to patch over the `find_opclass` function from GraphBLAS because
    # the original function returns the subclass name, which results in
    # incorrect branching logic when a method like `Matrix.apply` is called.
    if isinstance(gb_op, OpBase):
        if isinstance(gb_op, UnaryOp):
            opclass = 'UnaryOp'
        elif isinstance(gb_op, SelectOp):
            opclass = 'SelectOp'
        elif isinstance(gb_op, IndexUnaryOp):
            opclass = 'IndexUnaryOp'
        elif isinstance(gb_op, Monoid):
            opclass = 'Monoid'
        elif isinstance(gb_op, BinaryOp):
            opclass = 'BinaryOp'
        elif isinstance(gb_op, Semiring):
            opclass = 'Semiring'
        else:
            opclass = type(gb_op).__name__
    elif isinstance(gb_op, TypedOpBase):
        opclass = gb_op.opclass
    elif isinstance(gb_op, ParameterizedUdf):
        gb_op = gb_op()  # Use default parameters of parameterized UDFs
        gb_op, opclass = find_opclass_subclass_compat(gb_op)
    else:
        opclass = UNKNOWN_OPCLASS
    return gb_op, opclass
gb.operator.find_opclass = find_opclass_subclass_compat


class ExplicitReturnTypeMixin:
    def set_return_type(self, dtype: gb.dtypes.DataType) -> None:
        self._return_type = dtype


class BatchedUnaryOp(UnaryOp, ExplicitReturnTypeMixin):
    def _compile_udt(
        self,
        dtype: gb.dtypes.DataType,
        dtype2: Optional[gb.dtypes.DataType] = None,
    ) -> TypedUserUnaryOp:

        if dtype in self._udt_types:
            return self._udt_ops[dtype]

        # This differs from the python-graphblas implementation in that we
        # require the user to specify the return type explicitly. This is
        # because the numba function will fail to compile, since we've
        # coded it to accept only pointer arguments and to require the
        # output array pointer as the first argument.
        # numba_func = self._numba_func
        # sig = (numba.types.CPointer(dtype.numba_type.dtype),)
        # numba_func.compile(sig)
        # ret_type = lookup_dtype(numba_func.overloads[sig].signature.return_type)
        numba_func = self._numba_func
        ret_type = lookup_dtype(self._return_type)

        unary_wrapper, wrapper_sig = _get_udt_wrapper_batched(
            numba_func, ret_type, dtype
        )
        unary_wrapper = numba.cfunc(wrapper_sig, nopython=True)(unary_wrapper)
        new_unary = ffi_new("GrB_UnaryOp*")
        check_status_carg(
            lib.GrB_UnaryOp_new(
                new_unary, unary_wrapper.cffi, ret_type._carg, dtype._carg),
            "UnaryOp",
            new_unary,
        )
        op = TypedUserUnaryOp(self, self.name, dtype, ret_type, new_unary[0])
        self._udt_types[dtype] = ret_type
        self._udt_ops[dtype] = op
        return op


class BatchedIndexUnaryOp(IndexUnaryOp, ExplicitReturnTypeMixin):
    def _compile_udt(
        self,
        dtype: gb.dtypes.DataType,
        dtype2: Optional[gb.dtypes.DataType] = None,
    ) -> TypedUserBinaryOp:
        if dtype2 is None:  # pragma: no cover
            #dtype2 = gb.dtypes.lookup_dtype(dtype.numba_type.dtype)
            dtype2 = dtype
        dtypes = (dtype, dtype2)
        if dtypes in self._udt_types:
            return self._udt_ops[dtypes]

        numba_func = self._numba_func
        ret_type = lookup_dtype(self._return_type)
        indexunary_wrapper, wrapper_sig = _get_udt_wrapper_batched(
            numba_func, ret_type, dtype, dtype2, include_indexes=True
        )

        indexunary_wrapper = numba.cfunc(wrapper_sig, nopython=True)(indexunary_wrapper)
        new_indexunary = ffi_new("GrB_IndexUnaryOp*")
        check_status_carg(
            lib.GrB_IndexUnaryOp_new(
                new_indexunary,
                indexunary_wrapper.cffi,
                ret_type._carg,
                dtype._carg,
                dtype2._carg,
            ),
            "IndexUnaryOp",
            new_indexunary,
        )
        op = TypedUserIndexUnaryOp(
            self,
            self.name,
            dtype,
            ret_type,
            new_indexunary[0],
            dtype2=dtype2,
        )
        self._udt_types[dtypes] = ret_type
        self._udt_ops[dtypes] = op
        return op


class BatchedBinaryOp(BinaryOp, ExplicitReturnTypeMixin):
    def _compile_udt(
        self,
        dtype: gb.dtypes.DataType,
        dtype2: Optional[gb.dtypes.DataType] = None,
    ) -> TypedUserBinaryOp:

        if dtype2 is None:
            dtype2 = dtype
        dtypes = (dtype, dtype2)
        if dtypes in self._udt_types:
            return self._udt_ops[dtypes]

        numba_func = self._numba_func
        ret_type = lookup_dtype(self._return_type)
        binary_wrapper, wrapper_sig = _get_udt_wrapper_batched(
            numba_func, ret_type, dtype, dtype2)
        binary_wrapper = numba.cfunc(wrapper_sig, nopython=True)(binary_wrapper)
        new_binary = ffi_new("GrB_BinaryOp*")
        check_status_carg(
            lib.GrB_BinaryOp_new(
                new_binary,
                binary_wrapper.cffi,
                ret_type._carg,
                dtype._carg,
                dtype2._carg,
            ),
            "BinaryOp",
            new_binary,
        )
        op = TypedUserBinaryOp(
            self,
            self.name,
            dtype,
            ret_type,
            new_binary[0],
            dtype2=dtype2,
        )
        self._udt_types[dtypes] = ret_type
        self._udt_ops[dtypes] = op
        return op


class BatchedMonoid(Monoid):
    @classmethod
    def _build(cls, name, binaryop, identity, *, anonymous=False):
        # python-graphblas requires this be strictly a BinaryOp, but we
        # allow it to be any subclass, such as a BatchedBinaryOp.
        if not isinstance(binaryop, BinaryOp):
            raise TypeError(f"binaryop must be a BinaryOp, not {type(binaryop)}")
        if name is None:
            name = binaryop.name
        new_type_obj = cls(name, binaryop, identity, anonymous=anonymous)
        if not binaryop._is_udt:
            if not isinstance(identity, Mapping):
                identities = dict.fromkeys(binaryop.types, identity)
                explicit_identities = False
            else:
                identities = {lookup_dtype(key): val for key, val in identity.items()}
                explicit_identities = True
            for type_, identity in identities.items():
                ret_type = binaryop[type_].return_type
                # If there is a domain mismatch, then DomainMismatch will be raised
                # below if identities were explicitly given.
                if type_ != ret_type and not explicit_identities:
                    continue
                new_monoid = ffi_new("GrB_Monoid*")
                func = libget(f"GrB_Monoid_new_{type_.name}")
                zcast = ffi.cast(type_.c_type, identity)
                check_status_carg(
                    func(new_monoid, binaryop[type_].gb_obj, zcast), "Monoid", new_monoid[0]
                )
                op = TypedUserMonoid(
                    new_type_obj,
                    name,
                    type_,
                    ret_type,
                    new_monoid[0],
                    binaryop[type_],
                    identity,
                )
                new_type_obj._add(op)
        return new_type_obj


class BatchedSemiring(Semiring):
    @classmethod
    def _build(cls, name, monoid, binaryop, *, anonymous=False):
        if not isinstance(monoid, Monoid):
            raise TypeError(f"monoid must be a Monoid, not {type(monoid)}")
        if not isinstance(binaryop, BinaryOp):
            raise TypeError(f"binaryop must be a BinaryOp, not {type(binaryop)}")
        if name is None:
            name = f"{monoid.name}_{binaryop.name}".replace(".", "_")
        new_type_obj = cls(name, monoid, binaryop, anonymous=anonymous)
        if binaryop._is_udt:
            return new_type_obj
        for binary_in, binary_func in binaryop._typed_ops.items():
            binary_out = binary_func.return_type
            # Unfortunately, we can't have user-defined monoids over bools yet
            # because numba can't compile correctly.
            if (
                binary_out not in monoid.types
                # Are all coercions bad, or just to bool?
                or monoid.coercions.get(binary_out, binary_out) != binary_out
            ):
                continue
            new_semiring = ffi_new("GrB_Semiring*")
            check_status_carg(
                lib.GrB_Semiring_new(new_semiring, monoid[binary_out].gb_obj, binary_func.gb_obj),
                "Semiring",
                new_semiring,
            )
            ret_type = monoid[binary_out].return_type
            op = TypedUserSemiring(
                new_type_obj,
                name,
                binary_in,
                ret_type,
                new_semiring[0],
                monoid[binary_out],
                binary_func,
            )
            new_type_obj._add(op)
        return new_type_obj


import time


gb.ss.config['burble'] = True
n_iter = 10
batch_size = 100
batch_type((batch_size,))


N = gb.Matrix.from_values(
    rows=(0, 3),
    columns=(0, 1),
    values=np.random.rand(2, batch_size).astype(np.float32),
)

def random_rcv(size, n_vals, batch_size):
    idx = np.random.choice(size ** 2, n_vals, replace=False)
    idx = np.sort(idx)
    rows = idx // size
    cols = idx % size
    vals = np.random.rand(n_vals, batch_size).astype(np.float32)
    return rows, cols, vals

size = 10000
n_vals = 10000
rows, cols, vals = random_rcv(size, n_vals, batch_size)
N = gb.Matrix.from_values(
    rows=rows.tolist(),
    columns=cols.tolist(),
    values=vals,
    nrows=size,
    ncols=size,
)
M = gb.Matrix.from_values(
    rows=rows.tolist(),
    columns=cols.tolist(),
    values=vals,
    nrows=size,
    ncols=size,
)
o = gb.unary.exp_batched_100_f32(N).new()
o = gb.binary.plus_batched_100_f32(N | M).new()
o = gb.indexunary.allle_batched_100_f32(N, np.random.rand(batch_size)).new()
o = gb.semiring.plus_times_batched_100_f32(M @ N).new()

rows_X, cols_X, vals_X = random_rcv(size, n_vals, batch_size)
rows_Y, cols_Y, vals_Y = random_rcv(size, n_vals, batch_size)
X = gb.Matrix.from_values(
    rows=rows_X.tolist(),
    columns=cols_X.tolist(),
    values=vals_X,
    nrows=size,
    ncols=size,
)
Y = gb.Matrix.from_values(
    rows=rows_Y.tolist(),
    columns=cols_Y.tolist(),
    values=vals_Y,
    nrows=size,
    ncols=size,
)

start_batched_unop = time.time()
o = gb.unary.exp_batched_100_f32(X).new()
end_batched_unop = time.time()

start_batched_binop = time.time()
o = gb.binary.plus_batched_100_f32(X | Y).new()
end_batched_binop = time.time()

start_batched_matmul = time.time()
o = gb.semiring.plus_times_batched_100_f32(X @ Y).new()
end_batched_matmul = time.time()

Xs = [
    gb.Matrix.from_values(
        rows=rows_X,
        columns=cols_X,
        values=vals_X[..., i],
        nrows=size,
        ncols=size,
    )
    for i in range(batch_size)
]
Ys = [
    gb.Matrix.from_values(
        rows=rows_Y,
        columns=cols_Y,
        values=vals_Y[..., i],
        nrows=size,
        ncols=size,
    )
    for i in range(batch_size)
]
start_loop_unop = time.time()
os = [gb.unary.exp(x).new() for x in Xs]
end_loop_unop = time.time()

start_loop_binop = time.time()
os = [gb.binary.plus(x | y).new() for x, y in zip(Xs, Ys)]
end_loop_binop = time.time()

start_loop_matmul = time.time()
os = [gb.semiring.plus_times(x @ y).new() for x, y in zip(Xs, Ys)]
end_loop_matmul = time.time()

print(end_batched_unop - start_batched_unop)
print(end_loop_unop - start_loop_unop)

print(end_batched_binop - start_batched_binop)
print(end_loop_binop - start_loop_binop)

print(end_batched_matmul - start_batched_matmul)
print(end_loop_matmul - start_loop_matmul)
