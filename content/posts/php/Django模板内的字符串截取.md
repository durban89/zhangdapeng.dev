---
title: "Django模板内的字符串截取"
date: "2025-06-20 10:31:49"
slug: "django-mu-ban-nei-de-zi-fu-chuan-jie-qu"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django模板内的字符串截取/"
  - "/2025/06/20/Django模板内的字符串截取.html"
  - "/Django模板内的字符串截取/"
  - "/Django模板内的字符串截取.html"
  - "/2025/06/20/django-mu-ban-nei-de-zi-fu-chuan-jie-qu/"
  - "/2025/06/20/django-mu-ban-nei-de-zi-fu-chuan-jie-qu.html"
  - "/django-mu-ban-nei-de-zi-fu-chuan-jie-qu.html"
---
django模板内的字符串截取

1,变量前30个字符,用于中文不行

```html
{{ content |truncatewords:"30"}}
```

取变量前500个字符，可用于中文

```html
{{ content |slice:"30" }} 
```
