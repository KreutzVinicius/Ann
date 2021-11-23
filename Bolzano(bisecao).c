#include <stdio.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) >= 0)
    {
        printf("O Teorema de Bolzano nao sabe dizer se existe uma raiz para f no intervalo [%.12f, %.12f] ", a, b);
        return;
    }
    else
    {
        double m = 0;
        for (int i = 0; i < n; i++)
        {
            m = 0.5 * (a + b);
            printf("x%d = %.16f\n", i + 1, m);
            if (f(m) == 0)
            {
                printf("Voce encontrou uma raiz para f: z = %.16f", m);
                return;
            }
            if (f(a) * f(m) < 0)
            {
                b = m;
            }
            else
            {
                a = m;
            }
        }
    }
}

double f(double x)
{
    return (x + 1.0 - (3.0 * sin(x)));
}

int main()
{

    double a = 1.08648;
    double b = 2.90884;
    int n = 12;

    bisection(f, a, b, n);
}
