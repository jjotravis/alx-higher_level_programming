$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
    $.each(response.results, function(index, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>')
    });
});
