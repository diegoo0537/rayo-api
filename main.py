from fastapi import FastAPI
import jugadores

# https://rayo-api.onrender.com/

app = FastAPI()

# Routers
app.include_router(jugadores.router)

# https://rayo-api.onrender.com/
@app.get("/")
async def root():
    return "Rayo de Hortaleza"