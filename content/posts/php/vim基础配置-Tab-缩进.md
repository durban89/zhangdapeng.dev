---
title: "vim基础配置 - Tab（缩进）"
date: "2025-07-15 09:52:26"
slug: "vim-ji-chu-pei-zhi-tab-suo-jin"
categories: ["技术"]
tags: ["Vim"]
aliases:
  - "/2025/07/15/vim基础配置-Tab（缩进）/"
  - "/2025/07/15/vim基础配置-Tab（缩进）.html"
  - "/vim基础配置-Tab（缩进）/"
  - "/vim基础配置-Tab（缩进）.html"
  - "/2025/07/15/vim基础配置-Tab-缩进/"
  - "/2025/07/15/vim基础配置-Tab-缩进.html"
  - "/2025/07/15/vim-ji-chu-pei-zhi-tab-suo-jin/"
  - "/2025/07/15/vim-ji-chu-pei-zhi-tab-suo-jin.html"
  - "/vim-ji-chu-pei-zhi-tab-suo-jin.html"
---
使用vim最开始的时候，如果是写python的话，首先需要配置的就是缩进

如果缩进没有配置，对于入门pyhton的小白，可以说是非常苦恼，因为缩进出问题的话，代码写了也是编译不通过的

### 如何配置tab

首先打开`~/.vimrc，`没有的话自己创建一个`~/.vimrc`

在.vimrc中添加如下配置

```bash
set shiftwidth=4 " 缩进的宽度
set softtabstop=4 " 退回缩进的宽度
set nu " 显示行号
set autoindent " 自动缩进
```

配置完之后保存，再进行编辑文件的时候，在操作换行时缩进的宽度就变成了4

### VIM 缩进（这个适用于在打开vim的情况下）

VIM设置自动缩进：

```bash
set autoindent
set cindent
```

VIM Tab键宽度

```bash
set tabstop=4
```

统一设置为缩进为4

```bash
set softtabstop=4
set shiftwidth=4
```

不要用空格键代替空格

```bash
set noexpandtab
```

显示行号:

```bash
set number
```

以上命令的输入需要在打开vim的情况下，先输入`:`(冒号)之后在输入对应的命令
