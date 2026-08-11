---
title: "PHP 之 Composer 的 NpmRepository错误"
date: "2025-07-03 11:07:33"
slug: "php-zhi-composer-de-npmrepository-cuo-wu"
categories: ["技术"]
tags: ["PHP", "Composer"]
aliases:
  - "/2025/07/03/PHP-之-Composer-的-NpmRepository错误/"
  - "/2025/07/03/PHP-之-Composer-的-NpmRepository错误.html"
  - "/PHP-之-Composer-的-NpmRepository错误/"
  - "/PHP-之-Composer-的-NpmRepository错误.html"
  - "/2025/07/03/php-zhi-composer-de-npmrepository-cuo-wu/"
  - "/2025/07/03/php-zhi-composer-de-npmrepository-cuo-wu.html"
  - "/php-zhi-composer-de-npmrepository-cuo-wu.html"
---
最近进行了一次composer的update操作。
然后在我自己的项目里面运行了。

```bash
composer install
```

的操作，结果出现了很多的错误以前从未见过。

> Class Fxp\Composer\AssetPlugin\Repository\NpmRepository does not exist
>
> The "yiisoft/yii2-composer" plugin requires composer-plugin-api 1.0.0, this *WIL L* break in the future and it should be fixed ASAP (require ^1.0 for example).
>
> [ReflectionException] Class Fxp\Composer\AssetPlugin\Repository\NpmRepository does not exist
>
> [ErrorException]
>
> Declaration of Fxp\Composer\AssetPlugin\Repository\AbstractAssetsRepository::w hatProvides() should be compatible with Composer\Repository\ComposerRepository:: whatProvides(Composer\DependencyResolver\Pool $pool, $name, $bypassFilters = fal se)

解决方案就是：更新你的 `fxp/composer-asset-plugin`:

```bash
php composer.phar global update fxp/composer-asset-plugin --no-plugins
```

如果还是不行的话，可以试试下面这个

```bash
composer global require fxp/composer-asset-plugin --no-plugins
```


