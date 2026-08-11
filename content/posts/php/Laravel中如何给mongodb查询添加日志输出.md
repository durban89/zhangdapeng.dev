---
title: "Laravel中如何给mongodb查询添加日志输出"
date: "2025-07-15 09:51:23"
slug: "laravel-zhong-ru-he-gei-mongodb-cha-xun-tian-jia-ri-zhi-shu-chu"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/15/Laravel中如何给mongodb查询添加日志输出/"
  - "/2025/07/15/Laravel中如何给mongodb查询添加日志输出.html"
  - "/Laravel中如何给mongodb查询添加日志输出/"
  - "/Laravel中如何给mongodb查询添加日志输出.html"
  - "/2025/07/15/laravel-zhong-ru-he-gei-mongodb-cha-xun-tian-jia-ri-zhi-shu-chu/"
  - "/2025/07/15/laravel-zhong-ru-he-gei-mongodb-cha-xun-tian-jia-ri-zhi-shu-chu.html"
  - "/laravel-zhong-ru-he-gei-mongodb-cha-xun-tian-jia-ri-zhi-shu-chu.html"
---
给mongodb添加查询日志输出方法非常简单，可以像下面这样添加

```php
DB::connection('mongodb')->enableQueryLog();
DB::connection('mongodb')->getQueryLog();
```

“`mongodb`”的配置是在database.php中配置的

```php
'mongodb' => [
    'driver' => 'mongodb',
    'dsn' => env('MONGODB_DSN'),
    'database' => env('MONGODB_DATABASE'),
],
```

为什么要加这段代码之后才会有日志输出呢

原因是因为默认的情况下，laravel只针对默认的数据库配置进行日志输出

可以尝试打开`config/database.php`文件，找到类似下面这行

```php
'default' => env('DB_CONNECTION', 'mysql'),
```

默认情况下执行的是下面的代码

```php
DB::enableQueryLog();
DB::getQueryLog();
```

既然是默认获取的也是默认的数据库配置查询

参考：[参考1](https://stackoverflow.com/questions/59476305/how-can-i-get-mongodb-query-log-in-laravel)
