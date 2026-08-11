---
title: "MySQL存储过程与Laravel中使用方式"
date: "2025-07-11 10:29:25"
slug: "mysql-cun-chu-guo-cheng-yu-laravel-zhong-shi-yong-fang-shi"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/11/MySQL存储过程与Laravel中使用方式/"
  - "/2025/07/11/MySQL存储过程与Laravel中使用方式.html"
  - "/MySQL存储过程与Laravel中使用方式/"
  - "/MySQL存储过程与Laravel中使用方式.html"
  - "/2025/07/11/mysql-cun-chu-guo-cheng-yu-laravel-zhong-shi-yong-fang-shi/"
  - "/2025/07/11/mysql-cun-chu-guo-cheng-yu-laravel-zhong-shi-yong-fang-shi.html"
  - "/mysql-cun-chu-guo-cheng-yu-laravel-zhong-shi-yong-fang-shi.html"
---
MySQL 5.0 版本开始支持存储过程。 存储过程（Stored Procedure）是一种在数据库中存储复杂程序，以便外部程序调用的一种数据库对象。 存储过程是为了完成特定功能的SQL语句集，经编译创建并保存在数据库中，用户可通过指定存储过程的名字并给定参数(需要时)来调用执行。

### 优点

1.存储过程只在创造时进行编译，以后每次执行存储过程都不需再重新编译，而一般 SQL 语句每执行一次就编译一次,所以使用存储过程可提高数据库执行速度。

2.当对数据库进行复杂操作时(如对多个表进行 Update,Insert,Query,Delete 时），可将此复杂操作用存储过程封装起来与数据库提供的事务处理结合一起使用。这些操作，如果用程序来完成，就变成了一条条的 SQL 语句，可能要多次连接数据库。而换成存储，只需要连接一次数据库就可以了。

3.存储过程可以重复使用,可减少数据库开发人员的工作量。

4.安全性高,可设定只有某此用户才具有对指定存储过程的使用权。

### 缺点

1.如果更改范围大到需要对输入存储过程的参数进行更改，或者要更改由其返回的数据，则您仍需要更新程序集中的代码以添加参数、更新 GetValue() 调用，等等，这时候估计比较繁琐了。

2.可移植性差由于存储过程将应用程序绑定到 SQL Server，因此使用存储过程封装业务逻辑将限制应用程序的可移植性。如果应用程序的可移植性在您的环境中非常重要，则将业务逻辑封装在不特定于 RDBMS 的中间层中可能是一个更佳的选择。

3.大量采用存储过程进行业务逻辑的开发致命的缺点是很多存储过程不支持面向对象的设计，无法采用面向对象的方式将业务逻辑进行封装，从而无法形成通用的可支持复用的业务逻辑框架。

4.代码可读性差,相当难维护. 区别一，存储过程保存在数据库里面，存储过程可以被连接此数据库的所有程序设计语言和程序使用，自定义函数不能。

### Laravel中如何使用

创建存储过程（两个参数，第一个参数为 activityid，第二个参数为 ids）

```sql
CREATE PROCEDURE update_records(IN activityid INTEGER ,ids text)
BEGIN
UPDATE wall_records SET activity_id = activityid
WHERE FIND_IN_SET (cid,ids); # 等于 where ids in ('1,2,3')
END;
```

代码调用

```php
\DB::update('call update_records(1,"1,2,3")');
```
