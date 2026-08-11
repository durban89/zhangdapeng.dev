---
title: "CentOS 6.6 通过 yum 升级gcc到4.7/4.8"
date: "2025-07-02 16:00:33"
slug: "centos-66-tong-guo-yum-sheng-ji-gcc-dao-4748"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/02/CentOS-6.6-通过-yum-升级gcc到4.7/4.8/"
  - "/2025/07/02/CentOS-6.6-通过-yum-升级gcc到4.7/4.8.html"
  - "/CentOS-6.6-通过-yum-升级gcc到4.7/4.8/"
  - "/CentOS-6.6-通过-yum-升级gcc到4.7/4.8.html"
  - "/2025/07/02/CentOS-6-6-通过-yum-升级gcc到4-7-4-8/"
  - "/2025/07/02/CentOS-6-6-通过-yum-升级gcc到4-7-4-8.html"
  - "/2025/07/02/centos-66-tong-guo-yum-sheng-ji-gcc-dao-4748/"
  - "/2025/07/02/centos-66-tong-guo-yum-sheng-ji-gcc-dao-4748.html"
  - "/centos-66-tong-guo-yum-sheng-ji-gcc-dao-4748.html"
---
前文：

别傻了，还通过源码去安装，很费时间的，而且安装完你还要去考虑本地的gcc版本问题，这里给大家提供一个很简答的方法.

第一部分：升级到4.7

```bash
cd /etc/yum.repos.d
wget http://people.centos.org/tru/devtools-1.1/devtools-1.1.repo 
yum --enablerepo=testing-1.1-devtools-6 install devtoolset-1.1-gcc devtoolset-1.1-gcc-c++
```

这个将安装的文件放在了

```bash
/opt/centos/devtoolset-1.1
```

如果想要编辑器去处理的话，这样操作

```bash
export CC=/opt/centos/devtoolset-1.1/root/usr/bin/gcc  
export CPP=/opt/centos/devtoolset-1.1/root/usr/bin/cpp
export CXX=/opt/centos/devtoolset-1.1/root/usr/bin/c++
```

如果你想要gcc替换本地的，当然不是真的去替换，只要把他放在我们的/usrlocal/bin下面就好了，不必去管系统自带的【/usr/bin】。

```bash
ln -s /opt/rh/devtoolset-1.1/root/usr/bin/* /usr/local/bin/
hash -r
gcc --version
```

第二部分：升级到4.8【这个应该是目前最新的啦，不过网上查的话已经到5.2啦，感觉落后一点比较稳，当然还有就是这个版本是新的里面使用最多的】

```bash
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo
```

或

```bash
cd /etc/yum.repos.d
wget http://people.centos.org/tru/devtools-2/devtools-2.repo
```

然后

```bash
yum install devtoolset-2-gcc devtoolset-2-binutils devtoolset-2-gcc-c++
```

这个将安装的文件放在了

```bash
/opt/rh/devtoolset-2
```

如果想要编辑器去处理的话，这样操作

```bash
export CC=/opt/rh/devtoolset-2/root/usr/bin/gcc  
export CPP=/opt/rh/devtoolset-2/root/usr/bin/cpp
export CXX=/opt/rh/devtoolset-2/root/usr/bin/c++
```

如果你想要gcc替换本地的，当然不是真的去替换，只要把他放在我们的/usrlocal/bin下面就好了，不必去管系统自带的【/usr/bin】。

```bash
ln -s /opt/rh/devtoolset-2/root/usr/bin/* /usr/local/bin/
hash -r
gcc --version
```

这个两个部分的路径变了【请看这里】：http://people.centos.org/tru/devtools-2/readme

参考资料：http://superuser.com/questions/381160/how-to-install-gcc-4-7-x-4-8-x-on-centos

