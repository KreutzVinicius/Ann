
#include <stdio.h>

#define ROWS 3
#define COLS 3

void seidel(double a[ROWS][COLS], double b[ROWS], double chute[COLS], int n)
{
    for (int it = 0; it < n; it++)
    {
        for (int i = 0; i < ROWS; i++)
        {
            double xi = b[i];
            for (int j = 0; j < COLS; j++)
            {
                if (i != j)
                {
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            chute[i] = xi;
        }
        printf("x^(%d) -> ", it + 1);
        for (int k = 0; k < COLS; k++)
        {
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
    }
}

int main()
{
    double a[ROWS][COLS] = {{4, 1, -1}, {1, -5, 1}, {2, 1, 7}};
    double b[ROWS] = {7, -10, -3};

    double chute[COLS] = {0, -1, 0};

    int n = 10;

    seidel(a, b, chute, n);
}
