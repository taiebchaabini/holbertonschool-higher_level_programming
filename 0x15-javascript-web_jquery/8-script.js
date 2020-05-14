const $ = window.$;
$(document).ready(function () {
  $.ajax('https://swapi-api.hbtn.io/api/films/?format=json').done(function (data) {
    data.results.forEach(element => {
      $('UL#list_movies').append('<li>' + element.title + '</li>');
    });
  });
});
