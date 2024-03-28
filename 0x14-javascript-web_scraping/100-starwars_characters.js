#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		return;
	}
	if (response.statusCode !== 200) {
		console.error('Failed to get successful response:', response.statusCode);
		return;
	}
	const movie = JSON.parse(body);
	movie.characters.forEach(characterUrl => {
		request(characterUrl, (error, response, body) => {
			if (!error && response.statusCode === 200) {
				const character = JSON.parse(body);
				console.log(character.name);
			}
		});
	});
});
