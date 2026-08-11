---
title: "使用MySQL时如何精准查询慢SQL"
date: "2025-07-14 14:44:56"
slug: "shi-yong-mysql-shi-ru-he-jing-zhun-cha-xun-man-sql"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/14/使用MySQL时如何精准查询慢SQL/"
  - "/2025/07/14/使用MySQL时如何精准查询慢SQL.html"
  - "/使用MySQL时如何精准查询慢SQL/"
  - "/使用MySQL时如何精准查询慢SQL.html"
  - "/2025/07/14/shi-yong-mysql-shi-ru-he-jing-zhun-cha-xun-man-sql/"
  - "/2025/07/14/shi-yong-mysql-shi-ru-he-jing-zhun-cha-xun-man-sql.html"
  - "/shi-yong-mysql-shi-ru-he-jing-zhun-cha-xun-man-sql.html"
---
使用MySQL时如何精准查询慢SQL

在做技术开发的过程中，当产品在访问量很大的情况下，如果发现数据库cpu或者iops飙升，那么可以看看是不是有慢sql

但是慢sql如何查询，需要我们一个一个查吗，这个比较耗费人力成本

不如我推荐一个命令

```sql
select * from information_schema.processlist where COMMAND <> 'Sleep';
```

经过这样的查询就能累出所有运行中的sql，这个时候就可以看到哪个sql执行时间长了，

正常情况下我们会遇到类似如下的输出

```bash
+-----+------+-----------+------+---------+------+-----------+----------------------------------------------+
| ID  | USER | HOST      | DB   | COMMAND | TIME | STATE     | INFO                                         |
+-----+------+-----------+------+---------+------+-----------+----------------------------------------------+
| 106 | root | localhost | NULL | Query   |    0 | executing | select * from information_schema.processlist |
+-----+------+-----------+------+---------+------+-----------+----------------------------------------------+
```

我们可以通过TIME判断出哪条sql执行时间比较久
