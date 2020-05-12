#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request('https://swapi-api.hbtn.io/api/people', function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  if (request.statusCode === 200) {
    const response = JSON.parse(request.body);
    let film;
    let character;
    for (let i = 0; i < response.results.length; i++) {
      character = response.results[i];
      for (let b = 0; b < character.films.length; b++) {
        film = character.films[b];
        if (film === 'https://swapi-api.hbtn.io/api/films/' + argv[2] + '/') { console.log(character.name); }
      }
    }
  }
});
