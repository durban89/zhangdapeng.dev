---
title: "Intellij IDEA java: constant string too long"
date: "2025-07-03 11:58:09"
slug: "intellij-idea-java-constant-string-too-long"
categories: ["技术"]
tags: ["IntelliJ"]
aliases:
  - "/2025/07/03/Intellij-IDEA-java:-constant-string-too-long/"
  - "/2025/07/03/Intellij-IDEA-java:-constant-string-too-long.html"
  - "/Intellij-IDEA-java:-constant-string-too-long/"
  - "/Intellij-IDEA-java:-constant-string-too-long.html"
  - "/2025/07/03/Intellij-IDEA-java-constant-string-too-long/"
  - "/2025/07/03/Intellij-IDEA-java-constant-string-too-long.html"
  - "/2025/07/03/intellij-idea-java-constant-string-too-long/"
  - "/2025/07/03/intellij-idea-java-constant-string-too-long.html"
  - "/intellij-idea-java-constant-string-too-long.html"
---
Intellij IDEA,这个编辑器今天在做Base64转pdf的过程中遇到了奇怪的问题：“常量字符串太长”

搜索问答思路：

1. 我搜索了soft wrap的配置，把他们都设为取消:没用;

2. Google问题，得到jetbrains答案：vim插件，卸载之，没用;

3. 无奈之下，求助与熟练操作intellij idea的朋友，答曰“大概是jdk的问题“。摸索之，改之，无用;

最终的答案：

最后修改了Java compiler下的Use compiler为Eclipse，成功。


