#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n)
{
    double fa = f(a);
    double fb = f(b);
    if (fa * fb >= 0)
    {
        printf("O Teorema nao sabe dizer se existe raiz para f no intervalo [%.16f,%.16f]\n", a, b);
        return;
    }
    else
    {
        double x;
        for (int i = 0; i < n; i++)
        {

            x = (a * fb - b * fa) / (fb - fa);
            printf("x%d = %.16f\n", i + 1, x);
            double fx = f(x);
            if (f(x) == 0)
            {
                printf("A raiz de f é x = .16f\n", x);
                return;
            }
            if (fa * fx < 0)
            {
                b = x;
                fb = fx;
            }
            else
            {
                a = x;
                fa = fx;
            }
        }
    }
}

double f(double x)
{
    return exp(5 * x) - 2;
}

int main()
{

    //intervalo inicial
    double a = 1.0;
    double b = 2.0;
    //numero de iteracoes
    int n = 11;

    false_position(f, a, b, n);
}