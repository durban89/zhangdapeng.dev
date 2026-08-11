---
title: "Webpack hot server 设置"
date: "2025-07-02 11:26:34"
slug: "webpack-hot-server-she-zhi"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/02/Webpack-hot-server-设置/"
  - "/2025/07/02/Webpack-hot-server-设置.html"
  - "/Webpack-hot-server-设置/"
  - "/Webpack-hot-server-设置.html"
  - "/2025/07/02/webpack-hot-server-she-zhi/"
  - "/2025/07/02/webpack-hot-server-she-zhi.html"
  - "/webpack-hot-server-she-zhi.html"
---
使用node的express或connect作为server来启动项目的如何去设置webpack-dev-server

这里举例子说明【为这里使用的是connect，express同理】，三个文件

```js
development.js  //启动文件
webpack.config.development.js //开发模式的配置文件
webpack.dev.server.js //webpack-dev-server 启动的辅助文件
```

先来看development.js文件

```js
'use strict';
var http = require('http');
var connect = require('connect');
var urllib = require('urllib');
var staticServe = require('serve-static');
var finalhandler = require('finalhandler');
var debug = require('debug')('proxy');
var args = require("tinyclap")(); // 启动参数parser
var proxy = require('proxy-middleware');
var path = require('path');
var url = require('url');
var bodyParser = require('body-parser');
var app = connect();
//=====================配置阶段
var config = require('./config');
if (args.argv && args.argv['f']) {
  config = require(args.argv['f']);
}
var stServe = staticServe('./app', {index: 'index.html'});
app.use(bodyParser.urlencoded({extended: false}));
//这里是主要的
// Any requests to localhost:3000/build is proxied
// to webpack-dev-server
require('./webpack.dev.server')(app);
//=====================启动阶段
app.use(function(req, res) {
  var done = finalhandler(req, res);
  stServe(req, res, done);
});
http.createServer(app).listen(config.port);
console.log('Server listen on port %d.', config.port);
```

这里

```js
require('./webpack.dev.server')(app);
```

是关键

再来看webpack.config.development.js：

```js
'use strict';
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var webpack = require('webpack');
var bower_components_dir = path.join(__dirname, 'app/js/bower_components');
module.exports = {
  devtool:'eval',
  entry: {
    'main':[
      "webpack/hot/dev-server",
      'webpack-dev-server/client?http://127.0.0.1:8080',
      './app/js/index.js'
    ] //演示单入口文件
  },
  output: {
    path: path.join(__dirname, 'app/js/out'),  //打包输出的路径
    filename: '[name].js',              //打包后的名字
    publicPath: "/js/out/"                //html引用路径，在这里是本地地址。
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin('common.js'),
    new ExtractTextPlugin("styles.css"),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  ],
  // 新添加的module属性
  module: {
    loaders: [
      {test: /\.es6$/, exclude: /bower_components/, loader: "babel"},
      {test: /\.jsx?$/, exclude: /bower_components/, loader: "jsx-loader?insertPragma=React.DOM&harmony"}
    ]
  }
};
```

这里主要是entry部分和output部分

接下来再看webpack.dev.server.js；

```js
'use strict';
var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config.development');
var proxy = require('proxy-middleware');
var url = require('url');
var urllib = require('urllib');
var debug = require('debug');
module.exports = function(app) {
  //异步 静态文件
  app.use('/js/out', proxy('http://127.0.0.1:8080/js/out'));
  var server = new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    noInfo: false,
    historyApiFallback: true,
    stats: { colors: true },
    headers: { 'Access-Control-Allow-Origin': '*' }
  }).listen(8080, '127.0.0.1', function(err,result) {
    if (err) {
      console.log(err);
    }
    console.log('Webpack Listening at 127.0.0.1:8080');
  });
}
```

这里主要是函数区域部分，做了一个proxy处理，将所有的js和css文件转到webpack-dev-server服务端

最后index.html文件里面的js和css静态文件照常处理就好，只要能解析到/js/out上面就好

