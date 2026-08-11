---
title: "Yii-Gii的安装和配置"
date: "2025-06-03 15:05:48"
slug: "yii-gii-de-an-zhuang-he-pei-zhi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii-Gii的安装和配置/"
  - "/2025/06/03/Yii-Gii的安装和配置.html"
  - "/Yii-Gii的安装和配置/"
  - "/Yii-Gii的安装和配置.html"
  - "/2025/06/03/yii-gii-de-an-zhuang-he-pei-zhi/"
  - "/2025/06/03/yii-gii-de-an-zhuang-he-pei-zhi.html"
  - "/yii-gii-de-an-zhuang-he-pei-zhi.html"
---
Gii 是基于 web 的 Yii framework 代码生成器。

开始配置

可以在你的应用程序配置文件中增加以下代码以使用该模块：

```php
'modules' => [
    'gii' => [
        'class' => 'system.gii.GiiModule',
        'username' => 'dev',
        'password' => 'yiidev',
    ],
],
```

运行

打开浏览器，输入 `http://localhost/yourapp/index.php?r=gii`，使用刚才在配置文件中填的 username 和 password 登录。
