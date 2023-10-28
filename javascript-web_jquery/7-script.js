$(function() {
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json" , function(data) {
        let addName = data.name;

        $("#character").text(addName);
    });
});
