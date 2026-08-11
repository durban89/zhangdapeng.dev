---
title: "Webpack4+React16+ReactRouter4+Redux整合开发 - Redux Logger日志相关配置"
date: "2025-07-04 14:27:37"
slug: "webpack4react16reactrouter4redux-zheng-he-kai-fa-redux-logger-ri-zhi-xiang-guan-pei-zhi"
categories: ["技术"]
tags: ["Webpack", "ReactJS", "React-Router", "Redux"]
aliases:
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发-Redux-Logger日志相关配置/"
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发-Redux-Logger日志相关配置.html"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发-Redux-Logger日志相关配置/"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发-Redux-Logger日志相关配置.html"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发-Redux-Logger日志相关配置/"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发-Redux-Logger日志相关配置.html"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa-redux-logger-ri-zhi-xiang-guan-pei-zhi/"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa-redux-logger-ri-zhi-xiang-guan-pei.html"
  - "/webpack4react16reactrouter4redux-zheng-he-kai-fa-redux-logger-ri-zhi-xiang-guan-pei-zhi.html"
---
之前的几篇文章继承了redux，这里不得不说下与redux开发相关的一些配置redux-logger，其实有很多，也有另外一种方式，这里我觉得这个是比较好的，这里做下记录，跟大家分享下。

首先clone代码

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git redux-devtools
cd redux-devtools
npm install 

npm start
```

然后安装redux-logger

```bash
npm install redux-logger
```

打开src/index.jsx  
引入redux-logger

```js
import { createLogger } from 'redux-logger';
```

更新修改代码结果如下

```js
const middleware = [];
if (typeof __DEV__ !== 'undefined') {
  middleware.push(createLogger()); // 创建日志
}
// 为了添加多个中间件 我们重新改造middleware
middleware.push(routerMiddleware(history));

// 这行是DevTools的配置 后面做详细说明
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  connectRouter(history)(rootReducer),
  initialState,
  composeEnhancer(applyMiddleware(...middleware)), // 中间件引入
);
```

日志一般是在开发环境中使用，我们需要加个变量来做下控制，这里通过修改webpack.config.js中的plugins加入

```js
new webpack.DefinePlugin({
  'global.GENTLY': false,
  __DEV__: true,
})
```

配置完结果如下

```js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

let config = {
  entry: {
    app: [
      'webpack/hot/only-dev-server',
      'react-hot-loader/patch',
      './src/index.jsx',
    ],
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

if (process.env.NODE_ENV === 'production') {
  config = Object.assign({}, config, {
    mode: 'production',
  });
} else {
  const {
    plugins,
  } = config;
  plugins.push(new webpack.DefinePlugin({
    'global.GENTLY': false,
    __DEV__: true,
  }));
  config = Object.assign({}, config, {
    mode: 'development',
    devtool: 'eval',
    devServer: {
      hot: true,
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
    plugins,
  });
}

module.exports = config;
```

重新执行

```bash
npm start
```

打开计数器，通过chrome的devtools可以看到类似如下图的日志，这样我们在做数据交互的时候就能清晰的了解到具体的数据调用情况

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528643041/gowhich/WX20180610-085442_2x.png)

这里前提说下，Chrome浏览器最好是安装下redux的Chrome扩展，不知道的可自行百度或google下，后面的文章有需要的话，在详细说下。

实践项目地址

<https://github.com/durban89/webpack4-react16-reactrouter-demo.git>

tag:[v_1.0.3](https://github.com/durban89/webpack4-react16-reactrouter-demo/releases/tag/v_1.0.3)
