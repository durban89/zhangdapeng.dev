+++
title = "从零搭建 Antigravity 开发环境：Ubuntu VPS + Linux Desktop + tmux"

description = "记录如何使用 Ubuntu VPS 搭建完整的 Antigravity AI 开发环境，通过 XFCE、XRDP、Tailscale、Zsh、Node.js 和 tmux 构建稳定、可长期运行的远程 AI 开发工作站。"

summary = "使用 Ubuntu VPS、XFCE、XRDP、Tailscale 和 tmux，搭建一个稳定、安全且可长期运行的 Antigravity AI 开发环境。"

date = 2026-08-18T12:00:00+09:00
lastmod = 2026-08-18T12:00:00+09:00

draft = false

slug = "build-antigravity-development-environment"

categories = [
    "AI Development",
    "Linux"
]

tags = [
    "Antigravity",
    "AI Coding",
    "Ubuntu",
    "VPS",
    "Linux Desktop",
    "tmux",
    "Tailscale",
    "XRDP",
    "Remote Development"
]

keywords = [
    "Antigravity",
    "Antigravity CLI",
    "Ubuntu VPS",
    "AI Coding",
    "AI Development Environment",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "tmux",
    "Remote Development"
]

series = [
    "AI Development Environment"
]

image = "cover.webp"

images = [
    "cover.webp"
]

[article]
toc = true
readingTime = true
+++

# 从零搭建 Antigravity 开发环境：Ubuntu VPS + Linux Desktop + tmux + 云端工作流

> 一套适合独立开发者的 Antigravity 开发环境搭建记录。

## 前言

作为一名独立开发者，我一直在寻找一种更加稳定、独立的 AI 编程环境。

本地电脑虽然方便，但也存在一些问题：

* 本地网络环境可能影响 AI 服务的访问
* Google Gemini / Antigravity 等服务可能存在区域限制
* 本地电脑关机后，AI 编程任务无法继续运行
* CLI 会话容易因为终端关闭而中断
* 开发环境迁移和备份比较麻烦

因此，我最终选择搭建一台长期使用的 Linux VPS，并在 VPS 上配置完整的桌面环境，通过远程桌面连接进行开发。

最终的架构大致如下：

```text
本地电脑
    │
    │ Tailscale / RDP / SSH
    ▼
Ubuntu VPS
    │
    ├── XFCE Desktop
    ├── XRDP
    ├── Zsh
    ├── Node.js
    ├── Git
    ├── tmux
    └── Antigravity CLI
            │
            ▼
      AI Coding Workflow
```

这篇文章记录整个搭建过程，以及过程中遇到的一些问题。

---

# 1. 为什么选择 VPS 而不是本地运行？

最开始，我是在本地 Linux 环境中尝试使用 Gemini CLI 和 Antigravity。

但是很快遇到了几个问题。

## 1.1 区域限制

部分 AI 服务会根据以下信息判断用户所在地区：

* IP 地址
* Google Account 地区
* Google Play 国家或地区
* 账号历史信息
* 登录环境

即使更换网络，也不一定能够完全解决问题。

因此，我希望使用一个更加稳定的海外 Linux 环境作为长期开发环境。

---

## 1.2 让开发环境独立运行

使用 VPS 的最大优势之一，就是：

> 开发环境不再依赖本地电脑。

即使关闭自己的电脑：

* Git 项目仍然保留在 VPS
* tmux 会话仍然运行
* AI CLI 不会因为 SSH 断开而立即终止
* 可以随时从其他设备重新连接

对于独立开发者来说，这种体验非常方便。

---

# 2. 选择 Ubuntu VPS

最终我选择了一台 Ubuntu VPS。

主要考虑以下几个因素：

* 价格相对便宜
* 可以长期运行
* 支持 SSH
* 可以安装 Linux Desktop
* 可以运行 Node.js
* 可以运行 AI Coding CLI
* 可以通过 Tailscale 建立安全的私有网络

系统选择 Ubuntu。

Ubuntu 的优点是：

* 软件生态成熟
* 文档非常多
* Node.js、Git、Docker 等开发工具支持完善
* 大多数 AI CLI 都优先支持 Linux

---

# 3. 安装 Linux Desktop

VPS 默认通常只有命令行环境。

为了获得更加接近本地电脑的体验，我在 VPS 上安装了 XFCE Desktop。

安装：

```bash
sudo apt update
sudo apt install xfce4 xfce4-goodies -y
```

XFCE 非常适合 VPS 环境。

相比 GNOME 或 KDE：

