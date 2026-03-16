#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;
    int *v = (int*) malloc(n * sizeof(int)); // aloca vetor dinamicamente

    for(int i=0; i<n; i++)
        v[i] = i*10;

    for(int i=0; i<n; i++)
        printf("v[%d] = %d\n", i, v[i]);

    free(v); // libera memória
    return 0;
}
