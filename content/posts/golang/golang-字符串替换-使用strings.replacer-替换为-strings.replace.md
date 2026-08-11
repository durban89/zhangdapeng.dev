---
title: "golang 字符串替换 使用strings.replacer 替换为 strings.replace"
date: "2025-08-05 09:48:52"
slug: "golang-zi-fu-chuan-ti-huan-shi-yong-stringsreplacer-ti-huan-wei-stringsreplace"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/golang-字符串替换-使用strings.replacer-替换为-strings.replace/"
  - "/2025/08/05/golang-字符串替换-使用strings.replacer-替换为-strings.replace.html"
  - "/golang-字符串替换-使用strings.replacer-替换为-strings.replace/"
  - "/golang-字符串替换-使用strings.replacer-替换为-strings.replace.html"
  - "/2025/08/05/golang-zi-fu-chuan-ti-huan-shi-yong-stringsreplacer-ti-huan-wei-stringsreplace/"
  - "/2025/08/05/golang-zi-fu-chuan-ti-huan-shi-yong-stringsreplacer-ti-huan-wei-stringsreplace.html"
  - "/golang-zi-fu-chuan-ti-huan-shi-yong-stringsreplacer-ti-huan-wei-stringsreplace.html"
---
golang 字符串替换 使用strings.replacer 替换为 strings.replace

strings.replace的使用方式

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "aaa bbb ddd fff aaa"
	keyword := "aaa"
	str = strings.ReplaceAll(str, keyword, "**")

	fmt.Println(str)
}
```

strings.replacer的使用方式

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "aaa bbb ddd fff aaa"
	keyword := "aaa"
	replacer := strings.NewReplacer(keyword, "**")
	str = replacer.Replace(str)

	fmt.Println(str)
}
```

为什么要替换

“we see that **Replace**creates **more** runtime **memory allocations** than **New Replacer**.”

参考：

---

https://medium.com/@vikram.ingawale91/golang-strings-replace-vs-strings-replacer-a7b2d2b71593

https://levelup.gitconnected.com/multi-string-replace-in-golang-with-replacer-148d4173f439
