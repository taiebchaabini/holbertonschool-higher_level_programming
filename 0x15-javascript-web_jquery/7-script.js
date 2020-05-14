const $ = window.$;
$(document).ready(function () {
  $.ajax('https://swapi-api.hbtn.io/api/people/5/?format=json').done(function (data) {
    $('DIV#character').text(data.name);
  });
});
