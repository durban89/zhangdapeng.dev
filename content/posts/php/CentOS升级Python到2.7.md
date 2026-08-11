---
title: "CentOS升级Python到2.7"
date: "2025-06-30 14:31:03"
slug: "centos-sheng-ji-python-dao-27"
categories: ["技术"]
tags: ["CentOS", "Python"]
aliases:
  - "/2025/06/30/CentOS升级Python到2.7/"
  - "/2025/06/30/CentOS升级Python到2.7.html"
  - "/CentOS升级Python到2.7/"
  - "/CentOS升级Python到2.7.html"
  - "/2025/06/30/centos-sheng-ji-python-dao-27/"
  - "/2025/06/30/centos-sheng-ji-python-dao-27.html"
  - "/centos-sheng-ji-python-dao-27.html"
---
CentOS 6.3上安装的python版本是2.6，不能满足我运行软件的要求，所以对python进行升级。搜索一下了之后发现，也并不是那么单纯简单。

下载，解压，编译，安装，这些都是常规操作了。据说系统自带的旧版本python被严重依赖，所以不能卸载原Python，这里选择全新安装.

```bash
tar -xvf Python-2.7.7.tgz
cd Python-2.7.7
./configure --prefix=/usr/local/python2.7
make
make install
```

安装好后可以运行一下Python看看是否正常了

```bash
/usr/local/python2.7/bin/python2.7 -V
```

接下来需要创建一个链接来使系统默认python变为python2.7。

```bash
ln -fs /usr/local/python2.7/bin/python /usr/bin/python
```

运行python查看版本

```bashbash
python -V
```

进行更改后，yum果然无法运行了。修改/usr/bin/yum文件

```bash
vi /usr/bin/yum
```

将第一行的

```bash
#!/usr/bin/python
```

中的python改为系统原有的python版本，我的如下：

```bash
#!/usr/bin/python2.6
```


