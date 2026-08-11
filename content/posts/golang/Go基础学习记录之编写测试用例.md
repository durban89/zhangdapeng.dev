---
title: "Go基础学习记录之编写测试用例"
date: "2025-08-04 11:39:18"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-bian-xie-ce-shi-yong-li"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之编写测试用例/"
  - "/2025/08/04/Go基础学习记录之编写测试用例.html"
  - "/Go基础学习记录之编写测试用例/"
  - "/Go基础学习记录之编写测试用例.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bian-xie-ce-shi-yong-li/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bian-xie-ce-shi-yong-li.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-bian-xie-ce-shi-yong-li.html"
---
在开发过程中，非常重要的一步是测试我们的代码以确保其质量和完整性。我们需要确保每个函数都返回预期的结果，并且我们的代码执行得最佳。我们已经知道单元测试的重点是在程序的设计或实现中发现逻辑错误。它们用于在早期检测和暴露代码中的问题，以便我们可以在它们失控之前更容易地修复它们。我们还知道，性能测试是为了优化我们的代码而进行的，这样它在负载下是稳定的，并且可以保持高水平的并发性。在本篇文章中，我们将看一些关于如何在Go中实现单元和性能测试的常见问题。

Go语言带有一个名为testing的轻量级测试框架，我们可以使用`go test`命令执行单元和性能测试。Go的测试框架与测试其他语言的框架类似。您可以使用它们开发各种测试套件，其中可能包括单元测试，基准测试，压力测试等测试。让我们逐步了解Go中的测试。

### 如何编写测试用例

由于`go test`命令只能在包含所有相应文件的目录中执行，因此我们将创建一个新的项目目录`gotest`，以便我们所有的代码和测试代码都在同一目录中。

让我们继续在名为gotest.go和gotest\_test.go的目录中创建两个文件

1. Gotest.go ：这个文件声明了我们的包名，并且有一个执行除法操作的函数：

```go
package gotest

import (
    "errors"
)

func Division(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("Divisor can not be 0")
    }
    return a / b, nil
}
```

1. Gotest\_test.go：这是我们的单元测试文件。请记住以下测试文件的原则：
2. 文件名必须以\_test.go结尾，以便go测试可以找到并执行相应的代码
3. 您必须导入测试包
4. 所有测试用例函数都以Test开头
5. 测试用例遵循源代码顺序
6. TestXxx()形式的测试函数采用testing.T参数;我们可以使用此类型来记录错误或获取测试状态
7. 在函数TestXxx(t \* testing.T)的函数中，Xxx部分可以是任何字母数字组合，但第一个字母不能是小写字母[az]。例如，Testintdiv将是无效的函数名称。
8. 通过调用testing.T中的Error，Errorf，FailNow，Fatal或FatalIf测试方法之一。对我们的测试函数，我们可能无法通过测试。另外，我们可以调用testing.T的Log方法.T来记录错误日志中的信息。

这是我们的测试代码：

```go
package gotest

import (
    "testing"
)

func Test_Division_1(t *testing.T) {
    // try a unit test on function
    if i, e := Division(6, 2); i != 3 || e != nil { 
        // If it is not as expected, then the test has failed 
        t.Error("division function tests do not pass ") 
    } else {
        // record the expected information
        t.Log("first test passed ") 
    }
}

func Test_Division_2(t *testing.T) {
    t.Error("just does not pass")
}
```

在项目目录中执行`go test`时，它将显示以下信息：

```bash
--- FAIL: Test_Division_2 (0.00 seconds)
gotest_test.go: 16: is not passed
FAIL
exit status 1
FAIL gotest 0.013s
```

我们可以从这个结果中看到第二个测试函数没有通过，因为我们使用t.Error在死胡同中写了。但是我们的第一个测试功能呢？默认情况下，执行go test不会显示测试结果。我们需要提供详细参数-v 比如 `go test -v`来显示以下输出：

```bash
=== RUN Test_Division_1
--- PASS: Test_Division_1 (0.00 seconds)
gotest_test.go: 11: first test passed
=== RUN Test_Division_2
--- FAIL: Test_Division_2 (0.00 seconds)
gotest_test.go: 16: is not passed
FAIL
exit status 1
FAIL gotest 0.012s
```

以上输出详细显示了我们的测试结果。 我们看到测试函数1 Test\_Division\_1通过，测试函数2 Test\_Division\_2失败，最后得出结论我们的测试套件没有通过。 接下来，我们使用以下代码修改测试功能2：

```go
func Test_Division_2(t *testing.T) {
    // try a unit test on function
    if _, e := Division(6, 0); e == nil { 
        // If it is not as expected, then the error
        t.Error("Division did not work as expected.") 
    } else {
        // record some of the information you expect to record
        t.Log("one test passed.", e) 
    }
}
```

我们再次执行`go test -v`。现在应显示以下信息 - 测试套件已通过〜：

```bash
=== RUN Test_Division_1
--- PASS: Test_Division_1 (0.00 seconds)
gotest_test.go: 11: first test passed
=== RUN Test_Division_2
--- PASS: Test_Division_2 (0.00 seconds)
gotest_test.go: 20: one test passed. divisor can not be 0
PASS
ok gotest 0.013s
```

### 如何写压力测试

压力测试用于检测功能性能，并且与单元测试有一些相似之处（我们不会在此处讨论），但是我们需要注意以下几点：

* 压力测试必须遵循以下格式，其中XXX可以是任何字母数字组合，其第一个字母不能是小写字母。 `func BenchmarkXXX (b *testing.B){...}`
* 默认情况下，Go测试不执行功能压力测试。如果要执行压力测试，则需要使用以下格式设置标志`-test.bench="test_name_regex"`。例如，要在套件中运行所有压力测试，您可以运行`go test -test.bench=".*"`。
* 在压力测试中，请记住使用testing.B.N任何循环体，以便测试可以正常运行。
* 和以前一样，测试文件名必须以\_test.go结尾

在这里，我们创建一个名为webbench\_test.go的压力测试文件：

```go
package gotest

import (
    "testing"
)

func Benchmark_Division(b *testing.B) {
    for i := 0; i < b.N; i++ { // use b.N for looping
        Division(4, 5)
    }
}

func Benchmark_TimeConsumingFunction(b *testing.B) {
    b.StopTimer() // call the function to stop the stress test time count

    // Do some initialization work, such as reading file data, database connections and the like,
    // So that our benchmarks reflect the performance of the function itself

    b.StartTimer() // re-start time
    for i := 0; i < b.N; i++ {
        Division(4, 5)
    }
}
```

然后我们执行`go test -file webbench_test.go -test.bench =".*"`命令，它输出以下结果：

```bash
PASS
Benchmark_Division 500000000 7.76 ns/ op
Benchmark_TimeConsumingFunction 500000000 7.80 ns/ op
ok gotest 9.364s
```

上述结果表明我们没有执行任何TestXXX单元测试功能，而只执行了BenchmarkXXX测试（完全符合预期）。 第一个Benchmark\_Division测试显示我们的Division（）函数执行了5亿次，平均执行时间为7.76ns。 第二个Benchmark\_TimeConsumingFunction显示我们的TmeConsumingFunction执行了5亿次，平均执行时间为7.80ns。 最后，它输出我们的测试套件的总执行时间。

### 小结

从我们在Go中对单元和压力测试的简短讨论中，我们可以看到测试包非常轻量级，但包含有用的实用程序。我们看到写入单元和压力测试非常简单，使用Go的内置go test命令可以更轻松地运行它们。每次我们修改代码时，我们都可以运行go test来开始回归测试。
