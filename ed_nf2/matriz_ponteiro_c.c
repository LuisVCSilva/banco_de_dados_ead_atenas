#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 2, cols = 3;
    int **mat;

    // aloca ponteiros para as linhas
    mat = (int**) malloc(rows * sizeof(int*));
    for(int i=0; i<rows; i++)
        mat[i] = (int*) malloc(cols * sizeof(int));

    // inicializa
    int count = 1;
    for(int i=0; i<rows; i++)
        for(int j=0; j<cols; j++)
            mat[i][j] = count++;

    // imprime
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++)
            printf("%d ", mat[i][j]);
        printf("\n");
    }

    // libera memória
    for(int i=0; i<rows; i++)
        free(mat[i]);
    free(mat);

    return 0;
}
