---
title: "Yii路径知识点摘要"
date: "2025-06-17 17:19:59"
slug: "yii-lu-jing-zhi-shi-dian-zhai-yao"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/17/Yii路径知识点摘要/"
  - "/2025/06/17/Yii路径知识点摘要.html"
  - "/Yii路径知识点摘要/"
  - "/Yii路径知识点摘要.html"
  - "/2025/06/17/yii-lu-jing-zhi-shi-dian-zhai-yao/"
  - "/2025/06/17/yii-lu-jing-zhi-shi-dian-zhai-yao.html"
  - "/yii-lu-jing-zhi-shi-dian-zhai-yao.html"
---
如果是 // 就会默认去调用protected/views/layouts，//代表 绝对路径  
其实 就是 绝对和相对的关系/代表相对路径,如module/user下的layout  
用单斜杠的话默认会先找当前已经激活的模块底下的view,若当前未有激活的模块则从系统根目录下开始找,双斜杠的话就直接从系统根下开始找

### [Yii framework已经定义的命名空间常量](#1)

**system: 指向Yii框架目录; YII\framework**  
**zii: 指向zii library 目录; YII\framework\zii**  
**application : 指向应用程序基本目录; protected\**  
**webroot: 指向包含里入口脚本 文件的目录. 此别名自 1.0.3 版起生效. \**  
**ext : 指向包含所有第三方扩展的目录, 从版本 1.0.8 可用; \protected\extensions**

```php
Yii::getPathOfAlias('zii'); 
Yii::import ('zii.*');
Yii::setPathOfAlias('backend', $backend); 
'import' => [
    'backend.models.*', 
]
```

应用的主目录是指包含所有安全系数比较高的PHP代码和数据的根目录。在默认情况下，这个目录一般是入口代码所在目录的一个目录： protected 。这个路径可以通过在application configuration里设置 basePath来改变.  
YII framework路径

```php
Yii::getFrameworkPath()
```

protected/runtime


```php
Yii::app()->getRuntimePath();
```

protected/venders目录

```php
Yii::import('application.venders.*');
```

或在protected/config/main.php说明

```php
'import '=> [   
    // ......    
    'application.venders.*',    
],
```

插入meta信息


```php
Yii::app()->clientScript->registerMetaTag('关键字','keywords');  
Yii::app()->clientScript->registerMetaTag('一些描述','description');  
Yii::app()->clientScript->registerMetaTag('作者','author');  
Yii::app()->clientScript->registerMetaTag(' text/html;charset=utf-8', null, 'Content-Type');  
//<link rel="alternate" type="application/rss+xml" href="http://www.dreamdu.com/feed/" />
Yii::app()->clientScript->registerLinkTag('alternate','application/rss+xml',$this->createUrl('/feed'));
```

如何在控制器添加CSS文件或JavaScript文件

```php
Yii::app()->clientScript->registerCssFile(Yii::app()->baseUrl.'/css/my.css');  
Yii::app()->clientScript->registerScriptFile(Yii::app()->baseUrl.'/css/my.js');  
<?php echo $this->module->assetsUrl; ?>/css/main.css  
//调用YII框架中framework/web/js/source的js,其中registerCoreScript key调用的文件在framework/web/js/packages.php列表中可以查看
Yii::app()->clientScript->registerCoreScript('jquery');
```

在view中得到当前controller的ID方法：

```php
Yii::app()->getController()->id;  
```

在view中得到当前action的ID方法：

```php
Yii::app()->getController()->getAction()->id;  
```

yii获取ip地址

```php
Yii::app()->request->userHostAddress; 
```

yii判断提交方式

```php
Yii::app()->request->isPostRequest 
```

得到当前域名:

```php
Yii::app()->request->hostInfo
```

得到proteced目录的物理路径

```php
YII::app()->basePath; 
```

获得上一页的url以返回

```php
Yii::app()->request->urlReferrer; 
```

得到当前url

```php
Yii::app()->request->url; 
```

得到当前home url

```php
Yii::app()->homeUrl 
```

得到当前return url

```php
Yii::app()->user->returnUrl 
```

项目路径

```php
dirname(Yii::app()->BasePath)  
Yii::app()->getBaseUrl(true);  
<?php echo $this->getLayoutFile('main'); ?>
$this->redirect('index.php?r=admin/manage');
```

`createUrl()`

```php
echo $this->createUrl('urlBoyLeeTest');  
//out => /yii_lab/index.php?r=lab/urlBoyLeeTest  
$this->createUrl('post/read') // /index.php/post/read  
<?php echo Yii::app()->request->baseUrl; ?>/css/screen.css  
Yii::app()->theme->baseUrl.'/images/FileName.gif'
```

`createAbsoluteUrl()`

```php
echo $this->createAbsoluteUrl('urlBoyLeeTest');  
//out => http://localhost/yii_lab/index.php?r=lab/urlBoyLeeTest
```

