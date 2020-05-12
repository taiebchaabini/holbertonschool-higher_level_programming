#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  if (request.statusCode === 200) {
    const response = JSON.parse(request.body);
    let c = 0;
    let characters = '';
    for (const i in response.results) {
      characters = response.results[i].characters;
      for (let i = 0; i < characters.length; i++) {
        if (characters[i] === 'https://swapi-api.hbtn.io/api/people/18/') {
          c += 1;
        }
      }
    }
    console.log(c);
  }
});
