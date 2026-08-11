---
title: "Go基础学习记录之部署和维护(三)"
date: "2025-08-04 18:07:23"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-san"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之部署和维护(三)/"
  - "/2025/08/04/Go基础学习记录之部署和维护(三).html"
  - "/Go基础学习记录之部署和维护(三)/"
  - "/Go基础学习记录之部署和维护(三).html"
  - "/2025/08/04/Go基础学习记录之部署和维护-三/"
  - "/2025/08/04/Go基础学习记录之部署和维护-三.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-san/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-san.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-san.html"
---
### 部署

当我们的Web应用程序最终生产就绪时，部署它所需的步骤是什么？ 在Go中，在编译程序之后创建封装我们的应用程序的可执行文件。 用C编写的程序可以完美地作为后台守护程序进程运行，但是Go还没有对守护进程的本机支持。 好消息是我们可以使用第三方工具来帮助我们管理Go应用程序的部署，其中包括Supervisord，upstart和daemontools等。 本节将向您介绍Supervisord过程控制系统的一些基础知识。

守护进程

目前，Go程序不能作为守护进程运行（有关其他信息，请参阅github上的未解决问题）。 在Go中分叉现有线程很困难，因为无法确保所有已使用的线程中的一致状态。

但是，我们可以看到许多在线实现守护进程的尝试，例如以下两种方式;

* MarGo使用Command部署应用程序概念的一个实现。 如果您真的想要对应用程序进行守护，建议使用类似于以下内容的代码：

```go
d := flag.Bool("d", false, "Whether or not to launch in the background(like a daemon)")
if *d {
    cmd := exec.Command(os.Args[0],
        "-close-fds",
        "-addr", *addr,
        "-call", *call,
    )
    serr, err := cmd.StderrPipe()
    if err != nil {
        log.Fatalln(err)
    }
    err = cmd.Start()
    if err != nil {
        log.Fatalln(err)
    }
    s, err := ioutil.ReadAll(serr)
    s = bytes.TrimSpace(s)
    if bytes.HasPrefix(s, []byte("addr: ")) {
        fmt.Println(string(s))
        cmd.Process.Release()
    } else {
        log.Printf("unexpected response from MarGo: `%s` error: `%v`\n", s, err)
        cmd.Process.Kill()
    }
}
```

* 另一种解决方案是使用系统调用，但这种解决方案并不完美：

```go
package main

import (
    "log"
    "os"
    "syscall"
)

func daemon(nochdir, noclose int) int {
    var ret, ret2 uintptr
    var err uintptr

    darwin := syscall.OS == "darwin"

    // already a daemon
    if syscall.Getppid() == 1 {
        return 0
    }

    // fork off the parent process
    ret, ret2, err = syscall.RawSyscall(syscall.SYS_FORK, 0, 0, 0)
    if err != 0 {
        return -1
    }

    // failure
    if ret2 < 0 {
        os.Exit(-1)
    }

    // handle exception for darwin
    if darwin && ret2 == 1 {
        ret = 0
    }

    // if we got a good PID, then we call exit the parent process.
    if ret > 0 {
        os.Exit(0)
    }

    /* Change the file mode mask */
    _ = syscall.Umask(0)

    // create a new SID for the child process
    s_ret, s_errno := syscall.Setsid()
    if s_errno != 0 {
        log.Printf("Error: syscall.Setsid errno: %d", s_errno)
    }
    if s_ret < 0 {
        return -1
    }

    if nochdir == 0 {
        os.Chdir("/")
    }

    if noclose == 0 {
        f, e := os.OpenFile("/dev/null", os.O_RDWR, 0)
        if e == nil {
            fd := f.Fd()
            syscall.Dup2(fd, os.Stdin.Fd())
            syscall.Dup2(fd, os.Stdout.Fd())
            syscall.Dup2(fd, os.Stderr.Fd())
        }
    }

    return 0
}
```

