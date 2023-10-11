document.addEventListener("DOMContentLoaded", runJavascript);

function runJavascript() {
    // we call the tag header
    const etiquetaHeader = document.querySelector("header");
    // we call the id red_header
    const  divRed = document.querySelector("#red_header");

    divRed.addEventListener('click', changeRedColor);

    function  changeRedColor() {
        etiquetaHeader.classList.add("red");
    }
}