---
title: "Go基础学习记录之如何在Golang中使用Session"
date: "2025-08-01 11:35:14"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-ru-he-zai-golang-zhong-shi-yong-session"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之如何在Golang中使用Session/"
  - "/2025/08/01/Go基础学习记录之如何在Golang中使用Session.html"
  - "/Go基础学习记录之如何在Golang中使用Session/"
  - "/Go基础学习记录之如何在Golang中使用Session.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-zai-golang-zhong-shi-yong-session/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-zai-golang-zhong-shi-yong-session.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-zai-golang-zhong-shi-yong-session.html"
---
Session背后的基本原则是服务器维护每个客户端的信息，客户端依赖唯一的SessionID来访问此信息。  
当用户访问Web应用程序时，服务器将根据需要使用以下三个步骤创建新Session：

1. 创建唯一的Session ID  
2. 打开数据存储空间：通常我们将Session保存在内存中，但如果系统意外中断，您将丢失所有Session数据。如果Web应用程序处理敏感数据（例如电子商务），这可能是一个非常严重的问题。为了解决此问题，您可以将Session数据保存在数据库或文件系统中。这使得数据持久性更加可靠，并且易于与其他应用程序共享，但需要权衡的是，读取和写入这些Session需要更多的服务器端IO。  
3. 将唯一SessionID发送到客户端。

这里的关键步骤是将唯一Session ID发送到客户端。在标准HTTP响应的上下文中，您可以使用响应行，标题或正文来完成此操作;因此，我们有两种方法将Session ID发送给客户端：通过cookie或URL重写。

1. Cookie：服务器可以轻松地在响应标头内使用Set-cookie将Session ID发送到客户端，然后客户端可以将此cookie用于将来的请求;我们经常将包含Session信息的cookie的到期时间设置为0，这意味着cookie将保存在内存中，并且只有在用户关闭浏览器后才会被删除。  
2. URL重写：将Session ID作为参数附加到所有页面的URL中。这种方式看起来很混乱，但如果客户在浏览器中禁用了cookie，那么这是最好的选择。

## **使用Go来管理Session**

## Session管理设计

1. 全局Session管理。  
2. 保持Session ID唯一。  
3. 为每个用户准备一个Session。  
4. Session存储在内存，文件或数据库中。  
5. 处理过期的Session。

接下来，通过完整实例来演示下如何实现上面的设计

### 全局Session管理

定义全局Session管理器：

```go
// Manager Session管理
type Manager struct {
    cookieName  string
    lock        sync.Mutex
    provider    Provider
    maxLifeTime int64
}
// GetManager 获取Session Manager
func GetManager(providerName string, cookieName string, maxLifeTime int64) (*Manager, error) {
    provider, ok := providers[providerName]
    if !ok {
        return nil, fmt.Errorf("session: unknown provide %q (forgotten import?)", providerName)
    }    

    return &Manager{
        cookieName:  cookieName,
        maxLifeTime: maxLifeTime,
        provider:    provider,
    }, nil
}
```

在main()函数中创建一个全局Session管理器：

```go
var appSession *Manager

// 初始化session manager
func init() {
	appSession, _ = GetManager("memory", "sessionid", 3600)

	go appSession.SessionGC()
}
```

我们知道我们可以通过多种方式保存Session，包括内存，文件系统或直接进入数据库。我们需要定义一个Provider接口，以表示Session管理器的底层结构：

```go
// Provider 接口
type Provider interface {
    SessionInit(sid string) (Session, error)
    SessionRead(sid string) (Session, error)
    SessionDestroy(sid string) error
    SessionGC(maxLifeTime int64)
}
```

1. SessionInit实现Session的初始化，如果成功则返回新Session。  
2. SessionRead返回由相应sid表示的Session。创建一个新Session，如果它尚不存在则返回它。  
3. SessionDestroy给定一个sid，删除相应的Session。  
4. SessionGC根据maxLifeTime删除过期的Session变量。那么我们的Session接口应该有什么方法呢？如果您有任何Web开发经验，您应该知道Session只有四个操作：设置值，获取值，删除值和获取当前Session ID。因此，我们的Session接口应该有四种方法来执行这些操作。

```go
// Session 接口
type Session interface {
    Set(key, value interface{}) error // 设置Session
    Get(key interface{}) interface{}  // 获取Session
    Del(key interface{}) error        // 删除Session
    SID() string                      // 当前Session ID
}
```

这个设计源于database/sql/driver，它首先定义接口，然后在我们想要使用它时注册特定的结构。以下代码是Session寄存器功能的内部实现。

