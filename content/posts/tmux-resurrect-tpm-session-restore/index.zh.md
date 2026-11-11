+++
title = "使用 Tmux-Resurrect 与 TPM 实现 Tmux 会话持久化与恢复"
date = 2026-11-11T14:30:00+08:00
lastmod = 2026-11-11T14:30:00+08:00
description = "详细介绍如何通过 Tmux Plugin Manager（TPM）安装 tmux-resurrect 和 tmux-continuum，实现 Tmux 会话保存、手动恢复与自动恢复，并解决插件未加载和快捷键失效等常见问题。"
slug = "tmux-resurrect-tpm-session-restore"
image = "./cover.png"
image_alt = "Tmux terminal showing multiple split panes and restored development sessions"
toc = true
draft = false
tags = ["tmux", "linux", "terminal", "development-tools"]
categories = ["Development", "Linux"]
+++

在日常开发过程中，Tmux 是一个非常实用的终端复用工具。通过 Session、Window 和 Pane，我们可以将不同的开发任务组织在同一个终端环境中，同时保持各个任务之间相互独立。

然而，Tmux 默认并不会将当前会话状态持久化到磁盘。一旦服务器重启、Tmux 服务被意外终止，或者手动执行了 `tmux kill-server`，原本创建的会话、窗口布局以及工作目录就可能全部丢失。

如果每次重启都需要重新创建 Session、拆分 Pane 并切换到对应的项目目录，无疑会影响开发效率。

本文介绍如何通过 **TPM（Tmux Plugin Manager）** 安装和管理 `tmux-resurrect`，并配合 `tmux-continuum` 实现自动保存与恢复，从而减少重复配置终端环境的工作。

<!--more-->

## 一、认识 Tmux-Resurrect 与 Tmux-Continuum

在开始配置之前，先了解这两个插件各自负责什么。

### 1. tmux-resurrect：手动保存与恢复

[tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) 是一个用于持久化 Tmux 环境的插件。

它可以保存和恢复以下信息：

- 所有 Session、Window 和 Pane。
- Window 和 Pane 的排列顺序。
- 每个 Pane 当前的工作目录（CWD）。
- 窗口内部的 Pane 布局，包括缩放状态。
- 当前激活的 Session、Window 和 Pane。
- 部分支持的运行中程序。
- 可选恢复 Vim / Neovim 会话和 Pane 历史内容。

默认提供两个快捷键：

| 快捷键 | 功能 |
|---|---|
| `Prefix + Ctrl-s` | 保存当前 Tmux 环境 |
| `Prefix + Ctrl-r` | 恢复上一次保存的环境 |

其中，`Prefix` 默认是 `Ctrl + b`，但如果你修改过 Tmux 的前缀键，请使用自己的配置。

### 2. tmux-continuum：自动保存与恢复

[tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) 是建立在 `tmux-resurrect` 之上的自动化插件。

它主要提供两个功能：

- **自动保存**：默认每隔 15 分钟保存一次 Tmux 环境。
- **自动恢复**：在 Tmux Server 启动时，自动恢复最近一次保存的环境。

两者的关系可以简单理解为：

- `tmux-resurrect` 负责保存和恢复。
- `tmux-continuum` 负责定期触发保存，以及在 Tmux Server 启动时触发恢复。

如果只需要手动保存和恢复，安装 `tmux-resurrect` 即可。如果希望服务器重启后自动恢复，建议同时安装这两个插件。

## 二、问题排查：为什么恢复快捷键没有反应？

在实际配置过程中，有些用户会直接在 `~/.tmux.conf` 中添加插件声明：

```tmux
set -g @plugin 'tmux-plugins/tmux-resurrect'
```

然后尝试按下：

```text
Ctrl + b
Ctrl + r
```

但 Tmux 并没有任何反应。

这通常是因为 **TPM 尚未安装、初始化，或者插件尚未真正安装**。

需要注意的是，下面这条配置：

```tmux
set -g @plugin 'tmux-plugins/tmux-resurrect'
```

只是告诉 TPM 需要管理哪个插件，并不会自动下载或加载插件。

TPM 本身也需要先安装到本地，然后通过配置文件中的初始化命令加载。最后还需要执行插件安装操作，才能真正使用 `tmux-resurrect`。

因此，完整流程是：

1. 安装 TPM。
2. 在 `~/.tmux.conf` 中声明插件。
3. 初始化 TPM。
4. 使用 TPM 安装插件。

下面按照这个顺序完成配置。

## 三、安装 TPM 与配置插件

### 1. 安装 Tmux Plugin Manager