* 占用资源更少
* 对低配置 VPS 更友好
* 远程桌面体验不错
* 稳定性较高

---

# 4. 安装 XRDP

安装 XRDP：

```bash
sudo apt install xrdp -y
```

启动并设置开机启动：

```bash
sudo systemctl enable xrdp
sudo systemctl start xrdp
```

检查状态：

```bash
systemctl status xrdp
```

如果看到：

```text
active (running)
```

说明 XRDP 已经正常运行。

XRDP 默认监听：

```text
3389
```

端口。

---

# 5. 使用 Tailscale 保护 VPS

直接暴露 RDP 端口到公网并不是一个理想方案。

因此，我选择使用 Tailscale。

Tailscale 可以让：

```text
本地电脑
      │
      │ 私有加密网络
      ▼
VPS
```

设备之间直接建立安全连接。

安装完成后，可以查看状态：

```bash
tailscale status
```

获取当前设备 IP：

```bash
tailscale ip
```

之后可以通过 Tailscale IP 使用：

* SSH
* RDP
* 其他内部服务

这样就不需要直接暴露 RDP 到公网。

---

# 6. 安装 Zsh

为了获得更好的终端体验，我使用 Zsh。

安装：

```bash
sudo apt install zsh -y
```

设置默认 Shell：

```bash
chsh -s $(which zsh)
```

重新登录后检查：

```bash
echo $SHELL
```

应该看到类似：

```text
/usr/bin/zsh
```

---

# 7. 安装 Node.js

Antigravity CLI 依赖 Node.js 环境。

我使用 NVM 管理 Node.js。

安装 NVM 后，可以安装 Node.js：

```bash
nvm install 22
```

检查：

```bash
node -v
npm -v
```

我的环境中使用的是：

```text
Node.js v22.x
```

建议使用 NVM 管理 Node.js，而不是直接通过系统包管理器安装。

原因是：

* 可以安装多个 Node.js 版本
* 可以快速切换版本
* 不会污染系统环境
* 更适合开发环境

---

# 8. 安装 Antigravity CLI

在 Node.js 环境准备完成之后，就可以安装 Antigravity CLI。

安装完成后，可以检查：

```bash
antigravity --version
```

如果终端提示：

```text
command not found
```

通常需要检查：

```bash
which antigravity
```

以及：

```bash
echo $PATH
```

如果通过 npm 全局安装，也可以检查：

```bash
npm root -g
npm config get prefix
```

常见问题通常来自：

* Node.js 环境没有加载
* NVM 没有在 `.zshrc` 中初始化
* npm 全局 bin 路径没有加入 `$PATH`

---

# 9. 使用 tmux 保持 Antigravity 会话

这是整个环境中非常重要的一部分。

如果直接通过 SSH 或远程终端运行：

```bash
antigravity
```

一旦：

* 网络断开
* SSH 关闭
* 本地电脑休眠
* RDP 连接中断

可能导致终端任务受到影响。

因此，我使用 tmux。

安装：

```bash
sudo apt install tmux -y
```

创建一个新的会话：

```bash
tmux new -s antigravity
```

然后启动 Antigravity：

```bash
antigravity
```

---

## 9.1 退出 tmux 但保持程序运行

按：

```text
Ctrl + B
```

然后按：

```text
D
```

即可 Detach 当前 tmux。

此时：

```text
SSH 关闭
RDP 关闭
本地电脑关闭
```

tmux 内部的程序仍然继续运行。

---

## 9.2 查看 tmux 会话

```bash
tmux ls
```

例如：

```text
antigravity: 1 windows
```

重新连接：

```bash
tmux attach -t antigravity
```

这样就可以恢复之前的工作环境。

---

# 10. 推荐的 Antigravity 工作流

我目前比较推荐以下结构。

```text
~/projects
│
├── project-a
│   ├── tmux
│   └── antigravity
│
├── project-b
│   ├── tmux
│   └── antigravity
│
└── project-c
    ├── tmux
    └── antigravity
```

每个项目使用独立的 tmux Session。

例如：

```bash
tmux new -s project-a
```

进入项目：

```bash
cd ~/projects/project-a
```

然后运行：

```bash
antigravity
```

这样不同项目之间不会互相干扰。

查看所有 Session：

```bash
tmux ls
```

重新进入：

```bash
tmux attach -t project-a
```

---

# 11. Antigravity CLI 会话管理

在使用 AI Coding CLI 时，一个非常容易忽略的问题就是：

> CLI 会话记录通常不应该只依赖本地缓存。

