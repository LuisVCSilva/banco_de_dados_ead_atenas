#include <stdio.h>
#include <string.h>

#define MAX 100

typedef struct {
    char data[MAX];
    int topo;
} Pilha;

// Inicializa pilha
void init(Pilha *p) {
    p->topo = -1;
}

// Empilha
void push(Pilha *p, char c) {
    if (p->topo < MAX - 1)
        p->data[++(p->topo)] = c;
}

// Desempilha
char pop(Pilha *p) {
    if (p->topo >= 0)
        return p->data[(p->topo)--];
    return '\0'; // pilha vazia
}

// Verifica se pilha está vazia
int vazia(Pilha *p) {
    return p->topo == -1;
}

// Verifica parênteses balanceados
int verifica_parenteses(const char *str) {
    Pilha p;
    init(&p);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '(') {
            push(&p, '(');
        } else if (str[i] == ')') {
            if (vazia(&p)) return 0; // fechou sem abrir
            pop(&p);
        }
    }
    return vazia(&p); // se vazia = balanceado
}

int main() {
    char expressoes[][MAX] = {"(())", "(()())", "())(", "((())"};
    int n = 4;

    for (int i = 0; i < n; i++) {
        printf("%s : %s\n", expressoes[i],
               verifica_parenteses(expressoes[i]) ? "Balanceado" : "Não balanceado");
    }

    return 0;
}
