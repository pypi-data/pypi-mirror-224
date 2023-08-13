#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
GraphBLAS primitives
~~~~~~~~~~~~~~~~~~~~
Primitive operations with a backend based on GraphBLAS. Currently minimal
functionality is implemented, but the goal is to provide a full suite of
differentiable operations on semirings, etc.
"""
from typing import Callable, Tuple, Union

import jax
import jax.numpy as jnp
from jax import core
from jax.experimental import host_callback
import graphblas as gb
import numpy as np


def graphblas_call_impl(
    fn: Callable,
    *pparams,
    result_shape: Union[Tuple[int, ...], Tuple[Tuple[int, ...], ...]],
    result_dtype: Union[np.dtype, Tuple[np.dtype, ...]],
    **params,
):
    return host_callback.call(
        fn,
        pparams,
        result_shape=result_shape,
    )


def _abstract_shell(out_shapes, out_dtypes):
    return tuple(
        core.ShapedArray(shape, dtype)
        for shape, dtype in zip(out_shapes, out_dtypes)
    )


def graphblas_call_abstract_eval(
    fn: Callable,
    *pparams,
    result_shape: Union[Tuple[int, ...], Tuple[Tuple[int, ...], ...]],
    result_dtype: Union[np.dtype, Tuple[np.dtype, ...]],
    **params,
):
    return _abstract_shell(result_shape, result_dtype)


graphblas_p = core.Primitive('graphblas')
graphblas_p.def_impl(graphblas_call_impl)
graphblas_p.def_abstract_eval(graphblas_call_abstract_eval)




import jax
import jax.numpy as jnp
from jax.experimental import sparse
import graphblas as gb

from hypercoil.functional.sparse import random_sparse


class CCOO(sparse.BCOO):
    """
    A batched sparse matrix in batch-common coordinate format.

    Parameters
    ----------
    data : array_like
        An array of shape ``(*batch_dims, nnz)`` containing the non-zero
        values of the matrix.
    indices : array_like
        An array of shape ``(nnz, n_sparse)`` or ``(n_rows, nnz, 1)``
        containing the indices of the non-zero values of the matrix. Indices
        are shared across batch dimensions.
    shape : tuple of int
        The shape of the matrix.
    """
    pass


def bcoo_to_graphblas(x):
    if x.n_dense > 0:
        raise NotImplementedError(
            'GraphBLAS does not support matrices with trailing '
            'dense dimensions')
    if x.n_sparse > 2:
        raise NotImplementedError(
            'GraphBLAS does not support matrices with more than '
            'two sparse dimensions')
    elif x.n_sparse == 2:
        row_idx = x.indices[..., 0]
        col_idx = x.indices[..., 1]
        if x.n_batch == 0:
            return gb.Matrix.from_values(
                row_idx,
                col_idx,
                x.data,
                nrows=x.shape[-2],
                ncols=x.shape[-1],
            )
    else:
        row_idx = np.arange(x.data.shape[-2])
        col_idx = x.indices


idx = jnp.array([[0, 0, 1, 2], [2, 3, 0, 0]])
data = jnp.array([1, 2, 3, 4], dtype=jnp.float32)
shape = (4, 4)
x = sparse.BCOO((data, idx.T), shape=shape)


mask = np.random.rand(4, 4) > 0.5
data = np.random.randn(2, 2, 4, 4) * mask
x = sparse.BCOO.fromdense(data)
