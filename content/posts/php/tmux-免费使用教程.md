---
title: "tmux 免费使用教程"
date: "2025-07-10 10:57:49"
slug: "tmux-mian-fei-shi-yong-jiao-cheng"
categories: ["技术"]
tags: ["Tmux"]
aliases:
  - "/2025/07/10/tmux-免费使用教程/"
  - "/2025/07/10/tmux-免费使用教程.html"
  - "/tmux-免费使用教程/"
  - "/tmux-免费使用教程.html"
  - "/2025/07/10/tmux-mian-fei-shi-yong-jiao-cheng/"
  - "/2025/07/10/tmux-mian-fei-shi-yong-jiao-cheng.html"
  - "/tmux-mian-fei-shi-yong-jiao-cheng.html"
---
tmux 是一款终端复用命令行工具，一般用于 Terminal 的窗口管理。tmux 可以在终端软件重启后通过命令行恢复上次的 session ，而终端软件则不行。tmux 简洁优雅、订制性强，学会之后也能在 Linux 上使用，有助于逼格提升。tmux 由于存在前缀快捷键，所以不存在快捷键冲突问题。

## 安装

安装方法可以去github上[tmux](https://github.com/tmux/tmux)具体了解安装方法，我这里只介绍mac下的安装方法

mac下安装使用下面这个命令

```bash
brew install tmux
```

安装完成后，运行 `tmux` 新建一个 tmux 的会话（session），此时窗口唯一的变化是在底部会出现一个 tmux 的状态栏。我们先按下 tmux 默认的前缀快捷键 `⌃b(`注：⌃ 为 Mac 的 control 键`)` 将其激活为快捷键接收模式，再按下 `%` ，即可将当前窗口切分为左右两个窗格。

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560156885/gowhich/gw_981_1.png)

## 快捷键

一般情况下 tmux 中所有的快捷键都需要和前缀快捷键 `⌃b` 来组合使用（注：⌃ 为 Mac 的 control 键），以下是常用的窗格（pane）快捷键列表，大家可以依次尝试下：

### 窗格操作

* `%` 左右平分出两个窗格
* `"` 上下平分出两个窗格
* `x` 关闭当前窗格
* `{` 当前窗格前移
* `}` 当前窗格后移
* `;` 选择上次使用的窗格
* `o` 选择下一个窗格，也可以使用上下左右方向键来选择
* `space` 切换窗格布局，tmux 内置了五种窗格布局，也可以通过 `⌥1` 至 `⌥5`来切换
* `z` 最大化当前窗格，再次执行可恢复原来大小
* `q` 显示所有窗格的序号，在序号出现期间按下对应的数字，即可跳转至对应的窗格

### 窗口操作

* `c` 新建窗口，此时当前窗口会切换至新窗口，不影响原有窗口的状态
* `p` 切换至上一窗口
* `n` 切换至下一窗口
* `w` 窗口列表选择，注意 macOS 下使用 `⌃p` 和 `⌃n` 进行上下选择
* `&` 关闭当前窗口
* `,` 重命名窗口，可以使用中文，重命名后能在 tmux 状态栏更快速的识别窗口 id
* `0` 切换至 0 号窗口，使用其他数字 id 切换至对应窗口
* `f` 根据窗口名搜索选择窗口，可模糊匹配

### 会话操作

* `$` 重命名当前会话
* `s` 选择会话列表
* `d` detach 当前会话，运行后将会退出 tmux 进程，返回至 shell 主进程，可以使用attach tmux attach恢复所有窗口

在 shell 主进程下运行以下命令可以操作 tmux 会话：

```bash
tmux new -s foo # 新建名称为 foo 的会话
tmux ls # 列出所有 tmux 会话
tmux a # 恢复至上一次的会话
tmux a -t foo # 恢复名称为 foo 的会话，会话默认名称为数字
tmux kill-session -t foo # 删除名称为 foo 的会话
tmux kill-server # 删除所有的会话
```
