---
title: "Centos 安装php5.4.36+mysql5.5+apache2.4.10（一）"
date: "2025-06-30 12:00:41"
slug: "centos-an-zhuang-php5436mysql55apache2410-yi"
categories: ["技术"]
tags: ["PHP", "CentOS", "MySQL", "Apache"]
aliases:
  - "/2025/06/30/Centos-安装php5.4.36+mysql5.5+apache2.4.10（一）/"
  - "/2025/06/30/Centos-安装php5.4.36+mysql5.5+apache2.4.10（一）.html"
  - "/Centos-安装php5.4.36+mysql5.5+apache2.4.10（一）/"
  - "/Centos-安装php5.4.36+mysql5.5+apache2.4.10（一）.html"
  - "/2025/06/30/CentOS-安装php5-4-36-mysql5-5-apache2-4-10-一/"
  - "/2025/06/30/CentOS-安装php5-4-36-mysql5-5-apache2-4-10-一.html"
  - "/2025/06/30/centos-an-zhuang-php5436mysql55apache2410-yi/"
  - "/2025/06/30/centos-an-zhuang-php5436mysql55apache2410-yi.html"
  - "/centos-an-zhuang-php5436mysql55apache2410-yi.html"
---
```bash
1、MySQL 源码安装
//================================
下载源码：
ftp://ftp.jaist.ac.jp/pub/mysql/Downloads/
此处下载：mysql-5.5.41.tar.gz
//================================
解压//不解释
//================================
下载编译文件
http://www.cmake.org/files/v3.1/cmake-3.1.0.tar.gz
//================================
编译安装cmake
//================================
安装 ncurses ncurses-devel
//================================
安装mysql
cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/alidata/mysql/data -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci  -DEXTRA_CHARSETS=all -DENABLED_LOCAL_INFILE=1
//================================
make && make install
   
2、安装apache2.4.10
//=================apr安装
yum remove apr-util-devel apr apr-util-mysql apr-docs apr-devel apr-util apr-util-doc
   
wget http://archive.apache.org/dist/apr/apr-1.4.5.tar.gz
wget http://archive.apache.org/dist/apr/apr-util-1.3.12.tar.gz 
wget http://jaist.dl.sourceforge.net/project/pcre/pcre/8.10/pcre-8.10.zip
   
以上第三个按照顺序解压安装
apache2.4.10编译安装使用如下命令
./configure --prefix=/usr/local/apr
make && make install  
   
3、安装php5.4.36
   
//安装gd扩展
wget http://liquidtelecom.dl.sourceforge.net/project/libpng/zlib/1.2.8/zlib-1.2.8.tar.gz
wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.0.tar.bz2
wget http://www.ijg.org/files/jpegsrc.v9.tar.gz
wget http://sourceforge.net/projects/libpng/files/libpng16/1.6.16/libpng-1.6.16.tar.gz/download
wget http://down1.chinaunix.net/distfiles/gd-2.0.32.tar.gz
   
按照上面的顺序依次安装
zlib安装
./configure --prefix=/usr/local/zlib && make && make install
freetype安装
./configure --prefix=/usr/local/freetype && make && make install
jpegsrc安装
./configure --prefix=/usr/local/jpeg && make && make install
libpng安装
./configure --prefix=/usr/local/libpng && make && make install
gd2安装
./configure --prefix=/usr/local/gd2 --with-zlib=/usr/local/zlib --with-freetype-dir=/usr/local/freetype --with-jpeg-dir=/usr/local/jpeg --with-libpng-dir=/usr/local/libpng&& make && make install
   
解压安装php//不解释
//================================
yum install libxml2
yum install libxml2-devel -y
//================================
./configure --prefix=/usr/local/php --with-config-file-path=/etc --with-gd=/usr/local/gd2 --with-freetype-dir=/usr/local/freetype --with-apxs2=/usr/local/apache2/bin/apxs --with-mysql=/usr/local/mysql --with-mysqli=mysqlnd
//================================
make && make install
```

待续。。。


