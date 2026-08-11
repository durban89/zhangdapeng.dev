---
title: "Windows下git bash乱码问题"
date: "2025-06-27 10:59:57"
slug: "windows-xia-git-bash-luan-ma-wen-ti"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/06/27/Windows下git-bash乱码问题/"
  - "/2025/06/27/Windows下git-bash乱码问题.html"
  - "/Windows下git-bash乱码问题/"
  - "/Windows下git-bash乱码问题.html"
  - "/2025/06/27/windows-xia-git-bash-luan-ma-wen-ti/"
  - "/2025/06/27/windows-xia-git-bash-luan-ma-wen-ti.html"
  - "/windows-xia-git-bash-luan-ma-wen-ti.html"
---
转载某个牛逼的人物，做个记录，

如果找不到就到git的安装目录下面去看看。

```bash
1,/etc/gitconfig：
[gui]
    encoding = utf-8 #代码库统一用urf-8,在git gui中可以正常显示中文
[i18n]
    commitencoding = GB2312 #log编码，window下默认gb2312,声明后发到服务器才不会乱码
[svn]
    pathnameencoding = GB2312 #支持中文路径
2,/etc/git-completion.bash:
alias ls='ls --show-control-chars --color=auto'  #ls能够正常显示中文
3,/etc/inputrc:
set output-meta on   #bash中可以正常输入中文
set convert-meta off
4,/etc/profile:
export LESSHARSET=utf-8   #$ git log 命令不像其它 vcs 一样，n 条 log 从头滚到底，它会恰当地停在第一页，按 space 键再往后翻页。这是通过将 log 送给 less 处理实现的。以上即是设置 less 的字符编码，使得 $ git log 可以正常显示中文。
```

如果没有就加上吧，有了的话就改下，如果是一样的话就不用修改了。

---

参考文章：

http://www.cnblogs.com/Gukw/archive/2012/01/16/2323417.html


