---
title: "Django 生成sitemap的简单方式"
date: "2025-06-25 10:26:43"
slug: "django-sheng-cheng-sitemap-de-jian-dan-fang-shi"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/25/Django-生成sitemap的简单方式/"
  - "/2025/06/25/Django-生成sitemap的简单方式.html"
  - "/Django-生成sitemap的简单方式/"
  - "/Django-生成sitemap的简单方式.html"
  - "/2025/06/25/django-sheng-cheng-sitemap-de-jian-dan-fang-shi/"
  - "/2025/06/25/django-sheng-cheng-sitemap-de-jian-dan-fang-shi.html"
  - "/django-sheng-cheng-sitemap-de-jian-dan-fang-shi.html"
---
gowhich最近的一个网站使用django搭建，急需sitemap这个家伙的帮助，so easy。

下面看下简介：

---

sitemaps 是 Google 最先引入的网站地图协议，采用 XML 格式，它的作用简而言之就是优化搜索引擎的索引效率，详细的解释可以参考 维基百科。

Bing、Yahoo 以及 Ask 都支持 sitemaps 协议。国内的百度最近也开始支持 sitemaps 协议，但我看百度官方文档的描述，<lastmod> 标签可能只支持精确到天 yyyy-mm-dd（制作通用的 sitemaps 协议可能需要注意这点，标准 sitemaps 协议支持非常精确的 W3C Datetime 格式）。

看看django的sitemap的框架吧

---

Django sitemap 框架的使用和设置

Django 的 contrib 包带了对网站地图协议的支持，使用起来非常方便，几行代码就可以搞定了。

首先需要在 `settings.py` 的 `INSTALLED_APPS` 列表中增加 `app 'django.contrib.sitemaps'`。

随后在 urls.py 文件中追加如下代码：

```python
# django.contrib.sitemaps
from django.contrib.sitemaps import GenericSitemap
from blogs.models import Blog
from news.models import News

blogs_dict = {
    'queryset': Blog.objects.all(),
    'date_field': 'modified_date',
}
news_dict = {
    'queryset': News.objects.all(),
    'date_field': 'modified_date',
}

sitemaps = {
    # 'flatpages': FlatPageSitemap,
    'blogs': GenericSitemap(blogs_dict, priority=0.6),
    'news': GenericSitemap(news_dict, priority=0.5),
}

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
```

Blog 和 News 换成需要为其建立地图的 Model 即可，其中 '`date_field`' 对应于网站地图协议的 lastmod（最后修改时间），所以值 `modified_date` 要换成对应 Model 用来保存最后修改时间的数据库字段。

---

***测试***

重启测试服务器后访问：http://127.0.0.1:8000/sitemap.xml 显示的是一个包含若干网站地图的索引（sitemap index）。

Google 和百度均支持网站地图索引，可以放心使用。使用网站地图索引的主要原因是，网站内容非常多时，生成的网站地图索引会非常大，检索效率低，搜索引擎为了分批检索，规定单个网站地图的条目不能超过 5 万个 URL 链接，总大小不超过 10M。

---

注意问题

django.contrib.sitemaps 依赖 django.contrib.sites app，必须启用。启用后需要到 "Sites" 中把缺省的 example.com 设置成真实域名；

Django 是动态生成网站地图，因此如果要提高搜索引擎的检索速度，获得更好的排名，应考虑将其静态化（django-static-sitemaps）。

---

参考链接

[Sitemap 协议标准](http://www.sitemaps.org/protocol.html)

[Google sitemap 帮助](https://support.google.com/webmasters/bin/answer.py?hl=en&answer=71453)

[百度 sitemap 帮助](http://www.baidu.com/search/sitemap_help.html)

[百度 sitemap 格式](http://zhanzhang.baidu.com/site/format)

[Django sitemap 框架](https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/)

[Django sites 框架](https://docs.djangoproject.com/en/dev/ref/contrib/sites)

