---
title: "CentOS 安装php5.4.36+mysql5.5+apache2.4.10（二）"
date: "2025-06-30 12:00:42"
slug: "centos-an-zhuang-php5436mysql55apache2410-er"
categories: ["技术"]
tags: ["PHP", "CentOS", "MySQL", "Apache"]
aliases:
  - "/2025/06/30/CentOS-安装php5.4.36+mysql5.5+apache2.4.10（二）/"
  - "/2025/06/30/CentOS-安装php5.4.36+mysql5.5+apache2.4.10（二）.html"
  - "/CentOS-安装php5.4.36+mysql5.5+apache2.4.10（二）/"
  - "/CentOS-安装php5.4.36+mysql5.5+apache2.4.10（二）.html"
  - "/2025/06/30/CentOS-安装php5-4-36-mysql5-5-apache2-4-10-二/"
  - "/2025/06/30/CentOS-安装php5-4-36-mysql5-5-apache2-4-10-二.html"
  - "/2025/06/30/centos-an-zhuang-php5436mysql55apache2410-er/"
  - "/2025/06/30/centos-an-zhuang-php5436mysql55apache2410-er.html"
  - "/centos-an-zhuang-php5436mysql55apache2410-er.html"
---
1、MySQL 源码安装

//================================

下载源码：

ftp://ftp.jaist.ac.jp/pub/mysql/Downloads/

此处下载：mysql-5.5.41.tar.gz

//================================下载安装cmake

http://www.cmake.org/files/v3.1/cmake-3.1.0.tar.gz

//================================编译安装cmake

```bash
./configure
```

```bash
//================================安装 ncurses ncurses-devel
yum install ncurses ncurses-devel
//================================创建mysql的安装目录及数据库存放目录
mkdir -p /usr/local/mysql
mkdir -p /usr/local/mysql/data
//================================创建mysql用户及用户组
groupadd mysql
useradd -r -g mysql mysql
//================================安装mysql
cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/alidata/mysql/data -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci  -DEXTRA_CHARSETS=all -DENABLED_LOCAL_INFILE=1
//================================
make && make install
//================================设置目录权限
chown -R root:mysql .
chown -R mysql:mysql data
cp support-files/my-medium.cnf /etc/my.cnf
//================================创建系统数据库的表
scripts/mysql_install_db --user=mysql
//================================设置环境变量
vi /root/.bash_profile
//================================设置mysql启动服务
cp support-files/mysql.server  /etc/init.d/mysqld
//================================修改MySQL的root用户的密码以及打开远程连接
mysql>use mysql;
mysql>desc user;
mysql> GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY "root";　　//为root添加远程连接的能力。
mysql>update user set Password = password('xxxxxx') where User='root';
mysql>select Host,User,Password  from user where User='root'; 
mysql>flush privileges;
mysql>exit
```

2、安装apache2.4.10

//=================apr安装

```bash
yum remove apr-util-devel apr apr-util-mysql apr-docs apr-devel apr-util apr-util-doc
  
wget http://archive.apache.org/dist/apr/apr-1.4.5.tar.gz
wget http://archive.apache.org/dist/apr/apr-util-1.3.12.tar.gz 
wget http://jaist.dl.sourceforge.net/project/pcre/pcre/8.10/pcre-8.10.zip
```

以上第三个按照顺序解压安装

apache2.4.10编译安装使用如下命令

```bash
./configure --prefix=/usr/local/httpd --with-pcre=/usr/local/pcre --sysconfdir=/etc --enable-so --enable-rewrite && make && make install
```

3、安装php5.4.36

```bash
//安装gd扩展
wget http://liquidtelecom.dl.sourceforge.net/project/libpng/zlib/1.2.8/zlib-1.2.8.tar.gz
wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.0.tar.bz2
wget http://www.ijg.org/files/jpegsrc.v9.tar.gz
wget http://sourceforge.net/projects/libpng/files/libpng16/1.6.16/libpng-1.6.16.tar.gz/download
wget http://down1.chinaunix.net/distfiles/gd-2.0.32.tar.gz
```

按照上面的顺序依次安装

zlib安装

```bash
./configure --prefix=/usr/local/zlib --enable-shared && make && make install
```

freetype安装

```bash
./configure --prefix=/usr/local/freetype --enable-shared && make && make install
```

jpegsrc安装

```bash
./configure --prefix=/usr/local/jpeg --enable-shared && make && make install
```

libpng安装

```bash
./configure --prefix=/usr/local/libpng --enable-shared && make && make install
```

gd2安装

```bash
./configure --prefix=/usr/local/gd2 --enable-shared --with-zlib=/usr/local/zlib --with-freetype=/usr/local/freetype --with-jpeg=/usr/local/jpeg --with-png=/usr/local/png && make && make install
```

解压安装php//不解释

//================================

```bash
yum install libxml2
yum install libxml2-devel -y
//================================
./configure --prefix=/usr/local/php --with-config-file-path=/etc --with-gd --with-jpeg-dir=/usr/local/jpeg/ --with-png-dir=/usr/local/png/ --with-freetype-dir=/usr/local/freetype --with-zlib-dir=/usr/local/zlib/ --with-zlib --with-apxs2=/usr/local/httpd/bin/apxs --with-mysql=/usr/local/mysql --with-mysqli=mysqlnd --without-pear && make && make install
```

---

configure能正常通过，make配置到最后报错：`make: *** [ext/gd/gd.lo] Error 1`

据说这个错误是php5.4的bug:

解决方法
```bash
vim /usr/local/gd2/include/gd_io.h
```

gdIOCtx结构中增加`void *data;`

如下:

==========================================================

```c
typedef struct gdIOCtx
{
  int (*getC) (struct gdIOCtx *);
  int (*getBuf) (struct gdIOCtx *, void *, int);
   
  void (*putC) (struct gdIOCtx *, int);
  int (*putBuf) (struct gdIOCtx *, const void *, int);
   
  int (*seek) (struct gdIOCtx *, const int);
   
  long (*tell) (struct gdIOCtx *);
   
  void (*gd_free) (struct gdIOCtx *);
  void (*data);         //新增的内容
}
gdIOCtx;
```


