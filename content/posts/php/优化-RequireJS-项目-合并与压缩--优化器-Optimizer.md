---
title: "优化 RequireJS 项目（合并与压缩）- 优化器（Optimizer）"
date: "2025-06-30 12:01:15"
slug: "you-hua-requirejs-xiang-mu-he-bing-yu-ya-suo-you-hua-qi-optimizer"
categories: ["技术"]
tags: ["RequireJS"]
aliases:
  - "/2025/06/30/优化-RequireJS-项目（合并与压缩）-优化器（Optimizer）/"
  - "/2025/06/30/优化-RequireJS-项目（合并与压缩）-优化器（Optimizer）.html"
  - "/优化-RequireJS-项目（合并与压缩）-优化器（Optimizer）/"
  - "/优化-RequireJS-项目（合并与压缩）-优化器（Optimizer）.html"
  - "/2025/06/30/优化-RequireJS-项目-合并与压缩-优化器-Optimizer/"
  - "/2025/06/30/优化-RequireJS-项目-合并与压缩-优化器-Optimizer.html"
  - "/2025/06/30/you-hua-requirejs-xiang-mu-he-bing-yu-ya-suo-you-hua-qi-optimizer/"
  - "/2025/06/30/you-hua-requirejs-xiang-mu-he-bing-yu-ya-suo-you-hua-qi-optimizer.html"
  - "/you-hua-requirejs-xiang-mu-he-bing-yu-ya-suo-you-hua-qi-optimizer.html"
---
最近在使用js开发项目，用到了requirejs，到后面会发现好多的js文件要加载，于是找到了优化js的方法，就是使用requirejs自带的Optimizer优化器。

具体操作如下：

*前提是你已经安装了nodejs：*

0.安装requirejs

```bash
sudo cnpm install requirejs -g / cnpm install requirejs -g / npm install requirejs -g /sudo npm install requirejs -g
```

1.构建一个配置文件(相对于执行文件夹)并包含指定的参数，build.js

2.编写build.js，内容如下（仅供参考）：

```js
({
    appDir: './',
    baseUrl: './',
    dir: './dist',
    modules: [
        {
            name: 'main'
        }
    ],
    fileExclusionRegExp: /^(r|build)\.js$/,
    optimizeCss: 'standard',
    removeCombined: true,
    paths: {
        jquery: 'vendor/jquery/dist/jquery.min',
        director: 'vendor/director/build/director.min',
        highcharts: 'vendor/highcharts/highcharts',
        react: 'vendor/react/react.min',
        reactAddons: 'vendor/react/react-with-addons.min',
        JSXTransformer: 'vendor/react/JSXTransformer',
        cookieStorage: 'vendor/cookie-storage/dist/cookie-storage',
        json2: 'vendor/json/json2',
        xdate: 'vendor/xdate/src/xdate',
        moment: 'vendor/moment/min/moment.min',
        jPages: 'vendor/jPages/js/jPages',
        numberFormat: 'vendor/number-format.js/lib/format.min',
        bootstrap:'vendor/bootstrap/dist/js/bootstrap.min',
        datetimepicker:'vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker',
        datetimepickerLanguage:'vendor/bootstrap-datetimepicker/js/locales/bootstrap-datetimepicker.zh-CN',
        fancybox:'vendor/fancybox/source/jquery.fancybox.pack',
        async:'vendor/async/lib/async'
    },
    shim: {
        'highcharts': {
            'deps': ['jquery'],
            'exports': 'Highcharts'      // Still gotta make this available //使用全局的Highcharts做为模块名称
        },
        'datetimepickerLanguage':{//因datetimepickerLanguage依赖datetimepicker,所以次代码是优先加载datetimepicker
            'deps':['datetimepicker']
        },
        'datetimepicker':{
            'deps':['css!vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min']
        },
        'bootstrap':{
            'deps':['jquery']
        },
        'fancybox':{
            'deps':[
                'jquery',
                'css!vendor/fancybox/source/jquery.fancybox.css'
            ]
        },
        'async':{
            'deps':[
                'vendor/async/deps/nodeunit',
                'css!vendor/async/deps/nodeunit.css'
            ]
        }
    },
    map: {
        '*': {
            'css': 'vendor/require-css/css'
        }
    }
})
```

3.执行命令

```bash
r.js -o build.js
```


