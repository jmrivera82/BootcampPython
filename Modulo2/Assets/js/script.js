
// Manipulación del DOM utilizando el evento mouseover y mouseout (Sesión 9 modulo 2 Exercises)

// index.html

const texto1 = document.getElementById('texto')

const texto3 = document.getElementById('datos')

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


const tituloExp = document.getElementById('titulo-exp')

tituloExp.addEventListener('mouseover', function(){
    tituloExp.style.backgroundColor = 'red'
})