```go
var providers = make(map[string]Provider)

// RegisterProvider 注册Session 寄存器
func RegisterProvider(name string, provider Provider) {
    if provider == nil {
        panic("session: Register provider is nil")
    }

    if _, p := providers[name]; p {
        panic("session: Register provider is existed")
    }

    providers[name] = provider
}
```

保持Session ID唯一

Session ID用于标识Web应用程序的用户，因此它们必须是唯一的。以下代码显示了如何实现此目标：

```go
// GenerateSID 产生唯一的Session ID
func (m *Manager) GenerateSID() string {
    b := make([]byte, 32)
    if _, err := io.ReadFull(rand.Reader, b); err != nil {
        return ""
    }
    return base64.URLEncoding.EncodeToString(b)
}
```

### 创建Session

我们需要分配或获取现有Session以验证用户操作。SessionStart函数用于检查与当前用户相关的任何Session的存在，并在未找到任何Session时创建新Session。

```go
// SessionStart 启动Session功能
func (m *Manager) SessionStart(w http.ResponseWriter, r *http.Request) (session Session) {
    m.lock.Lock()
    defer m.lock.Unlock()
    cookie, err := r.Cookie(m.cookieName)
    if err != nil || cookie.Value == "" {
        sid := m.GenerateSID()
        session, _ := m.provider.SessionInit(sid)
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
        session, _ := m.provider.SessionRead(sid)
    }

    return
}
```

以下是使用Session进行登录操作的示例。

```go
func login(w http.ResponseWriter, r *http.Request) {
    sess := appSession.SessionStart(w, r)
    r.ParseForm()
    if r.Method == "GET" {
        t, _ := template.ParseFiles("login.html")
        w.Header().Set("Content-Type", "text/html")
        t.Execute(w, sess.Get("username"))
    } else {
        sess.Set("username", r.Form["username"])
        http.Redirect(w, r, "/", 302)
    }
}
```

### Session的相关操作

SessionStart函数返回实现Session接口的变量。我们如何使用它？您在上面的示例中看到了session.Get("uid")以进行基本操作。现在让我们来看一个更详细的例子。

```go
func count(w http.ResponseWriter, r *http.Request) {
    sess := appSession.SessionStart(w, r)
    createtime := sess.Get("createtime")
    if createtime == nil {
        sess.Set("createtime", time.Now().Unix())
    } else if (createtime.(int64) + 360) < (time.Now().Unix()) {
        appSession.SessionDestroy(w, r)
        sess = appSession.SessionStart(w, r)
    }
    ct := sess.Get("countnum")
    if ct == nil {
        sess.Set("countnum", 1)
    } else {
        sess.Set("countnum", (ct.(int) + 1))
    }
    t, _ := template.ParseFiles("count.html")
    w.Header().Set("Content-Type", "text/html")
    t.Execute(w, sess.Get("countnum"))
}
```

如您所见，对Session进行操作只需在Set，Get和Delete操作中使用键/值模式。由于Session具有到期时间的概念，因此我们定义GC以更新Session的最新修改时间。这样，GC将不会删除已过期但仍在使用的Session。

### 注销Session

我们知道Web应用程序具有注销操作。当用户注销时，我们需要删除相应的Session。我们已经在上面的示例中使用了重置操作 - 现在让我们看一下函数体。

```go
// SessionDestory 注销Session
func (m *Manager) SessionDestory(w http.ResponseWriter, r *http.Request) {
    cookie, err := r.Cookie(m.cookieName)
    if err != nil || cookie.Value == "" {
        return
    }

    m.lock.Lock()
    defer m.lock.Unlock()
    m.provider.SessionDestroy(cookie.Value)
    expiredTime := time.Now()
    newCookie := http.Cookie{
        Name:     m.cookieName,
        Path:     "/",
        HttpOnly: true,
        Expires:  expiredTime,
        MaxAge:   -1,
    }
    http.SetCookie(w, &newCookie)
}
```

### 删除Session

让我们看看如何让Session管理器删除Session。我们需要在main()函数中启动GC：

```go
func init() {
    go appSession.SessionGC()
}

// SessionGC Session 垃圾回收
func (m *Manager) SessionGC() {
    m.lock.Lock()
    defer m.lock.Unlock()
    m.provider.SessionGC(m.maxLifeTime)
    time.AfterFunc(time.Duration(m.maxLifeTime), func() {
        m.SessionGC()
    })
}
```

我们看到GC充分利用了时间包中的计时器功能。  
它会在Session超时时自动调用GC，确保在maxLifeTime期间所有Session都可用。  
类似的解决方案可用于计算在线用户。
