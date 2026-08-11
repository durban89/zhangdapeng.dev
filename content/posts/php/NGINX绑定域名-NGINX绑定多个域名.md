---
title: "NGINX绑定域名 NGINX绑定多个域名"
date: "2025-06-26 10:32:35"
slug: "nginx-bang-ding-yu-ming-nginx-bang-ding-duo-ge-yu-ming"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/06/26/NGINX绑定域名-NGINX绑定多个域名/"
  - "/2025/06/26/NGINX绑定域名-NGINX绑定多个域名.html"
  - "/NGINX绑定域名-NGINX绑定多个域名/"
  - "/NGINX绑定域名-NGINX绑定多个域名.html"
  - "/2025/06/26/nginx-bang-ding-yu-ming-nginx-bang-ding-duo-ge-yu-ming/"
  - "/2025/06/26/nginx-bang-ding-yu-ming-nginx-bang-ding-duo-ge-yu-ming.html"
  - "/nginx-bang-ding-yu-ming-nginx-bang-ding-duo-ge-yu-ming.html"
---
nginx中配置域名的方法很简单，实现nginx的域名跳转我知道了如下的方法。

---

Server 名称使用 “server_name” 指令来定义，并决定用哪一个 server 区块来处理请求

#### [一、每个域名一个文件的写法](#1)

首先打开nginx域名配置文件存放目录：`/usr/local/nginx/conf/servers` ，如要绑定域名 www.gowhich.com 则在此目录建一个文件：www.gowhich.com.conf 然后在此文件中写规则，如：

```ini
server
{
    listen       80;
    server_name www.gowhich.com;#绑定域名
    index index.htm index.html index.php;#默认文件
    root /home/www/www.gowhich.com;#网站根目录
    include location.conf; #调用其他规则，也可去除
}
```

然后重起nginx服务器，域名就绑定成功了

nginx服务器重起命令：`/etc/init.d/nginx restart`

#### [二、一个文件多个域名的写法](#2)

一个文件添加多个域名的规则也是一样，只要把上面单个域名重复写下来就ok了，如：

```ini
server
{
	listen       80;
	server_name www.gowhich.com;             #绑定域名
	index index.htm index.html index.php;      #默认文件
	root /home/www/gowhich.com;               #网站根目录
	include location.conf;  #调用其他规则，也可去除
}

server
{
	listen       80;
	server_name  a.gowhich.com;    #绑定域名
	index index.htm index.html index.php;      #默认文件
	root /home/www/msn.gowhich.com;        #网站根目录
	include location.conf;  #调用其他规则，也可去除
}
```

#### [三、不带www的域名加301跳转](#3)

如果不带www的域名要加301跳转，那也是和绑定域名一样，先绑定不带www的域名，只是不用写网站目录，而是进行301跳转，如：

```ini
server
{
	listen 80;
	server_name gowhich.com;
	rewrite ^/(.*) http://www.gowhich.com/$1 permanent;
}
```

#### [四、添加404网页](#4)

添加404网页，都可又直接在里面添加，如：

```ini
server
{
	listen       80;
	server_name  www.gowhich.com;             #绑定域名
	index index.htm index.html index.php;      #默认文件
	root /home/www/gowhich.com;               #网站根目录
	include location.conf;#调用其他规则，也可去除
	error_page 404  /404.html;
}
```

#### [附Nginx批量配置多域名绑定](#5)

下面接着看，多域名绑定与解析另一方法

先给出我的全部配置吧，然后再一一解释

```ini
server 
{
	listen       80;
    server_name  localhost;
    set $mdomain 'ip';
    if ( $host ~* (w+.[a-zA-Z]+)$ ) {
    	set $mdomain $1;
    }
    if ( $host ~* (b(?!wwwb)w+).w+.[a-zA-Z]+$ ) {
    	set $mdir /$1;
    }
    location / {
	    index index.html index.php;
	    root /home/www/$mdomain$mdir;
    }
    location ~ .php$ {
        root           /home/www/$mdomain$mdir;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /home/www/$mdomain$mdir/$fastcgi_script_name;
        include        fastcgi_params;
    }
}
```

这是 server 下的，server 要放在 http 内。

##### [1.多域名解析](#5-1)

我的配置文件是根据正则表达式判断域名，然后域名赋给变量，然后变量组成路径

```ini
set $mdomain 'ip';
//设置变量 mdomain 的默认值为字符串"ip"
if ( $host ~* (w+.[a-zA-Z]+)$ ) {
    //对输入的域名进行正则表达式匹配；
    set $mdomain $1;
    //若匹配则设置变量 mdomain 为正则表达式括号的值；
}
```

匹配成功就把结果存入变量 mdomain 中，待用;

##### [2.二级域名解析到子文件夹](#5-2)

二级域名还是根据正则表达式匹配

```ini
if ( $host ~* (b(?!wwwb)w+).w+.[a-zA-Z]+$ ) {
    set $mdir /$1;
}
```

这是正则表达式的匹配结果。

还是取子域名加上"/"到变量 mdir 中；

location 解析

```ini
location / {
    index index.html index.php;
    root /home/www/$mdomain$mdir;
}
```

最后 root 到匹配的结果路径中，没有匹配的变量就为空了；例如：www.gowhich.com 解析的路径是 `/home/www/gowhich.com/www;`gowhich.com 解析的路径就是 `/home/www/gowhich.com;`

以上搜索的到的结果数据来源于网络，稍加做过修改，在使用过程中要根据具体情况进行具体设置。

参考文章:

http://www.111cn.net/sys/nginx/52852.htm

