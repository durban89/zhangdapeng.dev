---
title: "CentOS 7升级curl后导致php调用curl异常的问题"
date: "2025-07-11 11:16:16"
slug: "centos-7-sheng-ji-curl-hou-dao-zhi-php-diao-yong-curl-yi-chang-de-wen-ti"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/11/CentOS-7升级curl后导致php调用curl异常的问题/"
  - "/2025/07/11/CentOS-7升级curl后导致php调用curl异常的问题.html"
  - "/CentOS-7升级curl后导致php调用curl异常的问题/"
  - "/CentOS-7升级curl后导致php调用curl异常的问题.html"
  - "/2025/07/11/centos-7-sheng-ji-curl-hou-dao-zhi-php-diao-yong-curl-yi-chang-de-wen-ti/"
  - "/2025/07/11/centos-7-sheng-ji-curl-hou-dao-zhi-php-diao-yong-curl-yi-chang-de-wen-ti.html"
  - "/centos-7-sheng-ji-curl-hou-dao-zhi-php-diao-yong-curl-yi-chang-de-wen-ti.html"
---
背景介绍

使用的是阿里云的服务器，最近报警了，提示我服务器有漏洞，要进行修复升级，然后看了下详情，给出的修复命令如下

```bash
yum update libcurl-devel
yum update libcurl
yum update curl
```

好吧，我能力低，我技术不行，承认自己，于是便执行了下，执行完之后，没有发现任何异常。

但是！我邮箱在不断的收到curl的报错异常，于是我检查代码，添加各种日志，依然没有发现具体是哪里的问题，于是开始猜测访问频次高的接口。

不测不知道一测发现了问题

在PHP中用curl调用的时候第一次是没有问题的，第二次就出现问题了

但是在命令行下面都是正常的

基本报错日志信息如下

>*错误信息1*

```bash
* About to connect() to api.gowhich.com port 443 (#1)
*   Trying 10.252.117.104...
* Connected to api.gowhich.com (10.252.117.104) port 443 (#1)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
* Unable to initialize NSS database
* Initializing NSS with certpath: none
* Unable to initialize NSS
* Closing connection 1
```

>*错误信息2*

```bash
* Initializing NSS with certpath: none
* NSS error -5978 (PR_NOT_CONNECTED_ERROR)
* Network file descriptor is not connected
* Closing connection 0
int(35)
Network file descriptor is not connected
```

curl安装完之后的版本

```bash
curl -V
```

版本信息如下

```bash
curl 7.29.0 (x86_64-redhat-linux-gnu) libcurl/7.29.0 NSS/3.44 zlib/1.2.7 libidn/1.28 libssh2/1.8.0
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp scp sftp smtp smtps telnet tftp
Features: AsynchDNS GSS-Negotiate IDN IPv6 Largefile NTLM NTLM_WB SSL libz unix-sockets
```

通过如下命令访问

```bash
curl -I -X GET -v https://api.gowhich.com
```

结果如下

```bash
* About to connect() to api.gowhich.com port 443 (#0)
*   Trying 10.252.117.104...
* Connected to api.gowhich.com (10.252.117.104) port 443 (#0)
* Initializing NSS with certpath: none
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt
  CApath: none
* SSL connection using TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
* Server certificate:
*       subject: CN=*.gowhich.com
*       start date: 8月 05 00:00:00 2019 GMT
*       expire date: 10月 03 12:00:00 2020 GMT
*       common name: *.gowhich.com
*       issuer: CN=RapidSSL RSA CA 2018,OU=www.digicert.com,O=DigiCert Inc,C=US
> GET / HTTP/1.1
> User-Agent: curl/7.29.0
> Host: api.gowhich.com
> Accept: */*
>
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Server: nginx/1.6.3
Server: nginx/1.6.3
< Date: Tue, 18 Feb 2020 08:40:32 GMT
Date: Tue, 18 Feb 2020 08:40:32 GMT
< Content-Type: text/html; charset=utf-8
Content-Type: text/html; charset=utf-8
< Content-Length: 11
Content-Length: 11
< Connection: keep-alive
Connection: keep-alive
< ETag: W/"b-+mppjeYkbwpj8ck3uudlJA"
ETag: W/"b-+mppjeYkbwpj8ck3uudlJA"

<
* Excess found in a non pipelined read: excess = 11 url = / (zero-length body)
* Connection #0 to host api.gowhich.com left intact
```

通过上面的一系列问题，原因就是本机的php调用curl时出现了问题，我猜测时php不兼容nss版本的curl，但是我看过其他服务器使用确实是nss版本的curl，只不过nss的版本不同，

如果你是在命令行下执行php的话

可以通过加变量的方式，这个方法是网上查到的资料(命令如下)

```bash
export NSS_STRICT_NOFORK=DISABLED
```

如果要取消的话可以如下操作

```bash
export NSS_STRICT_NOFORK=1
```

或者

```bash
unset NSS_STRICT_NOFORK
```

但是文章上好像说 不建议在生产环境中使用

参考文章链接：https://cohan.dev/php-curl-libcurl-error-on-subsequent-requests/

但是我在webapp中要如何去设置这个参数，我还真不知道了。

最后的解决方案，替换nss版本的curl，改换成openssl版本的curl。

我下载的curl版本是 curl-7.27.0.tar.gz

然后下载一个与你php版本一致的包 我的是 php-7.0.6.tar.gz

(非root用户，但是有root权限的命令如下，如果是root的话，会有一些不同)

下载后分别解压下

```bash
tar -zxvf ***.tar.gz
```

先安装下curl

```bash
cd curl-7.27.0

./configure --without-nss --with-ssl
make && sudo make install
```

再安装php的curl

```bash
cd php-7.0.6/ext/curl
phpize
./configure --with-curl=/usr/local
make && sudo make install
```

安装完之后重启php-fpm

```bash
/etc/init.d/php-fpm restart
```

结果修复了。
