#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error('Error:', error);
  }
});
