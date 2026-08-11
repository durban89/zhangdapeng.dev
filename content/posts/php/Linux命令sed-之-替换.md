---
title: "Linux命令sed 之 替换"
date: "2025-07-03 11:08:10"
slug: "linux-ming-ling-sed-zhi-ti-huan"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/03/Linux命令sed-之-替换/"
  - "/2025/07/03/Linux命令sed-之-替换.html"
  - "/Linux命令sed-之-替换/"
  - "/Linux命令sed-之-替换.html"
  - "/2025/07/03/linux-ming-ling-sed-zhi-ti-huan/"
  - "/2025/07/03/linux-ming-ling-sed-zhi-ti-huan.html"
  - "/linux-ming-ling-sed-zhi-ti-huan.html"
---
最近做redis的集群配置，想到一个问题，就是配置文件要是我能用命令替换就好了，就不需要每次打开文件去编辑一遍。

于是让我发现了sed这个命令，那么今天就记录下如何来替换文件里面的内容。起始就是学习了，记得下次使用就好了。

首先新建目录

test

新建两个文件

test/a.txt

test/b.txt

```bash
ll test
```

结果如下

```bash
-rw-r--r--  1 durban126  staff    22B  7  9 00:42 a.txt
-rw-r--r--  1 durban126  staff    15B  7  9 00:25 b.txt
```

a.text的内容是

> wo wo gowhich gowhich

b.text的内容是

> eo eo gowhich gowhich

然后我们通过sed命令来做文件内容替换,将wo替换位eo

Mac OS 环境

```bash
sed -ig "s/wo/eo/g" `grep wo -rl ./test`
sed -i "" "s/wo/eo/g" `grep wo -rl ./test`
```

或

```bash
sed -i ".bak" "s/wo/eo/g" `grep wo -rl ./test`
```

Linux 环境

```bash
sed -i "s/wo/eo/g" `grep wo -rl ./test`
```

之所以不同，是因为Mac OS下要求强制备份。

我们先执行

```bash
sed -ig "s/wo/eo/g" `grep wo -rl ./test`
```

结果是：

```bash
-rw-r--r--  1 durban126  staff    22B  7  9 00:55 a.txt
-rw-r--r--  1 durban126  staff    22B  7  9 00:42 a.txtg
-rw-r--r--  1 durban126  staff    15B  7  9 00:25 b.txt
```

a.txt的内容是

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  cat test/a.txt
eo eo gowhich gowhich
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤
```

但是a.txtg就不是了，已做了备份处理

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  cat test/a.txtg
wo wo gowhich gowhich
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤
```

再来看看执行

```bash
sed -i "" "s/wo/eo/g" `grep wo -rl ./test`
```

结果是

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  ll test 
total 16
-rw-r--r--  1 durban126  staff    22B  7  9 01:06 a.txt
-rw-r--r--  1 durban126  staff    21B  7  9 00:58 b.txt
```

a.txt的内容也变化了。

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  cat test/a.txt 
eo eo gowhich gowhich
```

但是没有了备份文件了。

```bash
sed -i ".bak" "s/wo/eo/g" `grep wo -rl ./test`
```

这个命令就会跟

```bash
sed -ig "s/wo/eo/g" `grep wo -rl ./test`
```

类似了，做了文件备份喽

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  ll test 
total 24
-rw-r--r--  1 durban126  staff    22B  7  9 01:09 a.txt
-rw-r--r--  1 durban126  staff    22B  7  9 01:09 a.txt.bak
-rw-r--r--  1 durban126  staff    21B  7  9 00:58 b.txt
```

a.txt.bak的内容就是备份a.txt的内容了。

还有另外一个命令

```bash
sed -i "s/wo/eo/g" `grep wo -rl ./test`
```

结果是会报错了，

```bash
╭─xxxx@xxxx ~/php ‹ruby-2.2.1› 
╰─➤  sed -i "s/wo/eo/g" `grep wo -rl ./test` 
sed: 1: "./test/a.txt.bak": invalid command code .
```

所以还是区分下环境比较好。

但是命令

```bash
sed -ig "s/wo/eo/g" `grep wo -rl ./test`
```

是在另种情况下通用的。

PS:

-i 表示inplace edit，就地修改文件  
-r 表示搜索子目录  
-l 表示输出匹配的文件名


