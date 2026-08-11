---
title: "Nodejs 实现 通过POP3协议进行邮件的收取【指定日期范围】"
date: "2025-06-30 14:31:10"
slug: "nodejs-shi-xian-tong-guo-pop3-xie-yi-jin-xing-you-jian-de-shou-qu-zhi-ding-ri-qi-fan-wei"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-实现-通过POP3协议进行邮件的收取【指定日期范围】/"
  - "/2025/06/30/Nodejs-实现-通过POP3协议进行邮件的收取【指定日期范围】.html"
  - "/Nodejs-实现-通过POP3协议进行邮件的收取【指定日期范围】/"
  - "/Nodejs-实现-通过POP3协议进行邮件的收取【指定日期范围】.html"
  - "/2025/06/30/Nodejs-实现-通过POP3协议进行邮件的收取-指定日期范围/"
  - "/2025/06/30/Nodejs-实现-通过POP3协议进行邮件的收取-指定日期范围.html"
  - "/2025/06/30/nodejs-shi-xian-tong-guo-pop3-xie-yi-jin-xing-you-jian-de-shou-qu-zhi-ding-ri-qi-fan-we/"
  - "/2025/06/30/nodejs-shi-xian-tong-guo-pop3-xie-yi-jin-xing-you-jian-de-shou-qu-zhi-ding-ri-qi-fa.html"
  - "/nodejs-shi-xian-tong-guo-pop3-xie-yi-jin-xing-you-jian-de-shou-qu-zhi-ding-ri-qi-fan-wei.html"
---
最近在使用Nodejs通过POP3去获取用户的邮件，但是搜索了很多的Nodejs库，包括pop3、yapople等等，感觉yapople还比较好上手，但是在使用过程中发现，tls的这一块不是很完善，于是自己就补充了一下，新创建了一个文件，并在pop3里面实现了几个简单的方法，用来获取邮件的内容，并借用了分页的模式，可以获取海量的邮箱，存储的话，可以在此基础上进行修改的。

代码的话我这里借用了git的一个插件，我做了公开，大家可以去借用下，有不完善的地方可以一起探讨。
