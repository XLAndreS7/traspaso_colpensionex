from pydantic import BaseModel

class Cotizante(BaseModel):
    id: int
    nombre: str
    cedula: str
    fondo_actual: str
    fondo_destino: str
    embargo: bool = False  # Por defecto, embargo es False si no se especifica

    # Añadimos un campo para la prioridad (esto puede ser un número que indique la prioridad)
    prioridad: int = 0  # Por ejemplo, un número entero de prioridad

    def __repr__(self):
        return f"Cotizante(id={self.id}, nombre={self.nombre}, prioridad={self.prioridad}, fondo_actual={self.fondo_actual}, fondo_destino={self.fondo_destino}, embargo={self.embargo})"

    def __lt__(self, other):
        """Define cómo comparar dos cotizantes para la cola de prioridad."""
        if isinstance(other, Cotizante):
            return self.prioridad < other.prioridad  # Compara por el campo de prioridad
        return False


