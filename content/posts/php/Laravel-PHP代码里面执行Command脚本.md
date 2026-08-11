---
title: "Laravel - PHP代码里面执行Command脚本"
date: "2025-07-11 10:29:22"
slug: "laravel-php-dai-ma-li-mian-zhi-xing-command-jiao-ben"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/11/Laravel-PHP代码里面执行Command脚本/"
  - "/2025/07/11/Laravel-PHP代码里面执行Command脚本.html"
  - "/Laravel-PHP代码里面执行Command脚本/"
  - "/Laravel-PHP代码里面执行Command脚本.html"
  - "/2025/07/11/laravel-php-dai-ma-li-mian-zhi-xing-command-jiao-ben/"
  - "/2025/07/11/laravel-php-dai-ma-li-mian-zhi-xing-command-jiao-ben.html"
  - "/laravel-php-dai-ma-li-mian-zhi-xing-command-jiao-ben.html"
---
以前每次上线 我记得 都要执行一个很多的重复的脚本 我一直很苦恼 无法自拔 以至于快要放弃的时候 我发现了`\Artisan::call`没想到居然这么好用 以后我觉得我不在担心很多重复的脚本要执行了 因为有了这个东西 就可以自己写个循环 让他自己去跑了 我就不需要在一个一个执行命令去跑了  
示例如下

```php
$maxDate = '2020-06-29';
$minDate = '2019-06-20';
while($maxDate > $minDate) {
	$endDate = $maxDate;

	\Artisan::call('daodao:xxxx-ad-xxx-xxx-stat', ['date'=>$endDate]);

	$maxDate = date('Y-m-d', strtotime('-1 day', strtotime($endDate)));
}
```

其他详情请 点击[[这里](https://learnku.com/docs/laravel/5.1/artisan/1058)]

然后还有更详细的 用法

`callSilent` 这个 silent 应该也很实用
