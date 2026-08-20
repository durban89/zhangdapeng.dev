---
title: "自PHP 5.3.4版本开始mt_rand()函数的参数要求变动 mt_rand(): max(1) is smaller than min(2)"
date: "2025-06-27 10:26:22"
slug: "zi-php-534-ban-ben-kai-shi-mt-rand-han-shu-de-can-shu-yao-qiu-bian-dong-mt-rand-max1-is-smaller-than-min2"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/自PHP-5.3.4版本开始mt-rand()函数的参数要求变动-mt-rand():-max(1)-is-smaller-than-min(2)/"
  - "/2025/06/27/自PHP-5.3.4版本开始mt-rand()函数的参数要求变动-mt-rand():-max(1)-is-smaller-than-min(2).html"
  - "/自PHP-5.3.4版本开始mt-rand()函数的参数要求变动-mt-rand():-max(1)-is-smaller-than-min(2)/"
  - "/自PHP-5.3.4版本开始mt-rand()函数的参数要求变动-mt-rand():-max(1)-is-smaller-than-min(2).html"
  - "/2025/06/27/自PHP-5-3-4版本开始mt-rand-函数的参数要求变动-mt-rand-max-1-is-smaller-than-min-2/"
  - "/2025/06/27/自PHP-5-3-4版本开始mt-rand-函数的参数要求变动-mt-rand-max-1-is-smaller-than-min-2.html"
  - "/2025/06/27/自PHP-5-3-4版本开始mt_rand-函数的参数要求变动-mt_rand-max-1-is-smaller-than-min-2.html"
---
在PHP 5.3.3版本以前，`mt_rand($a, $b)`传入的参数$a和$b二者没有数字大小比较的限制，但是自5.3.4版本PHP开始，传入的参数必须满足`$a<=$b`，即`mt_rand(1, 1)`和`mt_rand(1, 2)`是可以的，但是`mt_rand(2, 1)`就会报错：`mt_rand():
max(1) is smaller than min(2)`。  
  
这样，如果你使用mt_rand()函数时不是输入的固定数字，而是传入的一个变量的话，就必须先将变量做一个比较，以确定哪个变量放在前边或后边。  
比如，例子片段：

```php
if ($a<$b) {
  $rnd = mt_rand($a, $b);
} else {
  $rnd = mt_rand($b, $a);
}
```

---

参考文章：

http://www.lc365.net/blog/b/15287/

