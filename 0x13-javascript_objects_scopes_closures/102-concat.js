#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const file1 = fs.readFileSync(args[2], 'utf8');
const file2 = fs.readFileSync(args[3], 'utf8');
const data = file1 + file2;
fs.writeFile(args[4], data, err => {
  if (err) {
    console.error(err);
  }
});
