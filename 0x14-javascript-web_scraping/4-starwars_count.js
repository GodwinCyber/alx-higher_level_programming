#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    return console.error('Error:', error);
  }
  if (response.statusCode !== 200) {
    return console.error('Failed to get successful response:', response.statusCode);
  }
  const films = JSON.parse(body).results;
  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });
  console.log(count);
});
