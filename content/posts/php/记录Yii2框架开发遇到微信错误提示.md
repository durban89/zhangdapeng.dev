---
title: "记录Yii2框架开发遇到微信错误提示"
date: "2025-07-08 15:15:56"
slug: "ji-lu-yii2-kuang-jia-kai-fa-yu-dao-wei-xin-cuo-wu-ti-shi"
categories: ["技术"]
tags: ["Yii", "PHP"]
aliases:
  - "/2025/07/08/记录Yii2框架开发遇到微信错误提示/"
  - "/2025/07/08/记录Yii2框架开发遇到微信错误提示.html"
  - "/记录Yii2框架开发遇到微信错误提示/"
  - "/记录Yii2框架开发遇到微信错误提示.html"
  - "/2025/07/08/ji-lu-yii2-kuang-jia-kai-fa-yu-dao-wei-xin-cuo-wu-ti-shi/"
  - "/2025/07/08/ji-lu-yii2-kuang-jia-kai-fa-yu-dao-wei-xin-cuo-wu-ti-shi.html"
  - "/ji-lu-yii2-kuang-jia-kai-fa-yu-dao-wei-xin-cuo-wu-ti-shi.html"
---
> 微信公共号开发，提示“该公众号暂时无法提供服务，请稍后再试”，如何解决？

以前使用Yii框架的时候，并没有像Yii2，以前的Yii框架似乎用起来在安全方面不如Yii2，后面在用Yii2的时候发现了一个有趣的事情。  
以前在用Yii框架做微信方面的开发的时候，开发模式需要添加对应的接口。  
这里一定要注意点的点是在做接口验证的时候是使用GET请求，这个毫无疑问没有任何问题，但是在验证完之后，进行接口上面的交互的时候就有问题了，使用的POST的请求。  
如果是以前的Yii的话，如果没有做严格的post请求的csrf验证的话，应该都是正常的。  
但是使用Yii2之后就会有问题，如下

```php
'request' => [
    'cookieValidationKey' => 'xxxxxx',
    'csrfParam' => 'xxxxxx',
],
```

这里的配置，我记得官网的例子或者是在使用Yii2创建项目之后就会添加这一部分，这个会导致在所有的Conroller写的action，post请求接收的时候系统会默认做csrf安全验证，导致在做微信开发的时候，这块post的请求也失效了，当时在action中加了log日志，很奇怪为什么action的方法也不执行。  
解决办法如下  
在对应的Controller中添加

```php
public $enableCsrfValidation = false;
```

这个是将请求的csrf验证做了关闭，也就是说所有请求到这个Controller的都不会做csrf的验证。这块的安全看来还是要通过其他方式避免一下，针对微信端的请求做处理，以实现安全的防护。

当然到这里说的也就只有程序上的问题，如果是真实的微信公众号的问题，那就只能找找微信客服解决了。

PS:  
现在的客服全都机器的，问一句根本不知道你想要啥，说实话还是喜欢跟人工客服打交道，人跟人交流不能退缩到原始，见面就只是哼哼，时代的进步不代表要减少沟通。
