---
title: "CentOS下SVN的配置"
date: "2025-06-05 17:31:37"
slug: "centos-xia-svn-de-pei-zhi"
categories: ["技术"]
tags: ["Linux", "CentOS"]
aliases:
  - "/2025/06/05/CentOS下SVN的配置/"
  - "/2025/06/05/CentOS下SVN的配置.html"
  - "/CentOS下SVN的配置/"
  - "/CentOS下SVN的配置.html"
  - "/2025/06/05/centos-xia-svn-de-pei-zhi/"
  - "/2025/06/05/centos-xia-svn-de-pei-zhi.html"
  - "/centos-xia-svn-de-pei-zhi.html"
---
在终端运行svn命令.如果没有安装,系统会提示安装

1.首先需要安装Subversion软件：
```shell
sudo apt-get install subversion
```

2.建立一个文件夹作为版本库的根目录

```shell 
mkdir /var/svnroot/
```

这个目录本身不是版本库，只是拿来装版本库的目录

3.进入这个目录，创建版本库

```shell 
cd /var/svnroot/
svnadmin create mysvn
```

以后如果有多个项目，可以继续在/var/svnroot/下面create新的版本库

4.配置vlink
```shell
cd /var/svnroot/vlink/conf/
ls
```

将会看到以下文件
```shell
authz passwd svnserve.conf
```

首先编辑 svnserve.conf
```shell
vim svnserve.conf
```

其中 anon-access 表示 匿名用户的权限，auth-access 表示经过认证的用户的权限。去掉前面的#注释，顶格写。一般说来像这样就可以了：
```shell
anon-access = none
auth-access = write
```

然后看到下面有 password-db 这个配置项。 这个是配置使用的密码文件。
```shell
password-db = passwd
```
为了以后多个版本库同时运行，建议改这个文件到 /var/svnroot/下面。比如： /var/svnroot/passed
```shell
password-db =/var/svnroot/passed
```
同理，authz-db这个也是，像这样：
```shell
/var/svnroot/authz
```
然后有个东西叫做realm，这个貌似是连接svn服务器的时候的提示句子。。不过设置成vlink的名字肯定没错。比如 vlink
```shell
realm = vlink
```

其他的不管。保存退出。

5.编辑 /var/svnroot/passwd
这个简单，像这样就可以了：

```shell
[users]
username=password
username=password
```

6.启动svnserve
```shell
sudo svnserve -d -r /var/svnroot/
```

`-r` 后面的参数是svnroot位置，而不是某个版本库的位置
要关闭svnserve可以直接用 kill 结束掉那个进程

7.Configure iptables
如果服务器上设置了iptables的话,你需要开启3690端口.
```shell
iptables -A INPUT -p tcp -i eth0 --dport 3690 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -i eth0 --dport 3690 -j ACCEPT
```

查看ipatbles: iptables -L 如果出现下面一行表示设置成功了: 
```shell
… ACCEPT tcp – anywhere anywhere tcp dpt:svn
```

8.测试 在本地 `svn co svn://xxx.xxx.xxx.xxx/vlink –username xxx –password xxx`
如果还有问题的我建议是将svnserve.conf文件中的有关authz注释掉，在测试。
我做的时候是有上面的问题，后来师兄注释掉后就好了，具体我也不明白什么原因
如何将想要的svn库中文件备份导出和导入呢（这里我没有测试过，大家可以测试一下，我们共同探讨）

9.将原来的Repository导出为一个文件dumpfile
```shell
svnadmin dump path/to/old-repo > dumpfile.svn
```
10.将dumpfile导入到新的Repository
```shell
svnadmin load path/to/new-repo < dumpfile.svn
```
11.本机svn的快速迁移方法:
```shell
svnadmin hotcopy old_rep_path new_rep_path
```
12.将原先服务器的配置文件备份后复制到新服务器中
`/etc/httpd/conf.d/subversion.conf`
还有repository目录下的authfile、auth.conf也需要备份后复制到新服务器中

13.linux下重新定位SVN URL方法:
如果更换了SVN服务器，就需要重新定位，指向新的SVN URL。
重新定位命令：`svn switch --relocate` 原svn地址 新svn地址
如何查看原svn地址？
查看原svn路径方法：`svn info`
