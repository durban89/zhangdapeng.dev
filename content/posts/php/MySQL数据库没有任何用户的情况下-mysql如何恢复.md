---
title: "MySQL数据库没有任何用户的情况下，mysql如何恢复"
date: "2025-06-30 12:00:40"
slug: "mysql-shu-ju-ku-mei-you-ren-he-yong-hu-de-qing-kuang-xia-mysql-ru-he-hui-fu"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/30/MySQL数据库没有任何用户的情况下，mysql如何恢复/"
  - "/2025/06/30/MySQL数据库没有任何用户的情况下，mysql如何恢复.html"
  - "/MySQL数据库没有任何用户的情况下，mysql如何恢复/"
  - "/MySQL数据库没有任何用户的情况下，mysql如何恢复.html"
  - "/2025/06/30/MySQL数据库没有任何用户的情况下-mysql如何恢复/"
  - "/2025/06/30/MySQL数据库没有任何用户的情况下-mysql如何恢复.html"
  - "/2025/06/30/mysql-shu-ju-ku-mei-you-ren-he-yong-hu-de-qing-kuang-xia-mysql-ru-he-hui-fu/"
  - "/2025/06/30/mysql-shu-ju-ku-mei-you-ren-he-yong-hu-de-qing-kuang-xia-mysql-ru-he-hui-fu.html"
  - "/mysql-shu-ju-ku-mei-you-ren-he-yong-hu-de-qing-kuang-xia-mysql-ru-he-hui-fu.html"
---
```bash
service mysql stop
```

修改配置文件，添加一行代码

```bash
skip-grant-tables
```

然后重启mysql

```bash
service mysql start
```

接下来执行

mysql -p后面直接回车，就会进入mysql的命令行，然后依次执行如下命令

```bash
insert into mysql.user set user='root',ssl_cipher='',x509_issuer='',x509_subject='';
```

```bash
update mysql.user set Host='localhost',select_priv='y', insert_priv='y',update_priv='y', Alter_priv='y',delete_priv='y',create_priv='y',drop_priv='y',reload_priv='y',shutdown_priv='y',Process_priv='y',file_priv='y',grant_priv='y',References_priv='y',index_priv='y',create_user_priv='y',show_db_priv='y',super_priv='y',create_tmp_table_priv='y',Lock_tables_priv='y',execute_priv='y',repl_slave_priv='y',repl_client_priv='y',create_view_priv='y',show_view_priv='y',create_routine_priv='y',alter_routine_priv='y',create_user_priv='y' where user='root';
```

```bash
update mysql.user set password=password('123456') where user='root';
```

```bash
flush privileges;
```


