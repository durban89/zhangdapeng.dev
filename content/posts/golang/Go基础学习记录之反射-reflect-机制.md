---
title: "Go基础学习记录之反射(reflect)机制"
date: "2025-08-01 10:32:23"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-fan-she-reflect-ji-zhi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之反射(reflect)机制/"
  - "/2025/08/01/Go基础学习记录之反射(reflect)机制.html"
  - "/Go基础学习记录之反射(reflect)机制/"
  - "/Go基础学习记录之反射(reflect)机制.html"
  - "/2025/08/01/Go基础学习记录之反射-reflect-机制/"
  - "/2025/08/01/Go基础学习记录之反射-reflect-机制.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-fan-she-reflect-ji-zhi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-fan-she-reflect-ji-zhi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-fan-she-reflect-ji-zhi.html"
---
为什么需要反射机制，这里引用网上的原话

> 有时候我们需要编写一个函数能够处理一类并不满足普通公共接口的类型的值，也可能是因为它们并没有确定的表示方式，或者是在我们设计该函数的时候这些类型可能还不存在。
>
> 一个大家熟悉的例子是fmt.Fprintf函数提供的字符串格式化处理逻辑，它可以用来对任意类型的值格式化并打印，甚至支持用户自定义的类型。让我们也来尝试实现一个类似功能的函数。为了简单起见，我们的函数只接收一个参数，然后返回和fmt.Sprint类似的格式化后的字符串。我们实现的函数名也叫Sprint。
>
> 我们首先用switch类型分支来测试输入参数是否实现了String方法，如果是的话就调用该方法。然后继续增加类型测试分支，检查这个值的动态类型是否是string、int、bool等基础类型，并在每种情况下执行相应的格式化操作。

至于我为什么要了解下这个问题，因为我遇到了呗，反射机制对于在使用第三方数据库的时候很有帮助，能够帮助我们判断返回的值，如果处理值，比如我之前分享的文章[Go基础学习记录之Web开发的博客文章列表展示功能]里面的查询函数Query，就用到了这个反射，MySQL的库中的Scan函数需要传入一个[]interface{}，而且值为指针类型，这个时候我们需要根据这个指针获取到interface{}然后转为对应的类型的值，最后组成程序需要的结果值返回给控制层来交给View去给到前端展示

## reflect.Type和reflect.Value

反射是由 reflect 包提供的。 它定义了两个重要的类型, Type 和 Value. 一个 Type 表示一个Go类型. 它是一个接口, 有许多方法来区分类型以及检查它们的组成部分, 例如一个结构体的成员或一个函数的参数等. 唯一能反映 reflect.Type 实现的是接口的类型描述信息, 也正是这个实体标识了接口值的动态类型.

### reflect.Type

函数 reflect.TypeOf 接受任意的 interface{} 类型, 并以reflect.Type形式返回其动态类型:

```go
t := reflect.TypeOf(3)  // a reflect.Type
fmt.Println(t.String()) // "int"
fmt.Println(t)          // "int"
```

其中 TypeOf(3) 调用将值 3 传给 interface{} 参数. 这里有个隐式的接口的接口，将一个具体的值转为接口类型会有一个隐式的接口转换操作, 它会创建一个包含两个信息的接口值: 操作数的动态类型(这里是int)和它的动态的值(这里是3).

因为 reflect.TypeOf 返回的是一个动态类型的接口值, 它总是返回具体的类型. 因此, 下面的代码将打印 ```\*os.File``` 而不是 "io.Writer". 稍后, 我们将看到能够表达接口类型的 reflect.Type.

```go
var w io.Writer = os.Stdout
fmt.Println(reflect.TypeOf(w)) // "*os.File"
```

要注意的是 reflect.Type 接口是满足 fmt.Stringer 接口的. 因为打印一个接口的动态类型对于调试和日志是有帮助的, fmt.Printf 提供了一个缩写 %T 参数, 内部使用 reflect.TypeOf 来输出:

```go
fmt.Printf("%T\n", 3) // "int"
```

### reflect.Value

reflect 包中另一个重要的类型是 Value. 一个 reflect.Value 可以装载任意类型的值. 函数 reflect.ValueOf 接受任意的 interface{} 类型, 并返回一个装载着其动态值的 reflect.Value. 和 reflect.TypeOf 类似, reflect.ValueOf 返回的结果也是具体的类型, 但是 reflect.Value 也可以持有一个接口值.

