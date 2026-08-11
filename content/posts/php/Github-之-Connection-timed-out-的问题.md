---
title: "Github 之 Connection timed out 的问题"
date: "2025-07-03 16:49:52"
slug: "github-zhi-connection-timed-out-de-wen-ti"
categories: ["技术"]
tags: ["Github"]
aliases:
  - "/2025/07/03/Github-之-Connection-timed-out-的问题/"
  - "/2025/07/03/Github-之-Connection-timed-out-的问题.html"
  - "/Github-之-Connection-timed-out-的问题/"
  - "/Github-之-Connection-timed-out-的问题.html"
  - "/2025/07/03/github-zhi-connection-timed-out-de-wen-ti/"
  - "/2025/07/03/github-zhi-connection-timed-out-de-wen-ti.html"
  - "/github-zhi-connection-timed-out-de-wen-ti.html"
---
最近push代码到github的时候出现了问题

> $ git push origin master
>
> ssh: connect to host github.com port 22: Operation timed out
>
> fatal: Could not read from remote repository.
>
> Please make sure you have the correct access rights
>
> and the repository exists.

经过google后找到了解决办法

先用如下命令进行测试

```bash
ssh -T -p 443 xx@xx
```

如果测试后出现下面类似的提示说明可以继续操作了

```bash
Hi userName! You've successfully authenticated, but GitHub does not provide shell access.
```

接下来编辑~/.ssh/config文件（没有则创建一个），然后加入下面的代码：

```bash
Host github.com 
    Hostname ssh.github.com 
    Port 443
```

最后在进行测试下

```bash
ssh -T xx@xxx
```

如果有如下提示表示可以进行正常操作了

```bash
Warning: Permanently added the RSA host key for IP address '[192.30.253.122]:443' to the list of known hosts. 
Hi yourname! You've successfully authenticated, but GitHub does not provide shell access.
```