首先，确保系统已经安装 Git 和 Tmux。

检查版本：

```bash
tmux -V
git --version
```

然后执行以下命令，将 TPM 克隆到默认插件目录：

```bash
git clone https://github.com/tmux-plugins/tpm.git ~/.tmux/plugins/tpm
```

安装完成后，可以检查目录：

```bash
ls -la ~/.tmux/plugins/tpm
```

如果能够看到 TPM 的相关文件，说明克隆成功。

### 2. 配置 ~/.tmux.conf

打开 Tmux 配置文件：

```bash
vim ~/.tmux.conf
```

如果文件不存在，可以直接创建。

添加以下配置：

```tmux
# ==========================================
# TPM Plugin Manager
# ==========================================

# Plugin declarations
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# ==========================================
# Tmux Resurrect
# ==========================================

# Restore pane contents (optional)
set -g @resurrect-capture-pane-contents 'on'

# ==========================================
# Tmux Continuum
# ==========================================

# Enable automatic restoration
set -g @continuum-restore 'on'

# Save the environment every 15 minutes (default)
set -g @continuum-save-interval '15'

# ==========================================
# Initialize TPM
# Keep this line at the very bottom!
# ==========================================

run '~/.tmux/plugins/tpm/tpm'
```

**配置说明：**

- `@plugin`：声明需要 TPM 管理的插件。
- `@resurrect-capture-pane-contents`：启用 Pane 历史内容的保存与恢复。
- `@continuum-restore`：启用 Tmux Server 启动时的自动恢复。
- `@continuum-save-interval`：设置自动保存间隔，单位为分钟。
- `run '~/.tmux/plugins/tpm/tpm'`：初始化 TPM。

特别注意：TPM 初始化命令必须放在配置文件的最后面，确保插件声明和相关选项先被读取。

### 3. 重新加载 Tmux 配置

保存配置文件后，进入正在运行的 Tmux 会话。

按下：

```text
Ctrl + b
:
```

进入 Tmux 命令模式，输入：

```bash
source-file ~/.tmux.conf
```

也可以直接在终端执行：

```bash
tmux source-file ~/.tmux.conf
```

此时 TPM 已经读取插件声明，但插件还没有真正下载和安装。

### 4. 使用 TPM 安装插件

这是整个过程中最关键的一步。

在 Tmux 会话中，按下：

```text
Ctrl + b
Shift + i
```

这里的 `I` 是大写字母 I，而不是小写字母 `i`。

TPM 会自动下载并加载配置文件中声明的插件。

等待安装完成，直到状态栏出现：

```text
Plugin(s) installed!
```

至此，`tmux-resurrect` 和 `tmux-continuum` 就已经安装完成。

## 四、验证会话保存与恢复

完成安装后，建议先测试手动保存与恢复功能，再验证自动恢复。

### 1. 手动保存当前会话

在 Tmux 中按下：

```text
Ctrl + b
Ctrl + s
```

如果插件工作正常，屏幕下方会出现：

```text
Tmux environment saved!
```

默认保存目录为：

```bash
~/.tmux/resurrect/
```

可以通过以下命令查看保存文件：

```bash
ls -lah ~/.tmux/resurrect/
```

通常可以看到以 `last` 结尾的状态文件，以及对应的时间戳备份文件。

### 2. 手动恢复会话

重新启动 Tmux 后，按下：

```text
Ctrl + b
Ctrl + r
```

如果恢复成功，状态栏会提示：

```text
Restoring tmux environment...
```

稍等片刻，之前保存的 Session、Window、Pane 布局以及工作目录就会重新出现。

### 3. 测试 Tmux Server 重启

如果希望验证会话是否真的可以跨 Tmux Server 重启恢复，可以执行以下测试：

**第一步：保存当前环境**

```bash
tmux
```

在 Tmux 中按下：

```text
Ctrl + b
Ctrl + s
```

确认保存成功。

**第二步：退出并终止 Tmux Server**

在普通终端中执行：

```bash
tmux kill-server
```

注意：这会终止当前 Tmux Server 下的所有会话，请确保已经保存需要恢复的状态。

**第三步：重新启动 Tmux**

```bash
tmux
```

如果只安装了 `tmux-resurrect`，需要手动执行：

```text
Ctrl + b
Ctrl + r
```

如果同时安装了 `tmux-continuum` 并启用了自动恢复，则在 Tmux Server 启动时会自动尝试恢复最近一次保存的环境。

注意：`tmux-continuum` 不会自动启动操作系统层面的 Tmux 进程。服务器重启后，仍然需要通过登录、Shell 配置或 systemd 等方式启动 Tmux Server，自动恢复功能才会触发。

