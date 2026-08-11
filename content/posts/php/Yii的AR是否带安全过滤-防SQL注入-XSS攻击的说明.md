---
title: "Yii的AR是否带安全过滤 防SQL注入 XSS攻击的说明"
date: "2025-06-18 11:28:12"
slug: "yii-de-ar-shi-fou-dai-an-quan-guo-lv-fang-sql-zhu-ru-xss-gong-ji-de-shuo-ming"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/18/Yii的AR是否带安全过滤-防SQL注入-XSS攻击的说明/"
  - "/2025/06/18/Yii的AR是否带安全过滤-防SQL注入-XSS攻击的说明.html"
  - "/Yii的AR是否带安全过滤-防SQL注入-XSS攻击的说明/"
  - "/Yii的AR是否带安全过滤-防SQL注入-XSS攻击的说明.html"
  - "/2025/06/18/yii-de-ar-shi-fou-dai-an-quan-guo-lv-fang-sql-zhu-ru-xss-gong-ji-de-shuo-ming/"
  - "/2025/06/18/yii-de-ar-shi-fou-dai-an-quan-guo-lv-fang-sql-zhu-ru-xss-gong-ji-de-shuo-ming.html"
  - "/yii-de-ar-shi-fou-dai-an-quan-guo-lv-fang-sql-zhu-ru-xss-gong-ji-de-shuo-ming.html"
---
关于这个说明，我引用了www.yiiframework.com 里面的qiang哥的

提到了两个问题：一是SQL Injection攻击，一个是XSS攻击。

> 对于前者，需要避免的是直接把用户输入嵌入到SQL里，例如："`SELECT * FROM tbl_user WHERE id={$_GET['id']}`"。  
> 恶意用户可以让`$_GET['id']`等于"`1; DELETE FROM tbl_user`"，这样就把所有的用户数据都删除了！非常危险！  
>   
> 解决办法有好几种。最简单的就是用param binding，请阅读PHP PDO获得相关知识。如果知道id是整数，也可以先把输入强制为整数。或者如果id是字串，可以用`CDbConnection::quoteValue()`把输入加上引号。如果你用的是AR，那么save()函数自动会使用param binding。如果你用findAll()之类的函数，自己生成condition部分，那就要特别小心不要直接嵌入输入。  
>   
> XSS攻击主要是要避免直接显示用户的输入数据。例如echo $user->description（假设description的数据来自用户的输入）。恶意用户可以让id为一段js代码，使得其它用户查看该页面后隐式执行该代码，从而被恶意用户获得登录cookie等安全信息。  
>
> 解决办法很简单，就是用`CHtml::encode()`。如果输入是HTML，可以用`CHtmlPurifier::purify()`来过滤有害代码。

