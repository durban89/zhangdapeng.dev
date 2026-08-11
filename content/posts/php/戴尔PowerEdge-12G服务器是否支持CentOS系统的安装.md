---
title: "戴尔PowerEdge 12G服务器是否支持CentOS系统的安装"
date: "2025-06-23 15:27:15"
slug: "dai-er-poweredge-12g-fu-wu-qi-shi-fou-zhi-chi-centos-xi-tong-de-an-zhuang"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/23/戴尔PowerEdge-12G服务器是否支持CentOS系统的安装/"
  - "/2025/06/23/戴尔PowerEdge-12G服务器是否支持CentOS系统的安装.html"
  - "/戴尔PowerEdge-12G服务器是否支持CentOS系统的安装/"
  - "/戴尔PowerEdge-12G服务器是否支持CentOS系统的安装.html"
  - "/2025/06/23/dai-er-poweredge-12g-fu-wu-qi-shi-fou-zhi-chi-centos-xi-tong-de-an-zhuang/"
  - "/2025/06/23/dai-er-poweredge-12g-fu-wu-qi-shi-fou-zhi-chi-centos-xi-tong-de-an-zhuang.html"
  - "/dai-er-poweredge-12g-fu-wu-qi-shi-fou-zhi-chi-centos-xi-tong-de-an-zhuang.html"
---
我们在采购戴尔服务器的时候，常常到遇到一些疑问，例如：PowerEdge 12G服务器能部署CentOS Linux不？有没有前辈实际安装实施过？具体版本要求？以及需要注意哪些？

下面风信网整理了一些这方面信息给大家参考，首先大家都知道戴尔官方是支持RHEL的，我们需要明白RHEL和CentOS的关系：

其实为什么有 CentOS？ CentOS 与 RHEL 有什么关系？

RHEL 在发行的时候，有两种方式。一种是二进制的发行方式，另外一种是源代码的发行方式。

无论是哪一种发行方式，你都可以免费获得（例如从网上下载），并再次发布。但如果你使用了他们的在线升级（包括补丁）或咨询服务，就必须要付费。

RHEL 一直都提供源代码的发行方式，CentOS 就是将 RHEL 发行的源代码从新编译一次，形成一个可使用的二进制版本。由于 LINUX 的源代码是 GNU，所以从获得 RHEL 的源代码到编译成新的二进制，都是合法。只是 REDHAT 是商标，所以必须在新的发行版里将 REDHAT 的商标去掉。

REDHAT 对这种发行版的态度是：“我们其实并不反对这种发行版，真正向我们付费的用户，他们重视的并不是系统本身，而是我们所提供的商业服务。”

所以，CentOS 可以得到 RHEL 的所有功能，甚至是更好的软件。但 CentOS 并不向用户提供商业支持，当然也不负上任何商业责任。

我正逐步将我的 RHEL 转到 CentOS 上，因为我不希望为 RHEL 升级而付费。当然，这是因为我已经有多年的 UNIX 使用经验，因此 RHEL 的商业技术支持对我来说并不重要。

但如果你是单纯的业务型企业，那么我还是建议你选购 RHEL 软件并购买相应服务。这样可以节省你的 IT 管理费用，并可得到专业服务。

一句话，选用 CentOS 还是 RHEL，取决于你所在公司是否拥有相应的技术力量。

戴尔的官方说法：

所以，我们不难得出一个结论，CentOS其实就是RHEL代码重新编译的一种衍生版的Linux操作系统。我们应该可以从戴尔12代服务器对 RHEL的支持，间接地得出其对应CentOS支持的大致情况。当然这个不能保证100%完全一致，重新编译也可能略有不同，但已十之八九。

请查阅戴尔服务器的系统兼容表：戴尔PowerEdge服务器对操作系统支持的兼容性矩阵表

其中RHEL兼容性查询见：https://hardware.redhat.com/list.cgi?product=Red%20Hat%20Hardware%20Certification&quicksearch=dell&showall=1

通过RHEL的兼容性，我们就可以大致了解CentOS版本对应12G服务器的支持

比如：PowerEdge R720支持RHEL的情况如下，你猜CentOS会怎样呢？


抽空做了个实例测试

我们看出戴尔PowerEdge 12G服务器在RHEL x_64支持6.1 以上版本，所以我的测试特意下载了CentOS发布的最新的x_64 6.4版

ISO文件可以非常方便地在www.centos.org 上下载

测试环境，戴尔标准的PowerEdge R620，H710p，Broadcom BCM5720。

**结论：CentOS提供了戴尔PowerEdge R620的系统原生驱动支持（Native driver support），即安装盘已经带有所有需要的驱动，包括PERC，网卡等。过程非常简单，无需额外的周折**

