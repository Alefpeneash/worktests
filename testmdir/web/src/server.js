const express = require('express');

const app = express();

const HOST = '0.0.0.0';
const PORT = 8080;

const db = require('./config/db.js');
const env = require('./config/env.js');

function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
}


app.get('/something', (req, res) => {
    const id = guid();
    db.something.create({
      id: id
    });
    (async () => {
      let newexemplar = await res.json(newexemplar);
    })();
})

app.get('/all', (req, res) => {
    db.something.create({id: id});

    (async () => {
      let something = await res.json(something);
    })();

 });

app.get('/', (req, res) => {
	res.send('Hello.<br><a href="env">env</a>');
})

app.get('/env', (req, res) => {
	res.send(process.env)

})


app.listen(PORT, HOST);
console.log('Running on http://' + HOST + ':' + PORT);
