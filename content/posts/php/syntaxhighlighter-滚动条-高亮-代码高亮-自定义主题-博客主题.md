---
title: "syntaxhighlighter 滚动条 高亮 代码高亮 自定义主题 博客主题"
date: "2025-06-20 11:07:28"
slug: "syntaxhighlighter-gun-dong-tiao-gao-liang-dai-ma-gao-liang-zi-ding-yi-zhu-ti-bo-ke-zhu-ti"
categories: ["技术"]
tags: ["HTML", "CSS"]
aliases:
  - "/2025/06/20/syntaxhighlighter-滚动条-高亮-代码高亮-自定义主题-博客主题/"
  - "/2025/06/20/syntaxhighlighter-滚动条-高亮-代码高亮-自定义主题-博客主题.html"
  - "/syntaxhighlighter-滚动条-高亮-代码高亮-自定义主题-博客主题/"
  - "/syntaxhighlighter-滚动条-高亮-代码高亮-自定义主题-博客主题.html"
  - "/2025/06/20/syntaxhighlighter-gun-dong-tiao-gao-liang-dai-ma-gao-liang-zi-ding-yi-zhu-ti-bo-ke-zhu-/"
  - "/2025/06/20/syntaxhighlighter-gun-dong-tiao-gao-liang-dai-ma-gao-liang-zi-ding-yi-zhu-ti-bo-ke-.html"
  - "/syntaxhighlighter-gun-dong-tiao-gao-liang-dai-ma-gao-liang-zi-ding-yi-zhu-ti-bo-ke-zhu-ti.html"
---
欢迎大家对我博客的支持，最近无意间发现自己的博客的代码高亮出现了问题，原因是自己在做搜索的时候，为了减少js的加载，将某个layout模块删掉了，导致最后出问题自己还不知道，今天改的时候，更是不知道该如何改了，因为忘记了之前自己是如何添加这段代码的啦。不过咱就是写代码的，重写会有更多的收获的。

我就贴出 一下自己的css代码

```css
/**
 * SyntaxHighlighter
 * http://alexgorbatchev.com/SyntaxHighlighter
 *
 * SyntaxHighlighter is donationware. If you are using it, please donate.
 * http://alexgorbatchev.com/SyntaxHighlighter/donate.html
 *
 * @version
 * 3.0.83 (July 02 2010)
 * 
 * @copyright
 * Copyright (C) 2004-2010 Alex Gorbatchev.
 *
 * @license
 * Dual licensed under the MIT and GPL licenses.
 */
.syntaxhighlighter {
  background-color: #34495E !important;
  border-radius: 5px;
}
.syntaxhighlighter .line.alt1 {
  background-color: #34495E !important;
}
.syntaxhighlighter .line.alt2 {
  background-color: #34495E !important;
}
.syntaxhighlighter .line.highlighted.alt1, .syntaxhighlighter .line.highlighted.alt2 {
  background-color: #34495E !important;
}
.syntaxhighlighter .line.highlighted.number {
  color: white !important;
}
.syntaxhighlighter table{
   margin: 1px 0 !important;
}
.syntaxhighlighter table caption {
  color: #f8f8f8 !important;
}
.syntaxhighlighter .gutter {
  color: white !important;
}
.syntaxhighlighter .gutter .line {
  border-right: 3px solid #1ABC9C !important;
}
.syntaxhighlighter .gutter .line.highlighted {
  background-color: #41a83e !important;
  color: #0a2b1d !important;
}
.syntaxhighlighter.printing .line .content {
  border: none !important;
}
.syntaxhighlighter.collapsed {
  overflow: visible !important;
}
.syntaxhighlighter.collapsed .toolbar {
  color: #96dd3b !important;
  background: black !important;
  border: 1px solid #41a83e !important;
}
.syntaxhighlighter.collapsed .toolbar a {
  color: #96dd3b !important;
}
.syntaxhighlighter.collapsed .toolbar a:hover {
  color: white !important;
}
.syntaxhighlighter .toolbar {
  color: white !important;
  background: #41a83e !important;
  border: none !important;
}
.syntaxhighlighter .toolbar a {
  color: white !important;
}
.syntaxhighlighter .toolbar a:hover {
  color: #ffe862 !important;
}
.syntaxhighlighter .plain, .syntaxhighlighter .plain a {
  color: #f8f8f8 !important;
}
.syntaxhighlighter .comments, .syntaxhighlighter .comments a {
  color: #336442 !important;
}
.syntaxhighlighter .string, .syntaxhighlighter .string a {
  color: #9df39f !important;
  background-color: #34495E;
}
.syntaxhighlighter .keyword {
  color: #96dd3b !important;
}
.syntaxhighlighter .preprocessor {
  color: #91bb9e !important;
}
.syntaxhighlighter .variable {
  color: #ffaa3e !important;
}
.syntaxhighlighter .value {
  color: #f7e741 !important;
}
.syntaxhighlighter .functions {
  color: #ffaa3e !important;
}
.syntaxhighlighter .constants {
  color: #e0e8ff !important;
}
.syntaxhighlighter .script {
  font-weight: bold !important;
  color: #96dd3b !important;
  background-color: none !important;
}
.syntaxhighlighter .color1, .syntaxhighlighter .color1 a {
  color: #eb939a !important;
}
.syntaxhighlighter .color2, .syntaxhighlighter .color2 a {
  color: #91bb9e !important;
}
.syntaxhighlighter .color3, .syntaxhighlighter .color3 a {
  color: #edef7d !important;
}

.syntaxhighlighter .comments {
  font-style: italic !important;
  background-color: #34495E;
}
.syntaxhighlighter .keyword {
  font-weight: bold !important;
}

code{
  background-color: #34495E;
  border:1px solid #34495E;
}
```

千万注意的是，不要光之引入此css代码，还有一个核心的代码也一定要引入进来，不然会出现更乱的情况

```html
<link href="/syntaxhighlighter/styles/shCore.css" rel="stylesheet">    
<link href="/syntaxhighlighter/styles/shThemeFlatUI.css" rel="stylesheet">
```
