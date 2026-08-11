---
title: "PHP 之 smarty 的奇葩语法"
date: "2025-06-27 10:26:05"
slug: "php-zhi-smarty-de-qi-pa-yu-fa"
categories: ["技术"]
tags: ["PHP", "Smarty"]
aliases:
  - "/2025/06/27/PHP-之-smarty-的奇葩语法/"
  - "/2025/06/27/PHP-之-smarty-的奇葩语法.html"
  - "/PHP-之-smarty-的奇葩语法/"
  - "/PHP-之-smarty-的奇葩语法.html"
  - "/2025/06/27/php-zhi-smarty-de-qi-pa-yu-fa/"
  - "/2025/06/27/php-zhi-smarty-de-qi-pa-yu-fa.html"
  - "/php-zhi-smarty-de-qi-pa-yu-fa.html"
---
最近观赏了一下smarty（不知道为啥还有人在使用这个东西啊），发现了一个奇葩的使用方法。

```php
{#function name=menu level=0#}
   {#foreach $data as $entry#}
    {#if is_array($entry)#}      
{#$entry@key#}
     {#call name=menu data=$entry level=$level+1#}
    {#else#}      
{#$entry#}
   {#/if#}
  {#/foreach#}  
{#/function#}

{#* create an array to demonstrate *#}
{#$menu = ['item1','item2','item3' => ['item3-1','item3-2','item3-3' =>
['item3-3-1','item3-3-2']],'item4']#}

{#* run the array through the function *#}
{#call name=menu data=$menu#}
{#* call menu data=$menu *#} {#* short-hand *#}
```

输出的结果是如下：

```html
<ul class="level0">
    <li>item1</li>
    <li>item2</li>
    <li>item3</li>
<ul class="level1">
    <li>item3-1</li>
    <li>item3-2</li>
    <li>item3-3</li>
<ul class="level2">
    <li>item3-3-1</li>
    <li>item3-3-2</li>
</ul>
</ul>
    <li>item4</li>
</ul>
```

这就是smarty的call的内置函数的试用方法

