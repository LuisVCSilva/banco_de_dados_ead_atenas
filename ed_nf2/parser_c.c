#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct Node {
    char op;       // operador ou '\0' se for número
    int value;     // valor se número
    struct Node *left, *right;
} Node;

// ===============================
// Cria nó
// ===============================
Node* new_node_op(char op, Node* left, Node* right){
    Node* n = (Node*)malloc(sizeof(Node));
    n->op = op; n->value = 0;
    n->left = left; n->right = right;
    return n;
}

Node* new_node_val(int val){
    Node* n = (Node*)malloc(sizeof(Node));
    n->op = '\0'; n->value = val;
    n->left = n->right = NULL;
    return n;
}

// ===============================
// Parser simples (recursive descent)
// ===============================
char* input;

Node* parse_factor();
Node* parse_term();
Node* parse_expression();

Node* parse_factor() {
    if (*input == '(') {
        input++;
        Node* node = parse_expression();
        if (*input == ')') input++;
        return node;
    } else {
        int val = 0;
        while (isdigit(*input)) {
            val = val*10 + (*input - '0');
            input++;
        }
        return new_node_val(val);
    }
}

Node* parse_term() {
    Node* node = parse_factor();
    while (*input == '*' || *input == '/') {
        char op = *input;
        input++;
        node = new_node_op(op, node, parse_factor());
    }
    return node;
}

Node* parse_expression() {
    Node* node = parse_term();
    while (*input == '+' || *input == '-') {
        char op = *input;
        input++;
        node = new_node_op(op, node, parse_term());
    }
    return node;
}

// ===============================
// Avaliação da árvore
// ===============================
int eval_tree(Node* node){
    if (node->op == '\0') return node->value;
    int l = eval_tree(node->left);
    int r = eval_tree(node->right);
    switch(node->op){
        case '+': return l + r;
        case '-': return l - r;
        case '*': return l * r;
        case '/': return l / r;
    }
    return 0;
}

// ===============================
int main(){
    char expr[] = "3+5*(2-4)";
    input = expr;
    Node* tree = parse_expression();
    printf("Resultado: %d\n", eval_tree(tree));
    return 0;
}
