---
title: "jQuery 实现 保持滚动条一直在底部"
date: "2025-07-01 11:35:56"
slug: "jquery-shi-xian-bao-chi-gun-dong-tiao-yi-zhi-zai-di-bu"
categories: ["技术"]
tags: ["jQuery"]
aliases:
  - "/2025/07/01/jQuery-实现-保持滚动条一直在底部/"
  - "/2025/07/01/jQuery-实现-保持滚动条一直在底部.html"
  - "/jQuery-实现-保持滚动条一直在底部/"
  - "/jQuery-实现-保持滚动条一直在底部.html"
  - "/2025/07/01/jquery-shi-xian-bao-chi-gun-dong-tiao-yi-zhi-zai-di-bu/"
  - "/2025/07/01/jquery-shi-xian-bao-chi-gun-dong-tiao-yi-zhi-zai-di-bu.html"
  - "/jquery-shi-xian-bao-chi-gun-dong-tiao-yi-zhi-zai-di-bu.html"
---
**jquery 实现 保持滚动条一直在底部**

```js
var e = $('#import-bill');  
e.scrollTop = e.scrollHeight;//让滚动条自动滚动顶部
$("#import-bill").scrollTop($("#import-bill")[0].scrollHeight);
```


