#include <stdio.h>
#define SIZE 5

typedef struct {
    int data[SIZE];
    int front, rear;
} Queue;

void enqueue(Queue *q, int val) {
    int next = (q->rear + 1) % SIZE;
    if (next != q->front) {
        q->data[q->rear] = val;
        q->rear = next;
    } else printf("Fila cheia!\n");
}

int dequeue(Queue *q) {
    if (q->front != q->rear) {
        int val = q->data[q->front];
        q->front = (q->front + 1) % SIZE;
        return val;
    }
    printf("Fila vazia!\n");
    return -1;
}

int main() {
    Queue q = {.front = 0, .rear = 0};
    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);

    printf("Elemento removido: %d\n", dequeue(&q));
    printf("Próximo na fila: %d\n", q.data[q.front]);
    return 0;
}
