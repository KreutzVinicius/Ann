def ralston(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (3/4) * h, y0 + (3/4*h*m1))
        yk = y0 + h * (m1 + 2 * m2) / 3
        # atualizando valores
        x0 += h
        y0 = yk
        r.append((x0, y0))
    return r


if __name__ == '__main__':
    # exemplo y´=1+xy, y(1)=2

    def f(x, y):
        return (y*(2-x))+x+1

    x0 = 1.34093
    y0 = 1.94211

    r = ralston(f, x0, y0, h=0.17124, n=10)

    i = 1
for x, y in r:
    print(f'x_{i}= {x}\ny_{i}= {y}\n')
    i += 1
