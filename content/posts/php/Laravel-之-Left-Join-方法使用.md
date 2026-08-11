---
title: "Laravel 之 Left Join 方法使用"
date: "2025-07-03 17:10:21"
slug: "laravel-zhi-left-join-fang-fa-shi-yong"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/03/Laravel-之-Left-Join-方法使用/"
  - "/2025/07/03/Laravel-之-Left-Join-方法使用.html"
  - "/Laravel-之-Left-Join-方法使用/"
  - "/Laravel-之-Left-Join-方法使用.html"
  - "/2025/07/03/laravel-zhi-left-join-fang-fa-shi-yong/"
  - "/2025/07/03/laravel-zhi-left-join-fang-fa-shi-yong.html"
  - "/laravel-zhi-left-join-fang-fa-shi-yong.html"
---
举例子如下：

```php
$models = static::where('user_id', $userId)->leftJoin('product_gift', function ($join) {
    $join->on('product_gift_exchange_order.prd_id', '=', 'product_gift.prd_id');
    $join->on('product_gift_exchange_order.gift_code', '=', 'product_gift.gift_code');
})->orderBy('product_gift_exchange_order.autokid', 'DESC')->get([
    'product_gift_exchange_order.autokid',
    'product_gift_exchange_order.ctime',
    'product_gift_exchange_order.exchange_amount',
    'product_gift.gift_name',
]);
```
