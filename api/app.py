# API para interactuar con el sistema de traspasos
from fastapi import FastAPI, HTTPException
from data.csv_handler import CSVHandler
from cache.super_cache import SuperCache
from models.cotizante import Cotizante
from logic.validations import BusinessLogic
from structures.priority_queue import PriorityQueue
from structures.linked_list import LinkedList

# Instancia de la aplicación FastAPI
app = FastAPI()

# Instancias globales
cache = SuperCache()
cola_prioridad = PriorityQueue()
lista_negra = LinkedList()



@app.post("/cargar_csv/{key}")
async def cargar_csv(key: str, file_path: str):
    """Carga datos desde un archivo CSV y los guarda en memoria."""
    try:
        handler = CSVHandler(file_path)
        rows = handler.read_all_rows()
        
        # Variables para almacenar los cotizantes procesados
        lista_negra_resultados = []
        cola_prioridad_resultados = []

        for row in rows:
            cotizante = Cotizante(**row)  # Convierte la fila en una instancia de Cotizante
            
            if not BusinessLogic.validar_cotizante(cotizante):
                continue  # Si no es válido, omitirlo
            
            if BusinessLogic.validar_embargo(cotizante):
                lista_negra.append(cotizante)
                lista_negra_resultados.append(cotizante.dict())
            else:
                cola_prioridad.push(1, cotizante)  # Prioridad fija por ahora
                cola_prioridad_resultados.append(cotizante.dict())
        
        return {
            "message": "Archivo procesado exitosamente.",
            "lista_negra": lista_negra_resultados,
            "cola_prioridad": cola_prioridad_resultados,
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")



@app.post("/validar_cotizante")
def validar_cotizante(cotizante: Cotizante):
    """Valida un cotizante y decide su destino."""
    if not BusinessLogic.validar_cotizante(cotizante):
        raise HTTPException(status_code=400, detail="Cotizante no válido para traslado.")

    if BusinessLogic.validar_embargo(cotizante):
        lista_negra.append(cotizante)
        return {"message": "Cotizante agregado a la lista negra.", "cotizante": cotizante.dict()}

    cola_prioridad.push(1, cotizante)  # Prioridad fija por ahora
    return {"message": "Cotizante validado y agregado a la cola de prioridad.", "cotizante": cotizante.dict()}


@app.get("/listar_prioridad")
def listar_prioridad():
    """Lista los cotizantes en la cola de prioridad."""
    if cola_prioridad.is_empty():
        raise HTTPException(status_code=404, detail="La cola de prioridad está vacía.")
    return {"cola_prioridad": cola_prioridad.to_list()}



@app.get("/listar_negra")
def listar_negra():
    """Lista los cotizantes en la lista negra."""
    if lista_negra.is_empty():
        raise HTTPException(status_code=404, detail="La lista negra está vacía.")
    return {"lista_negra": lista_negra.to_list()}

def vaciar_cache(key: str = None):
    """Vacía la caché completamente o elimina una clave específica."""
    try:
        if key:
            cache.clear_data(key)
            return {"message": f"Caché eliminada para la clave '{key}'"}
        cache.clear_data()
        return {"message": "Toda la caché ha sido vaciada."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/procesar_cotizante")
def procesar_cotizante():
    """Procesa un cotizante desde la cola de prioridad."""
    try:
        cotizante = cola_prioridad.pop()
        if not cotizante:
            raise HTTPException(status_code=404, detail="No hay cotizantes en la cola de prioridad.")
        # Simulación del procesamiento
        return {"message": "Cotizante procesado exitosamente.", "cotizante": cotizante}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/guardar_csv")
def guardar_csv(tipo: str, file_path: str):
    """Guarda los datos de la lista negra o cola de prioridad en un archivo CSV."""
    handler = CSVHandler(file_path)
    try:
        # Selección de la lista según el tipo
        if tipo == "negra":
            data = [cotizante.dict() for cotizante in list(lista_negra)]
        elif tipo == "prioridad":
            data = [cotizante.dict() for cotizante in cola_prioridad]
        else:
            raise HTTPException(status_code=400, detail="Tipo no válido. Use 'negra' o 'prioridad'.")

        # Verificar que la ruta tenga el nombre del archivo
        import os
        if not os.path.splitext(file_path)[1]:  # Verifica si no hay extensión
            raise HTTPException(status_code=400, detail="Debe proporcionar una extensión para el archivo (por ejemplo, .csv).")

        # Guardar los datos en el archivo CSV
        for row in data:
            handler.write_row(row)

        return {"message": f"Datos guardados en el archivo '{file_path}'."}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar archivo: {str(e)}")

