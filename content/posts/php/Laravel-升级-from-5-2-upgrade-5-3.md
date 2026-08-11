---
title: "laravel 升级 from 5.2 upgrade 5.3"
date: "2025-07-14 16:27:58"
slug: "laravel-sheng-ji-from-52-upgrade-53"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/14/laravel-升级-from-5.2-upgrade-5.3/"
  - "/2025/07/14/laravel-升级-from-5.2-upgrade-5.3.html"
  - "/laravel-升级-from-5.2-upgrade-5.3/"
  - "/laravel-升级-from-5.2-upgrade-5.3.html"
  - "/2025/07/14/Laravel-升级-from-5-2-upgrade-5-3/"
  - "/2025/07/14/Laravel-升级-from-5-2-upgrade-5-3.html"
  - "/2025/07/14/laravel-sheng-ji-from-52-upgrade-53/"
  - "/2025/07/14/laravel-sheng-ji-from-52-upgrade-53.html"
  - "/laravel-sheng-ji-from-52-upgrade-53.html"
---
laravel升级记录，laravel from 5.2 upgrade 5.3

升级之前我们要知道的第一个点，在5.3中被移除的方法如下，详情点击[这里](https://laravel.com/docs/5.3/upgrade#5.2-deprecations)

* 1 - `Illuminate\Contracts\Bus\SelfHandling` contract. Can be removed from jobs.
* 2 - The lists method on the Collection, query builder and Eloquent query builder objects has been renamed to pluck. The method signature remains the same.
* 3 - Implicit controller routes using `Route::controller` have been deprecated. Please use explicit route registration in your routes file. This will likely be extracted into a package.
* 4 - The get, post, and other route helper functions have been removed. You may use the Route facade instead.
* 5 - The database session driver from 5.1 has been renamed to legacy-database and will be removed. Consult notes on the "database session driver" above for more information.
* 6 - The `Str::randomBytes` function has been deprecated in favor of the random\_bytes native PHP function.
* 7 - The `Str::equals` function has been deprecated in favor of the hash\_equals native PHP function.
* 8 - `Illuminate\View\Expression` has been deprecated in favor of `Illuminate\Support\HtmlString`.
* The WincacheStore cache driver has been removed.

如果是在国内的话，记得更新镜像源，请参考[这里](https://www.gowhich.com/blog/1068)

然后修改composer.json中

```bash
"laravel/framework": "5.2.*",
```

改为

```bash
"laravel/framework": "5.3.*",
```

然后执行

```bash
composer update --verbose
```

或者

```bash
composer update --verbose --ignore-platform-reqs
```

如果遇到依赖问题，比如我这里遇到了`laravelcollective/html`，

类似`requires...satisfiable...`的提示

只需要将这个库暂时移除，然后在执行上面的命令

顺利的话，就安装成功了

然后在安装回刚刚移除的库，比如laravelcollective/html，这个时候可能会遇到，如果使用原来老的版本的话，会提示类似不兼容现在laravel5.3这个版本，需要针对性的安装对应的版本，如果不带版本号的话会安装最新版本，那个时候，依赖的项目会很多，composer会自动升级对应的依赖版本，建议不要这么做

最后安装完，参考[[这里](https://laravel.com/docs/5.3/upgrade#upgrade-5.3.0)]，修改对应的代码就可以了。
