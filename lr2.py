import numpy as np
from scipy import linalg, optimize
import matplotlib.pyplot as plt

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
    iterations = 0
    if right == fin:
        arr = np.linspace(left, right, 100)
        fig, ax = plt.subplots()
        ax.plot(arr, y(arr))
        ax.axhline(0.0, color='red', linestyle='--')
        plt.show(block=None)
    while iterations < 100:
        iterations = iterations + 1
        x = (left + right) / 2
        if(fun(left) > 0 and fun(x) < 0) or (fun(left) < 0 and fun(x) > 0):
            right = x
        else:
            left = x
    print(x)
    return x

fun_bisect(min, fin, y)
fun_bisect(mid, fin, y)

def func(x):
    return x**2 - 1.0



fig, ax = plt.subplots()
ax.plot (x,func(x))
ax.axhline(0.0,color = 'black', linestyle = '--')
plt.show(block=None)

try:
    np.testing.assert_array_almost_equal(fun_bisect(0.0, 3.0, func), optimize.root_scalar(func, bracket=[0.0, 3.0], method="bisect", maxiter=100).root, decimal=7 )
except AssertionError as E:
    print('Hi')
else:
    print("The implementation is correct.")
