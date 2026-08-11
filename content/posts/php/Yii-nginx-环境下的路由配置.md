---
title: "Yii nginx 环境下的路由配置"
date: "2025-06-17 18:57:40"
slug: "yii-nginx-huan-jing-xia-de-lu-you-pei-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/17/Yii-nginx-环境下的路由配置/"
  - "/2025/06/17/Yii-nginx-环境下的路由配置.html"
  - "/Yii-nginx-环境下的路由配置/"
  - "/Yii-nginx-环境下的路由配置.html"
  - "/2025/06/17/yii-nginx-huan-jing-xia-de-lu-you-pei-zhi/"
  - "/2025/06/17/yii-nginx-huan-jing-xia-de-lu-you-pei-zhi.html"
  - "/yii-nginx-huan-jing-xia-de-lu-you-pei-zhi.html"
---
### [Nginx配置](#1)

在nginx.conf的server {段添加类似如下代码：  
Nginx.conf代码:

```nginx
location / {
    if (!-e $request_filename){#必须有空格
        rewrite ^/(.*) /index.php last;
    }
}
```

### [在Yii的protected/conf/main.php去掉如下的注释](#2)

Php代码:

```php
'urlManager'=>array(
	'urlFormat'=>'path',
	'rules'=>array(
		'/'=>'/view',
		'//'=>'/',
		'/'=>'/',
	),
),
```
