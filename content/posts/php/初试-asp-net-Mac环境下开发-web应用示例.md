---
title: "初试 ASP.NET Mac环境下开发 web应用示例"
date: "2025-06-24 11:24:27"
slug: "chu-shi-aspnet-mac-huan-jing-xia-kai-fa-web-ying-yong-shi-li"
categories: ["技术"]
tags: ["ASP.NET"]
aliases:
  - "/2025/06/24/初试-ASP.NET-Mac环境下开发-web应用示例/"
  - "/2025/06/24/初试-ASP.NET-Mac环境下开发-web应用示例.html"
  - "/初试-ASP.NET-Mac环境下开发-web应用示例/"
  - "/初试-ASP.NET-Mac环境下开发-web应用示例.html"
  - "/2025/06/24/初试-asp-net-Mac环境下开发-web应用示例/"
  - "/2025/06/24/初试-asp-net-Mac环境下开发-web应用示例.html"
  - "/2025/06/24/chu-shi-aspnet-mac-huan-jing-xia-kai-fa-web-ying-yong-shi-li/"
  - "/2025/06/24/chu-shi-aspnet-mac-huan-jing-xia-kai-fa-web-ying-yong-shi-li.html"
  - "/chu-shi-aspnet-mac-huan-jing-xia-kai-fa-web-ying-yong-shi-li.html"
---
一、环境的搭建

开发工具的下载：[Mono](http://www.go-mono.com/mono-downloads/download.html)

我下载的时候名称好像不对，但是网络上说的是这个我列一下自己下载的文件吧

[XamarinStudio-4.0.12-3.dmg](http://download.xamarin.com/studio/Mac/XamarinStudio-4.0.12-3.dmg)

[Mono MRE installer](http://download.mono-project.com/archive/3.2.3/macos-10-x86/MonoFramework-MRE-3.2.3.macos10.xamarin.x86.pkg)

[Mono MDK installer](http://download.mono-project.com/archive/3.2.3/macos-10-x86/MonoFramework-MDK-3.2.3.macos10.xamarin.x86.pkg)

这是文件下载完后，直接安装就好了。

二、项目的创建

启动XamarinStudio,开始创建项目，如下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555323992/gowhich/406_1.png)

写上项目的名称，然后确定

接下来是创建Controller和View

创建Controller是这样的，请看下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324086/gowhich/406_2.png)

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324086/gowhich/406_3.png)

创建View是这样的，如下图，右击键Views目录，创建一个Home目录，然后在Home目录创建一个Index.aspx文件

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324181/gowhich/406_4.png)

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324181/gowhich/406_5.png)

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324252/gowhich/406_6.png)

最后的结构目录如下图：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324252/gowhich/406_7.png)

HomeController文件的内容如下：

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HelloWorld.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View ("Index");
        }
    }
}
```

Index.aspx文件的内容如下:

```html
<%@ Page Language="C#" Inherits="System.Web.Mvc.ViewPage" %>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <div>
        hello world
    </div>
</body>
```

三、直接运行

点击运行按钮

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324413/gowhich/406_8.png)

查看服务启动运行的端口（如下图）：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324413/gowhich/406_9.png)

浏览器访问就可以了。

参考文章：

[ASP.NET MVC案例教程（基于ASP.NET MVC beta）——第三篇：ASP.NET MVC全局观](http://www.cnblogs.com/leoo2sk/archive/2008/11/01/1324168.html)

[ASP.NET MVC3实战系列（一）：简单示例](http://www.cnblogs.com/cnblogsfans/archive/2011/09/01/2162227.html)

[ASP.NET视频教程](http://developer.51cto.com/developer/aspdotnet/)

[ASP.net Development on Mac 的開發環境選擇](http://carolhsu.github.io/blog/2012/08/18/asp-dot-net-development-on-mac-de-kai-fa-huan-jing-xuan-ze/)

以上文章内容更新于 2019年4月15日 ， 其实版本已过期，当日重新试了一下发现会提示mcs的问题

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555324413/gowhich/406_8.png)

建议使用新的版本及新的mono

