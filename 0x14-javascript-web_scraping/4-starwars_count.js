#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const CHARACTER_ID = '18';

request(API_URL, function (error, response, body) {
  if (error) {
    return console.error('Error:', error);
  }
  if (response.statusCode !== 200) {
    return console.error('Failed to get successful response:', response.statusCode);
  }
  let count = 0;
  const films = JSON.parse(body).results;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes('/' + CHARACTER_ID + '/')) {
        count++;
      }
    });
  });
  console.log(count);
});
