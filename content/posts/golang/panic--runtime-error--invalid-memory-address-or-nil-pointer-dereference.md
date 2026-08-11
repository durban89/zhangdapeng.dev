---
title: "panic: runtime error: invalid memory address or nil pointer dereference"
date: "2025-08-01 11:35:18"
slug: "panic-runtime-error-invalid-memory-address-or-nil-pointer-dereference"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/panic:-runtime-error:-invalid-memory-address-or-nil-pointer-dereference/"
  - "/2025/08/01/panic:-runtime-error:-invalid-memory-address-or-nil-pointer-dereference.html"
  - "/panic:-runtime-error:-invalid-memory-address-or-nil-pointer-dereference/"
  - "/panic:-runtime-error:-invalid-memory-address-or-nil-pointer-dereference.html"
  - "/2025/08/01/panic-runtime-error-invalid-memory-address-or-nil-pointer-dereference/"
  - "/2025/08/01/panic-runtime-error-invalid-memory-address-or-nil-pointer-dereference.html"
  - "/panic-runtime-error-invalid-memory-address-or-nil-pointer-dereference.html"
---
**panic: runtime error: invalid memory address or nil pointer dereference**

关于这个错误问题`panic: runtime error: invalid memory address or nil pointer dereference`，我是如何解决的

一般这个问题的出现，从提示上意思意思是无效的内存地址或空指针  
我遇到的问题是这样的我写了一个Session管理器，其中有一个函数是这样的

```go
// SessionStart 启动Session功能
func (m *Manager) SessionStart(w http.ResponseWriter, r *http.Request) (session Session, err error) {
    m.lock.Lock()
    defer m.lock.Unlock()
    cookie, err := r.Cookie(m.cookieName)

    if err != nil || cookie.Value == "" {
        sid := m.GenerateSID()
        session, err = m.provider.SessionInit(sid)
        if err != nil {
            return nil, err
        }
        newCookie := http.Cookie{
            Name:     m.cookieName,
            Value:    url.QueryEscape(sid),
            Path:     "/",
            HttpOnly: true,
            MaxAge:   int(m.maxLifeTime),
        }
        http.SetCookie(w, &newCookie)
    } else {
        sid, _ := url.QueryUnescape(cookie.Value)
        session, _ = m.provider.SessionRead(sid)
    }

    return
}
```

然后我在使用的时候，是这样的

```go
var appSession *session.Manager

// WelcomeLogin 欢迎登录页
func WelcomeLogin(w http.ResponseWriter, r *http.Request) {
    _, err := appSession.SessionStart(w, r)
    if err != nil {
        fmt.Println(err)
        return
    }

    cookie, err := r.Cookie("sessionid")
    if err != nil {
        fmt.Fprintf(w, "session")
    }

    fmt.Fprintf(w, cookie.Value)
}

func init() {
    appSession, _ := session.GetManager("memory", "sessionid", 3600)

    go appSession.SessionGC()
}
```

这段两端代码正常编译是没有任何问题，但是在调用WelcomeLogin的时候就报错了，因为WelcomeLogin函数调用了SessionStart，而SessionStart又调用了m.lock.Lock()。  
这里注意m.lock.Lock()中的m，从错误提示上看是m的郭，问题在哪里呢，我通过记录日志的方式找到了原因，其实

```go
appSession, _ := session.GetManager("memory", "sessionid", 3600)
```

这段代码和下面

```go
appSession, _ = session.GetManager("memory", "sessionid", 3600)
```

这段代码是有很大区别的  
使用第一段的时候  
appSession得到的值是nil，而使用第二段的代码的时候就能正常赋值了。

这个问题在以后使用init进行操作变量重新赋值的时候一定要注意。为什么我能突然想到这个问题，因为我之前的几篇文章是写如何使用MySQL的，其中有个init中初始化的时候，重新赋值连接的变量涉及到这个问题，但是的做法就是直接赋值，并没有通过':='的方式赋值

```go
// MySQLDB Conn
var MySQLDB *sql.DB

func init() {
    db, err := sql.Open("mysql", "root:123456@/wiki?charset=utf8")
    MySQLDB = db
    checkErr(err)
}
```
