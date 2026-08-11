---
title: "Ubuntu  Server在 戴尔PowerEdge 12G(R420/R620/R720) 上的问题"
date: "2025-06-23 15:27:19"
slug: "ubuntu-server-zai-dai-er-poweredge-12gr420r620r720-shang-de-wen-ti"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/23/Ubuntu-Server在-戴尔PowerEdge-12G(R420/R620/R720)-上的问题/"
  - "/2025/06/23/Ubuntu-Server在-戴尔PowerEdge-12G(R420/R620/R720)-上的问题.html"
  - "/Ubuntu-Server在-戴尔PowerEdge-12G(R420/R620/R720)-上的问题/"
  - "/Ubuntu-Server在-戴尔PowerEdge-12G(R420/R620/R720)-上的问题.html"
  - "/2025/06/23/Ubuntu-Server在-戴尔PowerEdge-12G-R420-R620-R720-上的问题/"
  - "/2025/06/23/Ubuntu-Server在-戴尔PowerEdge-12G-R420-R620-R720-上的问题.html"
  - "/2025/06/23/ubuntu-server-zai-dai-er-poweredge-12gr420r620r720-shang-de-wen-ti/"
  - "/2025/06/23/ubuntu-server-zai-dai-er-poweredge-12gr420r620r720-shang-de-wen-ti.html"
  - "/ubuntu-server-zai-dai-er-poweredge-12gr420r620r720-shang-de-wen-ti.html"
---
DELL 12G(R420/R620/R720) 的服务器在安装 Ubuntu 的时候会出现诸多的问题，原先的 10.04.x LTS 版本已经不支持了，现在非官方还支持的有 12.04，不过依然有不少问题。根据这个帖子的描述，。  
BIOS 会显示如下的 error log:

```bash
Critical CPU1 Status: Processor sensor for CPU1, IERR was asserted
Critical PCIE Fatal Err: Critical Event sensor, bus fatal error [Bus 1 Device 0 Function 0] was asserted
```

在 DELL 的官方博客上，我们也看到了其说明，DELL 12G 并不支持 Ubuntu 发型版本，但是其 12.04 LTS 及以后的版本可以通过修改一些东西来 workaround。

BIOS 中将 power management 设置为 maximum performance，禁用掉 C-State。

下面的就全是 ubuntu 这二货的 bug 了，难怪到现在 12G 的服务器也没出现在他的 certification 列表上。

给 sb_edac 以及 i7core_edac(3.2.0-28.44 修复) 打上 patch 或者加入 blacklist:

另外 acpi_pad(3.2.0-28.44 修复) 以及 mei(3.2.0-31.50 修复) 模块也要加到 blacklist 中，前者是电源节能的 driver，还在开发中，对于服务器来说也没有必要；后者在 watchdog timer 上会 。

```bash
# cat /etc/modprobe.d/blacklist-dell.conf
blacklist acpi_pad
blacklist mei
blacklist sb_edac
blacklist i7core_edac
```

这里有篇《Doing battle with a Dell R620 and Ubuntu》供欣赏 ;-)

除了 10.04.x 外，debian-6.0.6 以及 CentOS-6.3 等都会出现一些问题，包括安装过程中找不到网卡(BCM5720)驱动，找不到 RAID 的驱动等问题。换成 Intel 的 I350 的网卡之后，可以找到网卡驱。  
总之，Ubuntu 既然想做 server 版本，就要把他给做好，最重要的就是跟主流的硬件厂商(Dell, Hp)的支持程度，要么你就直接在网站上挂个『for test only』牌子让大家知道你做 server 只是玩玩？  
另外一件搞笑的事，12.04 的 kernel 已经不区分 server 跟 generic 了，官方的理由是『便于维护』。默认的 I/O 调度也变成了 cfq，这需要人肉改回 deadline；preemption model，tickless 等都会改变。好在这些影响对机器的性能应该不会太大。

这里有一篇关于 12.04 的不完全测评，可以参考下。在不大可能换硬件的情况下，或者说即使换了硬件，二者的支持如果不和谐的话，我们只能换发型版本。

结论：戴尔PowerEdge上不适合安装Ubuntu Server

