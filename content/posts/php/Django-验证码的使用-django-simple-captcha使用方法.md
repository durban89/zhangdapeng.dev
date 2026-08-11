---
title: "Django 验证码的使用django-simple-captcha使用方法"
date: "2025-06-26 10:32:07"
slug: "django-yan-zheng-ma-de-shi-yong-django-simple-captcha-shi-yong-fang-fa"
categories: ["技术"]
tags: ["Django", "Python"]
aliases:
  - "/2025/06/26/Django-验证码的使用django-simple-captcha使用方法/"
  - "/2025/06/26/Django-验证码的使用django-simple-captcha使用方法.html"
  - "/Django-验证码的使用django-simple-captcha使用方法/"
  - "/Django-验证码的使用django-simple-captcha使用方法.html"
  - "/2025/06/26/Django-验证码的使用-django-simple-captcha使用方法/"
  - "/2025/06/26/Django-验证码的使用-django-simple-captcha使用方法.html"
  - "/2025/06/26/django-yan-zheng-ma-de-shi-yong-django-simple-captcha-shi-yong-fang-fa/"
  - "/2025/06/26/django-yan-zheng-ma-de-shi-yong-django-simple-captcha-shi-yong-fang-fa.html"
  - "/django-yan-zheng-ma-de-shi-yong-django-simple-captcha-shi-yong-fang-fa.html"
---
关于Django的验证码的问题，进行再次的追究，找到了第二种方法

简单的简介和使用方法。并且关于在这里出现的问题我会在下篇文章进行说明，因为我在安装和使用的过程中还是遇到了问题的。大概的步骤如下

一、简介

项目地址：http://code.google.com/p/django-simple-captcha/

简介：是一个第三方django APP，用于为表单添加验证码图片

二、一般的使用方法

下载后python setup.py install进行安装

将下载包解压，将里面的captcha包复制到项目目录下，如myblog/captcha

settings.py里添加：

```python
INSTALLED_APPS(‘captcha’,)
```

urls.py里添加：

```python
url(r'^captcha/', include('captcha.urls')),
```

执行python manage.py syncdb生成所需数据库表

在需要用到captcha的forms.py文件里的合适位置添加下面的代码，增加验证码字段：

```python
from captcha.fields import CaptchaField
captcha=CaptchaField()
```

在处理表单提交的业务逻辑代码块里添加：

```python
if form.is_valid():
    human = True
```

三、与django的comments组件结合使用的方法（这里目前我是没有加到自己的项目里面）

如果你的项目里的评论系统直接使用的django内置的comments库，则comments库与此验证码库结合使用的方法如下：

执行前面的1至5步

在 `Python27\Lib\site-packages\django\contrib\comments\forms.py`文件中（windows环境下的路径），在CommentDetailsForm类里面添加验证码字段：

```python
from captcha.fields import CaptchaField
captcha= CaptchaField()
```

在`Python27\Lib\site-packages\django\contrib\comments\views\comments.py`文件中，在# Otherwise create the comment这句下面添加：

```python
human=True
```

修改表单模板：如果评论表单模板直接用的{{form}}则什么都不用修改；如果是自己定制的表单模板，则可添加如下：

```html
<p>
<label for="id_captcha">验证（必填）：</label> {{form.captcha}}
</p>
```

这样就基本能够使用了

---

参考文章：

http://newliu.com/post/5/

http://www.cnblogs.com/zackline/p/3365002.html

http://www.mysjtu.com/page/M0/S911/911080.html

