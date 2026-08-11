---
title: "MySQL 去除字段中的换行和回车符"
date: "2025-06-24 16:17:45"
slug: "mysql-qu-chu-zi-duan-zhong-de-huan-hang-he-hui-che-fu"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/24/MySQL-去除字段中的换行和回车符/"
  - "/2025/06/24/MySQL-去除字段中的换行和回车符.html"
  - "/MySQL-去除字段中的换行和回车符/"
  - "/MySQL-去除字段中的换行和回车符.html"
  - "/2025/06/24/mysql-qu-chu-zi-duan-zhong-de-huan-hang-he-hui-che-fu/"
  - "/2025/06/24/mysql-qu-chu-zi-duan-zhong-de-huan-hang-he-hui-che-fu.html"
  - "/mysql-qu-chu-zi-duan-zhong-de-huan-hang-he-hui-che-fu.html"
---
### [解决方法：](#0)

```sql
UPDATE tablename SET field = REPLACE(REPLACE(field, CHAR(10), ”), CHAR(13), ”);
```

char(10):  换行符  
char(13):  回车符

### [问题产生原因：](#1)

2种方法生成excel模式的报表：

1）手动生成

将表中的数据导出，生成CSV文件。

用mysqldump 导出数据

```sql
#mysqldump -u xxx -p --tab=/tmp/ --fields-terminated-by="#" DBName TBName
```

将会在tmp目录下生成TBName.txt 文件。

在EXCEL中导入生成的txt文件

2）直接生成csv格式文件

```bash
mysqldump -u samu -p -T --fields-terminated-by=","  --fields-enclosed-by=""
--lines-terminated-by="\n"  --fields-escaped-by=""  test Customer
```

或者：

```bash
mysqldump -u samu -p --tab=/tmp/ --fields-terminated-by=","  --fields-enclosed-by=""
--lines-terminated-by="\n"  --fields-escaped-by=""  test Customer
```

**但是，无论上面哪一种方法，如果表的某个列里包含回车符或者换行符，  
那么生成的CSV文件或者进行excel导入，都会将原本的1行数据，拆分成2行。  
因为CSV或者excel导入，是按数据的行来认定数据条数。  
所以，必须在此之前，将字段中的回车符或者换行符，进行替换。**

