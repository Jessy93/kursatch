const webpack  = require('webpack');

module.exports = {
  devServer: {
    proxy: 'rtsp://91.222.130.82:8554',
    proxy: 'http://localhost:5000'
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/kurstach/'
    : '/',
}