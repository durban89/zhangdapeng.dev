---
title: "MySQL Insert的几点操作(DELAYED 、IGNORE、ON DUPLICATE KEY UPDATE )"
date: "2025-06-24 11:24:31"
slug: "mysql-insert-de-ji-dian-cao-zuo-delayed-ignore-on-duplicate-key-update"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/24/MySQL-Insert的几点操作(DELAYED-、IGNORE、ON-DUPLICATE-KEY-UPDATE-)/"
  - "/2025/06/24/MySQL-Insert的几点操作(DELAYED-、IGNORE、ON-DUPLICATE-KEY-UPDATE-).html"
  - "/MySQL-Insert的几点操作(DELAYED-、IGNORE、ON-DUPLICATE-KEY-UPDATE-)/"
  - "/MySQL-Insert的几点操作(DELAYED-、IGNORE、ON-DUPLICATE-KEY-UPDATE-).html"
  - "/2025/06/24/MySQL-Insert的几点操作-DELAYED-IGNORE-ON-DUPLICATE-KEY-UPDATE/"
  - "/2025/06/24/MySQL-Insert的几点操作-DELAYED-IGNORE-ON-DUPLICATE-KEY-UPDATE.html"
  - "/2025/06/24/mysql-insert-de-ji-dian-cao-zuo-delayed-ignore-on-duplicate-key-update/"
  - "/2025/06/24/mysql-insert-de-ji-dian-cao-zuo-delayed-ignore-on-duplicate-key-update.html"
  - "/mysql-insert-de-ji-dian-cao-zuo-delayed-ignore-on-duplicate-key-update.html"
---
INSERT语法

```sql
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
       [INTO] tbl_name [(col_name,...)]
       VALUES ({expr | DEFAULT},...),(...),...
       [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```

或：

```sql
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
       [INTO] tbl_name
       SET col_name={expr | DEFAULT}, ...
       [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```

或：

```sql
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
       [INTO] tbl_name [(col_name,...)]
       SELECT ...
       [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```

## [一、DELAYED 的使用](#1)

使用延迟插入操作

DELAYED调节符应用于INSERT和REPLACE语句。当DELAYED插入操作到达的时候，

服务器把数据行放入一个队列中，并立即给客户端返回一个状态信息，这样客户

端就可以在数据表被真正地插入记录之前继续进行操作了。如果读取者从该数据

表中读取数据，队列中的数据就会被保持着，直到没有读取者为止。接着服务器

开始插入延迟数据行（delayed-row）队列中的数据行。在插入操作的同时，服务器

还要检查是否有新的读取请求到达和等待。如果有，延迟数据行队列就被挂起，

允许读取者继续操作。当没有读取者的时候，服务器再次开始插入延迟的数据行。

这个过程一直进行，直到队列空了为止。

几点要注意事项：

INSERT DELAYED应该仅用于指定值清单的INSERT语句。服务器忽略用于INSERT DELAYED...SELECT语句的DELAYED。

服务器忽略用于INSERT DELAYED...ON DUPLICATE UPDATE语句的DELAYED。

因为在行被插入前，语句立刻返回，所以您不能使用LAST\_INSERT\_ID()来获取AUTO\_INCREMENT值。AUTO\_INCREMENT值可能由语句生成。

对于SELECT语句，DELAYED行不可见，直到这些行确实被插入了为止。

DELAYED在从属复制服务器中被忽略了，因为DELAYED不会在从属服务器中产生与主服务器不一样的数据。

注意，目前在队列中的各行只保存在存储器中，直到它们被插入到表中为止。这意味着，如果您强行中止了mysqld（例如，使用kill -9）

或者如果mysqld意外停止，则所有没有被写入磁盘的行都会丢失。

## [二、IGNORE的使用](#2)

IGNORE是MySQL相对于标准SQL的扩展。如果在新表中有重复关键字，

或者当STRICT模式启动后出现警告，则使用IGNORE控制ALTER TABLE的运行。

如果没有指定IGNORE，当重复关键字错误发生时，复制操作被放弃，返回前一步骤。

如果指定了IGNORE，则对于有重复关键字的行，只使用第一行，其它有冲突的行被删除。

并且，对错误值进行修正，使之尽量接近正确值。

```sql
insert ignore into tb(...) value(...)
```

这样不用校验是否存在了，有则忽略，无则添加

## [三、ON DUPLICATE KEY UPDATE的使用](#3)

如果您指定了ON DUPLICATE KEY UPDATE，并且插入行后会导致在一个UNIQUE索引或PRIMARY KEY中出现重复值，则执行旧行UPDATE。例如，如果列a被定义为UNIQUE，并且包含值1，则以下两个语句具有相同的效果：

```sql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3)
    -> ON DUPLICATE KEY UPDATE c=c+1;
mysql> UPDATE table SET c=c+1 WHERE a=1;
```

如果行作为新记录被插入，则受影响行的值为1；

如果原有的记录被更新，则受影响行的值为2。

注释：如果列b也是唯一列，则INSERT与此UPDATE语句相当：

```sql
mysql> UPDATE table SET c=c+1 WHERE a=1 OR b=2 LIMIT 1;
```

如果a=1 OR b=2与多个行向匹配，则只有一个行被更新。通常，您应该尽量避免对带有多个唯一关键字的表使用ON DUPLICATE KEY子句。

您可以在UPDATE子句中使用VALUES(col\_name)函数从INSERT...UPDATE语句的INSERT部分引用列值。换句话说，如果没有发生重复关键字冲突，则UPDATE子句中的VALUES(col\_name)可以引用被插入的col\_name的值。本函数特别适用于多行插入。VALUES()函数只在INSERT...UPDATE语句中有意义，其它时候会返回NULL。

示例：

```sql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3),(4,5,6)
    -> ON DUPLICATE KEY UPDATE c=VALUES(a)+VALUES(b);
```

本语句与以下两个语句作用相同：

```sql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3)
    -> ON DUPLICATE KEY UPDATE c=3;
mysql> INSERT INTO table (a,b,c) VALUES (4,5,6)
    -> ON DUPLICATE KEY UPDATE c=9;
```

当您使用ON DUPLICATE KEY UPDATE时，DELAYED选项被忽略。

总结：

***DELAYED***做为快速插入，并不是很关心失效性，提高插入性能。

***IGNORE***只关注主键对应记录是不存在，无则添加，有则忽略。

***ON DUPLICATE KEY UPDATE*** 在添加时操作，关注非主键列，注意与ignore的区别。有则更新指定列，无则添加。

