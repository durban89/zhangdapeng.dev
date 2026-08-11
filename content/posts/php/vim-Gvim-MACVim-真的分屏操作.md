---
title: "vim Gvim MACVim 真的分屏操作"
date: "2025-06-18 11:29:02"
slug: "vim-gvim-macvim-zhen-de-fen-ping-cao-zuo"
categories: ["技术"]
tags: ["Vim"]
aliases:
  - "/2025/06/18/vim-Gvim-MACVim-真的分屏操作/"
  - "/2025/06/18/vim-Gvim-MACVim-真的分屏操作.html"
  - "/vim-Gvim-MACVim-真的分屏操作/"
  - "/vim-Gvim-MACVim-真的分屏操作.html"
  - "/2025/06/18/vim-gvim-macvim-zhen-de-fen-ping-cao-zuo/"
  - "/2025/06/18/vim-gvim-macvim-zhen-de-fen-ping-cao-zuo.html"
  - "/vim-gvim-macvim-zhen-de-fen-ping-cao-zuo.html"
---
1. 如何横/竖分屏打开新文件

```bash
:sp filename
:split filename
:vsp filename
:vsplit filename
:sview filename  ->只读分屏打开文件
```

从命令行直接打开多个文件且是分屏

```bash
vim -On file1, file2 ...  ->垂直分屏
vim -on file1, file2 ...  ->水平分屏
```

其中n为分几个屏  
  
2. 如何横/竖分屏打开当前文件

```bash
ctrl+W s
ctrl+W v
```

3. 如何切换分屏

```bash
ctrl+w w
ctrl+w h,j,k,l
ctrl+w 上下左右键头
```

4. 如何关闭分屏

```bash
ctrl+W c 关闭当前窗口
ctrl+w q 关闭当前窗口，若只有一个分屏且退出vim
:only  仅保留当前分屏
:hide  关闭当前分屏
```

5. 如何调整分屏的大小

```bash
ctrl+w = 所有分屏都统一高度
ctrl+w + 增加高度
ctrl+w - 减少高度
10 ctrl+w + 增加10行高度
```

6. 如何移动分屏

```bash
ctrl+W H,J,K,L
```

7.多标签

多个标签间进行切换时向右切换gt，向左切换用gT

在编辑的时候想增加一个标签就可以:tabnew filename

```bash
:tabc       关闭当前的tab

:tabo       关闭所有其他的tab

:tabs       查看所有打开的tab

:tabp      前一个

:tabn      后一个
```
