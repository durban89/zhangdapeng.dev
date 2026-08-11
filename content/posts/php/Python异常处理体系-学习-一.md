---
title: "Python异常处理体系--学习（一）"
date: "2025-06-23 16:27:04"
slug: "python-yi-chang-chu-li-ti-xi-xue-xi-yi"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/23/Python异常处理体系-学习（一）/"
  - "/2025/06/23/Python异常处理体系-学习（一）.html"
  - "/Python异常处理体系-学习（一）/"
  - "/Python异常处理体系-学习（一）.html"
  - "/2025/06/23/Python异常处理体系-学习-一/"
  - "/2025/06/23/Python异常处理体系-学习-一.html"
  - "/2025/06/23/python-yi-chang-chu-li-ti-xi-xue-xi-yi/"
  - "/2025/06/23/python-yi-chang-chu-li-ti-xi-xue-xi-yi.html"
  - "/python-yi-chang-chu-li-ti-xi-xue-xi-yi.html"
---
## [Python内建异常体系结构](#1)

> BaseException
>
> +-- SystemExit
>
> +-- KeyboardInterrupt
>
> +-- GeneratorExit
>
> +-- Exception
>
> +-- StopIteration
>
> +-- StandardError
>
> |    +-- BufferError
>
> |    +-- ArithmeticError
>
> |    |    +-- FloatingPointError
>
> |    |    +-- OverflowError
>
> |    |    +-- ZeroDivisionError
>
> |    +-- AssertionError
>
> |    +-- AttributeError
>
> |    +-- EnvironmentError
>
> |    |    +-- IOError
>
> |    |    +-- OSError
>
> |    |         +-- WindowsError (Windows)
>
> |    |         +-- VMSError (VMS)
>
> |    +-- EOFError
>
> |    +-- ImportError
>
> |    +-- LookupError
>
> |    |    +-- IndexError
>
> |    |    +-- KeyError
>
> |    +-- MemoryError
>
> |    +-- NameError
>
> |    |    +-- UnboundLocalError
>
> |    +-- ReferenceError
>
> |    +-- RuntimeError
>
> |    |    +-- NotImplementedError
>
> |    +-- SyntaxError
>
> |    |    +-- IndentationError
>
> |    |         +-- TabError
>
> |    +-- SystemError
>
> |    +-- TypeError
>
> |    +-- ValueError
>
> |         +-- UnicodeError
>
> |              +-- UnicodeDecodeError
>
> |              +-- UnicodeEncodeError
>
> |              +-- UnicodeTranslateError
>
> +-- Warning
>
> +-- DeprecationWarning
>
> +-- PendingDeprecationWarning
>
> +-- RuntimeWarning
>
> +-- SyntaxWarning
>
> +-- UserWarning
>
> +-- FutureWarning
>
> +-- ImportWarning
>
> +-- UnicodeWarning
>
> +-- BytesWarning

捕获异常的方式

### [方法一 捕获所有的异常](#1-1)

```python
''' 捕获异常的第一种方式，捕获所有的异常 '''


try:
    a = b
    b = c
except Exception,data:
    print Exception,":",data
```

输出：

```bash
＜type 'exceptions.Exception'＞ : local variable 'b' referenced before assignment
```

### [方法二 采用traceback模块查看异常，需要导入traceback模块](#1-2)

```python
''' 捕获异常的第二种方式，使用traceback查看异常 '''

try:
	a = b
	b = c
except:
	print traceback.print_exc()
```

输出：

```bash
Traceback (most recent call last):
File "test.py", line 20, in main
a = b
UnboundLocalError: local variable 'b' referenced before assignment
```

### [方法三 采用sys模块回溯最后的异常](#1-3)

```python
''' 捕获异常的第三种方式，使用sys模块捕获异常 '''

try:
	a = b
	b = c
except:
	info = sys.exc_info()
	print info
	print info[0]
	print info[1]
```

输出：

```bash
(＜type 'exceptions.UnboundLocalError'＞, UnboundLocalError("local 
variable 'b' referenced before assignment",),
＜traceback object at 0x00D243F0＞)
＜type 'exceptions.UnboundLocalError'＞
local variable 'b' referenced before assignment
```

