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


# def F1(f, x0, h):
    # return (f(x0+h)-f(x0))/h


# def f(x):
    # return math.cos(math.exp(1)**-x**2)+math.sin((x**2)/2)


x0 = 1.37601
# h = 1
col1 = [-0.09022436887893881, -0.10833062200062216, -
        0.11267802255173365, -0.11375150707090143]
print(col1)

r = richardson(col1)
