from fastapi import APIRouter, HTTPException

from servicios.servicio_personajes import (
    obtener_datos_api,
    URL_BASE
)
from modelos.modelo_personaje import (
    Personaje,
    PersonajeDetalle
)


router = APIRouter()

@router.get(
    "/",
    summary="Inicio de la API",
    description="Endpoint principal de bienvenida"
)
def inicio():
    return {"mensaje": "API de Rick and Morty"}



@router.get(
    "/personajes/vivos",
    response_model=list[Personaje],
    summary="Obtener personajes vivos",
    description="Retorna una lista de personajes cuyo estado es Alive"
)

def obtener_personajes_vivos():

    datos = obtener_datos_api(URL_BASE)

    if datos is None:
        raise HTTPException(
        status_code=500,
        detail="Error consumiendo la API externa"
    )

    personajes_vivos = []

    for personaje in datos["results"]:

        if personaje["status"] == "Alive":

            personajes_vivos.append({
                "nombre": personaje["name"],
                "especie": personaje["species"],
                "estado": personaje["status"]
            })

    return personajes_vivos

@router.get(
    "/personajes/humanos",
    response_model=list[Personaje],
    summary="Obtener personajes humanos",
    description="Retorna únicamente personajes de especie Human"
)

def obtener_personajes_humanos():

    datos = obtener_datos_api(URL_BASE)

    if datos is None:
        raise HTTPException(
        status_code=500,
        detail="Error consumiendo la API externa"
    )

    personajes_humanos = []

    for personaje in datos["results"]:

        if personaje["species"] == "Human":

            personajes_humanos.append({
                "nombre": personaje["name"],
                "especie": personaje["species"],
                "estado": personaje["status"]
            })

    return personajes_humanos

@router.get(
    "/personajes/buscar/{nombre}",
    response_model=list[PersonajeDetalle],
    summary="Buscar personaje",
    description="Busca personajes por nombre"
)
def buscar_personaje(nombre: str):

    datos = obtener_datos_api(f"{URL_BASE}/?name={nombre}")

    if datos is None:
        raise HTTPException(
        status_code=404,
        detail="No se encontraron personajes"
    )

    personajes_encontrados = []

    for personaje in datos["results"]:

        personajes_encontrados.append({
            "nombre": personaje["name"],
            "especie": personaje["species"],
            "estado": personaje["status"],
            "genero": personaje["gender"],
            "origen": personaje["origin"]["name"],
            "imagen": personaje["image"]
        })

    return personajes_encontrados