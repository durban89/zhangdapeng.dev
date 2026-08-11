---
title: "window.location.hash属性介绍"
date: "2025-06-27 09:45:15"
slug: "windowlocationhash-shu-xing-jie-shao"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/window.location.hash属性介绍/"
  - "/2025/06/27/window.location.hash属性介绍.html"
  - "/window.location.hash属性介绍/"
  - "/window.location.hash属性介绍.html"
  - "/2025/06/27/windowlocationhash-shu-xing-jie-shao/"
  - "/2025/06/27/windowlocationhash-shu-xing-jie-shao.html"
  - "/windowlocationhash-shu-xing-jie-shao.html"
---
来了解一下hash，javascript中的hash是啥。

location是javascript里边管理地址栏的内置对象，比如location.href就管理页面的url，用location.href=url就可以直接将页面重定向url。而location.hash则可以用来获取或设置页面的标签值。比如http://domain/#admin的location.hash="#admin" 。利用这个属性值可以做一个非常有意义的事情。

很多人都喜欢收藏网页，以便于以后的浏览。不过对于Ajax页面来说的话，一般用一个页面来处理所有的事务，也就是说，如果你浏览到一个Ajax页面里边有意思的内容，想将它收藏起来，可是地址只有一个呀，下次你打开这个地址，还是得像以往一样不断地去点击网页，找到你钟情的那个页面。另外的话，浏览器上的“前进”“后退”按钮也会失效，这于很多习惯了传统页面的用户来说，是一个很大的使用障碍。

那么，怎么用location.hash来解决这两个问题呢？其实一点也不神秘。

比如，某人的管理系统，主要功能有三个：普通搜索、高级搜索、后台管理，我分别给它们分配一个hash值：#search、#advsearch、#admin，在页面初始化的时候，通过window.location.hash来判断用户需要访问的页面，然后通过javascript来调整显示页面

```javascript
var hash; 
hash=(!window.location.hash)?"#search":window.location.hash; 
window.location.hash=hash; 
//调整地址栏地址，使前进、后退按钮能使用 
switch(hash){   
    case "#search":  
        selectPanel("pnlSearch");   //显示普通搜索面板  
        break;    
    case "#advsearch":    
        selectPanel("adSearch");    //显示高级搜索面板
        break;
    case "#admin":  
        selectPanel("adminSearch"); //显示后台搜索面板
        break;
}
```

通过`window.location.hash=hash`这个语句来调整地址栏的地址，使得浏览器里边的“前进”、“后退”按钮能正常使用（实质上欺骗了浏览器）。然后再根据hash值的不同来显示不同的面板（用户可以收藏对应的面板了），这就使得Ajax页面的浏览趋于传统化了。

不过现在有一个比较简单的解决方式。

```javascript
history.pushState()
```

---

参考文章：

http://www.cnblogs.com/china-aspx/archive/2008/04/20/1162597.html

