---
title: "MySQL 替换字段中某几个字符并更新"
date: "2025-07-14 16:28:12"
slug: "mysql-ti-huan-zi-duan-zhong-mou-ji-ge-zi-fu-bing-geng-xin"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/14/MySQL-替换字段中某几个字符并更新/"
  - "/2025/07/14/MySQL-替换字段中某几个字符并更新.html"
  - "/MySQL-替换字段中某几个字符并更新/"
  - "/MySQL-替换字段中某几个字符并更新.html"
  - "/2025/07/14/mysql-ti-huan-zi-duan-zhong-mou-ji-ge-zi-fu-bing-geng-xin/"
  - "/2025/07/14/mysql-ti-huan-zi-duan-zhong-mou-ji-ge-zi-fu-bing-geng-xin.html"
  - "/mysql-ti-huan-zi-duan-zhong-mou-ji-ge-zi-fu-bing-geng-xin.html"
---
mysql 替换字段中某几个字符并更新

```sql
UPDATE `database`.`table` 
SET `column` = REPLACE(column,'旧字符串','新字符串');
```
