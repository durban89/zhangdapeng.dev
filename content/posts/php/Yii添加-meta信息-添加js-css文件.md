---
title: "Yii添加 meta信息，添加js，css文件"
date: "2025-06-20 14:13:44"
slug: "yii-tian-jia-meta-xin-xi-tian-jia-js-css-wen-jian"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii添加-meta信息，添加js，css文件/"
  - "/2025/06/20/Yii添加-meta信息，添加js，css文件.html"
  - "/Yii添加-meta信息，添加js，css文件/"
  - "/Yii添加-meta信息，添加js，css文件.html"
  - "/2025/06/20/Yii添加-meta信息-添加js-css文件/"
  - "/2025/06/20/Yii添加-meta信息-添加js-css文件.html"
  - "/2025/06/20/yii-tian-jia-meta-xin-xi-tian-jia-js-css-wen-jian/"
  - "/2025/06/20/yii-tian-jia-meta-xin-xi-tian-jia-js-css-wen-jian.html"
  - "/yii-tian-jia-meta-xin-xi-tian-jia-js-css-wen-jian.html"
---
其实很简答的，只要你想加入类似keywords或者content的内容的meta的话是很简单的，代码如下：

```php
Yii::app()->clientScript->registerMetaTag('Content description ',"description");
Yii::app()->clientScript->registerMetaTag("新媒体指数、[name]vlinkage投票排名[rank]","keywords");
```

添加js，css文件

```php
Yii::app()->clientScript->registerCssFile(Yii::app()->baseUrl.'/css/my.css');
Yii::app()->clientScript->registerScriptFile(Yii::app()->baseUrl.'/css/my.js');
```
