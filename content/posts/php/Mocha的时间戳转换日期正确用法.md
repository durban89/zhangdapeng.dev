---
title: "Mocha的时间戳转换日期正确用法"
date: "2025-07-01 15:24:34"
slug: "mocha-de-shi-jian-chuo-zhuan-huan-ri-qi-zheng-que-yong-fa"
categories: ["技术"]
tags: ["Mocha"]
aliases:
  - "/2025/07/01/Mocha的时间戳转换日期正确用法/"
  - "/2025/07/01/Mocha的时间戳转换日期正确用法.html"
  - "/Mocha的时间戳转换日期正确用法/"
  - "/Mocha的时间戳转换日期正确用法.html"
  - "/2025/07/01/mocha-de-shi-jian-chuo-zhuan-huan-ri-qi-zheng-que-yong-fa/"
  - "/2025/07/01/mocha-de-shi-jian-chuo-zhuan-huan-ri-qi-zheng-que-yong-fa.html"
  - "/mocha-de-shi-jian-chuo-zhuan-huan-ri-qi-zheng-que-yong-fa.html"
---
```js
var date = '2015-09-10';
debug('date :',date);
var starttime = moment(Date.parse(date)).second(0).minute(0).hour(0).format('X');
var endtime = moment(Date.parse(date)).add(1,'day').second(0).minute(0).hour(0).format('X');
debug('starttime :',starttime);
debug('endtime :',endtime);
debug('starttime :',moment.unix(starttime).format('YYYY-MM-DD HH:mm:ss'));
debug('endtime :',moment.unix(endtime).format('YYYY-MM-DD HH:mm:ss'));
```

如果是日期字符串，请先用`Date.parse(date)`进行parse下。

如果是时间戳，请直接使用`moment.unix()`进行操作


