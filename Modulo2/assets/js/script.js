// Manipulación del DOM utilizando el evento mouseover y mouseout (Sesión 9 modulo 2 Exercises)

// los cambios producidos se visualizarán en el index.html

const texto1 = document.getElementById('titulo')

const texto3 = document.getElementById('sub-titulo')

console.log("prueba de carga del script")


texto1.addEventListener('mouseover', function() {
    texto1.style.color = '#9dc9c1e7'
})

texto1.addEventListener('mouseout', function() {
    texto1.style.color = 'whitesmoke'
})

texto3.addEventListener('mouseover', function() {
    texto3.style.color = '#9dc9c1e7'
})

texto3.addEventListener('mouseout', function() {
    texto3.style.color = 'whitesmoke'
})

//esta función agrandará el contenido del parrafo de presentación levemente.


document.addEventListener("DOMContentLoaded", function() {
    const contenido = document.getElementById("contenido")

    contenido.addEventListener("mouseenter", function() {
        this.style.transform = "scale(1.1)"
        this.style.transition = "transform 0.3s ease"
    })

    contenido.addEventListener("mouseleave", function() {
        this.style.transform = "scale(1)"
    })
})