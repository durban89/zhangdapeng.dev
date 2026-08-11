---
title: "webpack4 初体验 - 开发 - webpack-dev-server"
date: "2025-07-04 14:27:09"
slug: "webpack4-chu-ti-yan-kai-fa-webpack-dev-server"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-开发-webpack-dev-server/"
  - "/2025/07/04/webpack4-初体验-开发-webpack-dev-server.html"
  - "/webpack4-初体验-开发-webpack-dev-server/"
  - "/webpack4-初体验-开发-webpack-dev-server.html"
  - "/2025/07/04/webpack4-chu-ti-yan-kai-fa-webpack-dev-server/"
  - "/2025/07/04/webpack4-chu-ti-yan-kai-fa-webpack-dev-server.html"
  - "/webpack4-chu-ti-yan-kai-fa-webpack-dev-server.html"
---
webpack-dev-server 为开发人员提供了一个简单的 web 服务器，并且能够实时重新加载(live reloading)。让我们设置以下：

```bash
npm install --save-dev webpack-dev-server
```

修改配置文件，告诉开发服务器(dev server)，在哪里查找文件：webpack.config.js

```bash
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: {
    app: ['./src/index.js'],
    print: ['./src/print.js'],
  },
  devtool: 'eval',
  devServer: {
    contentBase: path.join(__dirname, "dist"),
    compress: true,
    port: 8083,
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'Webpack-输出管理'
    }),
  ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
        ],
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          'file-loader',
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader',
        ]
      },
      {
        test: /\.(csv|tsv)$/,
        use: [
          'csv-loader',
        ]
      },
      {
        test: /\.xml$/,
        use: [
          'xml-loader',
        ]
      }
    ],
  }
};
```

让我们添加一个 script 脚本，可以直接运行开发服务器(dev server)：  
package.json

```json
{
  "name": "webpack4-demo",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack",
    "start": "webpack-dev-server --open"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "clean-webpack-plugin": "^0.1.19",
    "css-loader": "^0.28.11",
    "csv-loader": "^2.1.1",
    "file-loader": "^1.1.11",
    "html-webpack-plugin": "^3.2.0",
    "style-loader": "^0.21.0",
    "webpack": "^4.9.1",
    "webpack-cli": "^2.1.4",
    "webpack-dev-server": "^3.1.4",
    "xml-loader": "^1.2.1"
  },
  "dependencies": {
    "lodash": "^4.17.10"
  }
}
```

现在，我们可以在命令行中运行 npm start，就会看到浏览器自动加载页面。如果现在修改和保存任意源文件，web 服务器就会自动重新加载编译后的代码。试一下！

webpack-dev-server 带有许多可配置的选项。转到[相关文档(https://webpack.docschina.org/configuration/dev-server)]以了解更多。

以上配置告知 webpack-dev-server，在 localhost:8083 下建立服务，将 dist 目录下的文件，作为可访问文件。

这里的配置只是一个非常简答的，如果遇到复杂点的项目可能要做些更多的配置，比如在使用react-router的情况下，这种情况下可能会由于路由的问题导致g更复杂的情况，针对此类的的文章后面跟大家进行分享。

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

项目地址：https://github.com/durban89/webpack4-demo
