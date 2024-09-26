#!/usr/bin/node

const request = require('request');

const title = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + title;

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log('error');
        return reject(error);
      }

      if (response.statusCode !== 200) {
        console.log('Status code not 200');
        return reject(new Error('Wrong status'));
      }

      const data = JSON.parse(body);
      resolve(data);
    });
  });
}

async function getFilmAndCharacters (url) {
  try {
    const film = await getRequest(url);
    const characterUrl = film.characters;
    for (let x = 0; x < characterUrl.length; x++) {
      const character = await getRequest(characterUrl[x]);
      console.log(character.name);
    }
  } catch (err) {
    console.error('Error:', err);
  }
}

getFilmAndCharacters(url);
