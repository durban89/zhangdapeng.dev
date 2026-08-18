+++

title = "从零搭建个人云端开发桌面：Vultr VPS + XFCE + XRDP + Tailscale + Remmina"

description = "记录如何使用 Vultr Ubuntu VPS 搭建轻量级 Linux 远程桌面，通过 XFCE、XRDP、Tailscale 和 Remmina 构建安全、稳定且可长期使用的个人云端开发工作站。"

summary = "使用 Vultr VPS、Ubuntu、XFCE、XRDP、Tailscale 和 Remmina，搭建一个安全、轻量且可长期使用的个人云端 Linux 开发桌面。"

date = 2026-08-18T12:00:00+09:00

lastmod = 2026-08-18T12:00:00+09:00

draft = false

slug = "build-personal-cloud-development-desktop"

categories = [
    "Linux",
    "Remote Development"
]

tags = [
    "Vultr",
    "Ubuntu",
    "VPS",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "Remmina",
    "Remote Desktop",
    "Remote Development"
]

keywords = [
    "Vultr VPS",
    "Ubuntu VPS",
    "Linux Remote Desktop",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "Remmina",
    "Remote Desktop",
    "Cloud Development",
    "Cloud Development Environment",
    "Remote Development",
    "Personal Development Environment"
]

series = [
    "Remote Development Environment"
]

image = "cover.webp"

images = [
    "cover.webp"
]

[article]

toc = true

readingTime = true

+++



# 从零搭建 Ubuntu VPS 远程桌面：Vultr + XFCE + XRDP + Tailscale + Remmina

> 使用 Vultr VPS 搭建一台 Linux 云端桌面，并通过 Tailscale + XRDP + Remmina 实现安全的远程访问。

作为独立开发者，我经常需要一台稳定的 Linux 环境来进行开发、测试和运行各种工具。

相比直接在本地电脑上配置复杂的开发环境，我更希望拥有一台：

* 随时可以访问
* 可以运行完整 Linux 桌面
* 可以安装浏览器和开发工具
* 不需要暴露远程桌面端口到公网
* 支持多设备访问

的云端开发环境。

最终，我选择了下面这套方案：

```text
本地 Linux / Windows / macOS
            │
            │
        Remmina
            │
            │
        Tailscale
            │
            │
      ┌──────────────┐
      │   Vultr VPS  │
      │              │
      │ Ubuntu Linux │
      │     +        │
      │    XFCE      │
      │     +        │
      │    XRDP      │
      └──────────────┘
```

整个方案的核心是：

> **Vultr 提供 VPS，Ubuntu 提供系统环境，XFCE 提供轻量级桌面，XRDP 提供远程桌面协议，Tailscale 负责安全网络连接，Remmina 作为远程桌面客户端。**

---

# 一、为什么选择 VPS + 远程桌面

传统 VPS 通常只提供 SSH 终端。

例如：

```bash
ssh root@your-server-ip
```

这种方式对于服务器管理已经足够，但如果需要运行：

* Google Chrome
* Claude
* Gemini
* Antigravity
* VS Code
* GUI 开发工具
* 浏览器插件测试
* 图形化 Git 工具

仅靠 SSH 就不够方便了。

因此，我们需要给 VPS 安装一个完整的 Linux 桌面环境。

最终的结构如下：

```text
VPS
│
├── Ubuntu
│
├── XFCE Desktop
│
├── XRDP
│
└── Tailscale
```

本地电脑通过：

```text
Remmina
    ↓
Tailscale 私有网络
    ↓
XRDP
    ↓
XFCE Desktop
```

连接到 VPS。

---

# 二、创建 Vultr Ubuntu VPS

首先创建一台 Vultr VPS。

系统可以选择 Ubuntu LTS。

例如：

```text
Ubuntu 26.04 LTS
```

创建完成后，可以先通过 SSH 登录服务器。

```bash
ssh root@your-server-ip
```

登录后先更新系统：

```bash
apt update
apt upgrade -y
```

如果使用普通用户，也可以：

```bash
sudo apt update
sudo apt upgrade -y
```

---

# 三、安装 XFCE 桌面环境

对于 VPS 来说，并不建议安装 GNOME 或 KDE。

