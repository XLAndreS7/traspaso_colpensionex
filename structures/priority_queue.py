import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority: int, item):
        """Agrega un elemento con prioridad específica."""
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        """Retira el elemento de mayor prioridad."""
        if self.queue:
            return heapq.heappop(self.queue)[1]
        raise IndexError("La cola está vacía")

    def is_empty(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self.queue) == 0

    def to_list(self):
        """Convierte la cola de prioridad en una lista de elementos."""
        return [item for priority, item in self.queue]

    def __repr__(self) -> str:
        """Representación de la cola como lista de elementos."""
        return str([item for priority, item in self.queue])
        # Hacemos que la cola de prioridad sea iterable
    def __iter__(self):
        """Permite iterar sobre los elementos de la cola de prioridad."""
        return (item for priority, item in self.queue)


