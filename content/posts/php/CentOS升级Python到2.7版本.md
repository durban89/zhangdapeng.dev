---
title: "CentOS升级Python到2.7版本"
date: "2025-06-27 10:25:55"
slug: "centos-sheng-ji-python-dao-27-ban-ben"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/27/CentOS升级Python到2.7版本/"
  - "/2025/06/27/CentOS升级Python到2.7版本.html"
  - "/CentOS升级Python到2.7版本/"
  - "/CentOS升级Python到2.7版本.html"
  - "/2025/06/27/centos-sheng-ji-python-dao-27-ban-ben/"
  - "/2025/06/27/centos-sheng-ji-python-dao-27-ban-ben.html"
  - "/centos-sheng-ji-python-dao-27-ban-ben.html"
---
查看python的版本

```bash
python -V
Python 2.4.3
```

1.先安装GCC

```bash
yum -y install gcc
```

2.下载Python-2.7.2

```bash
wget http://python.org/ftp/python/2.7.2/Python-2.7.2.tar.bz2
```

3.解压Python-2.7.2

```bash
tar -jxvf Python-2.7.2.tar.bz2
```

4.进入刚解压后的文件夹(可使用命令):

```bash
cd Python-2.7.2
```

5.安装

```bash
./configure
make all
make install
make clean
make distclean
```

6.查看版本信息

```bash
/usr/local/bin/python2.7 -V
```

7.建立软连接，使系统默认的python指向python2.7

正常情况下即使python2.7安装成功后，系统默认指向的python仍然是2.4.3版本，考虑到yum是基于python2.4.3才能正常工作，不敢轻易卸载。

如何实现将系统默认的python指向到2.7版本呢？

```bash
mv /usr/bin/python /usr/bin/python2.4
ln -s /usr/local/bin/python2.7 /usr/bin/python
```

检验python指向是否成功

```bash
python -V
```

8.解决系统python软链接指向python2.7版本后，yum不能正常工作

```bash
vi /usr/bin/yum
```

将文件头部的

```bash
#!/usr/bin/python
```

改成

```bash
#!/usr/bin/python2.4
```

---

参考文章：

http://my.oschina.net/zhangdapeng89/blog/86134

