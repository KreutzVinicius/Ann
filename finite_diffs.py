import numpy as np
import random


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

        return x**x

    x0 = 2
    ordem = 1

    # numPontos > ordem    sempre
    # lista de cordenadas x pra contruir a formula
    numPontos = 5
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [a + (b-a) * random.random() for _ in range(numPontos)]
    xs.sort()

    r = finite_diffs(xs, ordem, x0, f)
    print(f'aproximacao para a derivada {ordem} de f no ponto {x0} =', r)
