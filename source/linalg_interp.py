# Name: Matthew Davidson UCID: 30182729
# Contains two functions, first function solves Ax=b using the Guass-Seidel/Jacobi method.
#
# Import numpy and CubicSpline
import numpy as np
from scipy.interpolate import CubicSplin


# A: Coefficient Matrix
# b: Right hand vector
# x0: Initial Guess
# tol: Covergence tolerance
# alg: Algorithm choice = seidel

def gauss_iter_solve(A, b, x0=None, tol=1e-8, alg='seidel')
    # Convert "A" and "b" to arrays, "n" = # of rows
    A = np.array(A)
    n = A.shape [0]
    b = np.array(b)
    alg = alg.strip().lower()
    iter_max = 10000
    #
    if x0 is None:
        x = np.zero_like(b)
    else:
        x = np.array(x0).copy()
    #
    for iteration in range(iter_max):
        x_new = np.copy(x)

        for i in range(n):
            if alg == 'seidel':
                sum_1 = np.dot(A[i,:i], x_new[:i])
                sum_2 = np.dot(A[i, i+1:], x_new[i+1:])
            elif alg == 'jacobi':
                sum_1 = np.dot(A[i,:i], x[:i])
                sum_2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - (sum_1) - (sum_2)) / A[i, i]
    #
    #
    #
        x = x_new

def spline_function(xd, yd, order=3):
    if len(xd) != len(yd):

    if len(np.unique(xd)) != len(xd):

    if not np.all(np.diff(xd) > 0):

    if order not in [1, 2, 3]:

    if order == 1:
        return lambda x: np.interp(x, xd, yd)
    elif order == 2:
        return CubicSpline(xd, yd, bc_type="natural")
    elif order == 3:
        return CubicSpline(xd, yd)

    def spline(x):
        if np.any(x < xd[0]) or np.any(x > xd[-1]):

        return spline