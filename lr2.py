import numpy as np
from scipy import linalg, optimize
import matplotlib.pyplot as plt

x = np.linspace(0.01,5,100)
def y(x):
     return  (8 * np.log(x) + 8) / 5


fig, ax = plt.subplots()
ax.plot (x,y(x))
ax.axhline(0.0,color = 'red', linestyle = '--')
plt.show(block=None)

min = 0.01
fin = 5
mid = (min+fin)/2
def fun_bisect(left, right, fun, eps=0.0001, iteration = 0):
    x = (left + right) / 2
    if(iteration > 150):
        return 'Функція не сходиться'
    if fun(x) == 0 or abs(right - left) <= eps:
        print(f"In {iteration + 1} iteration x = {x}")
        print(x)
        return x
    elif (fun(left) > 0 and fun(x) < 0) or (fun(left) < 0 and fun(x) > 0):
        iteration = iteration + 1
        print(f"In {iteration} iteration x = {x}")
        return fun_bisect(left, x, fun, eps, iteration)
    else:
        iteration = iteration + 1
        print(f"In {iteration} iteration x = {x}")
        return fun_bisect(x, right, fun, eps, iteration)


fun_bisect(min, mid, y)

def func(x):
    return x**2 - 1.0



fig, ax = plt.subplots()
ax.plot (x,func(x))
ax.axhline(0.0,color = 'black', linestyle = '--')
plt.show(block=None)

try:
    np.testing.assert_array_almost_equal(fun_bisect(0.0, 3.0, func), optimize.root_scalar(func, bracket=[0.0, 3.0], method="bisect", maxiter=100).root, decimal=7 )
except AssertionError as E:
    print('zero not found')
else:
    print("The implementation is correct.")
