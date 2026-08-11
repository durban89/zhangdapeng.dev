---
title: "Go基础学习记录之密码存储"
date: "2025-08-04 11:38:52"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-mi-ma-cun-chu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之密码存储/"
  - "/2025/08/04/Go基础学习记录之密码存储.html"
  - "/Go基础学习记录之密码存储/"
  - "/Go基础学习记录之密码存储.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-mi-ma-cun-chu/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-mi-ma-cun-chu.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-mi-ma-cun-chu.html"
---
## 密码存储

多年来，许多网站都遭遇了用户密码数据的破坏。  
甚至像Linkedin和CSDN.net这样的顶级互联网公司也受到了影响。  
整个互联网都感受到了这些事件的影响，不容小觑。  
对于今天的互联网用户来说尤其如此，他们经常习惯在许多不同的网站上使用相同的密码。

作为Web开发人员，我们在实现密码存储方案时有很多选择。  
然而，这种自由往往是一把双刃剑。  
那么常见的陷阱是什么？我们如何避免陷入它们？

### 不好的解决方案

目前，最常用的密码存储方案是在存储它们之前使用单向散列明文密码。  
单向散列的最重要特征是在给定散列数据的情况下恢复原始数据是不可行的 - 因此单向散列中的“单向”。  
常用的加密单向散列算法包括SHA-256，SHA-1，MD5等。实例如下：

```go
//import "crypto/sha256"
h := sha256.New()
io.WriteString(h, "His money is twice tainted: 'taint yours and 'taint mine.")
fmt.Printf("% x", h.Sum(nil))

//import "crypto/sha1"
h := sha1.New()
io.WriteString(h, "His money is twice tainted: 'taint yours and 'taint mine.")
fmt.Printf("% x", h.Sum(nil))

//import "crypto/md5"
h := md5.New()
io.WriteString(h, "需要加密的密码")
fmt.Printf("%x", h.Sum(nil))
```

单向散列有两个关键特性：

1. 给定密码的单向散列，结果摘要始终是唯一确定的。  
2. 计算速度。随着技术的进步，完成数十亿次单向散列计算只需要一秒钟。

鉴于上述两个特征的组合，并考虑到大多数人使用某些公共密码组合的事实，攻击者可以计算所有常用密码的组合。  
即使您存储在数据库中的密码可能只是哈希值，但如果攻击者可以访问此数据库，他们可以将存储的哈希值与其预先计算的哈希值进行比较，以获得相应的密码。  
这种类型的攻击依赖于通常称为彩虹表的东西。

我们可以看到使用单向哈希散列用户数据可能还不够。  
一旦网站的数据库泄露，用户的原始密码可能会向全世界泄露。

### 好的解决方案

上面提到的方法可能足以抵御几年前的大多数黑客攻击，因为大多数攻击者都没有计算资源来计算大型彩虹表。  
但是，随着并行计算能力的提高，这些类型的攻击变得越来越可行。

鉴于时间和内存资源的实际限制，我们如何安全地存储密码以便第三方无法解密？  
解决方案是计算散列密码以故意增加资源量和破解它所需的时间。  
我们想要设计一个哈希，以便没有人可能拥有计算所需彩虹表所需的资源。

非常安全的系统利用散列算法，该算法考虑了计算给定密码摘要所需的时间和资源。  
这允许我们创建大规模执行计算成本高的密码摘要。  
计算的强度越大，攻击者预先计算彩虹表就越困难 - 以至于尝试它甚至是不可行的。

在Go中，建议您使用bcrypt包。包的源代码可以在以下链接中找到：  
https://github.com/golang/crypto/blob/master/bcrypt/bcrypt.go

以下是一个示例代码段，可用于散列，存储和验证用户密码：

```go
package main

import (
    "fmt"
    "log"

    "golang.org/x/crypto/bcrypt"
)

func main() {
    userPassword1 := "some user-provided password"

    // Generate "hash" to store from user password
    hash, err := bcrypt.GenerateFromPassword([]byte(userPassword1), bcrypt.DefaultCost)
    if err != nil {
        // TODO: Properly handle error
        log.Fatal(err)
    }
    fmt.Println("Hash to store:", string(hash))
    // Store this "hash" somewhere, e.g. in your database

    // After a while, the user wants to log in and you need to check the password he entered
    userPassword2 := "some user-provided password"
    hashFromDatabase := hash

    // Comparing the password with the hash
    if err := bcrypt.CompareHashAndPassword(hashFromDatabase, []byte(userPassword2)); err != nil {
        // TODO: Properly handle error
        log.Fatal(err)
    }

    fmt.Println("Password was correct!")
}
```

### 小结

如果您担心在线生活的安全性，可以采取以下步骤：  
1. 作为普通的互联网用户，我们建议使用LastPass进行密码存储和生成;  
在不同的网站上使用不同的密码  
2. 作为Go Web开发人员，我们强烈建议您使用上述专业且经过良好测试的方法之一来存储用户密码。
