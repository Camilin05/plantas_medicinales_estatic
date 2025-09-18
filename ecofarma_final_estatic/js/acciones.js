// Espera a que todo el contenido del HTML se cargue antes de ejecutar el script.
document.addEventListener('DOMContentLoaded', () => {

    /**
     * FUNCIONALIDAD 1: FILTRO DE BÚSQUEDA EN TIEMPO REAL
     * Busca en la lista de plantas y en la de síntomas.
     */
    const inicializarBuscador = (idInput, idContenedor, selectorItem) => {
        const inputBusqueda = document.getElementById(idInput);
        const contenedorItems = document.getElementById(idContenedor);

        // Si no encontramos los elementos en la página, no hacemos nada.
        if (!inputBusqueda || !contenedorItems) {
            return;
        }

        const items = contenedorItems.querySelectorAll(selectorItem);

        inputBusqueda.addEventListener('keyup', (e) => {
            const textoBuscado = e.target.value.toLowerCase();

            items.forEach(item => {
                const textoItem = item.textContent.toLowerCase();
                if (textoItem.includes(textoBuscado)) {
                    item.style.display = ''; // Muestra el elemento
                } else {
                    item.style.display = 'none'; // Oculta el elemento
                }
            });
        });
    };

    // Inicializamos los buscadores para cada página
    inicializarBuscador('buscador-plantas', 'lista-items', '.col');
    inicializarBuscador('buscador-sintomas', 'lista-items', '.list-group-item');


    /**
     * FUNCIONALIDAD 2: BOTÓN "VOLVER ARRIBA"
     * Aparece al hacer scroll y te lleva al inicio de la página suavemente.
     */
    const btnVolverArriba = document.getElementById('btn-volver-arriba');

    if (btnVolverArriba) {
        window.addEventListener('scroll', () => {
            // Si el scroll es mayor a 300px, muestra el botón. Si no, lo oculta.
            if (window.scrollY > 300) {
                btnVolverArriba.classList.add('mostrar');
            } else {
                btnVolverArriba.classList.remove('mostrar');
            }
        });

        btnVolverArriba.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Animación de scroll suave
            });
        });
    }


    /**
     * FUNCIONALIDAD 3: ANIMACIÓN DE ELEMENTOS AL HACER SCROLL
     * Los elementos aparecen con un efecto 'fade in' cuando entran en la pantalla.
     */
    const elementosAnimados = document.querySelectorAll('.animar-scroll');

    if (elementosAnimados.length > 0) {
        const observador = new IntersectionObserver((entradas) => {
            entradas.forEach(entrada => {
                if (entrada.isIntersecting) {
                    entrada.target.classList.add('visible');
                    observador.unobserve(entrada.target); // Para que la animación ocurra solo una vez
                }
            });
        }, {
            threshold: 0.1 // La animación se activa cuando el 10% del elemento es visible
        });

        elementosAnimados.forEach(elemento => {
            observador.observe(elemento);
        });
    }

});