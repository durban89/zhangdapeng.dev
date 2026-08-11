---
title: "Go基础学习记录之使用GDB进行调试(一)"
date: "2025-08-04 11:39:12"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试(一)/"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试(一).html"
  - "/Go基础学习记录之使用GDB进行调试(一)/"
  - "/Go基础学习记录之使用GDB进行调试(一).html"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试-一/"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试-一.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-yi/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-yi.html"
---
在任何应用程序的开发过程中，开发人员总是需要执行某种代码调试。 只要不明确地需要编译修改，PHP，Python和大多数其他动态语言都可以在运行时进行修改。 我们可以在动态操作环境中轻松打印数据，输出更改并直接打印变量信息。 在Go中，您当然可以使用Printlns对代码进行散布以显示用于调试目的的变量信息，但是每次都需要重新编译代码的任何更改。 这很快就会变得很麻烦。 如果您使用Python或Javascript编程，您将知道前者提供了诸如pdb和ipdb之类的工具用于调试，而后者具有类似的工具，能够动态显示变量信息并促进单步调试。 幸运的是，Go本身支持提供此类调试功能的类似工具：GDB。 本篇文章讲介绍使用GDB调试Go应用程序。

### GDB调试配置文件

GDB是一个功能强大的调试工具，面向类似UNIX的系统，由FSF（自由软件基金会）发布。 GDB允许我们执行以下操作：

1. 可以根据应用程序的特定要求自定义初始设置。
2. 可以进行设置，以便在开发人员控制台中调试的程序在指定的断点处停止（断点可以是条件表达式）。
3. 程序停止后，您可以检查其当前状态以查看发生的情况。
4. 动态更改当前程序的执行环境。

要使用GDB调试Go应用程序，您使用的GDB版本必须大于7.1。

1. 使用`-ldflags "-s"`将阻止打印标准调试信息
2. 使用`-gcflags "-N-l"`将阻止Go执行一些自动优化 - 聚合变量，函数等的优化。这些优化可能使GDB很难完成其工作，因此最好在编译时禁用它们使用这些标志。

一些GDB最常用的命令如下：

* list

也用于其缩写形式l，list用于显示源代码。 默认情况下，它显示十行代码，您可以指定要显示的行。 例如，命令列表15显示以线15为中心的十行代码，如下所示。

```go
10            time.Sleep(2 * time.Second)
11            c <- i
12        }
13        close(c)
14    }
15    
16    func main() {
17        msg := "Starting main"
18        fmt.Println(msg)
19        bus := make(chan int)
```

* break

在缩写形式b中也使用break，break用于设置断点，并用作定义断点设置点的参数。 例如，b 10在第十行设置断点。

* delete

在缩写形式d中也使用delete，删除用于删除断点。 设置断点后跟序列号。 序列号可以通过info breakpoints命令获得。 设置断点的相应序列号显示如下，以设置断点编号。

```bash
Num     Type           Disp Enb Address            What
2       breakpoint     keep y   0x0000000000400dc3 in main.main at /home/xxx/gdb.go:23
breakpoint already hit 1 time
```

* backtrace

缩写为bt，此命令用于打印代码的执行，例如：

```bash
#0  main.main () at /home/xxx/gdb.go:23
#1  0x000000000040d61e in runtime.main () at /home/xxx/go/src/pkg/runtime/proc.c:244
#2  0x000000000040d6c1 in schedunlock () at /home/xxx/go/src/pkg/runtime/proc.c:267
#3  0x0000000000000000 in ?? ()
```

* info

info命令可以与几个参数结合使用来显示信息。 通常使用以下参数：

* info locals

显示当前正在执行的程序的变量值

* info breakpoints

显示当前设置的断点列表

* info goroutines

显示正在运行的goroutine的当前列表，如以下代码所示，`*`表示当前执行

```javascript
* 1 running runtime.gosched
* 2 syscall runtime.entersyscall
3 waiting runtime.gosched
4 runnable runtime.gosched
```

* print

缩写为p，此命令用于打印变量或其他信息。 它将要打印的变量名称作为参数，当然，还有一些非常有用的函数，如$ len（）和$ cap（），可用于返回当前字符串，切片或映射的长度或容量。

* whatis

`whatis`用于显示当前变量类型，后跟变量名称。 例如，`whatis msg`，将输出以下内容：

```bash
type = struct string
```

* next

缩写为n，next用于单步调试以跳到下一步。 当有断点时，您可以输入n跳转到下一步继续

* continue

缩写为c，continue用于跳出当前断点，后面可以跟一个参数N，后者指定跳过断点的次数

* set variable

此命令用于更改进程中变量的值。 它可以像这样使用：`set variable <var> = <value>`

未完待续…
