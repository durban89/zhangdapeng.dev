---
title: "Python 中 Unicode 简单使用"
date: "2025-06-20 11:51:02"
slug: "python-zhong-unicode-jian-dan-shi-yong"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/20/Python-中-Unicode-简单使用/"
  - "/2025/06/20/Python-中-Unicode-简单使用.html"
  - "/Python-中-Unicode-简单使用/"
  - "/Python-中-Unicode-简单使用.html"
  - "/2025/06/20/python-zhong-unicode-jian-dan-shi-yong/"
  - "/2025/06/20/python-zhong-unicode-jian-dan-shi-yong.html"
  - "/python-zhong-unicode-jian-dan-shi-yong.html"
---
一个很关键的并且要常记住的，就是代码中所有字符串都统一使用unicode，而不是str。这样，自己就能很清楚要处理的字符串类型了。请记住，是所有，任何地方。  
例如：

```python
>>> s1 = u'%s欢迎您!' % u'北京'
>>> s1
u'\u5317\u4eac\u6b22\u8fce\u60a8\uff01'
>>> print s1
北京欢迎你!
```

若像这样，就会抛异常：

```python
>>> s2 = '%s欢迎您!' % u'北京'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 2: ordinal not in range(128)
```

由UnicodeDecodeError可猜想得到，解析器尝试使用ascii对'%s欢迎您!'进行解码，由于'%s欢迎您!'实际是使用utf-8编码的（这是我系统终端默认的），所以使用ascii解码肯定会错，只要如下，就可以重现这个异常了：

```python
>>> s2 = '%s欢迎您!'.decode('ascii')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 2: ordinal not in range(128)
```

分清`encode`和`decode`。`str --> decode(c) --> unicode`, `unicode --> encode(c) --> str`，其中编码类型c必须相同。  
  
将unicode字符串写入文件前先使用特定编码对其进行编码(如`unicodestr.encode('utf-8')`)得到str，保证写入文件的是str；从文件读取到str，然后对其进行解码(如`encodestr.decode('utf-8')`)得到unicode。这是互逆的两个操作，编码类型一定要一致，否则会出现异常。  
  
自己支持了unicode，但是你团队的其他人是否都使用unicode呢？你使用的其他模块是否也使用unicode呢？这个一定要清楚的，不然同样会出现许多因为编码问题的异常。

