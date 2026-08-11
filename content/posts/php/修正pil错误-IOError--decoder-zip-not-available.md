---
title: "修正pil错误 IOError: decoder zip not available"
date: "2025-06-20 11:33:25"
slug: "xiu-zheng-pil-cuo-wu-ioerror-decoder-zip-not-available"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/20/修正pil错误-IOError:-decoder-zip-not-available/"
  - "/2025/06/20/修正pil错误-IOError:-decoder-zip-not-available.html"
  - "/修正pil错误-IOError:-decoder-zip-not-available/"
  - "/修正pil错误-IOError:-decoder-zip-not-available.html"
  - "/2025/06/20/修正pil错误-IOError-decoder-zip-not-available/"
  - "/2025/06/20/修正pil错误-IOError-decoder-zip-not-available.html"
  - "/2025/06/20/xiu-zheng-pil-cuo-wu-ioerror-decoder-zip-not-available/"
  - "/2025/06/20/xiu-zheng-pil-cuo-wu-ioerror-decoder-zip-not-available.html"
  - "/xiu-zheng-pil-cuo-wu-ioerror-decoder-zip-not-available.html"
---
关于修正UBUNTU下PIL错误 IOError: decoder zip not available

第一步，卸载PIL

```bash
easy_install pip//没有的话可以先安装
pip uninstall pil
```

第二步，下载ZLIB

下载地址：http://www.zlib.net/

也可以去：https://sourceforge.net/projects/libpng/?source=dlp

第三步，安装ZLIB

```bash
./configure 
make
make install
```

第四步，安装PIL

```bash
pip install pil
```

参看文章：

1，http://www.linuxdiyf.com/viewarticle.php?id=107892

2，http://www.zlib.net/

3，http://obroll.com/install-python-pil-python-image-library-on-ubuntu-11-10-oneiric/

4，http://stackoverflow.com/questions/3544155/need-help-with-a-pil-error-ioerror-decoder-zip-not-available

5，http://lutaf.com/128.htm

6，http://stackoverflow.com/questions/12555831/decoder-jpeg-not-available-error-when-following-django-photo-app-tutorial
