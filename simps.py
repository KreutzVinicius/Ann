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


a, b = 0.082, 4.64

x = [0.082, 0.309, 0.536, 0.715, 0.894, 0.9965, 1.099, 1.3085, 1.518, 2.0555, 2.593,
     2.653, 2.713, 2.7735, 2.834, 2.862, 2.89, 3.009, 3.128, 3.4645, 3.801, 4.2205, 4.64]
y = [1.488, 2.278, 2.841, 2.997, 2.94, 2.845, 2.726, 2.46, 2.23, 2.003, 2.344,
     2.414, 2.487, 2.563, 2.641, 2.677, 2.712, 2.851, 2.956, 2.84, 1.898, 1.024, 2.634]

n = len(x)

i1 = simps(f, a, b, n)
print(i1)
