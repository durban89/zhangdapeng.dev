---
title: "Django Strip/Remove HTML tags"
date: "2025-06-25 11:35:00"
slug: "django-stripremove-html-tags"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/25/Django-Strip/Remove-HTML-tags/"
  - "/2025/06/25/Django-Strip/Remove-HTML-tags.html"
  - "/Django-Strip/Remove-HTML-tags/"
  - "/Django-Strip/Remove-HTML-tags.html"
  - "/2025/06/25/Django-Strip-Remove-HTML-tags/"
  - "/2025/06/25/Django-Strip-Remove-HTML-tags.html"
  - "/2025/06/25/django-stripremove-html-tags/"
  - "/2025/06/25/django-stripremove-html-tags.html"
  - "/django-stripremove-html-tags.html"
---
在php中我们知道如果想要去掉html的标签的话，使用函数`strip_tags`在django中如何去去掉html的标签呢,下面是我在google中搜索到的结果。

To strip/remove HTML tags from an existing string we can use the `strip_tags` function.

```python
# import the strip_tags
from django.utils.html import strip_tags
# simple string with html inside.
html = '<p>paragraph</p>'
print html # will produce: <p>paragraph</p>
stripped = strip_tags(html)
print stripped # will produce: paragraph
```

This is also available as a template tag:

```html
{{ somevalue|striptags }}
```

If you want to remove only specific tags you need to use the removetags

```python
from django.template.defaultfilters import removetags
html = '<strong>Bold...</strong><p>paragraph....</p>'
stripped = removetags(html, 'strong') # removes the strong only.
stripped2 = removetags(html, 'strong p') # removes the strong AND p tags.
```

Also available in template:

```html
{{ value|removetags:"a span"|safe }}
```

在模板里面是使用去掉html标签的方法是不是很简单，嘿嘿。

---

参考的文章：

<http://snipplr.com/view/50835/>

