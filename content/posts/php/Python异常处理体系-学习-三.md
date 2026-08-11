---
title: "Python异常处理体系--学习（三）"
date: "2025-06-24 11:24:02"
slug: "python-yi-chang-chu-li-ti-xi-xue-xi-san"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/24/Python异常处理体系-学习（三）/"
  - "/2025/06/24/Python异常处理体系-学习（三）.html"
  - "/Python异常处理体系-学习（三）/"
  - "/Python异常处理体系-学习（三）.html"
  - "/2025/06/24/Python异常处理体系-学习-三/"
  - "/2025/06/24/Python异常处理体系-学习-三.html"
  - "/2025/06/24/python-yi-chang-chu-li-ti-xi-xue-xi-san/"
  - "/2025/06/24/python-yi-chang-chu-li-ti-xi-xue-xi-san.html"
  - "/python-yi-chang-chu-li-ti-xi-xue-xi-san.html"
---
## [异常处理的一些其它用途](#1)

除了处理实际的错误条件之外，对于异常还有许多其它的用处。在标准 Python 库中一个普通的用法就是试着导入一个模块，然后检查是否它能使用。

导入一个并不存在的模块将引发一个 ImportError 异常。你可以使用这种方法来定义多级别的功能――依靠在运行时哪个模块是有效的，或支持多种平台 (即平台特定代码被分离到不同的模块中)。

你也能通过创建一个从内置的 Exception 类继承的类定义你自己的异常，然后使用 raise 命令引发你的异常。如果你对此感兴趣，请看进一步阅读的部分。

下面的例子演示了如何使用异常支持特定平台功能。代码来自 getpass 模块，一个从用户获得口令的封装模块。获得口令在 UNIX、Windows 和 Mac OS 平台上的实现是不同的，但是这个代码封装了所有的不同之处。

例：支持特定平台功能

```python
# Bind the name getpass to the appropriate function
try:
    import termios, TERMIOS                    
except ImportError:
    try:
        import msvcrt                          
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass          
        else:                                  
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass
```

termios 是 UNIX 独有的一个模块，它提供了对于输入终端的底层控制。

如果这个模块无效 (因为它不在你的系统上，或你的系统不支持它)，则导入失败，Python 引发我们捕捉的 ImportError 异常。

OK，我们没有 termios，所以让我们试试 msvcrt，它是 Windows 独有的一个模块，可以提供在 Microsoft Visual C++ 运行服务中的许多有用的函数的一个API。如果导入失败，

Python 会引发我们捕捉的 ImportError 异常。

如果前两个不能工作，我们试着从 EasyDialogs 导入一个函数，它是 Mac OS 独有的一个模块，提供了各种各样类型的弹出对话框。再一次，如果导入失败，Python 会引发一个我们捕捉的 ImportError 异常。

这些平台特定的模块没有一个有效 (有可能，因为 Python 已经移植到了许多不同的平台上了)，所以我们需要回头使用一个缺省口令输入函数 (这个函数定义在 getpass 模块中的别的地方)。注意我们在这里所做的：我们将函数 `default_getpass` 赋给变量 getpass。如果你读了官方 getpass 文档，它会告诉你 getpass 模块定义了一个 getpass 函数。它是这样做的：通过绑定 getpass 到正确的函数来适应你的平台。然后当你调用 getpass 函数时，你实际上调用了平台特定的函数，是这段代码已经为你设置好的。你不需要知道或关心你的代码正运行在何种平台上；只要调用 getpass，则它总能正确处理。

一个 `try...except` 块可以有一条 else 子句，就像 if 语句。如果在 try 块中没有异常引发，然后 else 子句被执行。在本例中，那就意味着如果 from EasyDialogs import AskPassword 导入可工作，所以我们应该绑定 getpass 到 AskPassword 函数。其它每个 `try...except` 块有着相似的 else 子句，当我们发现一个 import 可用时，就绑定 getpass 到适合的函数。

自定义异常类，继承Exception类及其子类

```python
class MyError( ArithmeticError ):
    pass
class MyError2 ( Exception ):
    pass
```

