---
title: "webpack分离css单独打包"
date: "2025-07-01 15:25:05"
slug: "webpack-fen-li-css-dan-du-da-bao"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/01/webpack分离css单独打包/"
  - "/2025/07/01/webpack分离css单独打包.html"
  - "/webpack分离css单独打包/"
  - "/webpack分离css单独打包.html"
  - "/2025/07/01/Webpack分离css单独打包/"
  - "/2025/07/01/Webpack分离css单独打包.html"
  - "/2025/07/01/webpack-fen-li-css-dan-du-da-bao/"
  - "/2025/07/01/webpack-fen-li-css-dan-du-da-bao.html"
  - "/webpack-fen-li-css-dan-du-da-bao.html"
---
这个操作很简单的，只需要一个插件就好了，就是extract-text-webpack-plugin

1，安装extract-text-webpack-plugin

```bash
cnpm install extract-text-webpack-plugin --save-dev
```

2,配置文件添加对应配置

首先require一下

```js
var ExtractTextPlugin = require("extract-text-webpack-plugin");
```

plugins里面添加

```js
new ExtractTextPlugin("styles.css"),
```

我这里如下：

```js
plugins: [
  new webpack.optimize.CommonsChunkPlugin('common.js'),
  new ExtractTextPlugin("styles.css"),
],
```

modules里面对css的处理修改为

```js
{test:/\.css$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader")},
```

千万不要重复了，不然会不起作用的

我这里如下：

```js
module: {
  loaders: [
    {test:/\.css$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader")},
    {test: /\.scss$/, loader: "style!css!sass"},
    {test: /\.less$/, loader: "style!css!less"},
  ]
},
```

3，在引入文件里面添加需要的css，【举例如下】

```js
require('../less/app.less');
require('./bower_components/bootstrap-select/dist/css/bootstrap-select.min.css');
require('./bower_components/fancybox/source/jquery.fancybox.css');
```


