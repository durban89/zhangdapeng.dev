---
title: "给 Django 站点添加 favicon.ico"
date: "2025-06-19 10:48:10"
slug: "gei-django-zhan-dian-tian-jia-faviconico"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/19/给-Django-站点添加-favicon.ico/"
  - "/2025/06/19/给-Django-站点添加-favicon.ico.html"
  - "/给-Django-站点添加-favicon.ico/"
  - "/给-Django-站点添加-favicon.ico.html"
  - "/2025/06/19/给-Django-站点添加-favicon-ico/"
  - "/2025/06/19/给-Django-站点添加-favicon-ico.html"
  - "/2025/06/19/gei-django-zhan-dian-tian-jia-faviconico/"
  - "/2025/06/19/gei-django-zhan-dian-tian-jia-faviconico.html"
  - "/gei-django-zhan-dian-tian-jia-faviconico.html"
---
如何给 Django 开发的网站添加 favicon.ico 功能

三步：

1. 创建一个 favicon.ico 文件
2. 修改 urls.py ， 添加 "/favicon.ico" 路径。
3. 修改 html 模版

下面看实现步骤

第一步：创建一个 favicon.ico 文件

创建了一个 16x16 像素的透明画布，在添加一个text图层（写上“Y”），保存为 png 格式文件 favicon.png ， 重命名为 favicon.ico 即可: " "     
第二步：修改 urls.py  
在 URL 里添加：

```python
(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.MEDIA_URL+'images/favicon.ico'}),
```

第三步：修改 html 模版

在 html 模版的 head 部分添加：

```html
<link REL="SHORTCUT ICON" HREF="{{ MEDIA_URL }}images/favicon.ico">
```
