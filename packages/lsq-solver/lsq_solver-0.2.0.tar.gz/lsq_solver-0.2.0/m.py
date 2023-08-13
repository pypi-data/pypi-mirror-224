import numpy as np
from lsq_solver.auto_diff import diff_2point, diff_3point, diff_auto
from functools import partial
from num_dual import jacobian, gradient
from time import perf_counter


# def ff(x, y):
#     r0 = x[0]+2*x[1]+3*x[2]+y[0]-y[0]
#     r1 = x[1]*x[1]+x[2]+y[0]-y[0]
#     r2 = y[0]+x[0]-x[0]
#     return np.array([r0, r1, r2])

#     # pass
# a0 = np.array([1.0, 2, 3])
# a1 = np.array([1.0])
# print(diff_a(ff, a0, a1))
# par = partial(ff, y=a1)
# print(jacobian(par, a0))

# x = np.array([1.0, 2.0, 3.0])
# s = perf_counter()
# for _ in range(10000):
#     print(diff_auto(ff, x))
    # diff_2point((2, 3), ff, x)
#     diff_3point((2, 3), ff, x)
# print(perf_counter() - s)