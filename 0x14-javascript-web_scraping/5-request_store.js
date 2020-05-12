#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const fs = require('fs');
request(argv[2], function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  if (request.statusCode === 200) {
    const response = request.body;
    fs.writeFile(argv[3], response, 'utf-8', err => {
      if (err) { console.log(err); }
    });
  }
});
