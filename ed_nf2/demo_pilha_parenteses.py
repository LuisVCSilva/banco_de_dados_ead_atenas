def verifica_parenteses(expr):
    pilha = []

    for char in expr:
        if char == '(':
            pilha.append(char)  # empilha o '('
        elif char == ')':
            if not pilha:
                return False  # fechou sem abrir
            pilha.pop()  # desempilha '(' correspondente

    return len(pilha) == 0  # pilha vazia = todos balanceados

# Testes
expressoes = ["(())", "(()())", "())(", "((())"]
for e in expressoes:
    print(f"{e}: {'Balanceado' if verifica_parenteses(e) else 'Não balanceado'}")
