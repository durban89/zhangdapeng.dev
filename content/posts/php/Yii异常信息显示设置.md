---
title: "Yii异常信息显示设置"
date: "2025-06-25 10:09:34"
slug: "yii-yi-chang-xin-xi-xian-shi-she-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/25/Yii异常信息显示设置/"
  - "/2025/06/25/Yii异常信息显示设置.html"
  - "/Yii异常信息显示设置/"
  - "/Yii异常信息显示设置.html"
  - "/2025/06/25/yii-yi-chang-xin-xi-xian-shi-she-zhi/"
  - "/2025/06/25/yii-yi-chang-xin-xi-xian-shi-she-zhi.html"
  - "/yii-yi-chang-xin-xi-xian-shi-she-zhi.html"
---
### [第一步：log设置](#1)

```php
'log'=>array(
	'class'=>'CLogRouter',
	'routes'=>array(
		array(
			'class'=>'CFileLogRoute',
			'levels'=>'error, warning',
		),
        array(
            'class' => 'CProfileLogRoute',//显示页面加载的整个流程，包括mysql语句
            'levels' => 'profile',
        ),
        // array(
                // 'class' => 'CWebLogRoute',
                // 'levels' => 'profile,trace',
        // ),
		// uncomment the following to show log messages on web pages
		array(
			'class'=>'CWebLogRoute',
            'levels'=>'profile,error,warning,trace,info,xdebug',
            'showInFireBug'=>'true',//开启浏览器的firedebug
		),
		
	),
),
```

在log中添加

```php
array(
	'class'=>'CWebLogRoute',
    'levels'=>'profile,error,warning,trace,info,xdebug',
    'showInFireBug'=>'true',//开启浏览器的firedebug
),
```

'showInFireBug'=>'true'的使用必须开启浏览器的firebug

### [第二步：调试](#2)

开启浏览器，进行测试网站

从浏览器的firebug中可以看到，所有开启的错误提示