因为这些桌面环境通常比较重，会占用更多：

* 内存
* CPU
* GPU 资源

对于只有 1～2GB 内存的小型 VPS，XFCE 是一个比较合适的选择。

安装 XFCE：

```bash
sudo apt install xfce4 xfce4-goodies -y
```

安装过程中可能会出现显示管理器选择。

如果需要选择，可以使用：

```text
lightdm
```

XFCE 的特点：

* 占用资源较低
* 启动速度快
* 比较适合 VPS
* 远程桌面体验不错

安装完成后，服务器已经具备基本的 Linux 桌面环境。

---

# 四、安装 XRDP

XRDP 可以让 Linux VPS 支持微软 RDP 协议。

安装：

```bash
sudo apt install xrdp -y
```

安装完成后启动服务：

```bash
sudo systemctl enable xrdp
sudo systemctl start xrdp
```

检查服务状态：

```bash
sudo systemctl status xrdp
```

如果看到：

```text
active (running)
```

说明 XRDP 已经正常运行。

---

# 五、配置 XRDP 使用 XFCE

默认情况下，XRDP 有时不会正确启动 XFCE 桌面。

可以在用户目录创建：

```bash
nano ~/.xsession
```

写入：

```bash
startxfce4
```

保存后赋予执行权限：

```bash
chmod +x ~/.xsession
```

然后重新启动 XRDP：

```bash
sudo systemctl restart xrdp
```

这样，当远程桌面登录时，XRDP 就会启动 XFCE。

---

# 六、不要直接暴露 3389 端口

XRDP 默认使用：

```text
3389
```

理论上可以直接：

```text
你的电脑
   ↓
公网 IP
   ↓
VPS:3389
```

但是这样存在明显的安全问题。

公网扫描器经常扫描：

```text
3389
22
3306
6379
```

如果直接暴露 RDP 端口，可能会遇到：

* 暴力破解
* 密码猜测
* 漏洞扫描
* 恶意登录尝试

因此，我没有直接把 XRDP 暴露到公网。

而是使用：

> **Tailscale**

---

# 七、安装 Tailscale

Tailscale 基于 WireGuard，可以帮助不同设备建立一个私有网络。

安装：

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

然后登录：

```bash
sudo tailscale up
```

终端会提供一个登录地址。

使用浏览器登录自己的 Tailscale 账号。

登录完成后，查看 VPS 的 Tailscale IP：

```bash
tailscale ip
```

可能会得到：

```text
100.x.x.x
```

这个地址属于 Tailscale 私有网络。

---

# 八、配置安全网络结构

完成之后：

```text
┌─────────────────┐
│   本地电脑       │
│                 │
│  Tailscale      │
└────────┬────────┘
         │
         │ WireGuard 加密
         │
         ▼
┌─────────────────┐
│    Tailscale    │
│   Private Mesh  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Vultr VPS    │
│                 │
│  Tailscale IP   │
│   100.x.x.x     │
│                 │
│      XRDP       │
│       :3389     │
│                 │
│      XFCE       │
└─────────────────┘
```

此时：

XRDP 不需要直接暴露给公网。

本地设备和 VPS 都加入同一个 Tailscale 网络。

只有经过授权的设备才能访问 VPS。

---

# 九、本地安装 Remmina

如果你的本地电脑也是 Ubuntu 或其他 Linux 系统，可以使用 Remmina。

安装：

```bash
sudo apt install remmina -y
```

启动：

```bash
remmina
```

创建新的远程桌面连接。

协议选择：

```text
RDP
```

服务器填写：

```text
100.x.x.x
```

注意：

这里填写的是 VPS 的 **Tailscale IP**。

例如：

```text
100.64.12.34
```

用户名：

```text
你的 Linux 用户名
```

密码：

```text
Linux 用户密码
```

然后点击连接。

---

# 十、连接结构

整个连接过程如下：

```text
Remmina
    │
    │ RDP
    ▼
Tailscale Network
    │
    │ Encrypted
    ▼
Vultr VPS
    │
    ▼
XRDP
    │
    ▼
XFCE Desktop
```

最终效果就是：

