#!/usr/bin/node

const fs = require('fs');
const input = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, input, 'utf-8', function (error) {
  if (error) console.error(error);
});
