---
title: "Yii Apache 环境下的路由配置"
date: "2025-06-17 18:57:44"
slug: "yii-apache-huan-jing-xia-de-lu-you-pei-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/17/Yii-Apache-环境下的路由配置/"
  - "/2025/06/17/Yii-Apache-环境下的路由配置.html"
  - "/Yii-Apache-环境下的路由配置/"
  - "/Yii-Apache-环境下的路由配置.html"
  - "/2025/06/17/yii-apache-huan-jing-xia-de-lu-you-pei-zhi/"
  - "/2025/06/17/yii-apache-huan-jing-xia-de-lu-you-pei-zhi.html"
  - "/yii-apache-huan-jing-xia-de-lu-you-pei-zhi.html"
---
主配置文件，main.php的组件（components）中开启路由模式

```php
'urlManager' => [
    'urlFormat' => 'path',
    'showScriptName' => false,
    'urlSuffix' => '.html',
    'rules' => [
        '<controller:\w+>/<id:\d+>' => '<controller>/view',
        '<controller:\w+>/<action:\w+>/<id:\d+>' => '<controller>/<action>',
        '<controller:\w+>/<action:\w+>' => '<controller>/<action>',
    ],
],
```

去掉路径中index.php名称

在网站根目录下新键一个.htaccess文件

里面内容：

```apache
* show index.php?
* Options +FollowSymLinks
IndexIgnore *\/*
RewriteEngine on

# if a directory or a file exists, use it directly
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# otherwise forward it to index.php
RewriteRule . index.php
```
