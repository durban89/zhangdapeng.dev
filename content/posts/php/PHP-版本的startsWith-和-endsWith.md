---
title: "PHP 版本的startsWith 和 endsWith"
date: "2025-07-03 11:07:53"
slug: "php-ban-ben-de-startswith-he-endswith"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP-版本的startsWith-和-endsWith/"
  - "/2025/07/03/PHP-版本的startsWith-和-endsWith.html"
  - "/PHP-版本的startsWith-和-endsWith/"
  - "/PHP-版本的startsWith-和-endsWith.html"
  - "/2025/07/03/php-ban-ben-de-startswith-he-endswith/"
  - "/2025/07/03/php-ban-ben-de-startswith-he-endswith.html"
  - "/php-ban-ben-de-startswith-he-endswith.html"
---
JS处理字符串的时候，有些地方还是很方便的。

但是PHP也不是很逊色，也有对应的解决方案。

```php
function startsWith($haystack, $needle){
    return strncmp($haystack, $needle, strlen($needle)) === 0;
}

function endsWith($haystack, $needle){
    return $needle === '' || substr_compare($haystack, $needle, -strlen($needle)) === 0;
}
```

不理解`strcmp`和`substr_compare`的可以自己去查查文档


