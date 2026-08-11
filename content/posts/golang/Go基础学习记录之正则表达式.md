---
title: "Go基础学习记录之正则表达式"
date: "2025-08-01 11:35:44"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-zheng-ze-biao-da-shi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之正则表达式/"
  - "/2025/08/01/Go基础学习记录之正则表达式.html"
  - "/Go基础学习记录之正则表达式/"
  - "/Go基础学习记录之正则表达式.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zheng-ze-biao-da-shi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zheng-ze-biao-da-shi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-zheng-ze-biao-da-shi.html"
---
## 正则表达式

正则表达式("Regexp")是一种复杂但功能强大的正则匹配和文本操作工具。  
虽然它的表现不如纯文本匹配，但它更灵活。根据其语法，可以过滤源内容中的几乎任何类型的文本。  
如果需要在Web开发中收集数据，使用Regexp检索有意义的数据并不困难。

Go有regexp包，它为regexp提供官方支持。  
如果已经在其他编程语言中使用了regexp，那么应该熟悉它。  
注意，除了\C之外，Go实现了RE2标准。  
有关详细信息，请访问以下链接：http：//code.google.com/p/re2/wiki/Syntax。

Go的字符串包实际上可以执行许多工作，如搜索(包含，索引)，替换(替换)，解析(拆分，连接)等，并且它比Regexp更快。  
但是，这些都是微不足道的操作。  
如果要搜索不区分大小写的字符串，Regexp应该是您的最佳选择。  
因此，如果字符串包足以满足您的需求，只需使用它，因为它易于使用和阅读;  
如果您需要执行更高级的操作，请使用Regexp。

如果您看过前面几篇文章，有篇文章的表单验证，我们使用Regexp来验证用户输入信息的有效性。  
请注意，所有字符都是UTF-8。  
下面让我们了解Go regexp包的更多信息！

### 正则匹配

regexp包有3个匹配的函数：如果匹配了一个正则，则返回true，否则返回false。

```go
func Match(pattern string, b []byte) (matched bool, error error)
func MatchReader(pattern string, r io.RuneReader) (matched bool, error error)
func MatchString(pattern string, s string) (matched bool, error error)
```

这3个函数检查输入源输入的内容是否与正则匹配，如果匹配则返回true。  
但是，如果您的Regex有语法错误，它将返回错误。  
这些函数的3个输入源是`slice of byte`，`RuneReader`和`string`。  
以下是验证IP地址的示例：

```go
func IsIP(ip string) (b bool) {
	if m, _ := regexp.MatchString("^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}$", ip); !m {
		return false
	}

	return true
}
```

如上所见，在regexp包中使用正则并没有什么不同。  
以下是验证用户输入是否有效的另一个示例：

```go
func IsNumber() {
	if len(os.Args) == 1 {
		fmt.Println("Usage: regexp [string]")
		os.Exit(1)
	} else if m, _ := regexp.MatchString("^[0-9]+$", os.Args[1]); m {
		fmt.Println("Number")
	} else {
		fmt.Println("Not number")
	}
}
```

在上面的例子中，我们使用Match(Reader|String)来检查内容是否有效，但它们都很容易使用。

### 正则过滤

匹配正则可以验证内容，但不能从中剪切，过滤或收集数据。  
如果你想这样做，你必须使用Regexp的复杂正则。  
假设我们需要编写一个爬虫。  
以下是必须使用Regexp过滤和剪切数据的示例。

```go
package helpers

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"regexp"
	"strings"
)

func FetchWebContent() {
	resp, err := http.Get("https://www.baidu.com")
	if err != nil {
		fmt.Println(err)
		return
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		fmt.Println(err)
		return
	}

	src := string(body)

	// 将HTML标签转换为小写
	re, _ := regexp.Compile("\\<[\\S\\s]+?\\>")
	src = re.ReplaceAllStringFunc(src, strings.ToLower)

	// 移除 STYLE样式
	re, _ = regexp.Compile("\\<style[\\S\\s]+?\\</style\\>")
	src = re.ReplaceAllString(src, "")

	// 移除 SCRIPT标签的内容
	re, _ = regexp.Compile("\\<script[\\S\\s]+?\\</script\\>")
	src = re.ReplaceAllString(src, "")

	// 删除尖括号中的所有HTML代码，并替换为换行符。
	re, _ = regexp.Compile("\\<[\\S\\s]+?\\>")
	src = re.ReplaceAllString(src, "\n")

	// 删除连续换行符
	re, _ = regexp.Compile("\\s{2,}")
	src = re.ReplaceAllString(src, "\n")

	fmt.Println(strings.TrimSpace(src))
}
```

在这个例子中，我们使用Compile作为复杂正则的第一步。  
它验证您的Regex语法是否正确，然后返回Regexp以解析其他操作中的内容。  
以下是一些解析Regexp语法的函数：

```go
func Compile(expr string) (*Regexp, error)
func CompilePOSIX(expr string) (*Regexp, error)
func MustCompile(str string) *Regexp
func MustCompilePOSIX(str string) *Regexp
```

ComplePOSIX和Compile之间的区别在于前者必须使用最左边最长搜索的POSIX语法，而后者只是最左边的搜索。  
例如，对于Regexp [a-z]{2,4}和内容"aa09aaa88aaaa"，CompilePOSIX返回aaaa但Compile返回aa。  
当Regexp语法不正确时，`Must`前缀意味着panic，否则返回错误。  
现在我们知道如何创建一个新的Regexp，让我们看看这个结构提供的方法如何帮助我们对内容进行操作：

