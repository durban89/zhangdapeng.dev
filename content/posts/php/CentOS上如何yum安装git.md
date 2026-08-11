---
title: "CentOS上如何yum安装git"
date: "2025-06-27 10:25:58"
slug: "centos-shang-ru-he-yum-an-zhuang-git"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/27/CentOS上如何yum安装git/"
  - "/2025/06/27/CentOS上如何yum安装git.html"
  - "/CentOS上如何yum安装git/"
  - "/CentOS上如何yum安装git.html"
  - "/2025/06/27/centos-shang-ru-he-yum-an-zhuang-git/"
  - "/2025/06/27/centos-shang-ru-he-yum-an-zhuang-git.html"
  - "/centos-shang-ru-he-yum-an-zhuang-git.html"
---
`yum install git` 出现错误，会报错出现类似下面的情况

```bash
Setting up Install Process
No package git available.
Nothing to do
```

原因是因为没有资源文件存在，搜索不到吧，解决办法如下：

需要先添加EPEL(Extra Packages for Enterprise Linux) repository:

```bash
CentOS5.x 32-bit(x86/i386):
 rpm -Uvh http://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
CentOS5.x 64-bit(x64):
 rpm -Uvh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
 CentOS6.x32-bit (x86/i386):

 rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-5.noarch.rpm
CentOS6.x 64-bit(x64):
 rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-5.noarch.rpm
```

---

参考文章：

http://blog.csdn.net/laiahu/article/details/7516939

