from fastapi import APIRouter
from db import db

router = APIRouter(
    prefix="/jugadores",
    tags=["jugadores"],
    responses={404: {"message": "No encontrado"}}
)

# GET /jugadores
@router.get("/")
async def get_jugadores():
    docs = db.collection("jugadores").stream()

    jugadores = [doc.to_dict() | {"id": doc.id} for doc in docs]
    return jugadores

# GET /jugadores/{id}
@router.get("/{id}")
async def get_jugador(id: str):
    doc = db.collection("jugadores").document(id).get()

    if doc.exists:
        return doc.to_dict()
    return {"error": "Jugador no encontrado"}
