---
title: "MySQL: Pagination - SQL_CALC_FOUND_ROWS vs COUNT()-Query"
date: "2025-06-24 15:04:25"
slug: "mysql-pagination-sql-calc-found-rows-vs-count-query"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/24/MySQL:-Pagination-SQL-CALC-FOUND-ROWS-vs-COUNT()-Query/"
  - "/2025/06/24/MySQL:-Pagination-SQL-CALC-FOUND-ROWS-vs-COUNT()-Query.html"
  - "/MySQL:-Pagination-SQL-CALC-FOUND-ROWS-vs-COUNT()-Query/"
  - "/MySQL:-Pagination-SQL-CALC-FOUND-ROWS-vs-COUNT()-Query.html"
  - "/2025/06/24/MySQL-Pagination/"
  - "/2025/06/24/MySQL-Pagination.html"
  - "/2025/06/24/mysql-pagination-sql-calc-found-rows-vs-count-query/"
  - "/2025/06/24/mysql-pagination-sql-calc-found-rows-vs-count-query.html"
  - "/mysql-pagination-sql-calc-found-rows-vs-count-query.html"
---
关于Mysql的`SQL_CALC_FOUND_ROWS`的使用，网上有好多种说法，为了求证事实，google一搜索的话，就有好多，但是还是经过实际的测试才知道是不是好用或者不好用

> When using pagination for let's say a list of offers that where never clicked, you have to know the exact amount of offers (which were never clicked) in order to know how many pages you have. Now there are 2 possible ways of calculating the exact amount of offers: You can use either SQL_CALC_FOUND_ROWS or you can setup a second query with a COUNT() in it. I did the tests with SQL_NO_CACHE in order to get the best results possible. The clicks table has about 18.000.000 rows, the offer table about 800.000. Let's start with some time results.

### [Using SQL_CALC_FOUND_ROWS（使用SQL_CALC_FOUND_ROWS进行的测试）](#1)

```bash
mysql> SELECT SQL_NO_CACHE SQL_CALC_FOUND_ROWS o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 50,50;  
50 rows in set (30.84 sec)  
  
mysql> SELECT FOUND_ROWS();  
1 row in set (0.00 sec)
```

Using a second query with COUNT()（使用COUNT进行的测试）:

```bash
mysql> SELECT SQL_NO_CACHE o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 50,50;  
50 rows in set (0.03 sec)
  

mysql> SELECT SQL_NO_CACHE COUNT(o.offer_id)  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL;  
1 row in set (30.97 sec)
```

对于上面的是普通的情况下，看看下面这种情况：

> At a first glance they look equally fast, both taking about 30 seconds. But: They are only equally fast, when query caching is turned off. Let's assume we're on a high-traffic website where performance matters, so we turn the query cache on. MySQL Query caching is like a key-value cache with the key being the EXACT query and the resultset being the value. Once we turn on the cache, the pagination is way faster with the second query using COUNT().

为什么?

> When using SQL_CALC_FOUND_ROWS the application has to calculate the found rows every single time we turn the page, because the query changes, while the COUNT()-Query always remains the same, meaning that its result comes from the query cache from the second time on. Let's emulate:

### [Using SQL_CALC_FOUND_ROWS（使用SQL_CALC_FOUND_ROWS进行的测试）](#2)

```sql
mysql> SELECT SQL_CALC_FOUND_ROWS o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 50,50;  
50 rows in set (31.13 sec)  
  
mysql> SELECT FOUND_ROWS();  
1 row in set (0.00 sec)  
  
mysql> SELECT SQL_CALC_FOUND_ROWS o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 100,50;  
50 rows in set (30.71 sec)  
  
mysql> SELECT FOUND_ROWS();  
1 row in set (0.00 sec)
```

### [Using a second query with COUNT()（使用COUNT进行的测试）](#3)

```sql
mysql> SELECT o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 50,50;  
50 rows in set (0.03 sec)  
  
mysql> SELECT COUNT(o.offer_id)  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL;  
1 row in set (31.11 sec)  
  
mysql> SELECT o.offer_id  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL  
    -> LIMIT 100,50;  
50 rows in set (0.04 sec)  
  
mysql> SELECT COUNT(o.offer_id)  
    -> FROM offer AS o  
    -> LEFT JOIN clicks AS c  
    -> ON (o.offer_id = c.offer_id)  
    -> WHERE c.offer_id IS NULL;  
1 row in set (0.00 sec)
```

> While the SQL_CALC_FOUND_ROWS Queries took more than one minute together, the queries with the second COUNT() query only took a bit more than 30 seconds together, meaning they are twice as fast.
>
> I'm pretty sure there are situations where SQL_CALC_FOUND_ROWS is the way to go, but in cases like this one you definately wanna go for the COUNT()-Query.

看出来了吧，其实网上大家的说法都是差不多的，也没有说不对或者对，因为如果加上一个前提的话，就很明显了，也说明，只有在一定的情况下才可以使用，不然不但不起作用，还会起到相反的作用

