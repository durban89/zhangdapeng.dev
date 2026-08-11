---
title: "Django 后台表单标签的自定义"
date: "2025-06-26 10:32:31"
slug: "django-hou-tai-biao-dan-biao-qian-de-zi-ding-yi"
categories: ["技术"]
tags: ["Django", "Python"]
aliases:
  - "/2025/06/26/Django-后台表单标签的自定义/"
  - "/2025/06/26/Django-后台表单标签的自定义.html"
  - "/Django-后台表单标签的自定义/"
  - "/Django-后台表单标签的自定义.html"
  - "/2025/06/26/django-hou-tai-biao-dan-biao-qian-de-zi-ding-yi/"
  - "/2025/06/26/django-hou-tai-biao-dan-biao-qian-de-zi-ding-yi.html"
  - "/django-hou-tai-biao-dan-biao-qian-de-zi-ding-yi.html"
---
一直在使用django的后台，自动生成的表单的里面的标签让我着实模糊了一下。

其实很简单的，只要自己在创建表单的时候，稍加注意一下，加一个字段就可以搞定了。

代码示例：

```python
#!-*-coding=utf8-*-
from django.db import models
class Category(models.Model):
    id = models.AutoField(primary_key=True,db_index=True)
    title = models.CharField("分类名称",max_length=100,db_index=True,unique=True)
    created = models.DateTimeField("创建日期",auto_now_add=True)
    updated = models.DateTimeField("更新日期",auto_now=True,null=True,blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = "gifts_category"
        verbose_name = "Gifts分类"
        verbose_name_plural = "Gifts分类"
```

主要是这里

```python
title = models.CharField("分类名称",max_length=100,db_index=True,unique=True)
```

在传递参数的时候，前面加了一个自定义的名称,这里是"分类名称"

重新运行一下试试，就会有结果了