虽然上面的两个解决方案在Go中实现了守护进程，但我仍然不建议您使用任何一种方法，因为Go中没有对守护进程的正式支持。 尽管如此，第一个选项是更可行的选项，并且目前被一些着名的开源项目（如skynet）用于实现守护进程。

Supervisord

上面，我们看了两个常用于在Go中实现守护进程的方案，但这两种方法都缺乏官方支持。 因此，建议您使用第三方工具来管理应用程序部署。 在这里，我们来看看用Python实现的Supervisord项目，该项目为流程管理提供了广泛的工具。 Supervisord将帮助您对Go应用程序进行守护，还允许您使用一些简单的命令以及许多其他操作来执行诸如启动，关闭和重新启动应用程序之类的操作。 此外，Supervisord托管进程可以自动重启已崩溃的进程，确保程序可以从任何中断中恢复。

**安装Supervisord**

可以使用sudo easy\_install supervisor轻松安装Supervisord。 当然，还可以选择直接从官方网站下载，解压缩，进入文件夹，然后运行setup.py install手动安装。

* 如果您要使用easy\_install路由，则需要先安装setuptools

转到http://pypi.python.org/pypi/setuptools#files并下载相应的文件，具体取决于系统的python版本。 输入目录并执行sh setuptoolsxxxx.egg。 当脚本完成后，您将能够使用easy\_install命令安装Supervisord。

**配置Supervisord**

Supervisord的默认配置文件路径是/etc/supervisord.conf，可以使用文本编辑器进行修改。 以下是典型配置文件的外观：

```bash
;/etc/supervisord.conf
[unix_http_server]
file = /var/run/supervisord.sock
chmod = 0777
chown= root:root

[inet_http_server]
# Web management interface settings
port=9001
username = admin
password = yourpassword

[supervisorctl]
; Must 'unix_http_server' match the settings inside
serverurl = unix:///var/run/supervisord.sock

[supervisord]
logfile=/var/log/supervisord/supervisord.log ; (main log file;default $CWD/supervisord.log)
logfile_maxbytes=50MB       ; (max main logfile bytes b4 rotation;default 50MB)
logfile_backups=10          ; (num of main logfile rotation backups;default 10)
loglevel=info               ; (log level;default info; others: debug,warn,trace)
pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
nodaemon=true              ; (start in foreground if true;default false)
minfds=1024                 ; (min. avail startup file descriptors;default 1024)
minprocs=200                ; (min. avail process descriptors;default 200)
user=root                 ; (default is current user, required if root)
childlogdir=/var/log/supervisord/            ; ('AUTO' child log dir, default $TEMP)

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
; Manage the configuration of a single process, you can add multiple program
[program: blogdemon]
command =/data/blog/blogdemon
autostart = true
startsecs = 5
user = root
redirect_stderr = true
stdout_logfile =/var/log/supervisord/blogdemon.log
```

**Supervisord管理**

安装完成后，可以在命令行上使用两个Supervisord命令：supervisor和supervisorctl。 命令如下：

* supervisord：初始启动，启动和流程配置管理。
* supervisorctl stop programxxx：停止programxxx进程，其中programxxx是supervisord.conf文件中配置的值。 例如，如果您配置了[program：blogdemon]，则可以使用supervisorctl stop blogdemon命令终止该进程。
* supervisorctl start programxxx：启动programxxx进程
* supervisorctl restart programxxx：重启programxxx进程
* supervisorctl stop all：停止所有进程; 注意：启动，重启，停止不会加载最新的配置文件。
* supervisorctl reload：加载最新的配置文件，启动它们，并使用新配置管理所有进程。

### 小结

在本次分享中，我们描述了如何在Go中实现守护进程。 我们了解到Go本身并不支持守护进程，我们需要使用第三方工具来帮助我们管理守护进程。 其中一个工具是Supervisord过程控制系统，我们可以使用它来轻松部署和管理我们的Go程序。
