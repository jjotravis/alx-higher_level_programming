#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(url + id, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else if (resp.statusCode === 200) {
    const response = JSON.parse(body);
    console.log(response.title);
  } else {
    console.log('Error code: ' + resp.statusCode);
  }
});
