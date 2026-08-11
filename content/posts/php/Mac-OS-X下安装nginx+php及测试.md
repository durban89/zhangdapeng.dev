---
title: "Mac OS X下安装nginx+php及测试"
date: "2025-06-10 15:46:40"
slug: "mac-os-x-xia-an-zhuang-nginxphp-ji-ce-shi"
categories: ["技术"]
tags: ["Unix", "NGINX", "PHP"]
aliases:
  - "/2025/06/10/Mac-OS-X下安装nginx+php及测试/"
  - "/2025/06/10/Mac-OS-X下安装nginx+php及测试.html"
  - "/Mac-OS-X下安装nginx+php及测试/"
  - "/Mac-OS-X下安装nginx+php及测试.html"
  - "/2025/06/10/mac-os-x-xia-an-zhuang-nginxphp-ji-ce-shi/"
  - "/2025/06/10/mac-os-x-xia-an-zhuang-nginxphp-ji-ce-shi.html"
  - "/mac-os-x-xia-an-zhuang-nginxphp-ji-ce-shi.html"
---
---先安装XCode，这样才有GCC等必要开发工具包

默认XCode安装完成不会添加命令行支持，需要在XCode的“偏好设置-->下载-->选择下载命令行支持”

--命令行在 "应用程序--> 实用工具-->终端"

### [安装依赖的库](#1)

建议通过Macports来进行安装，（附[MacPorts安装使用说明](http://www.32133.com/skills/599.html)）。只需要执行如下指令：

```shell
sudo port install pcre
```

如果你已经通过自己下载pcre包来make & make install，很有可能会由于安装的pcre路径问题，在安装其他软件时会出问题。想要删除安装好的pcre，则只需要在下载下来的pcre解压文件夹下，执行make uninstall。

### [安装Nginx](#2)

方法一：仍然通过Macports，执行下面语句就ok

```shell
sudo port install nginx spawn-fcgi
```

方法二:

```shell
$curl -O http://nginx.org/download/nginx-0.8.53.tar.gz
$tar zxvf nginx-0.8.53.tar.gz
$cd nginx-0.8.53
$./configure --prefix=/usr/local/nginx --conf-path=/usr/local/nginx/conf/nginx.conf
$make
$sudo make install
```

配置文件为：`/usr/local/nginx/conf/nginx.conf`
默认安装在`/usr/local/nginx`
启动：输入以下命令启动Nginx，然后浏览器输入地址 http://localhost 进行测试，看到很大的字体的Welcome to nginx!就代表安装成功了

```shell
/usr/local/nginx/sbin/nginx
```

推荐关闭方式：

```shell
/usr/local/nginx/sbin/nginx -s stop
```

其他关闭方式：

```shell
ps -ef | grep nginx # 找到pid

sudo kill pid
```

### [安装PHP](#3)

```shell
sudo port install php5 +fastcgi fcgi php5-gd php5-mysql php5-sqlite php5-eaccelerator php5-curl php5-iconv
```

#### [配置文件](#3-1)

```shell
cd /opt/local/etc/php5
sudo cp php.ini-development php.ini
```

将时区修改为：`date.timezone = Asia/Chongqing`
错误级别修改为：`error\_reporting = E\_ALL & ~E\_NOTICE`

启动：

```shell
sudo /opt/local/bin/spawn-fcgi -C 2 -p 9000 -f /opt/local/bin/php-cgi
```

### [遇到NGINX PHP “No input file specified”问题，解决方法：](#4)

1、 php.ini（/opt/local/etc/php5/php.ini或者/etc/php5/cgi/php.ini）的配置中这两项

```shell
cgi.fix_pathinfo=1 （这个是自己添加的）
doc_root= （这行本来就有）
```

并修改下面：

```shell
location ~ \.php$ {
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  /var/www/sitepath$fastcgi_script_name;
    include               fastcgi_params;
}
```

`/var/www/sitepath`部分路径需要根据你主机主目录的实际情况填写，也可以用$document_root代替，其值实为PHP配置文件中的basedir一值。

测试方法：

在nginx的html目录下（默认为/usr/local/nginx/html），新建一个文件test.php，输入以下测试代码：

```php
<?php
//测试mysql
$link = mysql_connect('localhost', 'root', 'mysql密码');
if (!$link) {
    echo "mysql fail!";
} else {
    echo "mysql succees";
}
mysql_close();
//输出php信息
phpinfo();
```

通过http://localhost/test.php 访问，如果能正常显示，那恭喜你，ok了。

附nginx, php, mysql快捷启动代码，建议复制保存为startup.sh，每次通过执行./startup.sh，然后输入管理员密码，就一次性开启了三项服务：

```shell
#!/bin/sh
sudo /usr/local/nginx/sbin/nginx
sudo /opt/local/bin/spawn-fcgi -C 2 -p 9000 -f /opt/local/bin/php-cgi
sudo /usr/local/mysql/bin/mysqld_safe &
```

再附上nginx, php, mysql快捷关闭代码，建议复制保存为shutdown.sh，每次通过执行./shutdown.sh就关闭了三项服务：

```shell
#!/bin/sh
sudo /usr/local/nginx/sbin/nginx -s stop;
`ps -ef | grep php | head -n1|awk '{print "sudo kill "$2}'`;
sudo /usr/local/mysql/bin/mysqladmin -uroot -pms shutdown;
```

