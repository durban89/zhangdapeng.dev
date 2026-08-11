---
title: "ThinkPHP CSS js image 等文件 简单配置"
date: "2025-06-25 10:26:04"
slug: "thinkphp-css-js-image-deng-wen-jian-jian-dan-pei-zhi"
categories: ["技术"]
tags: ["PHP", "ThinkPHP"]
aliases:
  - "/2025/06/25/ThinkPHP-CSS-js-image-等文件-简单配置/"
  - "/2025/06/25/ThinkPHP-CSS-js-image-等文件-简单配置.html"
  - "/ThinkPHP-CSS-js-image-等文件-简单配置/"
  - "/ThinkPHP-CSS-js-image-等文件-简单配置.html"
  - "/2025/06/25/thinkphp-css-js-image-deng-wen-jian-jian-dan-pei-zhi/"
  - "/2025/06/25/thinkphp-css-js-image-deng-wen-jian-jian-dan-pei-zhi.html"
  - "/thinkphp-css-js-image-deng-wen-jian-jian-dan-pei-zhi.html"
---
首先介绍一下Thinkphp的目录结构

```shell
|--ThinkPHP（ThinkPHP目录）

|--Financial(项目目录)

    |--Common

    |--Conf

    |--Lang

    |--Lib

    |--Public

        |--Css

        |--Js

        |--Images

        |--Bootstrap

    |--Runtime

    |--Tpl

    |--Uploads

    index.php

    favicon.ico
```

目录结构如上：

index.php的文件配置如下：

```php
<?php
define('APP_NAME','');
define('APP_PATH','/home/davidzhang/local.ubuntu.new.financial.com/');
define('APP_DEBUG',TRUE); // 开启调试模式
require '../ThinkPHP/ThinkPHP.php';
?>
```

/home/davidzhang/local.ubuntu.new.financial.com/

这个目录是我项目的根目录

ok，之后是这些静态文件在项目中的引用，如下：

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
       <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
       <link href='__PUBLIC__/bootstrap/css/bootstrap.min.css' type='text/css' rel='stylesheet'/>
       <link href='__PUBLIC__/css/google-bootstrap.css' type='text/css' rel='stylesheet'/>
       <script src='__PUBLIC__/bootstrap/js/bootstrap.min.js' type='text/javascript'></script>
       <title>漫步者-财务管家</title>
    </head>
    <body>
        <div class='container-fluid'>
            <!-- 导航区 -->
            <div class='header'>
                <p>{$title}</p>
            </div>
            <!-- 内容区 -->
            <div class='container-fluid'>
                <div class='row-fluid'>
                   <div class='span12'>
                       <p>详细的内容展示</p>
                   </div>
                </div>
            </div>
            
            <!-- 脚步区 -->
            <div class='footer'>
               @Copyright2013 漫步者-财务管家
            </div>
        </div>
    </body>
</html>
```

欢迎指正。

