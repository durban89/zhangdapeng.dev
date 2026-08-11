---
title: "如何使用Property Wrappers - State和Binding"
date: "2025-07-15 09:50:57"
slug: "ru-he-shi-yong-property-wrappers-state-he-binding"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/15/如何使用Property-Wrappers-State和Binding/"
  - "/2025/07/15/如何使用Property-Wrappers-State和Binding.html"
  - "/如何使用Property-Wrappers-State和Binding/"
  - "/如何使用Property-Wrappers-State和Binding.html"
  - "/2025/07/15/ru-he-shi-yong-property-wrappers-state-he-binding/"
  - "/2025/07/15/ru-he-shi-yong-property-wrappers-state-he-binding.html"
  - "/ru-he-shi-yong-property-wrappers-state-he-binding.html"
---
### State Property Wrappers 的用法

示例如下

```cs
struct MyView: View {
    @State var myString: String = "Hello"
    var body: some View {
        OtherView(shareText: $myString)
    }
}
```

### Binding Property Wrappers 的用法

示例如下

```cpp
struct OtherView: View {
    @Binding var shareText: String

    var body: some View {
        Text(shareText)
    }
}
```

最后调用下MyView，如下（建议Playground中运行）

```cs
MyView(myString: "Hello world")
```
