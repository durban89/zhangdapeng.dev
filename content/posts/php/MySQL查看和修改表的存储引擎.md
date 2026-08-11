---
title: "MySQL查看和修改表的存储引擎"
date: "2025-06-30 11:49:07"
slug: "mysql-cha-kan-he-xiu-gai-biao-de-cun-chu-yin-qing"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/30/MySQL查看和修改表的存储引擎/"
  - "/2025/06/30/MySQL查看和修改表的存储引擎.html"
  - "/MySQL查看和修改表的存储引擎/"
  - "/MySQL查看和修改表的存储引擎.html"
  - "/2025/06/30/mysql-cha-kan-he-xiu-gai-biao-de-cun-chu-yin-qing/"
  - "/2025/06/30/mysql-cha-kan-he-xiu-gai-biao-de-cun-chu-yin-qing.html"
  - "/mysql-cha-kan-he-xiu-gai-biao-de-cun-chu-yin-qing.html"
---
MySQL查看和修改表的存储引擎

//=================

给表添加注释

```sql
ALTER TABLE sk_subscribe COMMENT='预约记录表';
```

给表的字段【列】添加注释

```sql
ALTER table sk_products MODIFY `has_cash` BIGINT DEFAULT 0 COMMENT '已经募集的金额'
```

修改表的引擎

```sql
show engines;//查看支持的引擎
show table status from wycf where name='sk_productscate';//查看表引擎
alter table sk_productscate engine=Myisam;//修改表引擎
```

//修改数据库默认引擎

关闭mysql服务： `net stop mysql`

找到mysql安装目录下的`my.ini`文件：

找到`default-storage-engine=INNODB` 改为`default-storage-engine=MYISAM`

找到`#skip-innodb` 改为`skip-innodb`

启动mysql服务：`net start mysql`


