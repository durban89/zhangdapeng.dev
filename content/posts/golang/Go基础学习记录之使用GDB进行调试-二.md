---
title: "Go基础学习记录之使用GDB进行调试(二)"
date: "2025-08-04 11:39:16"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试(二)/"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试(二).html"
  - "/Go基础学习记录之使用GDB进行调试(二)/"
  - "/Go基础学习记录之使用GDB进行调试(二).html"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试-二/"
  - "/2025/08/04/Go基础学习记录之使用GDB进行调试-二.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-er/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-shi-yong-gdb-jin-xing-tiao-shi-er.html"
---
续接上文【[Go基础学习记录之使用GDB进行调试(一)](https://www.xiaorongmao.com/blog/115)】

### 调试过程

现在，让我们看看下面的代码，看看GDB通常用于调试Go程序：

```go
package main

import (
    "fmt"
    "time"
)

func counting(c chan<- int) {
    for i := 0; i < 10; i++ {
        time.Sleep(2 * time.Second)
        c <- i
    }
    close(c)
}

func main() {
    msg := "Starting main"
    fmt.Println(msg)
    bus := make(chan int)
    msg = "starting a gofunc"
    go counting(bus)
    for count := range bus {
        fmt.Println("count:", count)
    }
}
```

现在我们编译文件，创建一个名为"gdbfile"的可执行文件：

```bash
go build -gcflags "-N -l" gdbfile.go
```

使用GDB命令开始调试：

```bash
gdb gdbfile
```

首次启动GDB后，您必须输入run命令才能看到程序正在运行。 然后，您将看到程序输出如下; 直接从命令行执行程序将输出完全相同的东西：

```bash
(gdb) run
Starting program: /home/xxx/gdbfile 
Starting main
count: 0
count: 1
count: 2
count: 3
count: 4
count: 5
count: 6
count: 7
count: 8
count: 9
[LWP 2771 exited]
[Inferior 1 (process 2771) exited normally]
```

好的，既然我们知道如何启动和运行程序，那么让我们来看看设置断点：

```bash
(gdb) b 23
Breakpoint 1 at 0x400d8d: file /home/xxx/gdbfile.go, line 23.
(gdb) run
Starting program: /home/xxx/gdbfile 
Starting main
[New LWP 3284]
[Switching to LWP 3284]

Breakpoint 1, main.main () at /home/xxx/gdbfile.go:23
23            fmt.Println("count:", count)
```

在上面的例子中，我们使用b 23命令在代码的第23行设置断点，然后输入run来启动程序。 当我们的程序在断点处停止时，我们通常需要查看相应的源代码上下文。 在我们的GDB会话中输入list命令，我们可以在断点之前看到五行代码：

```bash
(gdb) list
18        fmt.Println(msg)
19        bus := make(chan int)
20        msg = "starting a gofunc"
21        go counting(bus)
22        for count := range bus {
23            fmt.Println("count:", count)
24        }
25    }
```

现在GDB正在运行当前的程序环境，我们可以访问一些有用的调试信息，我们可以打印出来。 要查看相应的变量类型和值，请键入info locals：

```bash
(gdb) info locals
count = 0
bus = 0xf840001a50
(gdb) p count
$1 = 0
(gdb) p bus
$2 = (chan int) 0xf840001a50
(gdb) whatis bus
type = chan int
```

要让程序继续执行直到下一个断点，请输入c命令：

```bash
(gdb) c
Continuing.
count: 0
[New LWP 3303]
[Switching to LWP 3303]

Breakpoint 1, main.main () at /home/xxx/gdbfile.go:23
23 fmt.Println("count:", count)
(gdb) c
Continuing.
count: 1
[Switching to LWP 3302]

Breakpoint 1, main.main () at /home/xxx/gdbfile.go:23
23 fmt.Println("count:", count)
```

在每个c之后，代码将执行一次，然后跳转到for循环的下一次迭代。 当然，它将继续打印出适当的信息。

假设您需要更改当前执行环境中的上下文变量，跳过该过程然后继续下一步。 您可以通过首先使用info locals获取变量状态，然后使用set variable命令来修改它们：

```bash
(gdb) info locals
count = 2
bus = 0xf840001a50
(gdb) set variable count=9
(gdb) info locals
count = 9
bus = 0xf840001a50
(gdb) c
Continuing.
count: 9
[Switching to LWP 3302]

Breakpoint 1, main.main () at /home/xxx/gdbfile.go:23
23 fmt.Println("count:", count)
```

最后，在运行时，程序会创建一些goroutine。 我们可以使用info goroutines看到每个goroutine正在做什么：

```bash
(gdb) info goroutines
* 1 running runtime.gosched
* 2 syscall runtime.entersyscall 
3 waiting runtime.gosched 
4 runnable runtime.gosched
(gdb) goroutine 1 bt
#0 0x000000000040e33b in runtime.gosched () at /home/xxx/go/src/pkg/runtime/proc.c:927
#1 0x0000000000403091 in runtime.chanrecv (c=void, ep=void, selected=void, received=void)
at /home/xxx/go/src/pkg/runtime/chan.c:327
#2 0x000000000040316f in runtime.chanrecv2 (t=void, c=void)
at /home/xxx/go/src/pkg/runtime/chan.c:420
#3 0x0000000000400d6f in main.main () at /home/xxx/gdbfile.go:22
#4 0x000000000040d0c7 in runtime.main () at /home/xxx/go/src/pkg/runtime/proc.c:244
#5 0x000000000040d16a in schedunlock () at /home/xxx/go/src/pkg/runtime/proc.c:267
#6 0x0000000000000000 in ?? ()
```

从goroutines命令，我们可以更好地了解Go的运行时系统内部正在做什么; 清楚地显示每个功能的调用顺序。

### 小结

在本篇文章中，我们介绍了一些可用于调试Go应用程序的GDB调试器的基本命令。 其中包括run，print，info，set variable，continue，list和break命令等。 从上面的简单示例中，我希望您能够更好地了解调试过程如何在Go中使用GDB调试器。 如果您想获得更多调试技巧，请参阅其官方网站上的GDB手册。
