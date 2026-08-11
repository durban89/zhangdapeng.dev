---
title: "CentOS 之 非root情况下zsh安装命令记录"
date: "2025-07-03 17:37:43"
slug: "centos-zhi-fei-root-qing-kuang-xia-zsh-an-zhuang-ming-ling-ji-lu"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/03/CentOS-之-非root情况下zsh安装命令记录/"
  - "/2025/07/03/CentOS-之-非root情况下zsh安装命令记录.html"
  - "/CentOS-之-非root情况下zsh安装命令记录/"
  - "/CentOS-之-非root情况下zsh安装命令记录.html"
  - "/2025/07/03/centos-zhi-fei-root-qing-kuang-xia-zsh-an-zhuang-ming-ling-ji-lu/"
  - "/2025/07/03/centos-zhi-fei-root-qing-kuang-xia-zsh-an-zhuang-ming-ling-ji-lu.html"
  - "/centos-zhi-fei-root-qing-kuang-xia-zsh-an-zhuang-ming-ling-ji-lu.html"
---
第一步就是：下载zsh源码包

安装的前提是需要安装ncurses，可以看前面的文章[[Centos 之 非root情况下ncurses安装问题](https://www.gowhich.com/blog/806)]  
然后使用下面的命令进行安装

```bash
LDFLAGS=-L$HOME/lib CPPFLAGS=-I$HOME/include ./configure --prefix=$HOME --with-tcsetpgrp
make && make instal
```

运行zsh发生如下错误

```bash
zsh --version
```

> error while loading shared libraries: libncursesw.so.6: cannot open shared object file: No such file or directory

这个问题经过网络搜索，是由于执行zsh没有加载对应的动态库，因为我们的动态库安装在了我们自己的目录下面，通知执行下面的命令，即可得到解决

```bash
export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
```

顺便把它加到.bash\_profile里面吧，再次执行安装命令，即可安装完毕。

但是安装完 运行下面的命令

```bash
exec $HOME/bin/zsh -l 
```

会发生一直卡住不动，暂时不知道原因，哪位高手遇到解决了，可以留言给我，一起探讨。
