---
title: "Webpack4生产环境构建相关配置 - 基础配置"
date: "2025-07-07 15:52:04"
slug: "webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-ji-chu-pei-zhi"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4生产环境构建相关配置-基础配置/"
  - "/2025/07/07/Webpack4生产环境构建相关配置-基础配置.html"
  - "/Webpack4生产环境构建相关配置-基础配置/"
  - "/Webpack4生产环境构建相关配置-基础配置.html"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-ji-chu-pei-zhi/"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-ji-chu-pei-zhi.html"
  - "/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-ji-chu-pei-zhi.html"
---
这里为什么要实践下这个，引用下官方的原文

> 开发环境(development)和生产环境(production)的构建目标差异很大。在开发环境中，我们需要具有强大的、具有实时重新加载(live reloading)或热模块替换(hot module replacement)能力的 source map 和 localhost server。而在生产环境中，我们的目标则转向于关注更小的 bundle，更轻量的 source map，以及更优化的资源，以改善加载时间。由于要遵循逻辑分离，我们通常建议为每个环境编写彼此独立的 webpack 配置。
>
> 虽然，以上我们将生产环境和开发环境做了略微区分，但是，请注意，我们还是会遵循不重复原则(Don't repeat yourself - DRY)，保留一个“通用”配置。为了将这些配置合并在一起，我们将使用一个名为 webpack-merge 的工具。通过“通用”配置，我们不必在环境特定(environment-specific)的配置中重复代码。

下面让我们用我们之前文章的项目来做下实践

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
npm install --save-dev webpack-merge
```

创建文件webpack.common.js

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'React + ReactRouter Demo',
      filename: './index.html', // 调用的文件
      template: './index.html', // 模板文件
    }),
  ],
  output: {
    filename: '[name].bundle.js',
    chunkFilename: '[chunkhash].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/',
  },
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      loader: 'babel-loader',
      exclude: [
        path.resolve(__dirname, 'node_modules'),
      ],
      options: {
        plugins: ['transform-async-to-generator', 'transform-strict-mode', 'transform-object-assign', 'transform-decorators-legacy', 'react-hot-loader/babel'],
        presets: ['es2015', 'react', 'stage-0'],
      },
    },
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
      ],
    },
    {
      test: /\.(woff|woff2|eot|ttf|otf)$/,
      use: [
        'file-loader',
      ],
    },
    {
      test: /\.(csv|tsv)$/,
      use: [
        'csv-loader',
      ],
    },
    {
      test: /\.xml$/,
      use: [
        'xml-loader',
      ],
    },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // 这里是必须要加的，不然默认的值加载['.js','.json']为后缀的文件
    alias: {
      Actions: path.resolve(__dirname, 'src/actions'),
    },
  },
};
```

创建文件webpack.dev.js

```js
const merge = require('webpack-merge');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const path = require('path');
const common = require('./webpack.common');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'eval',
  entry: {
    app: [
      'webpack/hot/only-dev-server',
      'react-hot-loader/patch',
      './src/index.jsx',
    ],
  },
  devServer: {
    hot: true,
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 8083,
    historyApiFallback: {
      rewrites: [{
        from: /^\/$/,
        to: './index.html',
      }],
    },
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'React + ReactRouter Demo',
      filename: './index.html', // 调用的文件
      template: './index.html', // 模板文件
    }),
    new webpack.DefinePlugin({
      'global.GENTLY': false,
      __DEV__: true,
    }),
  ],
});
```

创建文件webpack.prod.js

```js
const merge = require('webpack-merge');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const common = require('./webpack.common');

module.exports = merge(common, {
  mode: 'production',
  entry: {
    app: [
      './src/index.jsx',
    ],
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'React + ReactRouter',
      filename: './index.html', // 调用的文件
      template: './index.html', // 模板文件
    }),
  ],
});
```

然后修改package.json

```json
"build": "npx webpack --config webpack.prod.js",
"start": "npx webpack-dev-server --open --hot --config webpack.dev.js"
```

指定具体的配置文件

接下来分别执行

```bash
npm run start // 开发环境执行
npm run build // 生产环境执行
```

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.6
```
