const path = require('path');

module.exports = {
  entry: './static/js/entry.js',
  output: {
    filename: 'webpack-gadgets.bundle.js',
    path: path.resolve(__dirname, 'static/js'),
    publicPath: "auto",
  },
  target: 'web',
  mode: 'production',
  devtool: 'source-map', 
};
