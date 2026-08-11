---
title: "Yii路由跳转forward/redirect"
date: "2025-06-20 14:13:40"
slug: "yii-lu-you-tiao-zhuan-forwardredirect"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii路由跳转forward/redirect/"
  - "/2025/06/20/Yii路由跳转forward/redirect.html"
  - "/Yii路由跳转forward/redirect/"
  - "/Yii路由跳转forward/redirect.html"
  - "/2025/06/20/Yii路由跳转forward-redirect/"
  - "/2025/06/20/Yii路由跳转forward-redirect.html"
  - "/2025/06/20/yii-lu-you-tiao-zhuan-forwardredirect/"
  - "/2025/06/20/yii-lu-you-tiao-zhuan-forwardredirect.html"
  - "/yii-lu-you-tiao-zhuan-forwardredirect.html"
---
关于Yii中的url的跳转，有两个方法，第一个是Redirect,第二个是Forward

### [Yii的Rediret](#1)

使用方法

```php
$this->redirect(array('index'));
```

对应的是当前controller的index action

http://www.localyii.com/testwebap/index.php?r=user/index

```php
$this->redirect(array('view','id'=>$model->id));
```

对应的是当前controller的view action并传递id参数值为3  
  
http://www.localyii.com/testwebap/index.php?r=user/view&id=3

```php
$this->redirect(array('/site/contact','id'=>12));
$this->redirect(array('site/contact','id'=>12));
```

http://www.localyii.com/testwebap/index.php?r=site/contact&id=12

```php
$this->redirect(array('site/contact','id'=>'idv','name'=>'namev'));
```

http://www.localyii.com/testwebap/index.php?r=site/contact&id=idv&name=namev

```php
$this->redirect(array('site/contact','v1','v2','v3'));
```

http://www.localyii.com/testwebap/index.php?r=site/contact&0=v1&1=v2&2=v3

```php
$this->redirect(array('site/contact','v1','v2','v3','#'=>'ttt'));
```

带anchor的  
http://www.localyii.com/testwebap/index.php?r=site/contact&0=v1&1=v2&2=v3#ttt

```php
$this->redirect(array('user/create','v1','v2','v3','#'=>'ttt'));
```

http://www.localyii.com/testwebap/index.php?r=user/create&0=v1&1=v2&2=v3#ttt  
modules的redirect

```php
$this->redirect(array('testmod/default/index','v1','v2','v3','#'=>'ttt'));
```

http://www.localyii.com/testwebap/index.php?r=testmod/default/index&0=v1&1=v2&2=v3#ttt  
跳转到一个绝对路径

```php
$this->redirect('http://www.baidu.com');
```

函数的原型是

```php
public function redirect($url,$terminate=true,$statusCode=302)
{
    if(strpos($url,'/')===0)
        $url=$this->getHostInfo().$url;
    header('Location: '.$url, true, $statusCode);
    if($terminate)
        Yii::app()->end();
}
```

### [Yii的forward](#2)

```php
$this->forward('/testmod/default/index');

$this->forward('testmod/default/index');
```

地址栏url

http://www.localyii.com/testwebap/index.php

forward是不需要参数的

函数的原型是：

```php
public function forward($route,$exit=true)
{
    if(strpos($route,'/')===false)
        $this->run($route);
    else
    {
        if($route[0]!=='/' && ($module=$this->getModule())!==null)
            $route=$module->getId().'/'.$route;
        Yii::app()->runController($route);
    }
    if($exit)
        Yii::app()->end();
}
```

### [forward和redirect的区别显而易见](#3)

1，浏览器url地址

2，是否支持绝对地址

3，是否传递参数
