---
title: "MongoDB 的php 驱动的安装"
date: "2025-06-24 14:46:11"
slug: "mongodb-de-php-qu-dong-de-an-zhuang"
categories: ["技术"]
tags: ["PHP", "MongoDB"]
aliases:
  - "/2025/06/24/MongoDB-的php-驱动的安装/"
  - "/2025/06/24/MongoDB-的php-驱动的安装.html"
  - "/MongoDB-的php-驱动的安装/"
  - "/MongoDB-的php-驱动的安装.html"
  - "/2025/06/24/mongodb-de-php-qu-dong-de-an-zhuang/"
  - "/2025/06/24/mongodb-de-php-qu-dong-de-an-zhuang.html"
  - "/mongodb-de-php-qu-dong-de-an-zhuang.html"
---
第一步：下载MongoDB的php驱动

下载地址：<https://github.com/mongodb/mongo-php-driver>

```bash
wget -O mongo-php-driver-master.zip https://github.com/mongodb/mongo-php-driver/archive/master.zip
```

第二步：解压

```bash
unzip mongo-php-driver-master.zip
```

第三步：安装

```bash
cd mongo-php-driver-master/
phpize
./configure
make
sudo make install
```

会出现类似

```bash
Installing shared extensions:     /usr/lib/php5/20090626+lfs/
```

或者是

```bash
Installing shared extensions:     /usr/local/php/lib/php/extensions/no-debug-non-zts-20090626/
```

表示安装成功

确保和运行的 PHP 是同一个扩展目录：

```bash
$ php -i | grep extension_dir
```

输出的结果如：

```ini
extension_dir => /usr/lib/php/extensions/no-debug-zts-20060613 =>/usr/lib/php/extensions/no-debug-zts-20060613
```

如果不一致，则需要修改 php.ini 里的 extension\_dir，或者把 mongo.so 移过去。

第四步：添加momgoDB扩展

打开php.ini

加入

```ini
extension=mongo.so
```

然后重新启动php-fpm

这里我遇到了一个问题：

```bash
php-fpm restart
php-fpm reload
php-fpm stop
php-fpm start
```

这几个命令似乎都木有用了。执行完后，总是提示我

> Usage: php [-n] [-e] [-h] [-i] [-m] [-v] [-t] [-p <prefix>] [-g <pid>] [-c <file>] [-d foo[=bar]] [-y <file>]
>
>   -c <path>|<file> Look for php.ini file in this directory
>
>   -n               No php.ini file will be used
>
>   -d foo[=bar]     Define INI entry foo with value 'bar'
>
>   -e               Generate extended information for debugger/profiler
>
>   -h               This help
>
>   -i               PHP information
>
>   -m               Show compiled in modules
>
>   -v               Version number
>
>   -p, --prefix <dir>
>
>                    Specify alternative prefix path to FastCGI process manager (default: /usr/local/php).
>
>   -g, --pid <file>
>
>                    Specify the PID file location.
>
>   -y, --fpm-config <file>
>
>                    Specify alternative path to FastCGI process manager config file.
>
>   -t, --test       Test FPM configuration and exit
>
>   -R, --allow-to-run-as-root
>
>                    Allow pool to run as root (disabled by default)

受不了，来点强制的措施吧

先kill所有的php-fpm的进程，然后直接执行

```bash
php-fpm
```

如果php-fpm的进程只有3，5个还好说，但是如果有几十个的话，我是觉得有点累：

试试下面这个脚本吧

```bash
#!/bin/sh
NAME="php-fpm"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi
echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "################################################"
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "################################################"
php5-fpm
```

或者是

```bash
#!/bin/sh
NAME="php-fpm"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi
echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "################################################"
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "################################################"
php-fpm
```

因为之前的那个是Ubuntu系统的，后面的这个是Centos系统的

然后输出phpinfo，搜索一下mongo，是不是已经存在了，如果还是木有的话，请留言

