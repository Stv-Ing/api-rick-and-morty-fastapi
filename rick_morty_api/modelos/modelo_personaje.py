from pydantic import BaseModel


class Personaje(BaseModel):

    nombre: str
    especie: str
    estado: str

class PersonajeDetalle(BaseModel):

    nombre: str
    especie: str
    estado: str
    genero: str
    origen: str
    imagen: str