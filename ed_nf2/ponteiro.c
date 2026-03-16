#include <stdio.h>

int main() {
    int a = 42;
    int *p = &a;  // p guarda o endereço de a

    printf("Valor de a: %d\n", a);        // 42
    printf("Endereço de a: %p\n", &a);    // endereço na memória
    printf("Valor via ponteiro: %d\n", *p); // 42

    *p = 100;  // altera o valor de a via ponteiro
    printf("Novo valor de a: %d\n", a);  // 100

    return 0;
}
