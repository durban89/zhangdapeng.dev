---
title: "如何解决在laravel中使用jenssegers/mongodb的问题解决方案"
date: "2025-07-10 10:58:05"
slug: "ru-he-jie-jue-zai-laravel-zhong-shi-yong-jenssegersmongodb-de-wen-ti-jie-jue-fang-an"
categories: ["技术"]
tags: ["PHP", "Laravel", "MongoDB"]
aliases:
  - "/2025/07/10/如何解决在laravel中使用jenssegers/mongodb的问题解决方案/"
  - "/2025/07/10/如何解决在laravel中使用jenssegers/mongodb的问题解决方案.html"
  - "/如何解决在laravel中使用jenssegers/mongodb的问题解决方案/"
  - "/如何解决在laravel中使用jenssegers/mongodb的问题解决方案.html"
  - "/2025/07/10/如何解决在laravel中使用jenssegers-mongodb的问题解决方案/"
  - "/2025/07/10/如何解决在laravel中使用jenssegers-mongodb的问题解决方案.html"
  - "/2025/07/10/ru-he-jie-jue-zai-laravel-zhong-shi-yong-jenssegersmongodb-de-wen-ti-jie-jue-fang-an/"
  - "/2025/07/10/ru-he-jie-jue-zai-laravel-zhong-shi-yong-jenssegersmongodb-de-wen-ti-jie-jue-fang-a.html"
  - "/ru-he-jie-jue-zai-laravel-zhong-shi-yong-jenssegersmongodb-de-wen-ti-jie-jue-fang-an.html"
---
在使用laravel中的时候，会遇到将扩展包直接加载到现有项目中，而且在项目提交中的时候忘记将composer.lock提交，其中个别原因肯定很多，多数是由于项目管理不善导致的，但是问题已经出来了，何必再去纠结，找到办法解决再谈后话。

下面是我的解决思路

1、将本地的composer.lock删除   
2、composer -vvv install  
注意，如果你的很慢的话，请适用下阿里云的的库吧

https://mirrors.aliyun.com/composer/

建议来个全局配置吧

```bash
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

你也许会想到我想换回原来的怎么办 或者不想用怎么办

```bash
composer config -g --unset repos.packagist
```

这个命令可以解决

之后会提示你需要一个mongodb的扩展，好烦哦

3、MongoDB 扩展安装

官方说明  
https://php.net/manual/en/mongodb.installation.php

mac下操作

```bash
brew install homebrew/php/php71-mongodb
```

不要意思 此命令已经被废弃了

> 2018-03-31 起弃用 homebrew/php

以后安装php扩展请用如下命令

```bash
pecl install mongodb
```

如果你的电脑不是同构brew安装的php请自行下载对应的版本扩展进行安装吧

```bash
Build process completed successfully
Installing '/usr/local/Cellar/[email protected]/7.1.16/pecl/20160303/mongodb.so'
install ok: channel://pecl.php.net/mongodb-1.5.5
Extension mongodb enabled in php.ini
```

这个是我的安装成功的结果截图

然后在执行以下

```bash
composer -vvv install 
```

问题得到解决
