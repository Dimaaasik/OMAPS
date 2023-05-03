import numpy as np
from matplotlib import pyplot as plt

iterations = 100
a = 0.1
b = 5
x = np.linspace(a, b)
x_k = (a+b)/2

def f(x):
    return (8 * np.log(x) + 8) / 5

def g(x):
    return x - 0.1*f(x)

plt.figure(figsize=(8,8))
plt.title('Метод простої ітерації')
plt.grid(True)
plt.plot(x, x, 'g')
plt.plot(x, g(x), 'r')


def fixed_point(iterations,eps,x_k):
    for k in range(iterations):

        g_x_k = g(x_k)
        if abs(g_x_k - x_k) < eps:
            return g_x_k
        else:
            plt.plot([x_k, x_k], [x_k, g(x_k)], 'b')
            x_k_plus_1 = g(x_k)
            plt.plot([x_k, g(x_k)], [x_k_plus_1, x_k_plus_1], 'b')
            x_k = x_k_plus_1
            print(f"In {k+1} iteration x = {x_k_plus_1}")


fixed_point(100, 0.0001,x_k)
plt.show()