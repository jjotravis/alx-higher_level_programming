#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else if (resp.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const chars = films[film].characters;
      for (const person in chars) {
        if (chars[person].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error code: ' + resp.statusCode);
  }
});
