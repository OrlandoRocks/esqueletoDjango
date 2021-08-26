const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/javascript"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        use:  "babel-loader",
        test: /\.js$/,
        exclude: /node_modules/,
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
          },
        ],
      },
      {
        use: ['style-loader', 'css-loader'],
        test: /\.css$/,
      },
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: [
                '@babel/env',
                '@babel/react',
                { 'plugins': ['@babel/plugin-proposal-class-properties'] },
              ],
            },
          },
        ],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
        'process.env.NODE_ENV' : JSON.stringify('development')
    })
  ]
};