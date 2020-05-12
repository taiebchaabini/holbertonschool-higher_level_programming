#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request(argv[2], function (error, request) {
  if (error) {
    console.log(error);
    return;
  }
  if (request.statusCode === 200) {
    const response = JSON.parse(request.body);
    const taskNb = {};
    let id = 0;
    for (let i = 0; i < response.length; i++) {
      id = response[i].userId;
      if (taskNb[id] === undefined) { taskNb[id] = 0; }
      taskNb[id] += 1;
    }
    console.log(taskNb);
  }
});
