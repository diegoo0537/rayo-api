from fastapi import APIRouter

router = APIRouter(prefix="/jugadores", # prefijo general
                   tags=["jugadores"], # etiqueta para documentacion
                   responses={404: {"message": "No encontrado"}}) # respuesta si falla el server

lista_jugadores = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

# http://127.0.0.1:8000/jugadores
@router.get("/")
async def jugadores():
   return lista_jugadores

# http://127.0.0.1:8000/jugadores/1
@router.get("/{id}")
async def jugadores(id: int):
    return lista_jugadores[id]