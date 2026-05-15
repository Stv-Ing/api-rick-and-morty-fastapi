# API de Rick and Morty con FastAPI

API desarrollada con FastAPI que consume la API pública de Rick and Morty.

El proyecto permite consultar personajes vivos, personajes humanos y realizar búsquedas por nombre.

---

# Tecnologías utilizadas

- Python
- FastAPI
- Requests
- Uvicorn
- Pydantic

---

# API externa utilizada

Rick and Morty API

https://rickandmortyapi.com/

---

# Instalación del proyecto

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Ingresar al proyecto

```bash
cd rick_morty_api
```

---

## 3. Crear entorno virtual

### Windows

```bash
python -m venv venv
```

---

## 4. Activar entorno virtual

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar servidor

```bash
uvicorn main:app --reload
```

---

# Documentación Swagger

Abrir en navegador:

```txt
http://127.0.0.1:8000/docs
```

---

# Endpoints disponibles

## Inicio

```http
GET /
```

Respuesta:

```json
{
  "mensaje": "API de Rick and Morty"
}
```

---

## Obtener personajes vivos

```http
GET /personajes/vivos
```

---

## Obtener personajes humanos

```http
GET /personajes/humanos
```

---

## Buscar personaje

```http
GET /personajes/buscar/{nombre}
```

Ejemplo:

```http
GET /personajes/buscar/rick
```

---

# Estructura del proyecto

```txt
project/
│
├── main.py
│
├── modelos/
│   └── modelo_personaje.py
│
├── rutas/
│   └── rutas_personajes.py
│
├── servicios/
│   └── servicio_personajes.py
│
└── requirements.txt
```

---

# Características del proyecto

- Consumo de API externa
- Endpoints personalizados
- Arquitectura modular
- Manejo de errores
- Modelos Pydantic
- Documentación automática con Swagger

---

# Autor

Nombre del estudiante o integrantes del equipo.