# spline cubico natural
import numpy as np
import math
from matplotlib import pyplot as plt
# (x1,y1), (x2, y2), (x3,y3)....


def spline(x, y):
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n-1)}

    A = [[1] + [0] * (n-1)]
    for i in range(1, n-1):
        row = [0]*n
        row[i-1] = h[i-1]
        row[i] = 2*(h[i-1]+h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n-1) + [1])

    B = [0]
    for k in range(1, n-1):
        row = 3 * (a[k+1] - a[k])/h[k]-3*(a[k]-a[k-1])/h[k-1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))

    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])

    s = {}
    for k in range(n-1):
        eq = f'{a[k]} {b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x-{x[k]})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]}

    return s


def f(x):
    return math.cos(x)**3 + 2*(math.cos(x)**2)+1


x = [0.277, 0.448, 0.802, 0.94, 1.246, 1.441,
     1.657, 1.732, 1.993, 2.222, 2.513, 2.663, 2.857]
y = [1.856, 1.522, 1.397, 1.885, 1.469, 1.544,
     1.146, 0.951, 0.741, 0.713, 1.122, 0.986, 1.191]


# y = [0 for i in range(len(x))]

# for i in range(len(x)):
#     y[i] = f(x[i])

eqs = spline(x, y)
print(eqs)


# for key, value, in eqs.items():
#     def p(x):
#         return eval(value['eq'])
#     t = np.linspace(*value['domain'], 100)
#     plt.plot(t, p(t), label=f'$S_{key}(x)$')


# plt.scatter(x, y)
# plt.legend()
# plt.savefig('spline.png')
