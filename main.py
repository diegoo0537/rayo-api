from fastapi import FastAPI
import jugadores

app = FastAPI()

# Routers
app.include_router(jugadores.router)

# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hola FastAPI"