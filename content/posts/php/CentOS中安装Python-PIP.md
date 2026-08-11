---
title: "CentOS中安装Python-PIP"
date: "2025-06-20 11:50:54"
slug: "centos-zhong-an-zhuang-python-pip"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/20/CentOS中安装Python-PIP/"
  - "/2025/06/20/CentOS中安装Python-PIP.html"
  - "/CentOS中安装Python-PIP/"
  - "/CentOS中安装Python-PIP.html"
  - "/2025/06/20/centos-zhong-an-zhuang-python-pip/"
  - "/2025/06/20/centos-zhong-an-zhuang-python-pip.html"
  - "/centos-zhong-an-zhuang-python-pip.html"
---
首先要安装 Setuptools

```bash
wget --no-check-certificate https://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg
sudo sh ./setuptools-0.6c11-py2.6.egg
```

安装PIP

```bash
wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-1.4.tar.gz
tar -zxvf ./pip-1.4.tar.gz
cd pip-1.4
sudo python setup.py install
```