## 五、常见问题排查

### 1. 按下 Prefix + I 没有反应

首先确认：

- TPM 是否已经克隆到 `~/.tmux/plugins/tpm`。
- `~/.tmux.conf` 中是否包含 TPM 初始化命令。
- 是否已经重新加载 Tmux 配置。
- 是否按下了大写字母 `I`，而不是小写字母 `i`。

也可以检查 TPM 文件是否存在：

```bash
ls ~/.tmux/plugins/tpm/tpm
```

### 2. Ctrl + s 或 Ctrl + r 没有反应

首先检查插件是否已经安装：

```bash
ls ~/.tmux/plugins/
```

确认其中是否存在：

```text
tpm/
tmux-resurrect/
tmux-continuum/
```

如果插件目录不存在，重新执行：

```text
Prefix + I
```

如果插件已经存在，但快捷键仍然没有反应，可以检查是否存在快捷键冲突：

```bash
tmux list-keys | grep -E 'C-s|C-r'
```

另外，部分终端环境可能会将 `Ctrl + s` 作为终端流控快捷键（XON/XOFF），导致按键被终端拦截。

可以在 Shell 中执行：

```bash
stty -ixon
```

如果希望永久生效，可以将该命令添加到 `~/.bashrc` 或 `~/.zshrc`。

### 3. 自动恢复没有生效

如果手动恢复正常，但自动恢复没有生效，请重点检查：

- 是否安装了 `tmux-continuum`。
- 是否配置了 `set -g @continuum-restore 'on'`。
- 是否已经成功安装并加载两个插件。
- 是否真正重新启动了 Tmux Server。

特别注意：重新执行 `source-file ~/.tmux.conf` 并不会触发自动恢复。`tmux-continuum` 只会在 Tmux Server 启动时执行自动恢复。

此外，自动保存依赖 Tmux Status Line 处于启用状态。如果其他插件覆盖了 `status-right` 配置，可能导致自动保存失效。可以尝试将 `tmux-continuum` 放在 TPM 插件列表的最后。

### 4. 找不到保存的会话文件

检查默认保存目录：

```bash
ls -lah ~/.tmux/resurrect/
```

如果目录不存在，先尝试手动保存：

```text
Prefix + Ctrl + s
```

同时检查当前用户是否具有该目录的读写权限。

## 六、Tmux-Resurrect 的能力边界

虽然 `tmux-resurrect` 可以恢复大部分 Tmux 环境，但它并不是一个完整的进程快照工具。

需要明确以下几点：

**可以恢复的内容：**

- Session、Window 和 Pane 结构。
- Pane 的排列布局。
- 工作目录。
- 当前活动窗口和 Pane。
- 部分受支持的终端程序。
- 可选的 Pane 历史内容。

**不能保证完整恢复的内容：**

- 所有正在运行的进程及其内部运行状态。
- 未保存的程序内存数据。
- 已断开的数据库连接或 SSH 连接。
- 正在执行的复杂交互式脚本。
- 程序内部的实时状态，例如尚未保存的编辑内容。

对于 Vim / Neovim 用户，可以进一步配置 `tmux-resurrect` 的编辑器会话恢复功能，利用编辑器自身的 Session 机制恢复文件和窗口状态。

因此，更准确地说，`tmux-resurrect` 恢复的是终端工作环境，而不是对所有应用程序进行完整的运行状态冻结。

## 七、总结

通过 TPM、`tmux-resurrect` 和 `tmux-continuum`，我们可以为 Tmux 建立一套简单而实用的会话持久化机制。

三者的职责分别是：

| 组件 | 主要职责 |
|---|---|
| TPM | 安装、管理和加载 Tmux 插件 |
| tmux-resurrect | 手动保存与恢复 Tmux 环境 |
| tmux-continuum | 定期自动保存与启动时自动恢复 |

对于经常使用 SSH 连接远程服务器、同时维护多个项目或需要长时间运行开发环境的用户，这套组合可以有效减少重复创建终端会话的工作。

**最后提醒：** 如果你的工作环境非常重要，建议定期检查 `~/.tmux/resurrect/` 中的保存文件，并将关键配置文件纳入 Git 管理。插件提供的是便利的会话恢复能力，不应替代真正的数据备份。

## 参考资料

- [Tmux Plugin Manager (TPM)](https://github.com/tmux-plugins/tpm)
- [Tmux Resurrect](https://github.com/tmux-plugins/tmux-resurrect)
- [Tmux Continuum](https://github.com/tmux-plugins/tmux-continuum)
