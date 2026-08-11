---
title: "Java7 Tomcat缓存的问题"
date: "2025-06-27 10:06:59"
slug: "java7-tomcat-huan-cun-de-wen-ti"
categories: ["技术"]
tags: ["Java", "Tomcat"]
aliases:
  - "/2025/06/27/Java7-Tomcat缓存的问题/"
  - "/2025/06/27/Java7-Tomcat缓存的问题.html"
  - "/Java7-Tomcat缓存的问题/"
  - "/Java7-Tomcat缓存的问题.html"
  - "/2025/06/27/java7-tomcat-huan-cun-de-wen-ti/"
  - "/2025/06/27/java7-tomcat-huan-cun-de-wen-ti.html"
  - "/java7-tomcat-huan-cun-de-wen-ti.html"
---
一般的在做jsp的开发的时候，会出现一个问题就是，将jsp文件提交后，刷新页面，内容没有改变。

我这里总结了几条方法，在实施之前先做如下操作。

1，删除work里面对应的项目的缓存文件，比如我的app是news，那么我就删除news就好了

2，清空浏览器的缓存，或者是重新打开一个浏览器

然后做如下的操作，使得我们的操作起作用：

1，修改server.xml文件，在相应的context中加上或者修改

```bash
reloadable="true"
```

结果就是:

```bash
<Context path="/news" docBase="/home/www/jspweb/news" debug="0" privileged="true" reloadable="true"> 
</Context>
```

3，在相应的jsp文件中加入如下代码：

```bash
<%
      response.setHeader("Cache-Control", "no-cache");
      response.setHeader("Pragma", "no-cache");
      response.setDateHeader("Expires", -1);
      response.setDateHeader("max-age", 0);
%>
```

然后打开页面试试吧，修改文件之后在重新传一下试试，如果没有效果可以联系下方的QQ群。

---

参考文章：

http://blog.csdn.net/redarmy_chen/article/details/7032671

http://g.kehou.com/t1007086668.html

