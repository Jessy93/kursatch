const webpack  = require('webpack');

module.exports = {
  devServer: {
    proxy: 'rtsp://91.222.130.82:3554',
    proxy: 'https://raw.githubusercontent.com/phoboslab/jsmpeg/master/jsmpeg.min.js',
    proxy: 'http://localhost:5000'
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/kurstach/'
    : '/',
}