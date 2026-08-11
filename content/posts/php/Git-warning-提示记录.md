---
title: "Git warning 提示记录"
date: "2025-07-14 16:22:14"
slug: "git-warning-ti-shi-ji-lu"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/14/Git-warning-提示记录/"
  - "/2025/07/14/Git-warning-提示记录.html"
  - "/Git-warning-提示记录/"
  - "/Git-warning-提示记录.html"
  - "/2025/07/14/git-warning-ti-shi-ji-lu/"
  - "/2025/07/14/git-warning-ti-shi-ji-lu.html"
  - "/git-warning-ti-shi-ji-lu.html"
---
git version 2.28.0

出现问题时执行的命令

```bash
git pull origin master
```

warning提示如下

warning: 不建议在没有为偏离分支指定合并策略时执行 pull 操作。 您可以在执行下一次  
pull 操作之前执行下面一条命令来抑制本消息：

`git config pull.rebase false  # 合并（缺省策略）`  
`git config pull.rebase true   # 变基`  
`git config pull.ff only       # 仅快进`

您可以将 "git config" 替换为 "`git config --global`" 以便为所有仓库设置  
缺省的配置项。您也可以在每次执行 pull 命令时添加 --rebase、--no-rebase，  
或者 --ff-only 参数覆盖缺省设置。
