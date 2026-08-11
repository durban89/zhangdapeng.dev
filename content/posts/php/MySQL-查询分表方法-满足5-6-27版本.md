---
title: "MySQL 查询分表方法 【满足5.6.27版本】"
date: "2025-07-03 11:07:50"
slug: "mysql-cha-xun-fen-biao-fang-fa-man-zu-5627-ban-ben"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/07/03/MySQL-查询分表方法-【满足5.6.27版本】/"
  - "/2025/07/03/MySQL-查询分表方法-【满足5.6.27版本】.html"
  - "/MySQL-查询分表方法-【满足5.6.27版本】/"
  - "/MySQL-查询分表方法-【满足5.6.27版本】.html"
  - "/2025/07/03/MySQL-查询分表方法-满足5-6-27版本/"
  - "/2025/07/03/MySQL-查询分表方法-满足5-6-27版本.html"
  - "/2025/07/03/mysql-cha-xun-fen-biao-fang-fa-man-zu-5627-ban-ben/"
  - "/2025/07/03/mysql-cha-xun-fen-biao-fang-fa-man-zu-5627-ban-ben.html"
  - "/mysql-cha-xun-fen-biao-fang-fa-man-zu-5627-ban-ben.html"
---
业务需求，将record表做了分表处理，那么问题就出现了，以前的接口就有问题了。

```sql
SELECT * FROM record WHRER xxxx;
```

这样的SQL语句就不能正常执行了，只好不会再有新的数据进来了，结果不是需要的数据。

于是找了一个我认为算是比较笨拙，但是还能用的方法，就是使用union的方式查询。

```sql
SELECT * FROM (
    SELECT * FROM record_0 WHERE xxxx union
    SELECT * FROM record_1 WHERE xxxx union
    SELECT * FROM record_2 WHERE xxxx union
    SELECT * FROM record_3 WHERE xxxx union
    SELECT * FROM record_4 WHERE xxxx
) t WHERE xxx
GROUP BY xx
ORDER BY xx
```

你是否有更好的方法，可以跟我联系。


