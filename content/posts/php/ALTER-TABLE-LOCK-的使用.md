---
title: "ALTER TABLE ... LOCK ... 的使用"
date: "2025-07-02 15:40:35"
slug: "alter-table-lock-de-shi-yong"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/02/ALTER-TABLE-...-LOCK-...-的使用/"
  - "/2025/07/02/ALTER-TABLE-...-LOCK-...-的使用.html"
  - "/ALTER-TABLE-...-LOCK-...-的使用/"
  - "/ALTER-TABLE-...-LOCK-...-的使用.html"
  - "/2025/07/02/ALTER-TABLE-LOCK-的使用/"
  - "/2025/07/02/ALTER-TABLE-LOCK-的使用.html"
  - "/2025/07/02/alter-table-lock-de-shi-yong/"
  - "/2025/07/02/alter-table-lock-de-shi-yong.html"
  - "/alter-table-lock-de-shi-yong.html"
---
来个示例，网上找了很久了，没发现同时添加多个字段的例子，我英文比较差，只能靠猜了，结果还真成了。

```sql
ALTER TABLE `record` 
	ADD COLUMN `rate_name` varchar(16) NOT NULL COMMENT '货币k值' AFTER `money`,
	ADD COLUMN `rate_money` decimal(16,4)  NOT NULL COMMENT '货币汇率' AFTER `rate_name`,LOCK=SHARED;
```

```sql
ALTER TABLE `record_list` 
	ADD COLUMN `rate_name` varchar(16) NOT NULL COMMENT '货币K值' AFTER `mtime`,
	ADD COLUMN `rate_list` varchar(32) NOT NULL COMMENT '货币ID组合' AFTER `rate_name`,
	ADD COLUMN `list_rate_budget` decimal(16,4)  NOT NULL COMMENT '预算汇率金额' AFTER `rate_list`,
	ADD COLUMN `date_start` bigint(20) NOT NULL COMMENT '起始日' AFTER `list_rate_budget`,LOCK=SHARED;
```

如下摘自原文档：https://dev.mysql.com/doc/refman/5.7/en/alter-table.html

> LOCK = DEFAULT
>
> Maximum level of concurrency for the given ALGORITHM clause (if any) and ALTER TABLE operation: Permit concurrent reads and writes if supported. If not, permit concurrent reads if supported. If not, enforce exclusive access.

> LOCK = NONE
>
> 如果MYSQL支持, 则同时发生度读操作和写操作. Otherwise, return an error message.

> LOCK = SHARED
>
> 如果MYSQL支持, 则允许并发读取但是阻塞写入。 Note that writes will be blocked even if concurrent writes are supported by the storage engine for the given ALGORITHM clause (if any) and ALTER TABLE operation. If concurrent reads are not supported, return an error message.

> LOCK = EXCLUSIVE
>
> 实施独占访问. This will be done even if concurrent reads/writes are supported by the storage engine for the given ALGORITHM clause (if any) and ALTER TABLE operation

估计会翻译有误，不过大概意思是这样的


