---
title: "paramiko的安装与使用"
date: "2025-06-23 16:26:58"
slug: "paramiko-de-an-zhuang-yu-shi-yong"
categories: ["技术"]
tags: ["Python", "Paramiko"]
aliases:
  - "/2025/06/23/paramiko的安装与使用/"
  - "/2025/06/23/paramiko的安装与使用.html"
  - "/paramiko的安装与使用/"
  - "/paramiko的安装与使用.html"
  - "/2025/06/23/paramiko-de-an-zhuang-yu-shi-yong/"
  - "/2025/06/23/paramiko-de-an-zhuang-yu-shi-yong.html"
  - "/paramiko-de-an-zhuang-yu-shi-yong.html"
---
### [简介](#1)

paramiko是用python语言写的一个模块，遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接。

由于使用的是python这样的能够跨平台运行的语言，所以所有python支持的平台，如Linux, Solaris, BSD, MacOS X, Windows等，paramiko都可以支持，因此，如果需要使用SSH从一个平台连接到另外一个平台，进行一系列的操作时，paramiko是最佳工具之一。

举个常见的例子，现有这样的需求：需要使用windows客户端，远程连接到Linux服务器，查看上面的日志状态，大家通常使用的方法会是：

1：用telnet

2：用PUTTY

3：用WinSCP

4：用XManager等…

那现在如果需求又增加一条，要从服务器上下载文件，该怎么办？那常用的办法可能会是：

1：Linux上安装FTP并配置

2：Linux上安装Sambe并配置…

大家会发现，常见的解决方法都会需要对远程服务器必要的配置，如果远程服务器只有一两台还好说，如果有N台，还需要逐台进行配置，或者需要使用代码进行以上操作时，上面的办法就不太方便了。

使用paramiko可以很好的解决以上问题，比起前面的方法，它仅需要在本地上安装相应的软件（python以及PyCrypto），对远程服务器没有配置要求，对于连接多台服务器，进行复杂的连接操作特别有帮助。

### [安装和使用](#2)

1、PyCrypto模块的安装（安装paramiko需要有PyCrypto的支持）

a、下载地址：<https://www.dlitz.net/software/pycrypto/>

b、解压：

```bash
tar -zxvf ./pycrypto-2.6.tar.gz
```

c、安装：

```bash
cd pycrypto-2.6/
sudo python ./setup.py install
```

2、paramiko模块的安装

a、下载地址：<https://github.com/zhangda89/paramiko/blob/master/paramiko/client.py>

b、解压：

```bash
unzip ./python-paramiko.zip
```

c、安装

```bash
cd paramiko-master/
sudo python setup.py install
```

3、运行任意命令，然后进行结果输出

```python
#!/usr/bin/python 
import paramiko
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("某IP地址",22,"用户名", "口令")
stdin, stdout, stderr = ssh.exec_command("你的命令")
print stdout.readlines()
ssh.close()
```

其中的”你的命令”可以任意linux支持的命令，如一些常用的命令：

df：查看磁盘使用情况  
uptime：显示系统运行时间信息  
cat：显示某文件内容  
mv/cp/mkdir/rmdir:对文件或目录进行操作  
/sbin/service/ xxxservice start/stop/restart：启动、停止、重启某服务  
netstat -ntl |grep 8080：查看8080端口的使用情况   
 或者 nc -zv localhost ：查看所有端口的使用情况   
find / -name XXX：查找某文件

4、下载文件

```python
#!/usr/bin/python 
import paramiko

t = paramiko.Transport(("主机","端口"))
t.connect(username = "用户名", password = "口令")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/var/log/system.log'
localpath='/tmp/system.log'
sftp.get(remotepath, localpath)
t.close()
```

5、上传文件

```python
#!/usr/bin/python 
import paramiko

t = paramiko.Transport(("主机","端口"))
t.connect(username = "用户名", password = "口令")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/var/log/system.log'
localpath='/tmp/system.log'
sftp.put(localpath,remotepath)
t.close()
```

参考文章：

[paramiko的安装与使用](http://www.cnblogs.com/gannan/archive/2012/02/06/2339883.html)

[python用paramiko模块上传本地目录到远程目录](http://wangwei007.blog.51cto.com/68019/1285412)

[paramiko ssh sftp](http://5ydycm.blog.51cto.com/115934/340854/)

[Python Scripts for Downloading Files via SFTP](http://engineering.monetate.com/2012/03/23/python-scripts-for-downloading-files-via-sftp/)

[Python中操控ssh和sftp](http://www.coder4.com/archives/3280)

