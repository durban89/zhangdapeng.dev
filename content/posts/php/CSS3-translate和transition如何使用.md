---
title: "CSS3 translate和transition如何使用"
date: "2025-07-10 11:52:48"
slug: "css3-translate-he-transition-ru-he-shi-yong"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/07/10/CSS3-translate和transition如何使用/"
  - "/2025/07/10/CSS3-translate和transition如何使用.html"
  - "/CSS3-translate和transition如何使用/"
  - "/CSS3-translate和transition如何使用.html"
  - "/2025/07/10/css3-translate-he-transition-ru-he-shi-yong/"
  - "/2025/07/10/css3-translate-he-transition-ru-he-shi-yong.html"
  - "/css3-translate-he-transition-ru-he-shi-yong.html"
---
translate和transition一直让我觉得，很牛皮很强大，怎么也学不会，其实是自己比较抗拒去了解她，接口看了不到半个小时的文档，大概了解了下，下面是示例，可以下载下来自己运行下试试

```html
<!DOCTYPE html>
<html>
<head>
  <title>translate和transition</title>
</head>
<body>
<style type="text/css">
  div {
    width: 100px;
    height: 75px;
    background-color: red;
    border: 1px solid black;
  }

  div#translate {
    transition: all 2s;
    -ms-transition: all 2s;
    -webkit-transition: all 2s;
  }

  div#translate:hover{
    transform: translate(50px, 100px);
    -ms-transform: translate(50px, 100px);
    -webkit-transform: translate(50px, 100px);
  }
</style>
<div>Hello, This is a Div element</div>
<div id='translate'>Hello, This is another Div element</div>
</body>
</html>
```

演示demo请点 [这里](/custom_pages/css3/translate.html)

* translate(a, b)：用官方的话说叫做2D转移，其实就是平面上的x轴和y轴移动，搞那么多名词就是因为我们学识太低，不想让我们容易了解

a - 在横向（左右方向）也就是x轴移动a单位距离，比如是10px，那么就移动10px，正值向右移动，负值向左移动 b - 在纵向（上下方向）也就是y轴移动b单位距离，比如是50px，那么就移动10px，正值向下移动，负值向上移动

起点在左上角哈，但是如果元素位置开始就设置了非原点的话就另说了，就是在元素基础上做计算

```bash
原点(0,0)-------
|
|
|
```

* transition 动画过渡

```bash
transition： property duration timing-function delay
```

> property - css属性

> duration - 动画执行时长 如果为0 动画不执行

> timing-function 动画执行方式 默认ease

> delay - 动画延迟执行时间 默认0

这四个是属性，别以为我是写了其他的属性，具体的看(文档)[<https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition>]

这里不再介绍，看我示例就知道了，