```go
v := reflect.ValueOf(3) // a reflect.Value
fmt.Println(v)          // "3"
fmt.Printf("%v\n", v)   // "3"
fmt.Println(v.String()) // NOTE: "<int Value>"
```

和 reflect.Type 类似, reflect.Value 也满足 fmt.Stringer 接口, 但是除非 Value 持有的是字符串, 否则 String 方法只返回其类型. 而使用 fmt 包的 %v 标志参数会对 reflect.Values 特殊处理.

对 Value 调用 Type 方法将返回具体类型所对应的 reflect.Type:

```go
t := v.Type()           // a reflect.Type
fmt.Println(t.String()) // "int"
```

reflect.ValueOf 的逆操作是 reflect.Value.Interface 方法. 它返回一个 interface{} 类型，装载着与 reflect.Value 相同的具体值:

```go
v = reflect.ValueOf(3)  // a reflect.Value
x := v.Interface()      // an interface{}
fmt.Println(x)          // "3"
i := x.(int)            // an int
fmt.Printf("%d\n", i)   // "3"
```

reflect.Value 和 interface{} 都能装载任意的值. 所不同的是, 一个空的接口隐藏了值内部的表示方式和所有方法, 因此只有我们知道具体的动态类型才能使用类型断言来访问内部的值(就像上面那样), 内部值我们没法访问. 相比之下, 一个 Value 则有很多方法来检查其内容, 无论它的具体类型是什么. 让我们再次尝试实现我们的格式化函数 format.Any.

我们使用 reflect.Value 的 Kind 方法来替代之前的类型 switch. 虽然还是有无穷多的类型, 但是它们的kinds类型却是有限的: Bool, String 和 所有数字类型的基础类型; Array 和 Struct 对应的聚合类型; Chan, Func, Ptr, Slice, 和 Map 对应的引用类型; interface 类型; 还有表示空值的 Invalid 类型. (空的 reflect.Value 的 kind 即为 Invalid.)

```go
package format

import (
    "reflect"
    "strconv"
)

// Any formats any value as a string.
func Any(value interface{}) string {
    return formatAtom(reflect.ValueOf(value))
}

// formatAtom formats a value without inspecting its internal structure.
func formatAtom(v reflect.Value) string {
    switch v.Kind() {
    case reflect.Invalid:
        return "invalid"
    case reflect.Int, reflect.Int8, reflect.Int16,
        reflect.Int32, reflect.Int64:
        return strconv.FormatInt(v.Int(), 10)
    case reflect.Uint, reflect.Uint8, reflect.Uint16,
        reflect.Uint32, reflect.Uint64, reflect.Uintptr:
        return strconv.FormatUint(v.Uint(), 10)
    // ...floating-point and complex cases omitted for brevity...
    case reflect.Bool:
        return strconv.FormatBool(v.Bool())
    case reflect.String:
        return strconv.Quote(v.String())
    case reflect.Chan, reflect.Func, reflect.Ptr, reflect.Slice, reflect.Map:
        return v.Type().String() + " 0x" +
            strconv.FormatUint(uint64(v.Pointer()), 16)
    default: // reflect.Array, reflect.Struct, reflect.Interface
        return v.Type().String() + " value"
    }
}
```

到目前为止, 我们的函数将每个值视作一个不可分割没有内部结构的物品, 因此它叫 formatAtom. 对于聚合类型(结构体和数组)和接口，只是打印值的类型, 对于引用类型(channels, functions, pointers, slices, 和 maps), 打印类型和十六进制的引用地址. 虽然还不够理想, 但是依然是一个重大的进步, 并且 Kind 只关心底层表示, format.Any 也支持具名类型. 例如:

```go
var x int64 = 1
var d time.Duration = 1 * time.Nanosecond
fmt.Println(format.Any(x))                  // "1"
fmt.Println(format.Any(d))                  // "1"
fmt.Println(format.Any([]int64{x}))         // "[]int64 0x8202b87b0"
fmt.Println(format.Any([]time.Duration{d})) // "[]time.Duration 0x8202b87e0"
```

资料查询

> http://www.gopl.io/  
> http://golang-china.github.io/gopl-zh/

如果想看具体信息的话可以转到这里

> https://docs.hacknode.org/gopl-zh/ch12/ch12-01.html