> 你在本地电脑上打开 Remmina，就像连接一台远程 Windows 电脑一样，直接进入 VPS 的 Ubuntu 桌面。

---

# 十一、常见问题

## 1. XRDP 无法连接

首先检查服务：

```bash
sudo systemctl status xrdp
```

如果没有启动：

```bash
sudo systemctl restart xrdp
```

然后检查端口：

```bash
sudo ss -tulpn | grep 3389
```

正常情况下应该看到：

```text
LISTEN
```

---

## 2. Remmina 显示连接失败

首先确认 Tailscale 是否正常。

本地：

```bash
tailscale status
```

VPS：

```bash
tailscale status
```

然后测试：

```bash
ping 100.x.x.x
```

如果无法 Ping 通，通常是：

* Tailscale 没有登录
* 设备不在同一个 Tailnet
* ACL 限制
* 网络连接异常

---

## 3. 登录后黑屏

可以检查：

```bash
~/.xsession
```

内容应该是：

```bash
startxfce4
```

然后重新启动：

```bash
sudo systemctl restart xrdp
```

必要时重新连接。

---

## 4. VPS 内存不足

如果 VPS 配置较低，例如：

```text
1 GB RAM
```

安装完整桌面后可能会比较吃力。

可以查看内存：

```bash
free -h
```

如果内存不足，可以增加 Swap。

查看 Swap：

```bash
swapon --show
```

如果已经有 Swap：

```text
Memory: 1.6Gi
Swap:   5.8Gi
```

对于轻量级开发环境通常可以正常使用。

---

# 十二、为什么选择 XFCE

常见 Linux 桌面对比如下：

| 桌面环境       | 资源占用 | VPS 推荐程度 |
| ---------- | ---- | -------- |
| GNOME      | 高    | ⭐⭐       |
| KDE Plasma | 中等   | ⭐⭐⭐      |
| XFCE       | 低    | ⭐⭐⭐⭐⭐    |
| LXQt       | 很低   | ⭐⭐⭐⭐     |

我的选择是：

```text
XFCE
```

原因很简单：

```text
轻量
稳定
速度快
适合远程桌面
```

对于 VPS 来说，不需要复杂的桌面动画。

更重要的是：

> **稳定、响应快、占用资源少。**

---

# 十三、最终环境

最终我的 VPS 环境如下：

```text
Vultr VPS
│
├── Ubuntu 26.04 LTS
│
├── XFCE Desktop
│
├── XRDP
│
├── Tailscale
│
├── Node.js
│
├── Git
│
├── Zsh
│
├── tmux
│
└── Chrome / Development Tools
```

本地：

```text
Linux Desktop
│
├── Remmina
│
└── Tailscale
```

---

# 十四、总结

这套方案的核心不是单纯搭建一个 Linux VPS。

而是搭建一台真正可以长期使用的：

> **Cloud Development Desktop**

整体架构：

```text
Local Computer
       │
       ▼
    Remmina
       │
       ▼
   Tailscale
       │
       ▼
    Vultr VPS
       │
       ▼
      XRDP
       │
       ▼
   XFCE Desktop
```

相比直接暴露 RDP 端口：

```text
公网
  ↓
VPS:3389
```

使用 Tailscale：

```text
Authorized Device
        ↓
Encrypted Private Network
        ↓
       VPS
```

安全性更高，也更适合个人开发者长期使用。

如果你和我一样，希望拥有一台：

* 随时可以访问
* 独立运行
* 不依赖本地电脑
* 支持 Linux GUI
* 可以运行浏览器和开发工具
* 可以远程开发
* 不直接暴露 RDP 到公网

的云端开发环境，那么：

> **Vultr + Ubuntu + XFCE + XRDP + Tailscale + Remmina**

是一套非常值得尝试的方案。

---

## 下一步

完成远程桌面之后，还可以继续搭建：

```text
VPS
│
├── Docker
│
├── k3s
│
├── GitHub Actions
│
├── 自动部署
│
├── Nginx / Caddy
│
├── HTTPS
│
└── 自己的开发环境
```

最终可以把这台 VPS 变成属于自己的：

> **个人云端开发工作站 + 自托管服务器 + 自动化部署平台。**
