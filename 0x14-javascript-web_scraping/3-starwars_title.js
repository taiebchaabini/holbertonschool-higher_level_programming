#!/usr/bin/node
const argv = process.argv;
const request = require('request');
if (argv.length === 3) {
  request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, request) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(request.body).title);
  });
}
