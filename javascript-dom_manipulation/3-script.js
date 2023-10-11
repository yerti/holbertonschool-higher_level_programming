// we call the tag header
const tagHeader =  document.querySelector("header");
// we call the id red_header
const divTogle =  document.querySelector("#toggle_header");

divTogle.addEventListener('click', changeColorToHeader);

// changes the color of the letter depending on what color it is
function changeColorToHeader() {
    if (tagHeader.classList.contains('red')) {
        tagHeader.classList.remove('red');
        tagHeader.classList.add('green');
    } else if (tagHeader.classList.contains('green')) {
        tagHeader.classList.remove('green');
        tagHeader.classList.add('red');
    }
}