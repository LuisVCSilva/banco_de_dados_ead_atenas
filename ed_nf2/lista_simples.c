#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

void insert(Node **head, int val) {
    Node *n = (Node*)malloc(sizeof(Node));
    n->data = val;
    n->next = *head;
    *head = n;
}

void printList(Node *head) {
    while(head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    Node *head = NULL;
    insert(&head, 10);
    insert(&head, 20);
    insert(&head, 30);

    printList(head);
    return 0;
}
