---
title: "RequireJS基础使用配置说明"
date: "2025-06-30 15:15:49"
slug: "requirejs-ji-chu-shi-yong-pei-zhi-shuo-ming"
categories: ["技术"]
tags: ["RequireJS"]
aliases:
  - "/2025/06/30/RequireJS基础使用配置说明/"
  - "/2025/06/30/RequireJS基础使用配置说明.html"
  - "/RequireJS基础使用配置说明/"
  - "/RequireJS基础使用配置说明.html"
  - "/2025/06/30/requirejs-ji-chu-shi-yong-pei-zhi-shuo-ming/"
  - "/2025/06/30/requirejs-ji-chu-shi-yong-pei-zhi-shuo-ming.html"
  - "/requirejs-ji-chu-shi-yong-pei-zhi-shuo-ming.html"
---
之前用过一次，后来想起来用，感觉好麻烦，还需要配置，但是感觉从大局考虑还是没必要偷懒的，那就记录一下吧。

```js
requirejs.config({
  baseUrl: '../components',//相对于此配置文件的库路径
  paths:{//路径是相对于上面的baseUrl
    'Bootstrap':'bootstrap/dist/js/bootstrap.min',
    'jquery':'jquery/dist/jquery.min',
    'chat':'../javascripts/chat',
  },
  //exports值，表明这个模块外部调用时的名称
  shim:{//包含了如何加载库和插件
    Bootstrap:{
      deps:[//deps数组，表明该模块的依赖性，
        'jquery',
        "css!bootstrap/dist/css/bootstrap.min"
      ]
    },
    jquery:{
      deps:[
        'css!../stylesheets/style.css'
      ]
    }
  },
  map: {
    '*': {
      'css': 'require-css/css' // or whatever the path to require-css is
    }
  }
});
require(['jquery','Bootstrap','chat'],function($,bootstrap,Chat){
  var chat = new Chat();
  chat.init();
});
```

几点提示paths的里面的名称不能在shim出现，不然就会变成了变量直接用paths里面的值替换了。

这里的map是为了引入require-css插件，以便可以引入自己需要的css文件。

可以说使用shim非常方便了控制了文件的加载顺序。嘿嘿，对了如果你想处理压缩的话可以参考我的另外一篇文件，搜索Requirejs就可以找到。


