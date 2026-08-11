---
title: "Laravel Validator 表单验证如何使用"
date: "2025-07-11 10:40:45"
slug: "laravel-validator-biao-dan-yan-zheng-ru-he-shi-yong"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/11/Laravel-Validator-表单验证如何使用/"
  - "/2025/07/11/Laravel-Validator-表单验证如何使用.html"
  - "/Laravel-Validator-表单验证如何使用/"
  - "/Laravel-Validator-表单验证如何使用.html"
  - "/2025/07/11/laravel-validator-biao-dan-yan-zheng-ru-he-shi-yong/"
  - "/2025/07/11/laravel-validator-biao-dan-yan-zheng-ru-he-shi-yong.html"
  - "/laravel-validator-biao-dan-yan-zheng-ru-he-shi-yong.html"
---
首先引入我们需要的Validator类

```php
use Illuminate\Support\Facades\Validator;
```

举个简单的例子

比如要验证密码的安全性

我们可以这样写代码

```php
public function index (Request $request) {
	$validate = Validator::make($request->all(), [
		'password' => [
			'required',
			'min:8',
			'regex:/^.*(?=.{3,})(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\d\X])(?=.*[!$#%]).*$/',
		],
	]);

	if ($validate->fails) {
		\Log::info($validate->messages()->toJson());
	}
}
```

如果像对验证的错误信息进行自定义

可以这样写代码

```php
public function index (Request $request) {
	$validate = Validator::make($request->all(), [
		'password' => [
			'required',
			'min:8',
			'regex:/^.*(?=.{3,})(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\d\X])(?=.*[!$#%]).*$/',
		],
	], [
		'password.min' => '密码格式长度错误',
		'password.regex' => '密码格式错误',
	]);

	if ($validate->fails) {
		\Log::info($validate->messages()->toJson());
	}
}
```
