document.addEventListener("DOMContentLoaded", saludar);

function saludar() {
    // Get a reference to the element with the id "hello"
    const divHello = document.getElementById('hello');

    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr') // url where we get the greeting information
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Display the translation of "hello" in the HTML element
            divHello.textContent = data.hello;
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
}