---
title: "Go基础学习记录之字符串处理(strings和strconv)"
date: "2025-08-01 11:35:59"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-zi-fu-chuan-chu-li-strings-he-strconv"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之字符串处理(strings和strconv)/"
  - "/2025/08/01/Go基础学习记录之字符串处理(strings和strconv).html"
  - "/Go基础学习记录之字符串处理(strings和strconv)/"
  - "/Go基础学习记录之字符串处理(strings和strconv).html"
  - "/2025/08/01/Go基础学习记录之字符串处理-strings和strconv/"
  - "/2025/08/01/Go基础学习记录之字符串处理-strings和strconv.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zi-fu-chuan-chu-li-strings-he-strconv/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zi-fu-chuan-chu-li-strings-he-strconv.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-zi-fu-chuan-chu-li-strings-he-strconv.html"
---
在Web上，我们看到的几乎所有内容（包括用户输入，数据库访问等）都由字符串表示。它们是Web开发中非常重要的一部分。在许多情况下，我们还需要拆分，连接，转换和操作字符串。本篇文章我们一起学习下Go标准库中的字符串和strconv包。

## 字符串包介绍

以下函数来自strings包。有关详细信息，请参阅官方文档：

> func Contains(s, substr string) bool  // 检查字符串s是否包含字符串substr，返回一个布尔值。

如下实例

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Contains("seafood", "foo"))
	fmt.Println(strings.Contains("seafood", "bar"))
	fmt.Println(strings.Contains("seafood", ""))
	fmt.Println(strings.Contains("", ""))
}
```

编译运行后得到Strings处理的结果如下

```bash
true
false
true
true
```

> func Join(a []string, sep string) string // 将切片中的字符串与分隔符`sep`组合在一起

如下实例

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	s := []string{"foo", "bar", "baz"}
	fmt.Println(strings.Join(s, ", "))
}
```

编译运行后得到Strings处理的结果如下

```bash
foo, bar, baz
```

> func Index(s, sep string) int // 在字符串s中查找sep的索引，如果找不到则返回-1。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("chicken", "ken"))
	fmt.Println(strings.Index("chicken", "dmr"))
}
```

编译运行后得到Strings处理的结果如下

```bash
4
-1
```

> func Repeat(s string, count int) string // 重复字符串的计数次数。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("ba" + strings.Repeat("na", 2))
}
```

编译运行后得到Strings处理的结果如下

```bash
banana
```

> func Replace(s, old, new string, n int) string // 将字符串old替换为字符串s中的字符串new。n是替换数量。如果n小于0，则替换所有实例。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Replace("oink oink oink", "k", "ky", 2))
	fmt.Println(strings.Replace("oink oink oink", "oink", "moo", -1))
}
```

编译运行后得到Strings处理的结果如下

```bash
oinky oinky oink
moo moo moo
```

> func Split(s, sep string) []string // 将带有分隔符的字符串s拆分为切片。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.Split("a,b,c", ","))
	fmt.Printf("%q\n", strings.Split("a man a plan a canal panama", "a "))
	fmt.Printf("%q\n", strings.Split(" xyz ", ""))
	fmt.Printf("%q\n", strings.Split("", "Bernardo O'Higgins"))
}
```

编译运行后得到Strings处理的结果如下

```bash
["a" "b" "c"]
["" "man " "plan " "canal panama"]
[" " "x" "y" "z" " "]
[""]
```

> func Trim(s string, cutset string) string // 如果字符串s最左边或最右边，删除字符串s的剪切集。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("[%q]", strings.Trim(" !!! Achtung !!! ", "! "))

}
```

编译运行后得到Strings处理的结果如下

```bash
["Achtung"]
```

> func Fields(s string) []string //删除空格项并将带有空格的字符串拆分为切片。

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("Fields are: %q", strings.Fields("  foo bar  baz   "))

}
```

编译运行后得到Strings处理的结果如下

```bash
Fields are: ["foo" "bar" "baz"]
```

## strconv包的介绍

以下函数来自strconv包。像往常一样，请参阅官方文档了解更多详情：

***追加系列，将数据转换为字符串，并附加到当前字节切片***。

实例演示如下

```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	str := make([]byte, 0, 100)
	str = strconv.AppendInt(str, 4567, 10)
	str = strconv.AppendBool(str, false)
	str = strconv.AppendQuote(str, "abcdefg")
	str = strconv.AppendQuoteRune(str, '单')
	fmt.Println(string(str))

}
```

编译运行后得到strconv处理的结果如下

```bash
4567false"abcdefg"'单'
```

***格式化系列，将其他数据类型转换为字符串。***

实例演示如下

```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := strconv.FormatBool(false)
	b := strconv.FormatFloat(123.23, 'g', 12, 64)
	c := strconv.FormatInt(1234, 10)
	d := strconv.FormatUint(12345, 10)
	e := strconv.Itoa(1023)
	fmt.Println(a, b, c, d, e)

}
```

编译运行后得到strconv处理的结果如下

```bash
false 123.23 1234 12345 1023
```

***解析系列，将字符串转换为其他类型。***

实例演示如下

```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	a, err := strconv.ParseBool("false")
	if err != nil {
		fmt.Println(err)
	}

	b, err := strconv.ParseFloat("123.23", 64)
	if err != nil {
		fmt.Println(err)
	}

	c, err := strconv.ParseInt("1234", 10, 64)
	if err != nil {
		fmt.Println(err)
	}

	d, err := strconv.ParseUint("12345", 10, 64)
	if err != nil {
		fmt.Println(err)
	}

	e := strconv.Itoa(1023)
	fmt.Println(a, b, c, d, e)
}
```

编译运行后得到strconv处理的结果如下

```bash
false 123.23 1234 12345 1023
```

今天的学习就到这里，明天继续。
