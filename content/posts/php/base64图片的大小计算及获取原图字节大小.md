---
title: "base64图片的大小计算及获取原图字节大小"
date: "2025-07-10 11:52:40"
slug: "base64-tu-pian-de-da-xiao-ji-suan-ji-huo-qu-yuan-tu-zi-jie-da-xiao"
categories: ["技术"]
tags: ["Base64"]
aliases:
  - "/2025/07/10/base64图片的大小计算及获取原图字节大小/"
  - "/2025/07/10/base64图片的大小计算及获取原图字节大小.html"
  - "/base64图片的大小计算及获取原图字节大小/"
  - "/base64图片的大小计算及获取原图字节大小.html"
  - "/2025/07/10/base64-tu-pian-de-da-xiao-ji-suan-ji-huo-qu-yuan-tu-zi-jie-da-xiao/"
  - "/2025/07/10/base64-tu-pian-de-da-xiao-ji-suan-ji-huo-qu-yuan-tu-zi-jie-da-xiao.html"
  - "/base64-tu-pian-de-da-xiao-ji-suan-ji-huo-qu-yuan-tu-zi-jie-da-xiao.html"
---
实现原理：根据`base64,`做区分，前面部分是类型，后面部分是真实的的图片字符串

比如下面的base64图片字符串

// 这里只是做了一个例子

`var base64DataStr = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABNoAAAigCAY ... pw52VLv8/zk3Uc3CN6sgAAAAASUVORK5CYII=';`

```js
function getBase64ImgSize(base64DataStr) {
  var tag = "base64,";
  var base64Data = '';

  // 截取字符串 获取"base64,"后面的字符串
  base64DataStr = base64Data = base64DataStr.substring(base64DataStr.indexOf(tag) + tag.length);

  // 根据末尾等号（'='）来再次确认真实base64图片字符串
  var eqTagIndex = base64DataStr.indexOf("=");
  base64DataStr = eqTagIndex != -1 ? base64DataStr.substring(0, eqTagIndex) : base64DataStr;

  // 计算大小
  var strLen = base64DataStr.length;
  var fileSize = strLen - (strLen / 8) * 2; // 这里的原理可以想一下为什么要这样做
  return {
    fileSize: fileSize,
    base64Data: base64Data,
  };
}
```

使用方式如下

```js
getBase64ImgSize(base64DataStr)
```

运行后得到的结果

```bash
{fileSize: 57, base64Data: "iVBORw0KGgoAAAANSUhEUgAABNoAAAigCAY ... pw52VLv8/zk3Uc3CN6sgAAAAASUVORK5CYII="}
```
