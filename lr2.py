import numpy as np
from scipy import linalg, optimize
import matplotlib.pyplot as plt

# x = np.linspace(0.01,5,100)
#
# def f(x):
#     return ( (5 * x) - ( (8 * np.log(x)) ) - 8)
#
#
# fig, ax = plt.subplots()
# ax.plot (x,f(x))
# ax.axhline(0.0,color = 'red', linestyle = '--')
# plt.show(block=None)
#
# def bisection(f, a, b, error_tolerance=1.0e-15, max_iterations=50):
#     iteration = 0
#     condition = True
#     while condition:
#         x = (a + b) / 2
#         if f(a) * f(x) < error_tolerance:
#             b = x
#         else:
#             a = x
#         iteration = iteration + 1
#         condition = iteration < max_iterations
#     return x
#
#
# print(bisection(f, 0.1, 2))
#
#
# def f(x):
#     return x**2 - 1.0
#
# try:
#     np.testing.assert_array_almost_equal(bisection(f, 0, 4.0), optimize.root_scalar(f, bracket=[0, 4.0], method="bisect").root, decimal=7)
# except AssertionError as E:
#     print(E)
# else:
#     print("The implementation is correct.")
#
#
# print('//////////////////////////////////////////////////////////////////////////')
#
# x = np.linspace(0,3,100)
# x[(x>-0.09)&(x<0.08)] = np.nan
#
# def ex2(x):
#     return ((x**3)-(x**2)-1)
# fig, ax = plt.subplots()
# ax.plot (x,f(x))
# ax.axhline(0.0,color = 'red', linestyle = '--')
# plt.show(block=None)
#
# print(bisection(ex2,0.1,2))

x = np.linspace(0.01,5,100)
def y(x):
     return ( (5 * x) - ( (8 * np.log(x)) ) - 8)


fig, ax = plt.subplots()
ax.plot (x,y(x))
ax.axhline(0.0,color = 'red', linestyle = '--')
plt.show(block=None)

min = 0.01
mid = 1
fin = 5

def fun_bisect(left, right, fun, eps=1e-6):
# остановился на том что хочу сделать краствый вывод графика, хз зачем
    if right == fin:
        arr = np.linspace(left, right, 100)
        fig, ax = plt.subplots()
        ax.plot(arr, y(arr))
        ax.axhline(0.0, color='red', linestyle='--')
        plt.show(block=None)
    x = (left + right) / 2

    if fun(x) == 0 or abs(right - left) <= eps:
        print(x)



        return
    elif (fun(left) > 0 and fun(x) < 0) or (fun(left) < 0 and fun(x) > 0):
        return fun_bisect(left, x, fun, eps)
    else:
        return fun_bisect(x, right, fun, eps)


# метод бисекции
fun_bisect(min, fin, y)
fun_bisect(mid, fin, y)