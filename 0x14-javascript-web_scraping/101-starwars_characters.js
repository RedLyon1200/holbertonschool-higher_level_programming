#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/people/';

function search (id, url) {
  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      const jsonobj = JSON.parse(body);
      const users = jsonobj.results;
      for (const user in users) {
        for (const film in users[user].films) {
          if (users[user].films[film].includes(id)) {
            console.log(users[user].name);
          }
        }
      }
      if (jsonobj.next !== null) {
        search(id, jsonobj.next);
      }
    } else {
      console.log('An error occured. Status code: ' + res.statusCode);
    }
  });
}
search(id, url);
