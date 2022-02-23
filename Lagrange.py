import math


def f(x):
    return (math.sin(x)**4) - (4 * math.sin(x)**2) + (math.cos(x**2)) + (math.exp(1)**-x**2) + 5


x = [-0.449, -0.284, -0.049, 0.171, 0.345,
     0.567, 0.63, 0.841, 1.012, 1.248, 1.464]
y = [0 for i in range(len(x))]

for i in range(len(x)):
    y[i] = f(x[i])


# def lagrange(x, y):

#     equation = ""

#     for i in range(len(x)):
#         num = '*'.join([f'(x{-xi:+})' for k, xi in enumerate(x) if k != i])
#         den = '*'.join([f'({x[i]}{-xi:+})' for k,
#                        xi in enumerate(x) if k != i])
#         equation += f'{y[i]:+}*({num})/({den})'

#     return equation


def lagrange(x, y):

    equation = ""

    for i in range(len(x)):
        den = '*'.join([f'({x[i]}{-xi:+})' for k,
                       xi in enumerate(x) if k != i])
        equation = f'{y[i]:+}/({den})'
        print(equation)

    return equation


if __name__ == '__main__':

    poly = lagrange(x, y)
    print(poly)

    def subs(x):
        return eval(poly)

    values = [-3.548, 1.991, 2.301, 2.826, 3.154, 3.193]
    for i in range(len(values)):
        print(f(values[i]) - subs(values[i]))

    from matplotlib import pyplot as plt
    import numpy as np

    # t = np.linspace(1, 7, 100)

    # plt.plot(t, subs(t))
    # plt.scatter(x, y)
    # plt.savefig("lagrange.png")
