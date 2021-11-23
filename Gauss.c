#include <stdio.h>
#include <math.h>

#define ROWS 4
#define COLS 5

void printMatrix(double array[ROWS][COLS])
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            printf("%.8f\t", array[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS])
{
    //percorre colunas
    for (int j = 0; j < COLS - 2; j++)
    {
        //percorrendo a coluna j]
        for (int i = j; i < ROWS; i++)
        {
            if (E[i][j] != 0)
            {
                if (i != j)
                {
                    //troca de linhas li e lj
                    double temp;
                    for (int k = 0; k < COLS; k++)
                    {
                        temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                // o pivor (elemento ij de E) é nao nulo
                //executa  operacoes em linha
                for (int m = j + 1; m < ROWS; m++)
                {
                    //a * Lj + Lm -> Lm
                    double a = -E[m][j] / E[j][j];
                    for (int n = j; n < COLS; n++)
                    {
                        E[m][n] += a * E[j][n];
                    }
                }
                printMatrix(E);
                printf("\n");
                break;
            }
            else
            {
                if (i == ROWS - 1)
                {
                    printf("Esse sistema não possui solução");
                }
            }
        }
    }
}

void reverse_substution(double E[ROWS][COLS])
{
    double answers[ROWS];
    for (int i = 0; i < ROWS; i++)
    {
        int d = ROWS - 1 - i;
        double b = E[d][COLS - 1]; //termo independente na linha d
        for (int j = d + 1; j < COLS - 1; j++)
        {
            b -= E[d][j] * answers[j];
        }
        double xd = b / E[d][d];
        answers[d] = xd;
        printf("x%d = %.16f\n", d + 1, xd);
    }
}

int main()
{

    double E[ROWS][COLS] = {{2, 4, 6, 2, 4}, {1, 2, -1, 3, 8}, {-3, 1, -2, 1, -2}, {1, 3, -3, -2, 6}};

    printMatrix(E);
    printf("\n");

    gauss(E);

    printf("\n");

    reverse_substution(E);
}