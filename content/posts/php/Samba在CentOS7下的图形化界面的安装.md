---
title: "Samba在CentOS7下的图形化界面的安装"
date: "2025-06-30 12:01:00"
slug: "samba-zai-centos7-xia-de-tu-xing-hua-jie-mian-de-an-zhuang"
categories: ["技术"]
tags: ["CentOS", "Linux", "Samba"]
aliases:
  - "/2025/06/30/Samba在CentOS7下的图形化界面的安装/"
  - "/2025/06/30/Samba在CentOS7下的图形化界面的安装.html"
  - "/Samba在CentOS7下的图形化界面的安装/"
  - "/Samba在CentOS7下的图形化界面的安装.html"
  - "/2025/06/30/samba-zai-centos7-xia-de-tu-xing-hua-jie-mian-de-an-zhuang/"
  - "/2025/06/30/samba-zai-centos7-xia-de-tu-xing-hua-jie-mian-de-an-zhuang.html"
  - "/samba-zai-centos7-xia-de-tu-xing-hua-jie-mian-de-an-zhuang.html"
---
第一步：下载 samba 的源码包

http://archives.fedoraproject.org/pub/archive/fedora/linux/releases/14/Everything/source/SRPMS/

下载文件：

system-config-samba-docs-1.0.9-1.fc14.src.rpm

system-config-samba-0.99.47-1.fc14.src.rpm

名称跟这个差不多的就可以，最好是下载最新的版本

第二步：安装 rpm-build  的编译工具，目的是编译 rpm 包。

```bash
yum install -y rpm-build
```

第三步：对源码包进行编译

```bash
rpmbuild --rebuild system-config-samba-0.99.47-1.fc14.src.rpm
rpmbuild --rebuild system-config-samba-docs-1.0.9-1.fc14.src.rpm
```

注意：在编译过程中会提示错误信息，请根据对应的提示安装对应的依赖包，

安装完执行同样的命令进行安装。

在此rpmbuild/RPMS/noarch/目录下会生成对应的包，以.rpm结尾

第四步：安装编译好的包,如下，实际可能名称不同

```bash
rpm -ivh system-config-samba-1.2.90-1.el6.noarch.rpm  system-config-samba-docs-1.0.9-1.el6.noarch.rpm
```

第五步：经过一系列的安装配置，下一步就是打开 samba 的图形化界面了

执行命令

```bash
system-config-samba/sudo system-config-samba
```


