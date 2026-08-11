---
title: "Bitbucket Cloud的新IP地址"
date: "2025-07-08 15:16:53"
slug: "bitbucket-cloud-de-xin-ip-di-zhi"
categories: ["技术"]
tags: ["Bitbucket"]
aliases:
  - "/2025/07/08/Bitbucket-Cloud的新IP地址/"
  - "/2025/07/08/Bitbucket-Cloud的新IP地址.html"
  - "/Bitbucket-Cloud的新IP地址/"
  - "/Bitbucket-Cloud的新IP地址.html"
  - "/2025/07/08/bitbucket-cloud-de-xin-ip-di-zhi/"
  - "/2025/07/08/bitbucket-cloud-de-xin-ip-di-zhi.html"
  - "/bitbucket-cloud-de-xin-ip-di-zhi.html"
---
### **我们在做什么？**

我们将从2018年7月29日星期日的UTC时间22:00开始逐步推出更改DNS记录，以指向新的IP地址。  
预计两周后，即8月15日，所有客户都将完成推出。

此迁移不会有任何停机时间，并且由于此迁移，大多数人不必做任何不同的事情。

### **我们为什么要这样做呢？**

Bitbucket近年来取得了惊人的增长，数百万用户在Bitbucket工作以构建更好的软件。  
作为其中的一部分，我们正计划进行云迁移，这将允许我们：

1. 利用云中的更多自动扩展功能
2. 轻松添加/删除网络服务容量
3. 与我们的Atlassian PaaS平台共同定位，该平台支持Jira，Confluence，StatusPage和其他Atlassian产品
4. 扩展Bitbucket的基础设施以满足未来需求
5. 我们新的云IP地址空间以及一些底层网络改进将使某些用户的响应时间明显加快，具体取决于位置
6. 同样重要的是，这些变化使我们更容易改善上游网络连接和负载平衡

### **这会对你有什么影响？**

大多数用户不必为此迁移做任何特殊操作。  
您的DNS服务器应在迁移后的几分钟内获取新IP，您的系统应立即开始使用新IP。  
不过，为了以防万一，我们将保留旧的IP运行几周。

### **防火墙考虑**

如果您使用防火墙控制入站或出站访问，则可能需要更新配置。  
请立即将这些新IP列入白名单;  
迁移完成后，您应该能够删除旧的IP。

bitbucket.org，bitbucket.com，api.bitbucket.org，bitbucket.io，bytebucket.org，altssh.bitbucket.org的新目标IP地址将是：

> IPv4: 18.205.93.0/25 and 13.52.5.0/25

> IPv6: 2406:da00:ff00::0/96\*

Note: 此IPv6范围包括Atlassian不必拥有的子网，但是匹配\* all \* Bitbucket IPv6 Atlassian IP的最长子网。  
我们将在https://confluence.atlassian.com/bitbucket/what-are-the-bitbucket-cloud-ip-addresses-i-should-use-to-configure-my-corporate上发布确切的IPv6地址列表  
-firewall-343343385.html很快。

根据https://confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html，Webhooks IP将保持不变

### **SSH考虑因素**

我们服务器的SSH密钥没有变化，因此大多数SSH客户端将继续工作而不会中断。  
但是，少数用户在推送或拉过SSH时可能会看到与此类似的警告：

```bash
Warning: the RSA host key for 'bitbucket.org' differs from the key for the IP address '18.205.93.1'
```

警告消息还会告诉您~/.ssh/known\_hosts中哪些行需要更改。  
在您喜欢的编辑器中打开该文件，删除或注释掉这些行，然后重试您的推送或拉动。

### **其他资源**

* Atlassian Public IP范围为JSON: https://ip-ranges.atlassian.com/ (将使用新地址进行更新，作为新IP推出的一部分)
* https://confluence.atlassian.com/bitbucket/what-are-the-bitbucket-cloud-ip-addresses-i-should-use-to-configure-my-corporate-firewall-343343385.html (将使用新地址进行更新，作为新IP推出的一部分)
