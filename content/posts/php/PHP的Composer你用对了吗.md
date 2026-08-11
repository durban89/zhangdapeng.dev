---
title: "PHP的Composer你用对了吗？"
date: "2025-07-14 14:54:59"
slug: "php-de-composer-ni-yong-dui-le-ma"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/14/PHP的Composer你用对了吗？/"
  - "/2025/07/14/PHP的Composer你用对了吗？.html"
  - "/PHP的Composer你用对了吗？/"
  - "/PHP的Composer你用对了吗？.html"
  - "/2025/07/14/PHP的Composer你用对了吗/"
  - "/2025/07/14/PHP的Composer你用对了吗.html"
  - "/2025/07/14/php-de-composer-ni-yong-dui-le-ma/"
  - "/2025/07/14/php-de-composer-ni-yong-dui-le-ma.html"
  - "/php-de-composer-ni-yong-dui-le-ma.html"
---
我们在使用php的框架的时候，比如laravel、yii2等

会用到composer这个安装包的工具，类似于nodejs的npm、python的pip

但是总有因为各种限制，安装包的时候不能访问到指定的资源

这个时候就有各种的第三方镜像资源可以供我们使用

我想说的是，第三方资源没问题，但是网上写文章的人就有问题了，以为你只告诉了如何配置，但是如果历史已经安装成功的，会有相关的安装历史记录的记录

比如composer会有composer.lock

比如nvm会有package-lock.json等类似的，方便下次安装的时候，保证对应的版本号不变

今天记录下如下正确的使用composer

1、安装composer，已经安装的可以跳过

2、配置源镜像

可以像下面这样全局配置

```bash
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

也可以像下面这样配置当前项目

```bash
composer config repo.packagist composer https://mirrors.aliyun.com/composer/
```

如果遇到不想用的情况，可以使用下面的命令取消

```bash
composer config -g --unset repos.packagist
```

```bash
composer config --unset repos.packagist
```

依次对应上面的不情况的配置

3、清缓存

```bash
composer clear
```

4、更新composer.lock

```bash
composer update --lock
```

5、开始使用新的源来安装包

```bash
composer install
```