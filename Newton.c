#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n)
{
    double x1;
    for (int i = 0; i < n; i++)
    {
        x1 = x0 - f(x0) / df(x0);
        printf("x%d = %.16f\n", i + 1, x1);
        x0 = x1;
    }
}

double f(double x)
{

    return exp(5 * x) - 2;
}
double df(double x)
{
    return 5 * exp(5 * x);
}

int main()
{

    double x0 = 1.19333;
    int n = 5;

    newton(f, df, x0, n);
}
