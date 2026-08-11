---
title: "Python 异常 ”ValueError width too big“ ”TypeError: cannot concatenate 'str' and 'exceptions.ValueError' objects“"
date: "2025-06-24 16:17:38"
slug: "python-yi-chang-valueerror-width-too-big-typeerror-cannot-concatenate-str-and-exceptionsvalueerror-objects"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/24/Python-异常-”ValueError-width-too-big“-”TypeError:-cannot-concatenate-'str'-and-'exceptio/"
  - "/2025/06/24/Python-异常-”ValueError-width-too-big“-”TypeError:-cannot-concatenate-'str'-and-'exce.html"
  - "/Python-异常-”ValueError-width-too-big“-”TypeError:-cannot-concatenate-'str'-and-'exceptions.ValueErr/"
  - "/Python-异常-”ValueError-width-too-big“-”TypeError:-cannot-concatenate-'str'-and-'exceptions.Valu.html"
  - "/2025/06/24/Python-异常-ValueError-width-too-big-TypeError-cannot-concatenate-str-and-exceptions-Valu/"
  - "/2025/06/24/Python-异常-ValueError-width-too-big-TypeError-cannot-concatenate-str-and-exceptions-.html"
  - "/2025/06/24/python-yi-chang-valueerror-width-too-big-typeerror-cannot-concatenate-str-and-exception/"
  - "/2025/06/24/python-yi-chang-valueerror-width-too-big-typeerror-cannot-concatenate-str-and-excep.html"
  - "/python-yi-chang-valueerror-width-too-big-typeerror-cannot-concatenate-str-and-exceptionsvaluee.html"
---
### [Python 异常](#1)

> “ ValueError width too big”
>
> “TypeError: cannot concatenate 'str' and 'exceptions.ValueError' objects ”

之所以出现以上的原因，请看下面的过程

我在执行这段代码的时候

```python
#纠正sp的数据
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = '350000000029' where sp LIKE '%350000000029%'
'''
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正sp的数据错误 : " + data

#纠正szmg的数据错误
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = 'szmg' where sp LIKE '%szmg%'
'''
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正szmg的数据错误 : " + data
```

先出现了这个错误

***ValueError width too big***

之后将代码调整为：

```python
#纠正sp的数据
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = '%(sp)s' where sp LIKE '%%350000000029%%'
''' % {'sp':'350000000029'}
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正sp的数据错误 : " + data

#纠正szmg的数据错误
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = 'szmg' where sp LIKE '%%szmg%%'
'''
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正szmg的数据错误 : " + data
```

出现了这个错误

***TypeError: cannot concatenate 'str' and 'exceptions.ValueError' objects***

**这里注意代码的变化**

最后将代码调整为：

```python
#纠正sp的数据
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = '350000000029' where sp LIKE '%%350000000029%%'
'''
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正sp的数据错误 : " + data

#纠正szmg的数据错误
sql = '''
UPDATE `itv_online_offline_origin_tmp` set sp = 'szmg' where sp LIKE '%%szmg%%'
'''
try:
    db_itv.get_conn().execute(sql)
except Exception,data:
    print "纠正szmg的数据错误 : " + data
```

一切恢复正常

### [原因分析：](#2)

导致问题的原因其实就是因为在

```sql
UPDATE `itv_online_offline_origin_tmp` set sp = '350000000029' where sp LIKE '%%350000000029%%'
```

**这条sql语句里面，python下执行的时候，要注意%（百分号）的处理，要使用两个%%（两个百分号）**

