---
title: "让Django的admin组件显示为中文"
date: "2025-06-20 09:52:21"
slug: "rang-django-de-admin-zu-jian-xian-shi-wei-zhong-wen"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/让Django的admin组件显示为中文/"
  - "/2025/06/20/让Django的admin组件显示为中文.html"
  - "/让Django的admin组件显示为中文/"
  - "/让Django的admin组件显示为中文.html"
  - "/2025/06/20/rang-django-de-admin-zu-jian-xian-shi-wei-zhong-wen/"
  - "/2025/06/20/rang-django-de-admin-zu-jian-xian-shi-wei-zhong-wen.html"
  - "/rang-django-de-admin-zu-jian-xian-shi-wei-zhong-wen.html"
---
django的admin组件默认显示为英文，使用中还是有很多不方便的。其实，django还是做好了国际化的工作的，要实现语言的转变，只需要如下操作：

在settings.py中找到`MIDDLEWARE_CLASSES`，在 `'django.contrib.sessions.middleware.SessionMiddleware'`后面添加一个中间件 `'django.middleware.locale.LocaleMiddleware'`，启动django，就会发现admin显示为中文的了
