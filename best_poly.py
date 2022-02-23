import matplotlib.pyplot as plt
import numpy as np


def best_poly(x: list[float], y: list[float], k: int) -> list[float]:
    n = len(x)
    if n <= k:
        raise ValueError(
            'O número de pontos deve ser maior que o grau k do polinômio')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k+1):
        somas[n] = sum(xi**n for xi in x)

    A = []
    B = []
    for i in range(k+1):
        row = []
        for j in range(k+1):
            row.append(somas[i+j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x, y)))

    return np.linalg.solve(A, B)


x = [-1.45, 0.854, 2.346]
y = [1.031, 2.147, 1.637]
# n = 10
# x = np.linspace(-2, 2, n)
# y = [2+0.5 * xi + 2.1 * xi ** 2 + np.pi * np.random.random() for xi in x]
k = 2

coeffs = best_poly(x, y, k)

print('coeficientes')
for a in coeffs:
    '{:.10f}'.format(a)
    print(f'{a}')


def p(x, coeffs):
    return coeffs[0] + sum(ci * x ** i for i, ci in enumerate(coeffs[1:], 1))


t = np.linspace(min(x), max(x), 200)
pt = [p(ti, coeffs)for ti in t]

plt.plot(t, pt)
plt.scatter(x, y)

plt.savefig('best_poly.png')
