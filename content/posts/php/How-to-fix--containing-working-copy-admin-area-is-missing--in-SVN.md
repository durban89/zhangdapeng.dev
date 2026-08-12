---
title: "How to fix “containing working copy admin area is missing” in SVN?"
date: "2025-06-17 18:57:25"
slug: "how-to-fix-containing-working-copy-admin-area-is-missing-in-svn"
categories: ["技术"]
tags: ["SVN"]
aliases:
  - "/2025/06/17/How-to-fix--containing-working-copy-admin-area-is-missing--in-SVN.html"
---
How to fix “containing working copy admin area is missing” in SVN?

svn: Directory '/xxx/xxx/ios/project/xx/xx/JSONKit' is missing

针对于这个问题：

第一步

```bash
svn cleanup
```

第二步

```bash
svn --force delete <directory-that-doesn't-exist-but-should>
```

ok解决了
