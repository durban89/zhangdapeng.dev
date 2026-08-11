---
title: "Error: \"DEVELOPER_DIR\" is not defined at ./symbolicatecrash line 53."
date: "2025-06-20 11:50:30"
slug: "error-developer-dir-is-not-defined-at-symbolicatecrash-line-53"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/Error:-\"DEVELOPER-DIR\"-is-not-defined-at-./symbolicatecrash-line-53./"
  - "/2025/06/20/Error:-\"DEVELOPER-DIR\"-is-not-defined-at-./symbolicatecrash-line-53..html"
  - "/Error:-\"DEVELOPER-DIR\"-is-not-defined-at-./symbolicatecrash-line-53./"
  - "/Error:-\"DEVELOPER-DIR\"-is-not-defined-at-./symbolicatecrash-line-53..html"
  - "/2025/06/20/Error-DEVELOPER-DIR-is-not-defined-at-symbolicatecrash-line-53/"
  - "/2025/06/20/Error-DEVELOPER-DIR-is-not-defined-at-symbolicatecrash-line-53.html"
  - "/2025/06/20/error-developer-dir-is-not-defined-at-symbolicatecrash-line-53/"
  - "/2025/06/20/error-developer-dir-is-not-defined-at-symbolicatecrash-line-53.html"
  - "/error-developer-dir-is-not-defined-at-symbolicatecrash-line-53.html"
---
项目问题解析“Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 53.”这个问题是最近调试app的时候出现的，因为自己提交的app遭到拒绝，需要调试，在使用symbolicatecrash的时候出现了问题。

在这里的解决办法是：

在不关闭当前终端的情况下，输入：

```bash
export DEVELOPER_DIR="/Applications/XCode.app/Contents/Developer"
```

然后再试试就可以了。
