---
title: "Composer不同php版本的使用方法"
date: "2025-07-15 10:29:04"
slug: "composer-bu-tong-php-ban-ben-de-shi-yong-fang-fa"
categories: ["技术"]
tags: ["Composer"]
aliases:
  - "/2025/07/15/Composer不同php版本的使用方法/"
  - "/2025/07/15/Composer不同php版本的使用方法.html"
  - "/Composer不同php版本的使用方法/"
  - "/Composer不同php版本的使用方法.html"
  - "/2025/07/15/composer-bu-tong-php-ban-ben-de-shi-yong-fang-fa/"
  - "/2025/07/15/composer-bu-tong-php-ban-ben-de-shi-yong-fang-fa.html"
  - "/composer-bu-tong-php-ban-ben-de-shi-yong-fang-fa.html"
---
composer不同php版本的使用方法

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

如果本地安装了多个版本的php，需要将不同版本的php重命名一下  
比如安装了

7.1 7.2 7.3 8.1 8.2  
那么，对应的重命名php的名称是  
php7.1 php7.2 php7.3 php8.1 php8.2

之后安装composer的时候直接使用对应重命名的php就好了  
比如使用php7.3

```bash
php7.3 -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php7.3 -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php7.3 composer-setup.php
php7.3 -r "unlink('composer-setup.php');"
```

如果需要制定composer的话，参考如下

```bash
php7.3 composer-setup.php --install-dir=/usr/local/bin --filename=composer7.3 
```

如果遇到错误提示

> The installation directory "/usr/local/bin" is not writable

请加上sudo

```bash
sudo php7.3 composer-setup.php --install-dir=/usr/local/bin --filename=composer7.3 
```

之后就可以正常使用composer的命令

```bash
php7.3 /usr/local/bin/composer7.3 install -vvv
```

不过执行命令的时候需要将composer替换为composer7.3

对于其他的版本的也可以使用类似的方式
