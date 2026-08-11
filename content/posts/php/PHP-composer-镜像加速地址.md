---
title: "PHP composer 镜像加速地址"
date: "2025-07-10 10:58:07"
slug: "php-composer-jing-xiang-jia-su-di-zhi"
categories: ["技术"]
tags: ["PHP", "Composer"]
aliases:
  - "/2025/07/10/PHP-composer-镜像加速地址/"
  - "/2025/07/10/PHP-composer-镜像加速地址.html"
  - "/PHP-composer-镜像加速地址/"
  - "/PHP-composer-镜像加速地址.html"
  - "/2025/07/10/php-composer-jing-xiang-jia-su-di-zhi/"
  - "/2025/07/10/php-composer-jing-xiang-jia-su-di-zhi.html"
  - "/php-composer-jing-xiang-jia-su-di-zhi.html"
---
### 阿里云 Composer 全量镜像（推荐）

镜像类型：全量镜像

更新时间：1 分钟

镜像地址：<https://mirrors.aliyun.com/composer/>

官方地址：<https://developer.aliyun.com/composer>

镜像说明：阿里云 CDN 加速，更新速度快，推荐使用

### 安畅网络镜像

镜像类型：全量镜像

更新时间：1 分钟

镜像地址：[https://php.cnpkg.org](https://php.cnpkg.org/)

官方地址：<https://php.cnpkg.org/>

镜像说明：此 Composer 镜像由安畅网络赞助，目前支持元数据、下载包全量代理。

### 交通大学镜像

镜像类型：非全量镜像

镜像地址：[https://packagist.mirrors.sjtug.sjtu.edu.cn](https://packagist.mirrors.sjtug.sjtu.edu.cn/)

官方地址：<https://packagist.mirrors.sjtug.sjtu.edu.cn/>

镜像说明：上海交通大学提供的 composer 镜像，稳定、快速、现代的镜像服务，推荐使用。

### 全局配置（推荐）

所有项目都会使用该镜像地址：

```bash
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

取消配置：

```bash
composer config -g --unset repos.packagist
```

项目配置

仅修改当前工程配置，仅当前工程可使用该镜像地址：

```bash
composer config repo.packagist composer https://mirrors.aliyun.com/composer/
```

取消配置：

```bash
composer config --unset repos.packagist
```

调试

composer 命令增加 -vvv 可输出详细的信息，命令如下：

```bash
composer -vvv require alibabacloud/sdk
```

### 忽略版本匹配

composer可以设置忽略版本匹配，命令是：

```bash
composer install --ignore-platform-reqs
```

或者

```bash
composer update --ignore-platform-reqs
```

再次执行composer命令可以正常安装包了

参考网址：<https://learnku.com/composer/wikis/30594>
