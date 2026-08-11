---
title: "Django 直接执行sql语句的使用方法 Performing raw SQL queries"
date: "2025-06-20 09:52:25"
slug: "django-zhi-jie-zhi-xing-sql-yu-ju-de-shi-yong-fang-fa-performing-raw-sql-queries"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django-直接执行sql语句的使用方法-Performing-raw-SQL-queries/"
  - "/2025/06/20/Django-直接执行sql语句的使用方法-Performing-raw-SQL-queries.html"
  - "/Django-直接执行sql语句的使用方法-Performing-raw-SQL-queries/"
  - "/Django-直接执行sql语句的使用方法-Performing-raw-SQL-queries.html"
  - "/2025/06/20/django-zhi-jie-zhi-xing-sql-yu-ju-de-shi-yong-fang-fa-performing-raw-sql-queries/"
  - "/2025/06/20/django-zhi-jie-zhi-xing-sql-yu-ju-de-shi-yong-fang-fa-performing-raw-sql-queries.html"
  - "/django-zhi-jie-zhi-xing-sql-yu-ju-de-shi-yong-fang-fa-performing-raw-sql-queries.html"
---
开始展示的前提是，看一下表的结构

```python
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
```

1，Performing raw SQL queries

你可以直接执行一个语句像这样

```python
for p in Person.objects.raw('SELECT * FROM myapp_person'):
    print(p)
```

官方提示不要使用下面这种方式

```python
lname = 'Doe'
query = 'SELECT * FROM myapp_person WHERE last_name = %s' % lname
Person.objects.raw(query)
```

2，Executing custom SQL directly

Sometimes even Manager.raw() isn’t quite enough: you might need to perform queries that don’t map cleanly to models, or directly execute UPDATE, INSERT, or DELETE queries.

是的，有时候Raw Sql Queries是满足不了我们的需求的，那么我们就直接执行一下好了。

```python
cursor = connection.cursor()
cursor.execute("UPDATE myapp_person SET first_name = 1 WHERE first_name = %s", [self.bar])
cursor.execute("SELECT `last_name` FROM myapp_person WHERE last_name = %s", [self.baz])
row = cursor.fetchone()
print_r(row)
```

还不错，需求挺大，满足也挺大，操作也简便，对项目的操作很便利
