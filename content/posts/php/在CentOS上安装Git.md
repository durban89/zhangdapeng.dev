---
title: "在CentOS上安装Git"
date: "2025-06-27 10:25:52"
slug: "zai-centos-shang-an-zhuang-git"
categories: ["技术"]
tags: ["CentOS", "Git", "Linux"]
aliases:
  - "/2025/06/27/在CentOS上安装Git/"
  - "/2025/06/27/在CentOS上安装Git.html"
  - "/在CentOS上安装Git/"
  - "/在CentOS上安装Git.html"
  - "/2025/06/27/zai-centos-shang-an-zhuang-git/"
  - "/2025/06/27/zai-centos-shang-an-zhuang-git.html"
  - "/zai-centos-shang-an-zhuang-git.html"
---
刚学了一下git在CentOS的安装方式，其实是这样子的，CentOS的yum源中没有git，只能自己编译安装，现在记录下编译安装的内容，留给自己备忘。

确保已安装了依赖的包

```bash
yum install curl
    
yum install curl-devel
    
yum install zlib-devel
    
yum install openssl-devel
    
yum install perl
    
yum install cpio
    
yum install expat-devel
    
yum install gettext-devel
```

下载最新的git包

```bash
wget http://www.codemonkey.org.uk/projects/git-snapshots/git/git-latest.tar.gz
    
tar xzvf git-latest.tar.gz
    
cd git-2011-11-30 ＃你的目录可能不是这个
    
autoconf
    
./configure
    
make
    
sudo make install
```

检查下安装的版本，大功告成

```bash
git --version
```

---

参考文章：

http://www.ccvita.com/370.html

