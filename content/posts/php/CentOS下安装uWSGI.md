---
title: "CentOS下安装uWSGI"
date: "2025-06-19 13:55:10"
slug: "centos-xia-an-zhuang-uwsgi"
categories: ["技术"]
tags: ["CentOS", "uWSGI"]
aliases:
  - "/2025/06/19/CentOS下安装uWSGI/"
  - "/2025/06/19/CentOS下安装uWSGI.html"
  - "/CentOS下安装uWSGI/"
  - "/CentOS下安装uWSGI.html"
  - "/2025/06/19/centos-xia-an-zhuang-uwsgi/"
  - "/2025/06/19/centos-xia-an-zhuang-uwsgi.html"
  - "/centos-xia-an-zhuang-uwsgi.html"
---
第一步：首先是下载文件：

下载地址

<http://projects.unbit.it/downloads/>

这里面有你自己想要的文件版本

第二步：执行两条命令

```bash
yum update
yum install python python-devel libxml2 libxml2-devel python-setuptools zlib-devel wget openssl-devel pcre pcre-devel sudo gcc make autoconf automake
```

第三步：解压安装

```bash
tar -zxvf uwsgi-0.9.6.5.tar.gz
mv uwsgi-0.9.6.5/ uwsgi/
cd uwsgi/
sudo python setup.py build
make
```

第四步：将安装成功的uwsgi文件copy一份到自己使用bin目录下，我的是copy到了/usr/local/bin目录

第五步：测试是否安装成功

```bash
uwsgi --help
```

会打印出类似下面的信息

```bash
Usage: /usr/local/bin/uwsgi [options...]
    -s|--socket                            bind to the specified UNIX/TCP socket using default protocol
    -s|--uwsgi-socket                      bind to the specified UNIX/TCP socket using uwsgi protocol
    --http-socket                          bind to the specified UNIX/TCP socket using HTTP protocol
    --http-socket-modifier1                force the specified modifier1 when using HTTP protocol
    --http-socket-modifier2                force the specified modifier2 when using HTTP protocol
    --fastcgi-socket                       bind to the specified UNIX/TCP socket using FastCGI protocol
    --fastcgi-nph-socket                   bind to the specified UNIX/TCP socket using FastCGI protocol (nph mode)
    --fastcgi-modifier1                    force the specified modifier1 when using FastCGI protocol
    --fastcgi-modifier2                    force the specified modifier2 when using FastCGI protocol
    --scgi-socket                          bind to the specified UNIX/TCP socket using SCGI protocol
    --scgi-nph-socket                      bind to the specified UNIX/TCP socket using SCGI protocol (nph mode)
    --scgi-modifier1                       force the specified modifier1 when using SCGI protocol
    --scgi-modifier2                       force the specified modifier2 when using SCGI protocol
    --protocol                             force the specified protocol for default sockets
    --socket-protocol                      force the specified protocol for default sockets
    --shared-socket                        create a shared sacket for advanced jailing or ipc
    --undeferred-shared-socket             create a shared sacket for advanced jailing or ipc (undeferred mode)
    -p|--processes                         spawn the specified number of workers/processes
    -p|--workers                           spawn the specified number of workers/processes
--More--
```

安装成功
