import math


def richardson(col1):
    col1 = [item for item in col1]
    n = len(col1)
    for j in range(n-1):
        temp_col = [0]*(n-1-j)
        for i in range(n-1-j):
            power = j+1
            temp_col[i] = (2 ** power * col1[i+1] - col1[i]) / (2**power-1)
        col1[:n-1-j] = temp_col
        print(temp_col)
    return col1[0]


def F1(f, x0, h):
    return (f(x0+h)-f(x0))/h


def f(x):
    return x ** x


x0 = 2
h = 0.5
col1 = [F1(f, x0, h/2 ** i) for i in range(4)]


# col1 = [11.764235376052373, 8.801083645679679, 7.694261146080478, 7.212711027043781]
print(col1)

r = richardson(col1)


def F2(f, x0, h):
    return (f(x0)-f(x0-h))/h


def g(x):
    return math.cos(2**x)


x0 = 1
h = 0.5
# col1 = [F2(f, x0, h/2 ** i) for i in range(4)]
# r = richardson(col1)
