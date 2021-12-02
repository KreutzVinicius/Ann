import math


def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b-a)/n
    somaOdd, somaEven = 0, 0
    for k in range(1, n, 2):
        somaOdd += f(a + k * h)
    for k in range(2, n, 2):
        somaEven += f(a + k * h)
    return (h/3) * (f(a) + 4*somaOdd + 2*somaEven + f(b))


def f(x):
    return math.exp(-x**2)


a, b = 0, 1
n = 1000

i1 = simps(f, a, b, n)
print(i1)