```go
func (re *Regexp) Find(b []byte) []byte
func (re *Regexp) FindAll(b []byte, n int) [][]byte
func (re *Regexp) FindAllIndex(b []byte, n int) [][]int
func (re *Regexp) FindAllString(s string, n int) []string
func (re *Regexp) FindAllStringIndex(s string, n int) [][]int
func (re *Regexp) FindAllStringSubmatch(s string, n int) [][]string
func (re *Regexp) FindAllStringSubmatchIndex(s string, n int) [][]int
func (re *Regexp) FindAllSubmatch(b []byte, n int) [][][]byte
func (re *Regexp) FindAllSubmatchIndex(b []byte, n int) [][]int
func (re *Regexp) FindIndex(b []byte) (loc []int)
func (re *Regexp) FindReaderIndex(r io.RuneReader) (loc []int)
func (re *Regexp) FindReaderSubmatchIndex(r io.RuneReader) []int
func (re *Regexp) FindString(s string) string
func (re *Regexp) FindStringIndex(s string) (loc []int)
func (re *Regexp) FindStringSubmatch(s string) []string
func (re *Regexp) FindStringSubmatchIndex(s string) []int
func (re *Regexp) FindSubmatch(b []byte) [][]byte
func (re *Regexp) FindSubmatchIndex(b []byte) []int
```

这18个方法包括不同输入源(byte slice, string 和 io.RuneReader)的相同函数，因此我们可以通过忽略输入源来真正简化此列表，如下所示：

```go
func (re *Regexp) Find(b []byte) []byte
func (re *Regexp) FindAll(b []byte, n int) [][]byte
func (re *Regexp) FindAllIndex(b []byte, n int) [][]int
func (re *Regexp) FindAllSubmatch(b []byte, n int) [][][]byte
func (re *Regexp) FindAllSubmatchIndex(b []byte, n int) [][]int
func (re *Regexp) FindIndex(b []byte) (loc []int)
func (re *Regexp) FindSubmatch(b []byte) [][]byte
func (re *Regexp) FindSubmatchIndex(b []byte) []int
```

代码示例：

```go
package helpers

import (
	"fmt"
	"regexp"
)

func Find() {
	a := "I am learning Go language"

	re, _ := regexp.Compile("[a-z]{2,4}")
	// 找到第一个匹配的
	one := re.Find([]byte(a))
	fmt.Println("Find:", string(one))

	// 找到所有匹配并保存到切片，n小于0表示返回所有匹配，如果大于0，则表示切片长度
	all := re.FindAll([]byte(a), -1)
	fmt.Println("FindAll:", all)

	// 查找第一个匹配，开始和结束位置的索引。
	index := re.FindIndex([]byte(a))
	fmt.Println("FindIndex:", index)

	// 查找所有匹配的索引，n执行与上面相同的工作。
	allindex := re.FindAllIndex([]byte(a), -1)
	fmt.Println("FindAllIndex:", allindex)

	re2, _ := regexp.Compile("am(.*)lang(.*)")

	// 找到第一个子匹配和返回数组，第一个元素包含所有元素，第二个元素包含first()的结果，第三个元素包含second()的结果
	// 执行后输出如下
	// the first element:am learning Go language
	// the second element: learning Go
	// the third element:uage
	submatch := re2.FindSubmatch([]byte(a))
	fmt.Println("FindSubmatch:", submatch)

	for _, v := range submatch {
		fmt.Println(string(v))
	}

	// 类似于FindIndex()
	submatchindex := re2.FindSubmatchIndex([]byte(a))
	fmt.Println("FindSubmatchIndex:", submatchindex)

	// FindAllSubmatch 找到所有子匹配
	allsubmatch := re2.FindAllSubmatch([]byte(a), -1)
	fmt.Println("FindAllSubmatch:", allsubmatch)

	// FindAllSubmatchIndex 找到所有子匹配的所以
	allsubmatchindex := re2.FindAllSubmatchIndex([]byte(a), -1)
	fmt.Println("FindAllSubmatchIndex:", allsubmatchindex)

}
```

正如我们之前提到的，Regexp还有3种匹配方法。  
它们与导出的函数完全相同。  
事实上，那些导出的函数实际上是在引擎盖下调用这些方法：

```go
func (re *Regexp) Match(b []byte) bool
func (re *Regexp) MatchReader(r io.RuneReader) bool
func (re *Regexp) MatchString(s string) bool
```

接下来，让我们看看如何使用Regex替换字符串：

```go
func (re *Regexp) ReplaceAll(src, repl []byte) []byte
func (re *Regexp) ReplaceAllFunc(src []byte, repl func([]byte) []byte) []byte
func (re *Regexp) ReplaceAllLiteral(src, repl []byte) []byte
func (re *Regexp) ReplaceAllLiteralString(src, repl string) string
func (re *Regexp) ReplaceAllString(src, repl string) string
func (re *Regexp) ReplaceAllStringFunc(src string, repl func(string) string) string
```

这些用于在刚才的爬行示例，因此我们在此不再进一步解释。  
我们来看看Expand的定义：

```go
func (re *Regexp) Expand(dst []byte, template []byte, src []byte, match []int) []byte
func (re *Regexp) ExpandString(dst []byte, template string, src string, match []int) []byte
```

那么我们如何使用Expand？

```go
package helpers

import (
	"fmt"
	"regexp"
)

func Expand() {
	src := []byte(`
		call hello alice
		hello bob
		call hello eve
	`)

	pat := regexp.MustCompile(`(?m)(call)\s+(?P<cmd>\w+)\S+(?P<arg>.+)\s*$`)
	res := []byte{}
	for _, s := range pat.FindAllSubmatchIndex(src, -1) {
		res = pat.Expand(res, []byte("$cmd('$arg')\n"), src, s)
	}
	fmt.Println(string(res))
}
```

此时，您已经在Go中学习了整个正则表达式包。  
我希望你能通过研究关键方法的例子来了解更多，这样你就可以自己做一些有趣的事情。
