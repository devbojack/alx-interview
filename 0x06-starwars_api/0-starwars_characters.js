#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
    try {
        const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
        const response = await request(endpoint);
        const filmData = JSON.parse(response.body);
        const characters = filmData.characters;

        for (let i = 0; i < characters.length; i++) {
            const urlCharacter = characters[i];
            const characterResponse = await request(urlCharacter);
            const characterData = JSON.parse(characterResponse.body);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

starwarsCharacters(filmID);
