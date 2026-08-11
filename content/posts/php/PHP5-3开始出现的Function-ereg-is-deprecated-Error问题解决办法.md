---
title: "PHP5.3开始出现的Function ereg() is deprecated Error问题解决办法"
date: "2025-06-27 10:59:04"
slug: "php53-kai-shi-chu-xian-de-function-ereg-is-deprecated-error-wen-ti-jie-jue-ban-fa"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/PHP5.3开始出现的Function-ereg()-is-deprecated-Error问题解决办法/"
  - "/2025/06/27/PHP5.3开始出现的Function-ereg()-is-deprecated-Error问题解决办法.html"
  - "/PHP5.3开始出现的Function-ereg()-is-deprecated-Error问题解决办法/"
  - "/PHP5.3开始出现的Function-ereg()-is-deprecated-Error问题解决办法.html"
  - "/2025/06/27/PHP5-3开始出现的Function-ereg-is-deprecated-Error问题解决办法/"
  - "/2025/06/27/PHP5-3开始出现的Function-ereg-is-deprecated-Error问题解决办法.html"
  - "/2025/06/27/php53-kai-shi-chu-xian-de-function-ereg-is-deprecated-error-wen-ti-jie-jue-ban-fa/"
  - "/2025/06/27/php53-kai-shi-chu-xian-de-function-ereg-is-deprecated-error-wen-ti-jie-jue-ban-fa.html"
  - "/php53-kai-shi-chu-xian-de-function-ereg-is-deprecated-error-wen-ti-jie-jue-ban-fa.html"
---
PHP 5.3 ereg() 无法正常使用，提示“Function ereg() is deprecated Error”。  
问题根源是php中有两种正则表示方法，一个是posix，一个是perl，php6打算废除posix的正则表示方法所以后来就加了个preg\_match。  
此问题解决办法很简单，在ereg前加个过滤提示信息符号即可：把ereg()变成@ereg()。  
这样屏蔽了提示信息，但根本问题还是没有解决，php在5.2版本以前ereg都使用正常，  
在5.3以后，就要用`preg_match`来代替`ereg`。  
所以就需要变成这样，原来：`ereg("^[0-9]*$",$page)`变成：`preg_match("/^[0-9]*$/",$page) ` 
特别提醒：posix与perl的很明显的表达区别就是是否加斜杠，所以与ereg相比，  
后者在正则的前后分别增加了两个"/"符号，不能缺少。  
Tips:此问题在php5.2之前版本不会出现。

---

参考文章：http://www.liuhuadong.com/archives/727

