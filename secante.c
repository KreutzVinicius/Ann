#include <stdio.h>
#include <math.h>

void secante(double (*f)(double), double x0, double x1, int n)
{
    for (int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if (fx1 == fx0)
        {
            printf("divisao por zero na iteração %d", i + 2);
            return;
        }
        double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        printf("x%d = %.16f\n", i + 2, x2);

        x0 = x1;
        x1 = x2;
    }
}

double f(double x)
{
    return x * x - 2;
}

int main()
{
    double x0 = 2.0;
    double x1 = 3.0;
    int n = 5;

    secante(f, x0, x1, n);
}