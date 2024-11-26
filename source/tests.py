# Name: Matthew Davidson UCID: 301182729
#
import numpy as np
from source.linalg_interp import (gauss_iter_solve, spline_function)

def test_gauss_iter_solve():
    A = np.array([[4, 1,], [2, 3]])
    b = np.array([1, 2])
    expected = np.linalg.solve(A, b)
    x = gauss_iter_solve(A, b)
    exp= np.linalg.solve(A, b)
    assert np.allclose(x, expected), "The Gauss-Seidel method failed"

    
def test_spline_function():
    xd = [0, 1, 2, 3]
    yd = [1, 2, 0, 3]


if __name__ == "__main__":
    test_gauss_iter_solve()
    test_spline_function()
    print("Tests have been passed")