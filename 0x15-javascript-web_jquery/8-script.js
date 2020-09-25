$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const titles = data.results;
  let nb = 0;
  for (const title in titles) {
    $('ul#list_movies').append('<li>' + ++nb + '- ' + titles[title].title + '</li>');
  }
});
