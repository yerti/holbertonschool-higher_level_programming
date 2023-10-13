const ulListMovies =  document.querySelector("#list_movies");

fetch('https://swapi-api.hbtn.io/api/films/?format=json') // URL Where do we get movie titles from
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const movie =  data.results;

        movie.forEach(movie => {
            const titleMovie = movie.title;
            const list = document.createElement('li');
            list.textContent =  titleMovie;
            ulListMovies.appendChild(list); // It returns us the list of movie titles
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
    })