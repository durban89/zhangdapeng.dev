---
title: "Yii 获取当前控制器和动作名"
date: "2025-06-17 17:19:48"
slug: "yii-huo-qu-dang-qian-kong-zhi-qi-he-dong-zuo-ming"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/17/Yii-获取当前控制器和动作名/"
  - "/2025/06/17/Yii-获取当前控制器和动作名.html"
  - "/Yii-获取当前控制器和动作名/"
  - "/Yii-获取当前控制器和动作名.html"
  - "/2025/06/17/yii-huo-qu-dang-qian-kong-zhi-qi-he-dong-zuo-ming/"
  - "/2025/06/17/yii-huo-qu-dang-qian-kong-zhi-qi-he-dong-zuo-ming.html"
  - "/yii-huo-qu-dang-qian-kong-zhi-qi-he-dong-zuo-ming.html"
---
我的总结是这样的：

1. 获取控制器名

```php
$this->controller = Yii::app()->controller->id;
```

2. 获取动作名

```php
$this->action = Yii::app()->controller->action->id;
```

参考的原文是这样的：

> 1. 获取控制器名

> 在控制器中获取控制器名:

> $name = $this->getId();

> 在视图中获取控制器名:

> $name = Yii::app()->controller->id;

> 2. 获取动作名

> 在控制器beforeAction()回调函数中获取动作名:

> $name = $action->id;

> 在其他地方获取动作名:

> $name = $this->getAction()->getId();

我试过几个，有几个不是很好用，但是我的总结里面是绝对可以使用的，因为是一个全局变量。
