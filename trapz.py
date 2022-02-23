import math


def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.exp(1)**-x**2


a = 0.051
b = 4.843
n = 21


r = trapz(f, a, b, n)

print(r)
