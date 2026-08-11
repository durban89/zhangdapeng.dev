---
title: "Webpack highcharts 打包处理"
date: "2025-07-01 15:24:56"
slug: "webpack-highcharts-da-bao-chu-li"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/01/Webpack-highcharts-打包处理/"
  - "/2025/07/01/Webpack-highcharts-打包处理.html"
  - "/Webpack-highcharts-打包处理/"
  - "/Webpack-highcharts-打包处理.html"
  - "/2025/07/01/webpack-highcharts-da-bao-chu-li/"
  - "/2025/07/01/webpack-highcharts-da-bao-chu-li.html"
  - "/webpack-highcharts-da-bao-chu-li.html"
---
//模块导入 Highcharts

```js
global.HighchartsAdapter = require('exports?HighchartsAdapter!../../bower_components/highcharts/adapters/standalone-framework.src');
module.exports = require('exports?Highcharts!../../bower_components/highcharts/highcharts.src');
```

在entry.js文件中加入这行代码

```js
../../bower_components/highcharts/adapters/standalone-framework.src
../../bower_components/highcharts/highcharts.src
```

这两行在上面的位置代表文件的位置


