---
title: "JavaScript 之 事件统计，防重复统计"
date: "2025-07-03 11:59:17"
slug: "javascript-zhi-shi-jian-tong-ji-fang-chong-fu-tong-ji"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/07/03/JavaScript-之-事件统计，防重复统计/"
  - "/2025/07/03/JavaScript-之-事件统计，防重复统计.html"
  - "/JavaScript-之-事件统计，防重复统计/"
  - "/JavaScript-之-事件统计，防重复统计.html"
  - "/2025/07/03/JavaScript-之-事件统计-防重复统计/"
  - "/2025/07/03/JavaScript-之-事件统计-防重复统计.html"
  - "/2025/07/03/javascript-zhi-shi-jian-tong-ji-fang-chong-fu-tong-ji/"
  - "/2025/07/03/javascript-zhi-shi-jian-tong-ji-fang-chong-fu-tong-ji.html"
  - "/javascript-zhi-shi-jian-tong-ji-fang-chong-fu-tong-ji.html"
---
事件统计防重复统计，不服来挑错

```js
function track(eventName, params) {
  var img = new Image();
  if(typeof params == 'object') {
    params = JSON.stringify(params);
  } else {
    params = '';
  }
  var t = new Date().valueOf();
  var random = Math.random();
  var referrer = document.referrer;
  img.src = '/track?event='+encodeURIComponent(eventName)+'&params=' + encodeURIComponent(params) + '&t='+t+'&r='+random+'&referrer='+referrer;
}
```

后端将r值t值,外加一个ip的值，作为唯一的索引。为了做到数据准确到达，程序端少操作为主，这样会减少操作事件，将逻辑交给数据库操作了，增加数据到达率。

```js
let insertEventSql = `REPLACE INTO ${config.mysql.prefix}xxxx.event_log 
                          (${keys.join(',')}) 
                          VALUES 
                          (${values.join(',')})`;
```


