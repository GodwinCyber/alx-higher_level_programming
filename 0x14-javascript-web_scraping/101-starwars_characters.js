#!/usr/bin/node
const request = require('request');

function fetchCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) return reject(new Error(error));
      if (response.statusCode !== 200) {
        return reject(new Error(`Failed to get a successful response: ${response.statusCode}`));
      }
      return resolve(JSON.parse(body).name);
    });
  });
}

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, async (error, response, body) => {
  if (error) return console.error('Error:', error);
  if (response.statusCode !== 200) return console.error('Failed to get a successful response:', response.statusCode);

  const movie = JSON.parse(body);
  for (const characterUrl of movie.characters) {
    try {
      const name = await fetchCharacterName(characterUrl);
      console.log(name);
    } catch (err) {
      console.error(err.message);
    }
  }
});
