#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Invalid response:', response.statusCode);
        return;
    }

    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    charactersUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error('Invalid response:', response.statusCode);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
