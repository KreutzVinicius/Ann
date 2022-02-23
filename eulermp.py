# metodo do ponto medio de Euler

# pvi y'= x+y , y(0)=1
# sol y(x) = 2 *exp(x)- x - 1

def eulermp(f, x0, y0, h, n):
    for k in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0+h*m1/2)
        y1 = y0 + h*m2
        # atualizar
        x0 += h
        y0 = y1
        yield x0, y0


if __name__ == '__main__':
    def f(x, y):
        return (y*(2-x))+x+1

    x0 = 1.81783
    y0 = 1.17566
    h = 0.14514
    n = 10

    resp = eulermp(f, x0, y0, h, n)

    for i, value in enumerate(resp, 1):
        xi, yi = value
        print(f'x_{i}= {xi}\ny_{i}= {yi}\n')
