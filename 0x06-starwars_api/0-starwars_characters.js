#!/usr/bin/node

const request = require('request');

async function starwarsCharacters(filmId) {
    try {
        const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
        const filmResponse = await request(endpoint);
        const filmData = JSON.parse(filmResponse.body);
        const charactersUrls = filmData.characters;

        for (const urlCharacter of charactersUrls) {
            const characterResponse = await request(urlCharacter);
            const characterData = JSON.parse(characterResponse.body);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

const filmID = process.argv[2];
starwarsCharacters(filmID);