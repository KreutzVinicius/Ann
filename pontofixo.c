#include <stdio.h>
#include <math.h>
// fazer verificaçao de existencia e unicidade antes de usar ponto fixo

double ex1(double x)
{
    return x / 2.0 + 1 / x;
}

double ex2(double x)
{
    return (x * x - 1.0) / 3.0;
}
void fixed_point(double (*f)(double), double x0, int n)
{
    double xn;
    for (int i = 0; i < n; i++)
    {
        xn = f(x0);
        printf("x%d=%.16f\n", i + 1, xn);
        x0 = xn;
    }
}

int main()
{

    double x0 = 1.678;
    int n = 3;

    fixed_point(ex1, x0, n);

    // float x0 = 0.76;
    // int n = 3;

    // fixed_point(ex2, x0, n);
}