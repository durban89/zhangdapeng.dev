---
title: "MySQL批量修改表前缀"
date: "2025-06-27 10:26:08"
slug: "mysql-pi-liang-xiu-gai-biao-qian-zhui"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/27/MySQL批量修改表前缀/"
  - "/2025/06/27/MySQL批量修改表前缀.html"
  - "/MySQL批量修改表前缀/"
  - "/MySQL批量修改表前缀.html"
  - "/2025/06/27/mysql-pi-liang-xiu-gai-biao-qian-zhui/"
  - "/2025/06/27/mysql-pi-liang-xiu-gai-biao-qian-zhui.html"
  - "/mysql-pi-liang-xiu-gai-biao-qian-zhui.html"
---
批量修改表名的操作方法:

```sql
SELECT CONCAT( 'ALTER TABLE ', TABLE_NAME, 'RENAME TO ', TABLE_NAME,';' )
FROM information_schema.TABLES
WHERE TABLE_NAME LIKE 'uc_%';
```

执行后得到如下的结果：

```sql
('ALTER TABLE uc_aaa RENAME TO uc_aaa;'),
('ALTER TABLE uc_bbb RENAME TO uc_bbb;')
```

导出结果到SQL文件中，然后去掉括号和引号，只保留如下的数据：

```sql
ALTER TABLE uc_aaa RENAME TO uc_aaa;
ALTER TABLE uc_bbb RENAME TO uc_bbb;
```

然后选择要修改的数据库，执行上面得到的SQL语句就可以了。  
附：  
1、批量删除指定前缀的表

```sql
SELECT CONCAT( 'drop table ', TABLE_NAME, ';' )
FROM information_schema.TABLES
WHERE TABLE_NAME LIKE 'uc_%';
```

2、“dbtable_name”改成“db_table_name”

```sql
SELECT CONCAT( 'ALTER TABLE ', TABLE_NAME, 'RENAME TO db_', SUBSTRING(TABLE_NAME,3),';' )
FROM information_schema.TABLES
WHERE TABLE_NAME LIKE 'db%';
```

---

参考文章：

http://www.islandcn.com/post/855.html

