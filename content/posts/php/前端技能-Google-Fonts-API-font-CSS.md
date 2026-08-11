---
title: "前端技能 Google Fonts API @font-CSS"
date: "2025-06-20 11:07:41"
slug: "qian-duan-ji-neng-google-fonts-api-font-css"
categories: ["技术"]
tags: ["HTML", "CSS", "Font"]
aliases:
  - "/2025/06/20/前端技能-Google-Fonts-API-@font-CSS/"
  - "/2025/06/20/前端技能-Google-Fonts-API-@font-CSS.html"
  - "/前端技能-Google-Fonts-API-@font-CSS/"
  - "/前端技能-Google-Fonts-API-@font-CSS.html"
  - "/2025/06/20/前端技能-Google-Fonts-API-font-CSS/"
  - "/2025/06/20/前端技能-Google-Fonts-API-font-CSS.html"
  - "/2025/06/20/qian-duan-ji-neng-google-fonts-api-font-css/"
  - "/2025/06/20/qian-duan-ji-neng-google-fonts-api-font-css.html"
  - "/qian-duan-ji-neng-google-fonts-api-font-css.html"
---
开篇之前，先来几个链接<http://www.font-face.com/#google_announcement>

对于前端，强大不是一般般般的。

先来看几个例子

```html
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Tangerine">
    <style>
      body {
        font-family: 'Tangerine', serif;
        font-size: 48px;
      }
    </style>
  </head>
  <body>
    <div>Making the Web Beautiful!</div>
  </body>
</html>
```

来看一下效果图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1589163977/gowhich/1.png)

加点css的修改

```css
body {
  font-family: 'Tangerine', serif;
  font-size: 48px;
  text-shadow: 4px 4px 4px #aaa;
}
```

再来看看效果

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1589163979/gowhich/2.png)

是不是很赞啦。

这种操作，在我们的项目中，还是很必要的，尤其是前端，从美感上讲，我觉得可以跟苹果的ui媲美，没准苹果也是在用这个呢。

实现原理很简单额

1，第一步，引入css，是google字体的css

```html
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Font+Name">
```

2，第二步，在css中使用自己引入的字体，也可以在自己的html代码中调用的

```bash
CSS selector {
  font-family: 'Font Name', serif;
}
<div style="font-family: 'Font Name', serif;">Your text</div>
```

如果字体不好看的话，还有很多的字体的，请看这里[http://www.google.com/fonts](https://www.google.com/fonts)

对于具体的字体的话，可以去这样调用的

```html
http://fonts.googleapis.com/css?family=Tangerine:bold,bolditalic|Inconsolata:italic|Droid+Sans
```

很好解释的

Tangerine:bold,bolditalic

Tangerine想要的字体的名字，bold,bolditalic想要得到的字体的样式，如果想要多个话，就是用|进行分割，迫不及待了，试验一下。
