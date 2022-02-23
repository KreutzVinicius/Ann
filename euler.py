# metodo do ponto medio de Euler

# pvi y'= x+y , y(0)=1
# sol y(x) = 2 *exp(x)- x - 1

def euler(f, x0: float, y0: float, h: float, n: int):
    xs, ys = [], []
    for k in range(n):
        x = x0 + k * h
        y = y0 + h * f(x, y0)
        xs.append(x+h)
        ys.append(y)
        y0 = y
    return xs, ys


if __name__ == '__main__':
    def f(x, y):
        return (y*(1-x))+x+2

    x0 = 1.10529
    y0 = 1.57733
    h = 0.14802
    n = 10

    resp = euler(f, x0, y0, h, n)

    i = 1
    for x, y in zip(*resp):
        print(f'x_{i}= {x}\ny_{i}= {y}\n')
        i += 1
