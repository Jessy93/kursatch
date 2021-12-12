const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();


const url = require('url');
const http = require('http');
const fs = require('fs');

const server = http.createServer();
const hostname = 'localhost';
const port = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());

server.listen(port, hostname, (err) => {
  if (err) return console.log(err)
  app.listen(port, (e) => {
    console.log(`Server running at http://localhost:${port}`);
  })
});

// app.post('/', (req, res) => {});

app.get('/', (req, res, next) => {})

const upload = require('./models/upload');
app.use('/models/upload', upload)

// const download = require('./models/download');
// app.use('/models/download', download)
