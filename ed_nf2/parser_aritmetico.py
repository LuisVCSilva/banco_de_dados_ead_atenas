import graphviz

# ===============================
# Nó da Árvore
# ===============================
class Node:
    def __init__(self, value):
        self.value = value  # operador ou número
        self.left = None
        self.right = None

# ===============================
# Parser Recursivo Simples
# ===============================
def parse_expression(tokens):
    """Recursivo para + e -"""
    node = parse_term(tokens)
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        new_node = Node(op)
        new_node.left = node
        new_node.right = parse_term(tokens)
        node = new_node
    return node

def parse_term(tokens):
    """Recursivo para * e /"""
    node = parse_factor(tokens)
    while tokens and tokens[0] in ('*', '/'):
        op = tokens.pop(0)
        new_node = Node(op)
        new_node.left = node
        new_node.right = parse_factor(tokens)
        node = new_node
    return node

def parse_factor(tokens):
    token = tokens.pop(0)
    if token == '(':
        node = parse_expression(tokens)
        tokens.pop(0)  # remove ')'
        return node
    else:
        return Node(token)  # número

# ===============================
# Avaliação da Árvore
# ===============================
def eval_tree(node):
    if node.value.isdigit():
        return int(node.value)
    left = eval_tree(node.left)
    right = eval_tree(node.right)
    if node.value == '+': return left + right
    if node.value == '-': return left - right
    if node.value == '*': return left * right
    if node.value == '/': return left / right

# ===============================
# Função para Plotar a Árvore
# ===============================
def plot_tree(node, filename='tree'):
    dot = graphviz.Digraph()
    
    def add_nodes_edges(node, parent=None):
        if node is None:
            return
        uid = str(id(node))
        dot.node(uid, node.value)
        if parent:
            dot.edge(str(id(parent)), uid)
        add_nodes_edges(node.left, node)
        add_nodes_edges(node.right, node)
    
    add_nodes_edges(node)
    dot.render(filename, format='png', cleanup=True)
    print(f"Árvore gerada em {filename}.png")

# ===============================
# Função Principal
# ===============================
def main():
    expr = "3 + 5 * (2 - 4)"
    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    tree = parse_expression(tokens)
    print(f"Resultado: {eval_tree(tree)}")
    plot_tree(tree, filename='arvore_aritmetica')

if __name__ == "__main__":
    main()
