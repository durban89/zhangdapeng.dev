---
title: "Linux中修改root帐户的登录用户名来加强系统保护"
date: "2025-07-02 11:31:36"
slug: "linux-zhong-xiu-gai-root-zhang-hu-de-deng-lu-yong-hu-ming-lai-jia-qiang-xi-tong-bao-hu"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/02/Linux中修改root帐户的登录用户名来加强系统保护/"
  - "/2025/07/02/Linux中修改root帐户的登录用户名来加强系统保护.html"
  - "/Linux中修改root帐户的登录用户名来加强系统保护/"
  - "/Linux中修改root帐户的登录用户名来加强系统保护.html"
  - "/2025/07/02/linux-zhong-xiu-gai-root-zhang-hu-de-deng-lu-yong-hu-ming-lai-jia-qiang-xi-tong-bao-hu/"
  - "/2025/07/02/linux-zhong-xiu-gai-root-zhang-hu-de-deng-lu-yong-hu-ming-lai-jia-qiang-xi-tong-bao.html"
  - "/linux-zhong-xiu-gai-root-zhang-hu-de-deng-lu-yong-hu-ming-lai-jia-qiang-xi-tong-bao-hu.html"
---
为了加强Linux的安全，修改linux的root的登录名会给系统带来额外的保护

操作只需要三步就可以搞定

**第一步：修改 /etc/passwd**

```bash
vi /etc/passwd
```

按i键进入编辑状态

修改第1行第1个root为新的用户名

按esc键退出编辑状态，并输入:wq!保存并退出

**第二步：修改 /etc/shadow**

```bash
vi /etc/shadow
```

按i键进入编辑状态

修改第1行第1个root为新的用户名

按esc键退出编辑状态，并输入:wq!强制保存并退出

**第三步: 修改 /etc/sudoers**

运行

```bash
vi /etc/sudoers
```

找到root    ALL=(ALL)       ALL

在下面添加一行：

```bash
新用户名    ALL=(ALL)       ALL
```

`:wq!`保存退出

为了保险起见自己可以另开一个console窗口试试


