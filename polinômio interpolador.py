import numpy as np
import math


def f(x: float) -> float:
    return math.pow(math.cos(x), 3) + 2*math.pow(math.cos(x), 2) + 1


x = [-2.725, -1.903, -1.146, -0.477, -0.084,
     0.867, 1.525, 2.137, 2.771, 3.569, 4.193]
# y = [2.1855222251295, 2.9099943786033, 3.0049069866832, 1.3125940405738, 0.0874021041426, 0.861418054178]


A = [[0 for i in range(len(x))] for j in range(len(x))]
B = [0 for i in range(len(x))]

for j in range(len(x)):
    for i in range(len(x)):
        A[j][i] = x[j] ** i

for i in range(len(x)):
    B[i] = f(x[i])

np.set_printoptions(precision=7)
A = np.array(A, dtype='float')
B = np.array(B, dtype='float')
C = np.linalg.solve(A, B)

np.set_printoptions(formatter={'float': '{: 0.7f}'.format})
print(C)
