#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else if (resp.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};
    for (const i in todos) {
      const task = todos[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Error code: ' + resp.statusCode);
  }
});
