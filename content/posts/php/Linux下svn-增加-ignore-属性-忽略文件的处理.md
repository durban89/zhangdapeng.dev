---
title: "Linux下svn 增加 ignore 属性(忽略文件的处理)"
date: "2025-06-27 10:07:10"
slug: "linux-xia-svn-zeng-jia-ignore-shu-xing-hu-lve-wen-jian-de-chu-li"
categories: ["技术"]
tags: ["Linux", "SVN"]
aliases:
  - "/2025/06/27/Linux下svn-增加-ignore-属性(忽略文件的处理)/"
  - "/2025/06/27/Linux下svn-增加-ignore-属性(忽略文件的处理).html"
  - "/Linux下svn-增加-ignore-属性(忽略文件的处理)/"
  - "/Linux下svn-增加-ignore-属性(忽略文件的处理).html"
  - "/2025/06/27/Linux下svn-增加-ignore-属性-忽略文件的处理/"
  - "/2025/06/27/Linux下svn-增加-ignore-属性-忽略文件的处理.html"
  - "/2025/06/27/linux-xia-svn-zeng-jia-ignore-shu-xing-hu-lve-wen-jian-de-chu-li/"
  - "/2025/06/27/linux-xia-svn-zeng-jia-ignore-shu-xing-hu-lve-wen-jian-de-chu-li.html"
  - "/linux-xia-svn-zeng-jia-ignore-shu-xing-hu-lve-wen-jian-de-chu-li.html"
---
一直不知道svn的忽略命令如何使用，经过google的查找，使用方法还是有的，做个记录好了。

如果想在SVN提交时，忽略某个文件，也就是某个文件不提交，可以使用

`svn propedit svn:ignore`命令。

下面详细介绍一下使用步骤。

单纯的看svn官方文档和一些网上搜索的资料，有时候真的不如亲自试验的好。

`svn propedit svn:ignore` 目录名称。

注意，在使用这个SVN的属性编辑前，你得确保后面的“目录名称”是SVN版本控制的目录。

如果要忽略此目录下的文件，可以如下操作。

比如，想忽略/product目录下的test.php文件。前提是/product目录必须在svn版本控制下，而test.php文件不在svn版本控制。

`svn st`先看一下状态，会显示如下：

```bash
?     /product/test.php
```

我们需要将test.php文件加入忽略列表。

此时先设置SVN默认的编辑器

```bash
export SVN_EDITOR=vim
```

然后，使用svn propedit svn:ignore ,用法如下

```bash
svn propedit svn:ignore /product
```

此时会出现一个VIM的编辑窗口，表示需要将某个文件加入到忽略列表里

我们在编辑窗口中，写入

```bash
test.php
```

然后保存，并退出VIM编辑器。

这时候会有一个提示：属性 “svn:ignore” 于 “product” 被设为新值。

表示文件test.php的svn:ignore属性设置成功。

然后使用`svn st`查看，会显示：

```bash
M        product
```

我们需要提交，然后这个svn:ignore属性才会起作用

```bash
svn ci -m '忽略test.php文件'
```

这时候，无论你如何修改test.php文件，再使用svn st时，也不会出现修改提示符合M了。

---

参考文章：

http://hi.baidu.com/phplinuxmysql/item/5146931478630e0a8ebde41b

