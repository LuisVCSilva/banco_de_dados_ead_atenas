class PrinterQueue:
    def __init__(self):
        self.queue = []  # lista simples para armazenar documentos

    def enqueue(self, document):
        self.queue.append(document)  # adiciona no final
        print(f"Documento '{document}' adicionado à fila.")

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia! Nenhum documento para imprimir.")
            return None
        document = self.queue.pop(0)  # remove do início (FIFO)
        print(f"Documento '{document}' impresso.")
        return document

    def is_empty(self):
        return len(self.queue) == 0

    def show_queue(self):
        print("Fila atual:", self.queue)


# --- Exemplo de uso ---
fila = PrinterQueue()

# Adicionando documentos
fila.enqueue("Doc1")
fila.enqueue("Doc2")
fila.enqueue("Doc3")

fila.show_queue()

# Processando a fila
fila.dequeue()
fila.dequeue()
fila.show_queue()
fila.dequeue()
fila.dequeue()  # tentativa de imprimir com fila vazia
