# Punto de entrada del sistema
from data.csv_handler import CSVHandler
from cache.super_cache import SuperCache
from models.cotizante import Cotizante
from api.app import app  # Asegúrate de que la ruta sea correcta
import uvicorn
from fastapi.responses import RedirectResponse

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    print("Sistema de traspaso Colpensionex iniciado.")
    print("Iniciando servidor de API...")
    uvicorn.run("api.app:app", host="127.0.0.1", port=8080, reload=True)


