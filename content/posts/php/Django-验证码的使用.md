---
title: "Django 验证码的使用"
date: "2025-06-25 11:35:16"
slug: "django-yan-zheng-ma-de-shi-yong"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/25/Django-验证码的使用/"
  - "/2025/06/25/Django-验证码的使用.html"
  - "/Django-验证码的使用/"
  - "/Django-验证码的使用.html"
  - "/2025/06/25/django-yan-zheng-ma-de-shi-yong/"
  - "/2025/06/25/django-yan-zheng-ma-de-shi-yong.html"
  - "/django-yan-zheng-ma-de-shi-yong.html"
---
关于django的验证码的使用，我在网上搜索的时候，目前只发现了两种，这里简单的记录下DjangoVerifyCode的使用方法。

---

在django中生成英文单词验证码,提供验证码图片生成,检查验证码等功能.

### [安装](#1)

```bash
pip install DjangoVerifyCode
```

or

```bash
easy_install DjangoVerifyCode
```

显示验证码(views.py)

```python
from DjangoVerifyCode import Code
def code(request):
    code = Code(request)
    return code.display()
```

检查用户输入的验证码是否正确(views.py)

```python
from DjangoVerifyCode import Code
def index(request):
    _code = request.GET.get('code') or ''
    if not _code:
        return render('index.html',locals())
 
    code = Code(request)
    if code.check(_code):
        return HttpResponse('验证成功')
    else:
        return HttpResponse('验证失败')
 #该代码片段来自于: http://www.sharejs.com/codes/python/7377
```

自定义

用户可根据自己的需要对DjangoVerifyCode.Code对象的属性进行设置

输出图片的宽度

code.img_width = 150

输出图片的高度

code.img_height = 30

验证码字体颜色

code.font_color = ['black','darkblue','darkred']

字体大小

font_size = 24

依赖包

PIL

安装PIL可以使用：

```python
pip install pil
```

我没有采用这种方法，一直还不知道如何在模板中使用，有哪位大神知道的，可以指教一二。

---

参考文章：

http://www.sharejs.com/codes/python/7377

http://www.100000000du.com/captcha/81556.html

