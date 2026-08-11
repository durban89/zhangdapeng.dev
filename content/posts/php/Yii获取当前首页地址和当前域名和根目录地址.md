---
title: "Yii获取当前首页地址和当前域名和根目录地址"
date: "2025-06-19 09:58:12"
slug: "yii-huo-qu-dang-qian-shou-ye-di-zhi-he-dang-qian-yu-ming-he-gen-mu-lu-di-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/19/Yii获取当前首页地址和当前域名和根目录地址/"
  - "/2025/06/19/Yii获取当前首页地址和当前域名和根目录地址.html"
  - "/Yii获取当前首页地址和当前域名和根目录地址/"
  - "/Yii获取当前首页地址和当前域名和根目录地址.html"
  - "/2025/06/19/yii-huo-qu-dang-qian-shou-ye-di-zhi-he-dang-qian-yu-ming-he-gen-mu-lu-di-zhi/"
  - "/2025/06/19/yii-huo-qu-dang-qian-shou-ye-di-zhi-he-dang-qian-yu-ming-he-gen-mu-lu-di-zhi.html"
  - "/yii-huo-qu-dang-qian-shou-ye-di-zhi-he-dang-qian-yu-ming-he-gen-mu-lu-di-zhi.html"
---
### [当前域名](#1)

```php
echo Yii::app()->request->hostInfo;
```

### [除域名外的URL](#2)

```php
echo Yii::app()->request->getUrl();
```

### [除域名外的首页地址](#3)

```php
echo Yii::app()->user->returnUrl;
```

### [除域名外的根目录地址](#4)

```php
echo Yii::app()->homeUrl;
```
