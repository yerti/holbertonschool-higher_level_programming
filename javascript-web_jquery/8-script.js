$(function() {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
        $.each(data.results, function(index, movie){
            $("#list_movies").append("<div>"+ movie.title + "</div>");
        });
    });
});
