import matplotlib.pyplot as plt
import numpy as np


def best_line(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi*yi for xi, yi in zip(x, y))

    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)


x = [0.403, 0.991, 1.756, 2.445, 3.525, 4.331, 5.348, 5.657, 6.359]
y = [4.387, 4.804, 4.88, 4.442, 3.212, 2.447, 2.242, 2.347, 2.728]
# x = np.linspace(-5, 5, 20)
# y = [-1 + 1.5 * xi + 1.25*np.random.random() for xi in x]

a0, a1 = best_line(x, y)
print(f'{a0=} e {a1=}')


def p(x, a0, a1):
    return a0+a1*x


t = np.linspace(min(x), max(x), 200)
pt = [p(ti, a0, a1)for ti in t]

plt.plot(t, pt)
plt.scatter(x, y)

plt.savefig('best_line.png')
