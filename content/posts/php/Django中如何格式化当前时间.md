---
title: "Django中如何格式化当前时间"
date: "2025-06-20 11:51:08"
slug: "django-zhong-ru-he-ge-shi-hua-dang-qian-shi-jian"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django中如何格式化当前时间/"
  - "/2025/06/20/Django中如何格式化当前时间.html"
  - "/Django中如何格式化当前时间/"
  - "/Django中如何格式化当前时间.html"
  - "/2025/06/20/django-zhong-ru-he-ge-shi-hua-dang-qian-shi-jian/"
  - "/2025/06/20/django-zhong-ru-he-ge-shi-hua-dang-qian-shi-jian.html"
  - "/django-zhong-ru-he-ge-shi-hua-dang-qian-shi-jian.html"
---
关于django的时间格式的问题，最近在做项目中，进坑啦，python基础没怎么学，就只有这样啦，继续努力

简单的时间格式是这样的：

```python
datetime.datetime.now()
#2012-03-15 11:50:57.728000
```

这个会返回 microsecond。因此这个是我们不需要的。所以得做一下修改

```python
datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S");
```

格式化之后，就得到了我们常见的格式了。  
附：strftime参数

```python
strftime(format[, tuple]) -> string
```

将指定的struct\_time(默认为当前时间)，根据指定的格式化字符串输出  
python中时间日期格式化符号：

```ini
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
```
