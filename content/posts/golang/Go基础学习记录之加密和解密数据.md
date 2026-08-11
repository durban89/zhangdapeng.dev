---
title: "Go基础学习记录之加密和解密数据"
date: "2025-08-04 11:38:56"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-jia-mi-he-jie-mi-shu-ju"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之加密和解密数据/"
  - "/2025/08/04/Go基础学习记录之加密和解密数据.html"
  - "/Go基础学习记录之加密和解密数据/"
  - "/Go基础学习记录之加密和解密数据.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-jia-mi-he-jie-mi-shu-ju/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-jia-mi-he-jie-mi-shu-ju.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-jia-mi-he-jie-mi-shu-ju.html"
---
## 加密和解密数据

上篇文章介绍了如何安全地存储密码，但有时可能需要修改已存储到数据库中的某些敏感加密数据。  
当需要数据解密时，我们应该使用对称加密算法，而不是我们之前介绍的单向散列技术。

### 高级加密和解密

Go语言在其crypto包中支持对称加密算法。  
如果您不知道自己在做什么，请不要在[GCM模式](https://en.wikipedia.org/wiki/Galois/Counter_Mode)下使用除AES之外的任何内容！  
1. crypto/aes包： AES（高级加密标准），也称为Rijndael加密方法，被美国联邦政府用作块加密标准。

在以下示例中，我们演示了如何在GCM模式下使用AES加密数据：

```go
package main

import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "errors"
    "fmt"
    "io"
    "log"
)

func main() {
    text := []byte("My name is Astaxie")
    key := []byte("the-key-has-to-be-32-bytes-long!")

    ciphertext, err := encrypt(text, key)
    if err != nil {
        // TODO: Properly handle error
        log.Fatal(err)
    }
    fmt.Printf("%s => %x\n", text, ciphertext)

    plaintext, err := decrypt(ciphertext, key)
    if err != nil {
        // TODO: Properly handle error
        log.Fatal(err)
    }
    fmt.Printf("%x => %s\n", ciphertext, plaintext)
}

func encrypt(plaintext []byte, key []byte) ([]byte, error) {
    c, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    gcm, err := cipher.NewGCM(c)
    if err != nil {
        return nil, err
    }

    nonce := make([]byte, gcm.NonceSize())
    if _, err = io.ReadFull(rand.Reader, nonce); err != nil {
        return nil, err
    }

    return gcm.Seal(nonce, nonce, plaintext, nil), nil
}

func decrypt(ciphertext []byte, key []byte) ([]byte, error) {
    c, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    gcm, err := cipher.NewGCM(c)
    if err != nil {
        return nil, err
    }

    nonceSize := gcm.NonceSize()
    if len(ciphertext) < nonceSize {
        return nil, errors.New("ciphertext too short")
    }

    nonce, ciphertext := ciphertext[:nonceSize], ciphertext[nonceSize:]
    return gcm.Open(nil, nonce, ciphertext, nil)
}
```

调用上述函数aes.NewCipher（其[]byte键参数必须为16,24或32，分别对应AES-128，AES-192或AES-256算法），返回一个实现三个的cipher.Block接口函数：

```go
type Block interface {
    // BlockSize returns the cipher's block size.
    BlockSize() int

    // Encrypt encrypts the first block in src into dst.
    // Dst and src may point at the same memory.
    Encrypt(dst, src []byte)

    // Decrypt decrypts the first block in src into dst.
    // Dst and src may point at the same memory.
    Decrypt(dst, src []byte)
}
```

这三个函数实现加密和解密操作;  
有关更详细的说明，请参阅Go文档。

### 小结

本节介绍可根据Web应用程序的加密和解密需求以不同方式使用的加密算法。  
对于具有基本安全要求的应用程序，建议在GCM模式下使用AES。
