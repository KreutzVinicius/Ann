def heun(f, x0, y0, h, n):
    r = []
    for _ in range(10):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h * (m1 + m2) / 2
        # atualizando valores
        x0 += h
        y0 = y1
        r.append((x0, y0))
    return r


if __name__ == '__main__':
    # exemplo y´=1+xy, y(1)=2

    def f(x, y):
        return (y*(2-x))+x+1
    x0 = 0.43323
    y0 = 2.96082

    r = heun(f, x0, y0, h=0.13527, n=10)

i = 1
for x, y in r:
    print(f'x_{i}= {x}\ny_{i}= {y}\n')
    i += 1
