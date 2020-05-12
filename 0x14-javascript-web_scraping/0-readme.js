#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
fs.readFile(argv[2], 'utf-8', function (err, content) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(content);
});
