---
title: "PHP8.5新功能预览"
date: "2025-06-27 13:30:01"
slug: "php85-xin-gong-neng-yu-lan"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/PHP8.5新功能预览/"
  - "/2025/06/27/PHP8.5新功能预览.html"
  - "/PHP8.5新功能预览/"
  - "/PHP8.5新功能预览.html"
  - "/2025/06/27/PHP8-5新功能预览/"
  - "/2025/06/27/PHP8-5新功能预览.html"
  - "/2025/06/27/php85-xin-gong-neng-yu-lan/"
  - "/2025/06/27/php85-xin-gong-neng-yu-lan.html"
  - "/php85-xin-gong-neng-yu-lan.html"
---
PHP 8.5 将于 2025 年 11 月发布，并带来一些有用的新功能和改进。此版本侧重于开发人员体验增强、新的实用程序函数和更好的调试功能。

### [新的数组函数](#1)

***array_first()*** 和 ***array_last()***

PHP 8.5 添加了两个请求量很大的函数，用于检索数组的第一个和最后一个值，补充了 PHP 7.3 中现有的`array_key_first()`和`array_key_last()`函数。

```php
$users = ['Alice', 'Bob', 'Charlie'];

$firstUser = array_first($users);  // 'Alice'
$lastUser = array_last($users);    // 'Charlie'

// Works with associative arrays too
$data = ['name' => 'John', 'age' => 30, 'city' => 'Berlin'];
echo array_first($data); // 'John'
echo array_last($data);  // 'Berlin'

// Returns null for empty arrays
$empty = [];
var_dump(array_first($empty)); // null
var_dump(array_last($empty));  // null
```

这些函数等效于：

`array_first($array)` → `$array[array_key_first($array)]`
`array_last($array)` → `$array[array_key_last($array)]`


### [管道操作](#2)


PHP 8.5 引入了一个新的管道运算符 ***(|>)***，它允许从左到右链接多个可调用对象，将左侧可调用对象的返回值传递给右侧可调用对象：

```php
$result = 'Hello World'
    |> strtoupper(...)
    |> str_shuffle(...)
    |> trim(...);
// 输出: 'LWHO LDLROE' (or similar shuffled result)

// 等价于:
$result = trim(str_shuffle(strtoupper('Hello World')));

// 或者等价于:
$result = 'Hello World';
$result = strtoupper($result);
$result = str_shuffle($result);
$result = trim($result);
```

管道运算符适用于任何可调用对象 - 函数、方法、闭包和第一类可调用对象。但是，它有一些限制：

- 所有可调用对象必须只接受一个必需的参数
- 不能使用具有按引用参数的函数(少数例外)
- 返回值始终作为第一个参数传递

### [新的错误和异常处理程序 getter](#3)

PHP 8.5 引入了两个新函数，允许您检索当前活动的错误和异常处理程序：`get_error_handler()`和`get_exception_handler()`。 这两个函数都返回当前可调用的处理程序，如果未设置自定义处理程序，则返回`null`。

### [新的cURL函数](#4) 


***curl_multi_get_handles()***

cURL 扩展获得了一个新函数，用于从多手柄中检索所有句柄：

```php
$multiHandle = curl_multi_init();

$ch1 = curl_init('https://api.example.com/users');
$ch2 = curl_init('https://api.example.com/posts');

curl_multi_add_handle($multiHandle, $ch1);
curl_multi_add_handle($multiHandle, $ch2);

// New in PHP 8.5: Get all handles
$handles = curl_multi_get_handles($multiHandle);
// Returns: [$ch1, $ch2]

// Execute and process results
$running = null;
do {
    curl_multi_exec($multiHandle, $running);
} while ($running > 0);

foreach ($handles as $handle) {
    $response = curl_multi_getcontent($handle);
    curl_multi_remove_handle($multiHandle, $handle);
}
```

### [新的Locale函数](#5)

***locale_is_right_to_left()***

PHP 8.5 添加了对检测从右到左 (RTL) 语言环境的支持，从而提高了国际化功能：

```php
// Check if locale uses RTL writing
$isRTL = locale_is_right_to_left('ar_SA'); // true (Arabic)
$isLTR = locale_is_right_to_left('en_US'); // false (English)
$isFarsi = locale_is_right_to_left('fa_IR'); // true (Persian/Farsi)

// Object-oriented approach
$isRTL = Locale::isRightToLeft('he_IL'); // true (Hebrew)
```

### [新PHP_BUILD_DATE常量](#6)


一个新的常量提供了 PHP 二进制文件的构建日期，用于调试和版本审计：

```php
echo PHP_BUILD_DATE; // e.g., 'Nov 15 2025 10:30:45'

// Useful for debugging in production
echo 'PHP Version: ' . PHP_VERSION . "\n";
echo 'Build Date: ' . PHP_BUILD_DATE . "\n";
```

### [CLI 增强功能](#7)

***php --ini=diff***

一个新的 CLI 选项，用于仅输出非默认 INI 指令：

```php
# Show only modified settings
php --ini=diff

# Example output:
# memory_limit = 256M (default: 128M)
# max_execution_time = 60 (default: 30)
```

