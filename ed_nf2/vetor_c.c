#include <stdio.h>

int main() {
    int v[5] = {1, 2, 3, 4, 5};  // vetor com 5 elementos

    for(int i=0; i<5; i++){
        printf("v[%d] = %d\n", i, v[i]);
    }

    return 0;
}
