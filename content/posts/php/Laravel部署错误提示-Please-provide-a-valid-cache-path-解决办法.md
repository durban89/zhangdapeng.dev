---
title: "Laravel部署错误提示“Please provide a valid cache path.”解决办法"
date: "2025-07-15 10:28:35"
slug: "laravel-bu-shu-cuo-wu-ti-shi-please-provide-a-valid-cache-path-jie-jue-ban-fa"
categories: ["技术"]
tags: ["Laravel"]
aliases:
  - "/2025/07/15/Laravel部署错误提示“Please-provide-a-valid-cache-path.”解决办法/"
  - "/2025/07/15/Laravel部署错误提示“Please-provide-a-valid-cache-path.”解决办法.html"
  - "/Laravel部署错误提示“Please-provide-a-valid-cache-path.”解决办法/"
  - "/Laravel部署错误提示“Please-provide-a-valid-cache-path.”解决办法.html"
  - "/2025/07/15/Laravel部署错误提示-Please-provide-a-valid-cache-path-解决办法/"
  - "/2025/07/15/Laravel部署错误提示-Please-provide-a-valid-cache-path-解决办法.html"
  - "/2025/07/15/laravel-bu-shu-cuo-wu-ti-shi-please-provide-a-valid-cache-path-jie-jue-ban-fa/"
  - "/2025/07/15/laravel-bu-shu-cuo-wu-ti-shi-please-provide-a-valid-cache-path-jie-jue-ban-fa.html"
  - "/laravel-bu-shu-cuo-wu-ti-shi-please-provide-a-valid-cache-path-jie-jue-ban-fa.html"
---
laravel部署错误提示“Please provide a valid cache path.”解决办法

解决方法如下：

1、确保`storage`目录下有如`app`，`framework`，`views`三个目录。

2、确保`storage/framework`目录下也有`cache`，`sessions`，`views`三个目录。

缺少以上目录就手动创建，然后访问网站首页试试。
