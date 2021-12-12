
module.exports = function () {
  let Client = require('ssh2-sftp-client');
  let sftp = new Client();

  sftp.connect({
    host: '10.60.3.202',
    port: '22',
    username: 'macbook',
    password: 'Jessy93'
  });
};


// function () {
//   let Client = require('ssh2-sftp-client');
//   let sftp = new Client();

//   sftp.connect({
//     host: '10.60.3.202',
//     port: '22',
//     username: 'macbook',
//     password: 'Jessy93'
//   }).then(() => {
//     return sftp.list('/Users/macbook/Desktop/media-users');
//   }).then(data => {
//     console.log(data, 'the data info');
//   }).catch(err => {
//     console.log(err, 'catch error');
//   });
// };