因为 VPS 可能：

* 被误删除
* 系统损坏
* 重装系统
* 更换服务器

因此建议定期备份。

例如：

```text
~/.cache/
~/.config/
~/.local/
```

以及项目目录：

```text
~/projects/
```

根据 Antigravity 实际的数据存储位置，可以将相关目录加入备份脚本。

例如：

```bash
tar -czf antigravity-backup.tar.gz \
~/.cache/antigravity \
~/projects
```

然后将备份上传到安全的云端存储。

---

# 12. 推荐的目录结构

我的 VPS 开发环境建议按照下面的方式组织：

```text
/home/daniel
│
├── projects
│   ├── PulseTimer
│   ├── IndieResizer
│   └── UnixTimestampConverter
│
├── backups
│
├── scripts
│
└── workspace
```

这样会比较清晰。

例如：

```bash
mkdir -p ~/projects
mkdir -p ~/backups
mkdir -p ~/scripts
mkdir -p ~/workspace
```

---

# 13. 自动备份思路

可以创建一个简单的备份脚本：

```bash
nano ~/scripts/backup.sh
```

示例：

```bash
#!/bin/bash

BACKUP_DIR="$HOME/backups"

mkdir -p "$BACKUP_DIR"

tar -czf \
"$BACKUP_DIR/projects-$(date +%F).tar.gz" \
"$HOME/projects"
```

增加执行权限：

```bash
chmod +x ~/scripts/backup.sh
```

手动执行：

```bash
~/scripts/backup.sh
```

之后可以通过：

```bash
crontab -e
```

设置每天自动备份。

例如每天凌晨 3 点：

```cron
0 3 * * * /home/daniel/scripts/backup.sh
```

---

# 14. 常见问题

## 14.1 `command not found: antigravity`

首先检查：

```bash
which antigravity
```

然后检查 Node.js：

```bash
node -v
npm -v
```

如果使用 NVM，需要确认 `.zshrc` 中已经加载：

```bash
export NVM_DIR="$HOME/.nvm"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

重新加载：

```bash
source ~/.zshrc
```

---

## 14.2 如何确认当前是否在 tmux？

执行：

```bash
echo $TMUX
```

如果返回类似：

```text
/tmp/tmux-1000/default,12345,0
```

说明当前正在 tmux 中。

如果没有任何输出，则通常不在 tmux Session 中。

---

## 14.3 tmux 如何恢复会话？

查看：

```bash
tmux ls
```

恢复：

```bash
tmux attach -t session-name
```

例如：

```bash
tmux attach -t antigravity
```

---

# 15. 最终架构

最终，我的开发环境大致如下：

```text
┌───────────────────────────────┐
│          本地电脑             │
│                               │
│  Browser / VS Code / Terminal │
└───────────────┬───────────────┘
                │
                │ Tailscale
                ▼
┌───────────────────────────────┐
│          Ubuntu VPS           │
│                               │
│  ┌─────────────────────────┐  │
│  │       XFCE Desktop      │  │
│  └─────────────────────────┘  │
│                               │
│  ┌─────────────────────────┐  │
│  │          XRDP           │  │
│  └─────────────────────────┘  │
│                               │
│  ┌─────────────────────────┐  │
│  │          Zsh            │  │
│  │          Node.js        │  │
│  │          Git            │  │
│  │          tmux           │  │
│  └─────────────┬───────────┘  │
│                │              │
│                ▼              │
│       Antigravity CLI         │
│                │              │
│                ▼              │
│          AI Development       │
└───────────────────────────────┘
```

---

# 总结

通过 VPS + Linux Desktop + Tailscale + tmux，我最终搭建了一套相对独立的 AI 开发环境。

这套环境最大的优势是：

* VPS 长期运行
* 开发环境与本地电脑分离
* 可以从多个设备访问
* tmux 可以保持 CLI 会话
* Tailscale 可以减少公网暴露
* 项目和开发环境可以统一管理
* 可以通过脚本自动备份

对于独立开发者来说，这种模式非常适合作为长期的开发工作站。

最终，你得到的并不仅仅是一台 VPS。

而是一个：

> **可以随时访问、长期运行、独立维护，并且可以持续扩展的 AI Development Workspace。**

未来还可以继续加入：

* Docker
* k3s
* GitHub Actions
* 自动部署
* HTTPS
* CI/CD
* 云端备份
* 多项目 AI Agent
* 自动化开发工作流

让这台 VPS 从单纯的远程服务器，逐渐变成属于自己的 **个人 AI 开发基础设施**。
