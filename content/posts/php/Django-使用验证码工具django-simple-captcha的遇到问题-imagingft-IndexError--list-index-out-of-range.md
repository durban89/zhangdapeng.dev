---
title: "Django 使用验证码工具django-simple-captcha的遇到问题{_imagingft,IndexError: list index out of range}"
date: "2025-06-26 10:32:12"
slug: "django-shi-yong-yan-zheng-ma-gong-ju-django-simple-captcha-de-yu-dao-wen-ti-imagingftindexerror-list-index-out-of-range"
categories: ["技术"]
tags: ["Django", "Python"]
aliases:
  - "/2025/06/26/Django-使用验证码工具django-simple-captcha的遇到问题{-imagingft,IndexError:-list-index-out-of-range/"
  - "/2025/06/26/Django-使用验证码工具django-simple-captcha的遇到问题{-imagingft,IndexError:-list-index-out-of-r.html"
  - "/Django-使用验证码工具django-simple-captcha的遇到问题{-imagingft,IndexError:-list-index-out-of-range}/"
  - "/Django-使用验证码工具django-simple-captcha的遇到问题{-imagingft,IndexError:-list-index-out-of-range}.html"
  - "/2025/06/26/Django-使用验证码工具django-simple-captcha的遇到问题-imagingft-IndexError-list-index-out-of-range/"
  - "/2025/06/26/Django-使用验证码工具django-simple-captcha的遇到问题-imagingft-IndexError-list-index-out-of-ran.html"
  - "/2025/06/26/django-shi-yong-yan-zheng-ma-gong-ju-django-simple-captcha-de-yu-dao-wen-ti-imagingftin/"
  - "/2025/06/26/django-shi-yong-yan-zheng-ma-gong-ju-django-simple-captcha-de-yu-dao-wen-ti-imaging.html"
  - "/django-shi-yong-yan-zheng-ma-gong-ju-django-simple-captcha-de-yu-dao-wen-ti-imagingftindexerro.html"
---
### [先来看看第一个问题](#1)

```bash
IndexError: list index out of range
```

就是这个简单的错误是因为我在django中使用django-simple-captcha的时候，没有在项目中运行下面的命令

```bash
python manage.py syncdb
```

就是一定要记得要进行数据库表的同步

### [第二个问题就是比较验证的操作量比较大的“`_imagingft`”问题](#2)

不过经过google的查找，按照下面的步骤进行就解决了问题，步骤如下

这个是由于PIL没有编译freetype导致的

查看 lib/python2.7/site-packages/PIL/

看看 `_imagingft.so` 是否存在

### [第一步安装ipeg库](#3)

最新的可以到http://www.ijg.org/files 这里去下载

```bash
wget http://www.ijg.org/files/jpegsrc.v7.tar.gz
tar -zxvf jpegsrc.v7.tar.gz
cd jpeg-7
CC="gcc -arch x86_64"
./configure --enable-shared --enable-static
make
make install
```

### [第二步安装freetype开发库](#4)

让PIL支持freetype的方法

1、安装freetype开发库

```bash
yum install freetype-devel
```

2、下载源代码http://effbot.org/downloads/Imaging-1.1.7.tar.gz

3、修改setup.py文件

修改

```bash
JPEG_ROOT = libinclude("/usr/local")

FREETYPE_ROOT = '/usr/lib64','/usr/include/freetype2/freetype'
```

---

关于freetype的安装我因为是在ubuntu环境下，不想运行yum，我是自己下载的，最近的源码可以到这个网址http://download.savannah.gnu.org/releases/freetype/ 下载，然后进行手动源码安装

第三步重新编译PIL进行安装（这里我采用的也是源码安装，源码的最新库的地址在http://effbot.org/downloads ）

```bash
python setup.py build_ext -i
```

--- FREETYPE2 support available  注意这一项

编译安装

```bash
python setup.py install
```

---

> 若上面的设置都失败，则只能拿出下面的杀手锏（我是没有经过这一步就成功了）：
>
> sudo apt-get build-dep python-imaging
>
> sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
>
> sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
>
> sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
>
> pip install -U PIL

安装成功的结果是

```bash
--------------------------------------------------------------------
PIL 1.1.7 SETUP SUMMARY
--------------------------------------------------------------------
version       1.1.7
platform      linux2 2.7.3 (default, Sep 26 2013, 20:08:41)
              [GCC 4.6.3]
--------------------------------------------------------------------
*** TKINTER support not available
--- JPEG support available
--- ZLIB (PNG/ZIP) support available
--- FREETYPE2 support available
*** LITTLECMS support not available
--------------------------------------------------------------------
```

参考文章：

http://www.cnblogs.com/descusr/p/3225874.html

