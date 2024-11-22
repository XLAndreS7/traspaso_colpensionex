# Proyecto Traspaso Colpensionex

## Descripción
Este proyecto automatiza el traslado de cotizantes desde fondos de pensiones privados hacia Colpensionex, manejando datos desde archivos CSV, validaciones de negocio y estructuras personalizadas.

## Requisitos
- Python 3.9+
- FastAPI
- Uvicorn

## Instalación
1. Clona este repositorio.
2. Instala las dependencias con:
   ```bash
   pip install fastapi uvicorn
   ```

## Ejecución
Ejecuta el servidor de la API:
```bash
python traspaso_colpensionex/main.py
```

## Endpoints
- **POST /cargar_csv/{key}**: Carga un archivo CSV en memoria.
- **POST /validar_cotizante**: Valida y organiza un cotizante.
- **GET /listar_prioridad**: Lista cotizantes en la cola de prioridad.
- **GET /listar_negra**: Lista cotizantes en la lista negra.
