---
title: "Webpack 打包jsx文件配置"
date: "2025-07-01 15:25:02"
slug: "webpack-da-bao-jsx-wen-jian-pei-zhi"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/01/Webpack-打包jsx文件配置/"
  - "/2025/07/01/Webpack-打包jsx文件配置.html"
  - "/Webpack-打包jsx文件配置/"
  - "/Webpack-打包jsx文件配置.html"
  - "/2025/07/01/webpack-da-bao-jsx-wen-jian-pei-zhi/"
  - "/2025/07/01/webpack-da-bao-jsx-wen-jian-pei-zhi.html"
  - "/webpack-da-bao-jsx-wen-jian-pei-zhi.html"
---
打包jsx文件，为了使得此文件可以直接被打包，并且在应用的时候不加入后缀，需要做以下几个步骤：

1，安装jsx-loader

```bash
$ npm install --save-dev jsx-loader
```

2，配置

```js
module: {
  loaders: [
    {
      //tell webpack to use jsx-loader for all *.jsx files
      test: /\.jsx$/,
      loader: 'jsx-loader?insertPragma=React.DOM&harmony'
    }
  ]
},
```

3，扩展设置

```js
resolve: {
  extensions: ['', '.js', '.jsx']
}
```


