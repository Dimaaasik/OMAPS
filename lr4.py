import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (8 * np.log(x) + 8) / 5

def df(x):
    return  8/x

def newton_raphson(f, df, x_0, error_tolerance=1.0e-15, max_iterations=500):
    x = x_0
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        dx = -fx / dfx
        x += dx
        if abs(x - x_0) < error_tolerance:
            break
    return x

x_root = newton_raphson(f, df, 2)
print(x_root)


x_vals = np.linspace(0.1, 3, 300)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label='f(x)')
ax.axhline(0.0,color = 'red', linestyle = '--')
plt.plot(x_root, f(x_root), 'ro', label='x_root')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()