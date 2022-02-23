from gettext import lngettext
import numpy as np
import random
import math


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p


def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        # para construir a matriz A
        A.append([0]*(n))
        for j in range(n):
            A[i][j] = xs[j] ** i
        # para construir a matriz B
        potencias = [k+1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i-ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)

    soma = 0
    for c, x in zip(cs, xs):
        soma += c * f(x)
    return soma


if __name__ == '__main__':

    def f(x):

        return math.cos(math.exp(1)**-x**2)+math.sin((x**2)/2)

    x0 = 0.92475
    ordem = 2

    num_pontos = 8
    # a = x0-0.25
    # b = x0+0.25
    # xs = [a+(b-a)*random.random()for _ in range(num_pontos)]
    # xs.sort()
    xs = [-0.24744322560350218, -0.2566232288681629, -
          0.25719743733473166, -0.25723254442903, -0.25723472203100073]
    r = finite_diffs(xs, ordem, x0, f)
    print(f'aproximacao para a derivada {ordem} de f no ponto {x0} =', r)
