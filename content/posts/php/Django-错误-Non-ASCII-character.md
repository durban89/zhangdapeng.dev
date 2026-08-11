---
title: "Django 错误 Non-ASCII character '\\\\xe6'"
date: "2025-06-19 10:29:28"
slug: "django-cuo-wu-non-ascii-character-xe6"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/19/Django-错误-Non-ASCII-character-'\\\\xe6'/"
  - "/2025/06/19/Django-错误-Non-ASCII-character-'\\\\xe6'.html"
  - "/Django-错误-Non-ASCII-character-'\\\\xe6'/"
  - "/Django-错误-Non-ASCII-character-'\\\\xe6'.html"
  - "/2025/06/19/Django-错误-Non-ASCII-character/"
  - "/2025/06/19/Django-错误-Non-ASCII-character.html"
  - "/2025/06/19/django-cuo-wu-non-ascii-character-xe6/"
  - "/2025/06/19/django-cuo-wu-non-ascii-character-xe6.html"
  - "/django-cuo-wu-non-ascii-character-xe6.html"
---
在使用django的时候，会遇到一个问题，就是“Non-ASCII character '\xe6'”这个错误

原因是如下，是我的配置文件中的一部分代码

```python
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('漫步者Feeling', 'xx@xx'),
)
```

提示一下，这里有中文，就是这个原因

修改一下，如下：

```python
# -*- coding: utf-8 -*-
# Django settings for walkerfree project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('漫步者Feeling', 'xx@xx'),
)
```

就是这句代码：`# -*- coding: utf-8 -*-  `
  
解决了。
