---
title: "jQuery 图片加载成功调用指定执行方法"
date: "2025-07-03 17:11:40"
slug: "jquery-tu-pian-jia-zai-cheng-gong-diao-yong-zhi-ding-zhi-xing-fang-fa"
categories: ["技术"]
tags: ["jQuery", "JavaScript"]
aliases:
  - "/2025/07/03/jQuery-图片加载成功调用指定执行方法/"
  - "/2025/07/03/jQuery-图片加载成功调用指定执行方法.html"
  - "/jQuery-图片加载成功调用指定执行方法/"
  - "/jQuery-图片加载成功调用指定执行方法.html"
  - "/2025/07/03/jquery-tu-pian-jia-zai-cheng-gong-diao-yong-zhi-ding-zhi-xing-fang-fa/"
  - "/2025/07/03/jquery-tu-pian-jia-zai-cheng-gong-diao-yong-zhi-ding-zhi-xing-fang-fa.html"
  - "/jquery-tu-pian-jia-zai-cheng-gong-diao-yong-zhi-ding-zhi-xing-fang-fa.html"
---
页面中总有一些操作是，需要图片加载完之后去做的，下面的代码可实现，需要的拿走

```js
$("img").one("load", function(v) {
  // 逻辑处理
  $(v.target).parent().parent().find('.over-shade').css({'height':$(v.target).height()});
}).each(function() {
  if(this.complete) $(this).load();
});
```
