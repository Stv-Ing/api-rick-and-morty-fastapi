const URL_BASE = "http://127.0.0.1:8000";


function mostrarPersonajes(personajes) {

    const contenedor = document.getElementById("resultado");

    contenedor.innerHTML = "";

    personajes.forEach(personaje => {

        let claseEstado = "unknown";

        if (personaje.estado === "Alive") {
            claseEstado = "alive";
        }

        else if (personaje.estado === "Dead") {
            claseEstado = "dead";
        }

        contenedor.innerHTML += `
        
            <div class="tarjeta">

                <img src="${personaje.imagen}" alt="personaje">

                <div class="info">

                    <h3>${personaje.nombre}</h3>

                    <p>
                        <strong>Especie:</strong>
                        ${personaje.especie}
                    </p>

                    <span class="estado ${claseEstado}">
                        ${personaje.estado}
                    </span>

                </div>

            </div>
        `;
    });
}

async function obtenerVivos() {

    const respuesta = await fetch(
        `${URL_BASE}/personajes/vivos`
    );

    const datos = await respuesta.json();

    mostrarPersonajes(datos);
}


async function obtenerHumanos() {

    const respuesta = await fetch(
        `${URL_BASE}/personajes/humanos`
    );

    const datos = await respuesta.json();

    mostrarPersonajes(datos);
}


async function buscarPersonaje() {

    const nombre = document.getElementById(
        "nombrePersonaje"
    ).value;

    const respuesta = await fetch(
        `${URL_BASE}/personajes/buscar/${nombre}`
    );

    const datos = await respuesta.json();

    mostrarPersonajes(datos);
}