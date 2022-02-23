
def rk4(f, x0: float, y0: float, h: float, n: int):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        m3 = f(x0 + h / 2, y0 + (h / 2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
        # atualizar x0 e y0
        x0 += h
        y0 = yk
        r.append((x0, y0))

    return r


if __name__ == '__main__':

    def f(x, y):
        return (y*(1-x))+x+2

    x0 = 1.07134
    y0 = 2.21151
    r = rk4(f, x0, y0, h=0.18025, n=10)
i = 1
for x, y in r:
    print(f' {i}.phi({x})= {y}')
    i += 1
