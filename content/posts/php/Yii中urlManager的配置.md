---
title: "Yii中urlManager的配置"
date: "2025-05-29 14:30:29"
slug: "yii-zhong-urlmanager-de-pei-zhi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/05/29/Yii中urlManager的配置/"
  - "/2025/05/29/Yii中urlManager的配置.html"
  - "/Yii中urlManager的配置/"
  - "/Yii中urlManager的配置.html"
  - "/2025/05/29/yii-zhong-urlmanager-de-pei-zhi/"
  - "/2025/05/29/yii-zhong-urlmanager-de-pei-zhi.html"
  - "/yii-zhong-urlmanager-de-pei-zhi.html"
---
第一步：

在main.php配置文件的component域中添加urlManager模块，并加入urlrules.

引入rule文件，代码如下

```php
$urls = include(dirname(__FILE__) . '/urlrules.php');
urlManager配置修改如下

'urlManager'=>array(
    'urlFormat' => 'path',
    'showScriptName' => false,//隐藏index.php 
    'urlSuffix' => '.html',//后缀 
    'rules' => $urls,
),
```

第二步:在同级目录下写urlrules.php.如：

```php
return array(
    '/index.html' => 'site/index', //首页
    'search' => 'search/index'，

);
```

第三步，当然是配置服务器的rewrite模块，使得入口为index.php

1)apache下，在网站根目录下建立.htaccess如下:

```bash
Options +FollowSymLinks 

IndexIgnore */* 

RewriteEngine on  
# if a directory or a file exists, use it directly 
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

RewriteRule . index.php
```

2) nginx下在php配置模块和location模块添加rewrite如下：

```bash
location / {
    root   /home/george/workspace/EclipsePHP/webroot;
    index  index.html index.php index.htm;
    #try_files $uri $uri/ @rewrite;
    if (!-f $request_filename){
        rewrite (.*) /index.php;
    }
}
location ~ \.php$ {
    root            /home/george/workspace/EclipsePHP/webroot;
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME   /home/george/workspace/EclipsePHP/webroot$fastcgi_script_name;
    include        fastcgi_params;
    if (!-f $request_filename){
        rewrite (.*) /index.php;
    }
}
```

完了，再看看你的网站的url 是不是漂亮了不少，同行努力！
