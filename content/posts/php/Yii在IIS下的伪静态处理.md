---
title: "Yii在IIS下的伪静态处理"
date: "2025-06-03 15:09:10"
slug: "yii-zai-iis-xia-de-wei-jing-tai-chu-li"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii在IIS下的伪静态处理/"
  - "/2025/06/03/Yii在IIS下的伪静态处理.html"
  - "/Yii在IIS下的伪静态处理/"
  - "/Yii在IIS下的伪静态处理.html"
  - "/2025/06/03/yii-zai-iis-xia-de-wei-jing-tai-chu-li/"
  - "/2025/06/03/yii-zai-iis-xia-de-wei-jing-tai-chu-li.html"
  - "/yii-zai-iis-xia-de-wei-jing-tai-chu-li.html"
---
Yii在IIS下的伪静态处理是，在根目录建立httpd.ini文件，然后使用IIS的伪静态规则，写入自己需要的规则：

我购买的虚拟主机在香港，因为windows的主机比较多，于是我也中招了，于是四处寻求方法，四处尝试，终于找到了适合Yii的伪静态规则：

代码如下：

```bash
[ISAPI_Rewrite]
# 3600 = 1 hour
CacheClockRate 3600
RepeatLimit 32
RewriteEngine On
#伪静态规则
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)/(.*)$ $1/index.php?$2
RewriteRule !\.(js|ico|gif|jpe?g|bmp|png|css)$ index.php [L]
我在虚拟机上测试通过了，哈哈，希望对你也有用

```
