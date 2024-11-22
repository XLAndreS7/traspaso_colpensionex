import csv
from typing import List, Dict, Any

class CSVHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_all_rows(self) -> List[Dict[str, Any]]:
        """Leer todas las filas de un archivo CSV, validando columnas requeridas y asegurando que las claves sean cadenas."""
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            required_columns = {"id", "nombre", "cedula", "fondo_actual", "fondo_destino", "embargo"}
            
            # Verificar que las columnas requeridas estén presentes
            if not required_columns.issubset(set(reader.fieldnames or [])):
                raise ValueError("El archivo CSV no tiene las columnas requeridas.")
            
            # Asegurarse de que las claves sean cadenas
            rows = []
            for row in reader:
                # Convertir las claves a cadenas, en caso de que no sean cadenas
                row = {str(key): value for key, value in row.items()}
                rows.append(row)
            
            return rows

    def write_row(self, row: Dict[str, Any]):
        """Escribir una fila en el archivo CSV."""
        with open(self.file_path, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            if file.tell() == 0:  # Escribe encabezado si el archivo está vacío
                writer.writeheader()
            writer.writerow(row)



   

