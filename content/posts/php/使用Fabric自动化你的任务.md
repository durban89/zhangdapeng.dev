---
title: "使用Fabric自动化你的任务"
date: "2025-06-24 11:24:20"
slug: "shi-yong-fabric-zi-dong-hua-ni-de-ren-wu"
categories: ["技术"]
tags: ["Python", "Fabric"]
aliases:
  - "/2025/06/24/使用Fabric自动化你的任务/"
  - "/2025/06/24/使用Fabric自动化你的任务.html"
  - "/使用Fabric自动化你的任务/"
  - "/使用Fabric自动化你的任务.html"
  - "/2025/06/24/shi-yong-fabric-zi-dong-hua-ni-de-ren-wu/"
  - "/2025/06/24/shi-yong-fabric-zi-dong-hua-ni-de-ren-wu.html"
  - "/shi-yong-fabric-zi-dong-hua-ni-de-ren-wu.html"
---
## [fabric是什么？](#1)

[Fabric](http://docs.fabfile.org/zh/1.8/)是一个Python库，可以通过SSH在多个host上批量执行任务。你可以编写任务脚本，然后通过Fabric在本地就可以使用SSH在大量远程服务器上自动运行。这些功能非常适合应用的自动化部署，或者执行系统管理任务。

让我们首先看一个例子。我们知道在 `*NIX` 下面，uname命令是查看系统的发行版。可以写这样一个Fabric脚本：

```python
from fabric.api import run
def host_type():
   run('uname -s')
```

将上面的脚本保存为fabfile.py，就可以通过fab命令在多个主机上执行host_type脚本了：

```python
$ fab -H localhost,linuxbox host_type
[localhost] run: uname -s
[localhost] out: Darwin
[linuxbox] run: uname -s
[linuxbox] out: Linux
```

执行过程中可能需要你输入系统密码。

## [安装](#2)

如果你看到这里了，说明你开始对Fabric感兴趣了。但是上述操作在你那里无法执行，因为你还没有安装Fabric。安装Fabric很简单，可以用pip或者easy_install，也可以下载原代码安装。

## [任务函数](#3)

很好，安装Fabric并没有难住你。可能你已经成功的执行了前面的任务，现在让我们更深入一些。

Fabric中的任务就是一个python函数，姑且让我们称之为“任务函数”。既然是python函数，那么对函数的一些用法也适用于任务函数。比如传递参数、互相调用、返回值等等。首先看一个传递参数的例子：

```python
def hello(name="world"):
   print("Hello %s!" % name)
```

在执行任务的时候，可以通过fab的命令行参数为任务函数传递参数：

```python
$ fab hello:name=Holbrook
Hello Holbrook!
```

组合任务的例子如下：

```python
from fabric.api import run
def host_type():
   run('uname -s')
def hello(name="world"):
   print("Hello %s!" % name)
def composite(name="world"):
   hello(name)
   host_type()
```

## [Fabric提供的命令](#4)

前面我们见过了fabric.api模块中的run函数，其功能是在远端主机上执行命令。fabric.api中还提供了local函数，用于执行本地（Fabric所在的主机）命令。如下：

```python
from fabric.api import local
def lslocal():
   local('ls')
```

类似远端命令和本地命令，Fabric也区分远端目录和本地目录。Fabric提供的对远端和本地目录的操作分别是cd和lcd。如果你用过命令行的ftp，这很容易理解。让我们看一个例子：

```python
def filepath():
   remote_dir = '/opt/xxx'
   with cd(remote_dir):
       run("touch README")
```

上面代码的功能是进入远端的`/opt/xxx`目录，并创建一个README文件。

Fabric还提供了很多的命令，比如文件操作等，可以参考Fabric的operations模块。

## [管理服务器连接](#5)

前面的例子中，都需要在fab命令行参数中指定server。当要管理大量服务器时很麻烦。Fabric提供了环境变量的字典env，其中就包含了hosts字典项，可以定义需要连接的server。如下：

```python
from fabric.api import env, run
env.hosts = ['host1', 'host2']
def mytask():
   run('ls /var/www')
```

也可以为每个任务单独指定要执行该任务的host列表：

```python
from fabric.api import env, run
def set_hosts():
   env.hosts = ['host1', 'host2']
def mytask():
   run('ls /var/www')
```

这样执行 `fab set_hosts mytask`时，就可以为`set_hosts`中指定的两个host执行mytask任务了。如果你懒得写函数，在fab命令行中指定也是一样的：

```python
fab mytask:hosts="host1;host2"
```

为了更方便的执行批量任务，Fabric中还定义了Role，有兴趣可以阅读其官方文档。

管理SSH密码、用户、端口

尽管更推荐使用SSH公钥认证，但是Fabric还是提供了管理密码的机制。Fabric提供了两层密码。

如果你的server有相同的密码，可以在env.password中设置默认的密码；如果server密码不同，还可以在env.passwords中设置(host,password）对，为每个server设置单独的ssh密码。

上面的host字符串采用这种格式：username@hostname:port。所以，在指定ssh密码的同时，也就指定了ssh用户。同密码一样，你也可以在env.user中指定一个默认的用户。如果都没有指定，执行fab命令时会提示你输入密码。

## [小结](#6)

使用Fabric，你可以管理一系列host的SSH连接（包括主机名，用户，密码），定义一系列的任务函数，然后灵活的指定在哪些host上执行哪些任务。这非常使用于需要管理大量host的场景，比如运维，私有云管理，应用自动化部署等。

本文只是一篇入门文档，远没有体现出Fabric的强大。实际上，Fabric还包括大量的功能，比如Role的定义，远程交互及异常处理，并发执行，文件操作等，并且不仅仅局限于命令行方式，可以在你的应用中调用Fabric。

希望本文能够引起你对Fabric的兴趣，并在你的实际应用中解决问题。

