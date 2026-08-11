---
title: "Composer安装SSL证书异常处理"
date: "2025-07-15 10:28:47"
slug: "composer-an-zhuang-ssl-zheng-shu-yi-chang-chu-li"
categories: ["技术"]
tags: ["Composer"]
aliases:
  - "/2025/07/15/Composer安装SSL证书异常处理/"
  - "/2025/07/15/Composer安装SSL证书异常处理.html"
  - "/Composer安装SSL证书异常处理/"
  - "/Composer安装SSL证书异常处理.html"
  - "/2025/07/15/composer-an-zhuang-ssl-zheng-shu-yi-chang-chu-li/"
  - "/2025/07/15/composer-an-zhuang-ssl-zheng-shu-yi-chang-chu-li.html"
  - "/composer-an-zhuang-ssl-zheng-shu-yi-chang-chu-li.html"
---
composer安装SSL证书异常处理，报错信息：error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed

最近发现composer的传统安装方式不行了

传统方式

```bash
curl --insecure -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

主要是，执行

```bash
curl --insecure -sS https://getcomposer.org/installer | php
```

报错。

有的时候报错

> All settings correct for using Composer  
> Downloading...  
> Failed to decode zlib stream

有的时候报错

> All settings correct for using Composer  
> Downloading...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. Open  
> SSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> Retrying...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. Open  
> SSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> Retrying...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. Open  
> SSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> The download failed repeatedly, aborting.

使用

```bash
curl --insecure -ksS https://getcomposer.org/installer | php
```

也不行，依然报错

> All settings correct for using Composer  
> Downloading...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. Open  
> SSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> Retrying...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. Open  
> SSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> Retrying...  
> The "https://getcomposer.org/versions" file could not be downloaded: SSL operation failed with code 1. OpenSSL Error messages:  
> error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed  
> Failed to enable crypto  
> failed to open stream: operation failed  
> The download failed repeatedly, aborting.

执行

```bash
php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');"
```

也不行。

可能是我服务器的证书问题，具体原因不详，具体解决方案如下

```bash
wget --no-check-certificate https://install.phpcomposer.com/installer -O ./composer-setup.php
```

下载安装文件，再下载证书文件

```bash
wget https://curl.haxx.se/ca/cacert.pem --no-check-certificate -O ./cacert.pem
```

修改php.ini中的openssl.cafile配置

```bash
vi /usr/local/lib/php.ini
```

修改为

```bash
openssl.cafile=/root/cacert.pem
```

退出修改在执行

```bash
php composer-setup.php
```

就可以安装成功了
