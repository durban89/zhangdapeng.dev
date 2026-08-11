---
title: "CSS opacity透明度继承问题"
date: "2025-06-09 16:18:15"
slug: "css-opacity-tou-ming-du-ji-cheng-wen-ti"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/06/09/CSS-opacity透明度继承问题/"
  - "/2025/06/09/CSS-opacity透明度继承问题.html"
  - "/CSS-opacity透明度继承问题/"
  - "/CSS-opacity透明度继承问题.html"
  - "/2025/06/09/css-opacity-tou-ming-du-ji-cheng-wen-ti/"
  - "/2025/06/09/css-opacity-tou-ming-du-ji-cheng-wen-ti.html"
  - "/css-opacity-tou-ming-du-ji-cheng-wen-ti.html"
---
元素透明的做法，大概如下

```css
#div.opacity{ filter:alpha(opacity:80);opacity:0.8; }
```

但是结果导致的问题是，里面所有的元素都开始透明了

通过搜索，搜集资料，我发现了一个解决问题的方法

HTML文件代码如下：

```html
<div class='well activity-outer'>
  <div class='activity-opacity'></div>
  <div class='activity-inner'>
    <h4>活动细则:</h4>
    <div class='detail'>
      <p style='margin:0;padding:0;text-indent:1em'>1. 手机拍摄黑龙江卫视乱世佳人照片并上传, 选择上传到“天心恋”和“重心恋”其中一组</p>
      <p style='margin:0;padding:0;text-indent:1em'>2. 普通观众点击支持，看哪些照片（带黑龙江卫视台标）获得支持多,优先获得奖品</p>
      <p style='margin:0;padding:0;text-indent:1em'>3. 本活动在和黑龙江卫视播出最后一期结束</p>
    </div>
  </div>
</div>
```

CSS文件代码如下：
```css
div.activity-outer{padding:0;background-color:transparent;border:0}
div.activity-opacity,
div.activity-inner{
    height:100px;
    width:938px;
    left:0;
    position:relative;
    top:0;
    border-radius: 4px 4px 4px 4px;
    border-color:#ccc;
}

div.activity-opacity{
    background-color:#ccc;
    filter:alpha(opacity:80);
    opacity:.8;
}
div.activity-inner{
    margin-top: -119px;
    padding: 14px 4px 0 10px;
  color:white
}
```
以上两个文件的代码，是我做的网站的一个摘录，主css文件采用的是bootstrap这个css框架，记录一下。
