---
title: "webpack4手动配置安装react开发"
date: "2025-07-04 14:27:21"
slug: "webpack4-shou-dong-pei-zhi-an-zhuang-react-kai-fa"
categories: ["技术"]
tags: ["Webpack", "ReactJS"]
aliases:
  - "/2025/07/04/webpack4手动配置安装react开发/"
  - "/2025/07/04/webpack4手动配置安装react开发.html"
  - "/webpack4手动配置安装react开发/"
  - "/webpack4手动配置安装react开发.html"
  - "/2025/07/04/webpack4-shou-dong-pei-zhi-an-zhuang-react-kai-fa/"
  - "/2025/07/04/webpack4-shou-dong-pei-zhi-an-zhuang-react-kai-fa.html"
  - "/webpack4-shou-dong-pei-zhi-an-zhuang-react-kai-fa.html"
---
截止目前，以前都是在使用webpack打包react来进行开发，为了跟随技术的步伐，今天来折腾下新版本的新用法

实践环境

```bash
webpack: 4.9.1
react: 16.4.0
```

1、创建项目并安装

```bash
mkdir webpack4_react16_reactrouter && cd webpack4_react16_reactrouter
```

```bash
npm init -y
```

```bash
npm install react react-dom  prop-types
```

```bash
npm install webpack webpack-cli html-webpack-plugin clean-webpack-plugin webpack-dev-server eslint eslint-plugin-html eslint-plugin-react babel-eslint eslint-config-airbnb eslint-plugin-jsx-a11y eslint-plugin-import babel-core babel-loader babel-plugin-transform-strict-mode babel-plugin-transform-object-assign babel-plugin-transform-decorators-legacy babel-preset-es2015 babel-preset-react babel-preset-stage-0 style-loader css-loader url-loader --save-dev
```

* react开发需要用到的
* babel相关的是用来做es5/es6语法解析的
* eslint相关的是用来做语言检查的

2、eslint、babel和webpack相关配置

.eslintrc

```js
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

.babelrc // 这个文件可以不用加 暂时不起作用

```js
{
    "plugins": [
        "transform-es2015-modules-commonjs"
    ]
}
```

修改webpack.config.js

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

let config = {
  mode: 'production',
  entry: {
    app: ['./src/index.jsx'],
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 8083,
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'React Demo',
      filename: './index.html', // 调用的文件
      template: './index.html', // 模板文件
    }),
  ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
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
  });
}

module.exports = config;
```

下面来修改index.js，修改index.js为index.jsx  
src/index.jsx

```js
import React from 'react';
import ReactDOM from 'react-dom';
import AppComponent from './components/AppComponent';

ReactDOM.render(
  (<AppComponent>React Demo</AppComponent>),
  document.getElementById('root'),
);
```

添加src/components/AppComponent.jsx

```js
import React from 'react';
import PropTypes from 'prop-types';

class AppComponent extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {};
  }

  render() {
    return (
      <div>{this.props.children}</div>
    );
  }
}

AppComponent.propTypes = {
  children: PropTypes.node.isRequired,
};

export default AppComponent;
```

修改index.html，这个只是作为一个模板来使用，具体的后期复杂逻辑，以后的文章分享

```html
<!doctype html>
<html>
  <head>
    <title></title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

项目目录最终的结构

```bash
├── README.md
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── components
│   │   └── AppComponent.jsx
│   ├── data.xml
│   ├── demo-image.png
│   ├── font.woff2
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   ├── glyphicons-halflings-regular.woff2
│   ├── index.css
│   ├── index.jsx
│   └── print.js
└── webpack.config.js
```

运行开发环境的命令

```bash
npm run start 
```

执行后，会看到页面展示React Demo，代表我们的程序加好了，之后可以直接进行相关的开发

```bash
npm run build // 打包
```

```bash
npm run build:package // 压缩打包
```

上面两个都会直接生成dist文件夹，然后里面会生成需要部署的所有文件

项目地址

https://github.com/durban89/webpack4-react16-demo.git

里面有很多细节是在本博客没有的 ，可以自己看下，不懂的可以加群交流。
