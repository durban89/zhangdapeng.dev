---
title: "MySQL 删除数据 Delete 语句 、Truncate 语句"
date: "2025-06-23 15:27:44"
slug: "mysql-shan-chu-shu-ju-delete-yu-ju-truncate-yu-ju"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/23/MySQL-删除数据-Delete-语句-、Truncate-语句/"
  - "/2025/06/23/MySQL-删除数据-Delete-语句-、Truncate-语句.html"
  - "/MySQL-删除数据-Delete-语句-、Truncate-语句/"
  - "/MySQL-删除数据-Delete-语句-、Truncate-语句.html"
  - "/2025/06/23/MySQL-删除数据-Delete-语句-Truncate-语句/"
  - "/2025/06/23/MySQL-删除数据-Delete-语句-Truncate-语句.html"
  - "/2025/06/23/mysql-shan-chu-shu-ju-delete-yu-ju-truncate-yu-ju/"
  - "/2025/06/23/mysql-shan-chu-shu-ju-delete-yu-ju-truncate-yu-ju.html"
  - "/mysql-shan-chu-shu-ju-delete-yu-ju-truncate-yu-ju.html"
---
如果数据库里面的数据有问题了，或者是有人捣乱，再或者就是您老人家看这条数据不爽，还有就是您想毁灭证据（其实总是会留下痕迹的）的时候，你就需要了解MySQL的Delete语句了。MySQL为我们提供了delete和truncate语句来删除数据。

delete 语句的定义：

经常和数据库打交道的孩子们，删除数据的时候用的大多都是 delete 语句。现在让我们来看一下 delete语句的定义。

```sql
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name
[WHERE where_definition]
[ORDER BY ...]
[LIMIT row_count]
```

delete 语句的示例：

MySQL的这些语法都和口语类似，你要指出你想从哪个表删除数据，还有删除哪些数据，这就够了。就像写记叙文的时候，时间、地点、人物、环境、情节几要素必不可少一样。

示例是最形象，最能说明问题的。按照上面的语法结构，我想删除 firends 表中所有 user\_name 等于 simaopig 的记录，就可以使用如下SQL语句：

```sql
delete from friends where user_name = 'simaopig';
```

delete 注意事项：

从语法结构中，我们就可以看出，和 update 语法一样，我们是可以省略 where 子句的。不过这是一个很危险的行为。因为如果不指定 where 子句，delete 将删除表中所有的记录，而且是立即删除，即使你想哭都没有地方，也没有时间，因为你需要马上和主管承认错误，并且立即找出MySQL日志，来回滚记录。不过一旦你有过一次这样的经历，我相信这一定是印象深刻的。

truncate 语句的简单说明：

这个语句之前我也没有接触过，也没有使用过。因为一般情况下，删除数据大家都在使用delete语句。其实这个 truncate 命令很简单，它的意思是：删除表的所有记录。相当于 delete 语句不写 where 子句一样。其语法结构为：

```sql
TRUNCATE [TABLE] tbl_name
```

这里简单的给出个示例，我想删除 friends 表中所有的记录，可以使用如下语句：

```sql
truncate table friends;
```

truncate 和 delete的效率问题：

如果想要删除表的所有数据，truncate语句要比 delete 语句快。因为 truncate 删除了表，然后根据表结构重新建立它，而 delete 删除的是记录，并没有尝试去修改表。这也是为什么当向一个使用 delete 清空的表插入数据时，MySQL 会记住前面产生的AUTOINCREMENT序列，并且继续利用它对AUTOINCREMENT字段编号。而truncate删除表后，表是从1开始为autoincrement字段编号。

不过truncate命令快规快，却不像delete命令那样对事务处理是安全的。因此，如果我们想要执行truncate删除的表正在进行事务处理，这个命令就会产生退出并产生错误信息。

