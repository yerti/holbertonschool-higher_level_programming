// we call the id update_header
const divUpdateHeader =  document.querySelector("#update_header");

// we give a click event to the id update_header
divUpdateHeader.addEventListener('click', addNewHeader);

// function that changes the header
function  addNewHeader() {
    let newHeader = document.querySelector("header");

    newHeader.innerText = "New Header!!!";
}