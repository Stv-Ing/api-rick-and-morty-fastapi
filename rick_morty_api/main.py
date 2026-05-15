from fastapi import FastAPI

from rutas.rutas_personajes import router

app = FastAPI(
    title="API de Rick and Morty",
    description="API desarrollada con FastAPI que consume la API pública de Rick and Morty",
    version="1.0.0"
)

app.include_router(router)