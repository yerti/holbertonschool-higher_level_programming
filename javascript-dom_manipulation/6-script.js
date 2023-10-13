const divCharacter = document.querySelector("#character");

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json') // URL where we get character information
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); 
    })
    .then(data => {
        const caharacterName = data.name;
        divCharacter.textContent =  caharacterName; // the name Leia Organa appears in the div tag
    })
    .catch(error => {
        console.error('An error occurred:', error);
    });