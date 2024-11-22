class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def __iter__(self):
        """Iterador para recorrer la lista."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """Representación de la lista para depuración."""
        elements = [str(data) for data in self]
        return " -> ".join(elements)

    def to_list(self):
        """Convierte la lista enlazada en una lista de cotizantes."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data.dict())
            current = current.next
        return elements