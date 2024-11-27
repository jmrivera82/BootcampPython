
// Manipulación del DOM utilizando el evento mouseover y mouseout (Sesión 9 modulo 2 Exercises)

// index.html

const texto1 = document.getElementById('texto-1')

const texto3 = document.getElementById('texto-3')

console.log("prueba de carga del script")


texto1.addEventListener('mouseover', function() {
    texto1.style.color = 'red'
})

texto1.addEventListener('mouseout', function() {
    texto1.style.color = 'black'
})

texto3.addEventListener('mouseover', function() {
    texto3.style.color = 'red'
})

texto3.addEventListener('mouseout', function() {
    texto3.style.color = 'black'
})


const tituloExp = document.getElementById('titulo-exp')

tituloExp.addEventListener('mouseover', function(){
    tituloExp.style.backgroundColor = 'red'
})