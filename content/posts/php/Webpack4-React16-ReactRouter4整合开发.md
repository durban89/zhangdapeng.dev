---
title: "Webpack4+React16+ReactRouter4整合开发"
date: "2025-07-04 14:27:27"
slug: "webpack4react16reactrouter4-zheng-he-kai-fa"
categories: ["技术"]
tags: ["Webpack", "ReactJS", "React-Router"]
aliases:
  - "/2025/07/04/Webpack4+React16+ReactRouter4整合开发/"
  - "/2025/07/04/Webpack4+React16+ReactRouter4整合开发.html"
  - "/Webpack4+React16+ReactRouter4整合开发/"
  - "/Webpack4+React16+ReactRouter4整合开发.html"
  - "/2025/07/04/Webpack4-React16-ReactRouter4整合开发/"
  - "/2025/07/04/Webpack4-React16-ReactRouter4整合开发.html"
  - "/2025/07/04/webpack4react16reactrouter4-zheng-he-kai-fa/"
  - "/2025/07/04/webpack4react16reactrouter4-zheng-he-kai-fa.html"
  - "/webpack4react16reactrouter4-zheng-he-kai-fa.html"
---
这次分享的内容有部分是跟之前的文章【[webpack4手动配置安装react开发](https://www.gowhich.com/blog/825)】大概类似，不同的是这次我们要结合reactr-router进行开发

1、 创建项目并安装

```bash
mkdir webpack4_react16_reactrouter && cd webpack4_react16_reactrouter
```

```bash
npm init -y
```

```bash
npm install react react-dom  prop-types react-router-dom
```

```bash
npm install webpack webpack-cli html-webpack-plugin clean-webpack-plugin webpack-dev-server eslint eslint-plugin-html eslint-plugin-react babel-eslint eslint-config-airbnb eslint-plugin-jsx-a11y eslint-plugin-import babel-core babel-loader babel-plugin-transform-strict-mode babel-plugin-transform-object-assign babel-plugin-transform-decorators-legacy babel-preset-es2015 babel-preset-react babel-preset-stage-0 style-loader css-loader url-loader --save-dev
```

* react开发需要用到的
* babel相关的是用来做es5/es6语法解析的
* eslint相关的是用来做语言检查的

2、eslint和webpack相关配置  
.eslintrc

```json
{
    "env": {
        "browser": true,
        "node": true,
        "es6": true,
        "jquery": true
    },
    "parser": "babel-eslint",
    "plugins": [
        "react",
        "html"
    ],
    "extends": [
        "airbnb"
    ],
    "rules": {
        "no-underscore-dangle": 0
    }
}
```

webpack.config.js

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

let config = {
  entry: {
    app: ['./src/index.jsx'],
  },
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
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      loader: 'babel-loader',
      exclude: [
        path.resolve(__dirname, 'node_modules'),
      ],
      options: {
        plugins: ['transform-async-to-generator', 'transform-strict-mode', 'transform-object-assign', 'transform-decorators-legacy'],
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
  },
};

if (process.env.NODE_ENV === 'production') {
  config = Object.assign({}, config, {
    mode: 'production',
  });
} else {
  config = Object.assign({}, config, {
    mode: 'development',
    devtool: 'eval',
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      compress: true,
      port: 8083,
    },
  });
}

module.exports = config;
```

index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>React + ReactRouter Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <div id="root"></div>
</body>
</html>
```

基本上整个目录结构就搭建完了。还是蛮繁琐的，但是自己了解了其中整个逻辑及流程，对自己是有意的，不过说不好未来就成体系了，直接调用就好了，比如现在的create-react-app，可以直接帮你创建一个项目，很不错的一个选择。  
但是搭建一个符合自己需求的更有价值。  
基本的都弄完了，接下来如何使用ReactRouter呢，先从入口文件开始  
src/index.jsx

```js
import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Link as ALink,
} from 'react-router-dom';

import AppComponent from './components/AppComponent';
import HomeComponent from './components/HomeComponent';
import AboutComponent from './components/AboutComponent';
import TopicsComponent from './components/TopicsComponent';

ReactDOM.render(
  (
    <Router>
      <AppComponent>
        <ul>
          <li><ALink to="/">首页</ALink></li>
          <li><ALink to="/about">关于</ALink></li>
          <li><ALink to="/topics">论题</ALink></li>
        </ul>
        <hr />

        <Route exact path="/" component={HomeComponent} />
        <Route path="/about" component={AboutComponent} />
        <Route path="/topics" component={TopicsComponent} />
      </AppComponent>
    </Router>
  ),
  document.getElementById('root'),
);
```

基本上整个实例是参考了官网的实例，只是针对自己的需求做局部的调整，对于需要使用React开发的同学完全可以入手了，关于数据相关的后面再继续讨论。

这里有个很重要的点，就是在使用webpack-dev-server的使用，当你跳转到某个路由的时候，再刷新会发现页面提示找不到，这个问题这里介绍一个解决方案  
historyApiFallback  
只需要在webpack.config.js中配置下

```js
historyApiFallback: {
  rewrites: [{
    from: /^\/$/,
    to: './index.html',
  },
  ],
},
```

最终的文件结构如下

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

let config = {
  entry: {
    app: ['./src/index.jsx'],
  },
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
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      loader: 'babel-loader',
      exclude: [
        path.resolve(__dirname, 'node_modules'),
      ],
      options: {
        plugins: ['transform-async-to-generator', 'transform-strict-mode', 'transform-object-assign', 'transform-decorators-legacy'],
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
  },
};

if (process.env.NODE_ENV === 'production') {
  config = Object.assign({}, config, {
    mode: 'production',
  });
} else {
  config = Object.assign({}, config, {
    mode: 'development',
    devtool: 'eval',
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      compress: true,
      port: 8083,
      historyApiFallback: {
        rewrites: [{
          from: /^\/$/,
          to: './index.html',
        },
        ],
      },
    },
  });
}

module.exports = config;
```

在运行npm start，修改代码试试，这里强调下版本，如果你的版本比我的新的话，要自己去看下官网的api是否有调整

实例环境，拉取github代码，看package.json，一切尽在你掌握之中  
实例项目地址:

https://github.com/durban89/webpack4-react16-reactrouter-demo.git  
tag: v_1.0.0
