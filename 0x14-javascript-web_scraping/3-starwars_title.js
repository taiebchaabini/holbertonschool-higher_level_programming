#!/usr/bin/node
const argv = process.argv;
const request = require('request');
let number = '';
if (argv[2]) { number = argv[2]; }
request('https://swapi-api.hbtn.io/api/films/' + number, function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  const response = JSON.parse(request.body);
  if (number !== '') {
    console.log(response.title);
    return;
  }
  for (const i in response.results) { console.log(response.results[i].title); }
});
