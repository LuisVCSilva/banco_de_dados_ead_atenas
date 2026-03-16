#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 5

typedef struct {
    char* data[SIZE];
    int front;
    int rear;
    int count;
} Queue;

// Inicializa fila
void initQueue(Queue *q){
    q->front = 0;
    q->rear = 0;
    q->count = 0;
}

// Verifica se a fila está vazia
int isEmpty(Queue *q){
    return q->count == 0;
}

// Verifica se a fila está cheia
int isFull(Queue *q){
    return q->count == SIZE;
}

// Adiciona documento
void enqueue(Queue *q, char* doc){
    if(isFull(q)){
        printf("Fila cheia! Não é possível adicionar '%s'.\n", doc);
        return;
    }
    q->data[q->rear] = doc;
    q->rear = (q->rear + 1) % SIZE;
    q->count++;
    printf("Documento '%s' adicionado à fila.\n", doc);
}

// Remove e imprime documento
void dequeue(Queue *q){
    if(isEmpty(q)){
        printf("Fila vazia! Nenhum documento para imprimir.\n");
        return;
    }
    char* doc = q->data[q->front];
    q->front = (q->front + 1) % SIZE;
    q->count--;
    printf("Documento '%s' impresso.\n", doc);
}

// Mostra estado atual da fila
void showQueue(Queue *q){
    printf("Fila atual: ");
    if(isEmpty(q)){
        printf("vazia\n");
        return;
    }
    int i = q->front;
    for(int c = 0; c < q->count; c++){
        printf("%s ", q->data[i]);
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main(){
    Queue fila;
    initQueue(&fila);

    // Adicionando documentos
    enqueue(&fila, "Doc1");
    enqueue(&fila, "Doc2");
    enqueue(&fila, "Doc3");

    showQueue(&fila);

    // Processando a fila
    dequeue(&fila);
    dequeue(&fila);
    showQueue(&fila);
    dequeue(&fila);
    dequeue(&fila); // tentativa com fila vazia

    return 0;
}
