---
title: "Django 后台上传图片的 操作过程"
date: "2025-06-20 11:33:28"
slug: "django-hou-tai-shang-chuan-tu-pian-de-cao-zuo-guo-cheng"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django-后台上传图片的-操作过程/"
  - "/2025/06/20/Django-后台上传图片的-操作过程.html"
  - "/Django-后台上传图片的-操作过程/"
  - "/Django-后台上传图片的-操作过程.html"
  - "/2025/06/20/django-hou-tai-shang-chuan-tu-pian-de-cao-zuo-guo-cheng/"
  - "/2025/06/20/django-hou-tai-shang-chuan-tu-pian-de-cao-zuo-guo-cheng.html"
  - "/django-hou-tai-shang-chuan-tu-pian-de-cao-zuo-guo-cheng.html"
---
最近在做自己的一个项目中，由于使用的是django框架，基于这个框架，其实后台用来添加图片是非常简单的，其实只要一个配置model就可以了

```python
# -*- coding: utf-8 -*- 
from __future__ import division
import os
import Image
from django.db import models
from datetime import datetime, timedelta
from django.utils.translation import ugettext as _
from walkerfree.settings import MEDIA_ROOT
from django.db.models.fields.files import ImageFieldFile

'''
上传图片的路径
'''
UPLOAD_ROOT = 'upload'
LARGE_ROOT = 'upload/large'
MIDDLE_ROOT = 'upload/middle'
SMALL_ROOT = 'upload/small'

def make_large_thumb(path, size = 480):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf

def make_middle_thumb(path, size = 320):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf

def make_small_thumb(path, size = 100):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf

class Woman(models.Model):
    IS_SHOW_CHOICES = (
        ('0',0),
        ('1',1)
    )
    title = models.CharField(max_length=255,help_text='标题')
    description = models.TextField(null=False,help_text='描述')
    url_address = models.URLField(max_length=255,help_text='信息地址')
    
    large_image = models.ImageField(upload_to = 'upload/large')
    middle_image = models.ImageField(upload_to = 'upload/middle')
    small_image = models.ImageField(upload_to = 'upload/small')

    large_image_url_address = models.URLField(null=True, blank=True, max_length=255, help_text='大图片的地址')
    middle_image_url_address = models.URLField(null=True, blank=True, max_length=255, help_text='中等图片的地址')
    small_image_url_address = models.URLField(null=True, blank=True, max_length=255, help_text='小图片的地址')

    is_show = models.PositiveSmallIntegerField(default=0, choices=IS_SHOW_CHOICES,null=True,help_text='是否在最前端显示')
    create_date = models.DateTimeField(auto_now=True,auto_now_add=True,help_text='创建日期')
    update_date = models.DateTimeField(auto_now=True,auto_now_add=True,help_text='更新日期')

    class Meta:
        verbose_name_plural = _('Woman')
            

    def save(self):
        super(Woman, self).save()
        large_image_base, large_image_ext = os.path.splitext(os.path.basename(self.large_image.path))
        middle_image_base, middle_image_ext = os.path.splitext(os.path.basename(self.middle_image.path))
        small_image_base, small_image_ext = os.path.splitext(os.path.basename(self.small_image.path))
        
        large_thumb_pixbuf = make_large_thumb(os.path.join(MEDIA_ROOT, self.large_image.name))
        middle_thumb_pixbuf = make_middle_thumb(os.path.join(MEDIA_ROOT, self.middle_image.name))
        small_thumb_pixbuf = make_small_thumb(os.path.join(MEDIA_ROOT, self.small_image.name))

        large_relate_thumb_path = os.path.join(LARGE_ROOT, large_image_base + '_large_' + large_image_ext)
        middle_relate_thumb_path = os.path.join(MIDDLE_ROOT, middle_image_base + '_middle_' + middle_image_ext)
        small_relate_thumb_path = os.path.join(SMALL_ROOT, small_image_base + '_small_' + small_image_ext)

        large_thumb_path = os.path.join(MEDIA_ROOT, large_relate_thumb_path)
        middle_thumb_path = os.path.join(MEDIA_ROOT, middle_relate_thumb_path)
        small_thumb_path = os.path.join(MEDIA_ROOT, small_relate_thumb_path)

        large_thumb_pixbuf.save(large_thumb_path)
        middle_thumb_pixbuf.save(middle_thumb_path)
        small_thumb_pixbuf.save(small_thumb_path)

        self.large_image = ImageFieldFile(self, self.large_image, large_thumb_path)
        self.middle_image = ImageFieldFile(self, self.middle_image, middle_thumb_path)
        self.small_image = ImageFieldFile(self, self.small_image, small_thumb_path)

        super(Woman, self).save()

    def __unicode__(self):
        return self.title
```

不要怀疑就这么简单。

然后在admin.py中注册一下，后台就可以使用了。

参看文章：

1，http://imtx.me/archives/693.html

2，http://www.zijin5.com/2013/07/django-admin-image-upload/
