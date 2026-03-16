#include <stdio.h>
#define SIZE 100

typedef struct {
    int data[SIZE];
    int top;
} Stack;

void push(Stack *s, int val) {
    if (s->top < SIZE-1) s->data[++s->top] = val;
    else printf("Pilha cheia!\n");
}

int pop(Stack *s) {
    if (s->top >= 0) return s->data[s->top--];
    printf("Pilha vazia!\n");
    return -1;
}

int main() {
    Stack s = {.top = -1};
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);

    printf("Elemento removido: %d\n", pop(&s));
    printf("Topo atual: %d\n", s.data[s.top]);
    return 0;
}
