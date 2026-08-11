---
title: "MySQL导出和导入记录"
date: "2025-07-04 14:27:18"
slug: "mysql-dao-chu-he-dao-ru-ji-lu"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/04/MySQL导出和导入记录/"
  - "/2025/07/04/MySQL导出和导入记录.html"
  - "/MySQL导出和导入记录/"
  - "/MySQL导出和导入记录.html"
  - "/2025/07/04/mysql-dao-chu-he-dao-ru-ji-lu/"
  - "/2025/07/04/mysql-dao-chu-he-dao-ru-ji-lu.html"
  - "/mysql-dao-chu-he-dao-ru-ji-lu.html"
---
1、导出

```bash
mysqldump -u root -h 127.0.0.1 -p 库名称 > 文件名称.sql # 之后是要输入密码的别忘记了
```

如

```bash
mysqldump -u root -h 127.0.0.1 -p gowhich > gowhich_dump.sql # 之后是要输入密码的别忘记了
```

2、导入

登录mysql创建数据库

```bash
mysql -u root -h 127.0.0.1 -p # 之后是要输入密码的别忘记了
```

```bash
create databases gowhich # 如果你已经有了自己想要导入的库的话，就不需要这一步了
```

创建完库之后退出  
执行

```bash
mysqldump -u root -h 127.0.0.1 -p 库名称 < 文件名称.sql # 之后是要输入密码的别忘记了
```

如

```bash
mysqldump -u root -h 127.0.0.1 -p gowhich < gowhich_dump.sql # 之后是要输入密码的别忘记了
```

登录mysql进行数据导入操作

```bash
mysql -u root -h 127.0.0.1 -p # 之后是要输入密码的别忘记了
source gowhich_dump.sql # 这一步是非常重要的一步
show database; # 查看数据库
show tables; # 查看数据库表
```

MySQL导入数据库失败的解决方法  
参考链接：http://www.chinastor.com/a/jishu/mysqlbf/0G3GV2014.html
