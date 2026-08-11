---
title: "Python异常处理体系--学习（二）"
date: "2025-06-23 16:27:08"
slug: "python-yi-chang-chu-li-ti-xi-xue-xi-er"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/23/Python异常处理体系-学习（二）/"
  - "/2025/06/23/Python异常处理体系-学习（二）.html"
  - "/Python异常处理体系-学习（二）/"
  - "/Python异常处理体系-学习（二）.html"
  - "/2025/06/23/Python异常处理体系-学习-二/"
  - "/2025/06/23/Python异常处理体系-学习-二.html"
  - "/2025/06/23/python-yi-chang-chu-li-ti-xi-xue-xi-er/"
  - "/2025/06/23/python-yi-chang-chu-li-ti-xi-xue-xi-er.html"
  - "/python-yi-chang-chu-li-ti-xi-xue-xi-er.html"
---
## [Python异常处理体系-结构形式](#1)

Python的异常处理可以向用户准确反馈出错信息，所有异常都是基类Exception的子类。自定义异常都是从基类Exception中继承。Python自动将所有内建的异常放到内建命名空间中，所以程序不必导入exceptions模块即可使用异常。

可以使用的语句结构形式：

### [方式一 使用try,except语句来捕获异常](#1-1)

可以有无数个except语句来处理异常，如果所有except语句都没捕获到,则抛出异常到调用此方法的函数内处理，直到系统的主函数来处理。

使用except子句需要注意的事情，就是多个except子句截获异常时，如果各个异常类之间具有继承关系，则子类应该写在前面，否则父类将会直接截获子类异常。放在后面的子类异常也就不会执行到了。

```python
try:
    #block
except [excpetion,[data...]]:
    #block
except [excpetion,[data...]]:
    #block
except [excpetion,[data...]]:
    #block
```

### [方式二 当没有异常发生的时候执行else语句](#1-2)

```python
try:
    #block
except  [excpetion,[data...]]:
    #block
else:
```

### [方式三 finally 语句,不管有没有发生异常都将执行finally语句块](#1-3)

例如我们在python中打开一个文件进行读写操作，我在操作过程中不管是否出现异常，最终都是要把该文件关闭的。

```python
try:
    #block
finally:
    #block
```

### [方式四 try,except,finally](#1-4)

```python
try:
    #block
except:
    #block
finally:
    #block
```

## [引发异常](#2)

`raise [exception[,data]]`

在Python中，要想引发异常，最简单的形式就是输入关键字raise，后跟要引发的异常的名称。

异常名称标识出具体的类：Python异常是那些类的对象。执行raise语句时，Python会创建指定的异常类的一个对象。

raise语句还可指定对异常对象进行初始化的参数。为此，请在异常类的名称后添加一个逗号以及指定的参数（或者由参数构成的一个元组）。

例：

```python
class MyError(Exception):
    pass
try:
    raise MyError #自己抛出一个异常
    raise ValueError,"invalid argument"
except MyError,data:
    print 'a error'
    
try:
    raise ValueError,"invalid argument"
except ValueError,data:
    print "message = ","invalid argument"
```

捕捉到的内容为：

```bash
a error
message =  invalid argument
```

