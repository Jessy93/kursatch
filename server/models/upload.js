const express = require('express');
const router = express.Router();
let multer = require('multer');
let upload = multer();
const fs = require('fs');

// const sftpSetup = require('../sftpSetup');
// sftpSetup();

const Client = require('ssh2-sftp-client');
let sftp = new Client;

const config = {
  host: '192.168.1.6',
  port: '22',
  username: 'macbook',
  password: 'Jessy93'
};

// Upload files 
router.post('/', upload.single('file'), (req, res) => {
  let f = req.file.buffer.toString('utf8');
  console.log(f);

  if (!req.file) {
    return res.status(500).send({ msg: "file is not found" })
  }
  sftp.connect(config, 'once')
    .then(() => {
      console.log(1);
      let data = fs.createReadStream(req.file.buffer.toString('utf8'));
      sftp.put(data, `/Users/macbook/Desktop/media-users/${req.file.originalname}`)
    })
    .then(() => {
      return sftp.end();
    })
    .catch(err => {
      console.error(err.message);
    });
})

module.exports = router;