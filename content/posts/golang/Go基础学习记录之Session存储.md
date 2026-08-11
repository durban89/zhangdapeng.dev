---
title: "Go基础学习记录之Session存储"
date: "2025-08-01 11:35:22"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-session-cun-chu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Session存储/"
  - "/2025/08/01/Go基础学习记录之Session存储.html"
  - "/Go基础学习记录之Session存储/"
  - "/Go基础学习记录之Session存储.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-session-cun-chu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-session-cun-chu.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-session-cun-chu.html"
---
Session存储

我们在上篇文章中介绍了一个简单的Session管理器的工作原理，除此之外，我们还定义了一个Session存储接口。在本次分享中，我将展示一个实现此接口的基于内存的会话存储引擎的示例。您也可以将其定制为其他形式的Session存储。

```go
package memory

import (
	"container/list"
	"sync"
	"time"

	"github.com/durban89/wiki/session"
)

// Store 存储
type Store struct {
	sid      string                      // unique session is
	lastTime time.Time                   // last save time
	value    map[interface{}]interface{} // session value save inside
}

// Provider 寄存器
type Provider struct {
	lock     sync.RWMutex             // locker
	sessions map[string]*list.Element // map in memory
	list     *list.List               // for gc
}

var memoryProvider = &Provider{list: list.New(), sessions: make(map[string]*list.Element)}

// Set Session
func (s *Store) Set(key, value interface{}) error {
	s.value[key] = value
	memoryProvider.SessionUpdate(s.sid)
	return nil
}

// Get Session
func (s *Store) Get(key interface{}) interface{} {
	memoryProvider.SessionUpdate(s.sid)
	if v, ok := s.value[key]; ok {
		return v
	}

	return nil

}

// Del Session
func (s *Store) Del(key interface{}) error {
	delete(s.value, key)
	memoryProvider.SessionUpdate(s.sid)
	return nil
}

// SID Session ID
func (s *Store) SID() string {
	return s.sid
}

// SessionInit 一个Session
func (p *Provider) SessionInit(sid string) (session.Session, error) {
	memoryProvider.lock.Lock()
	defer memoryProvider.lock.Unlock()
	v := make(map[interface{}]interface{}, 0)
	store := &Store{
		sid:      sid,
		lastTime: time.Now(),
		value:    v,
	}

	res := memoryProvider.list.PushBack(store)
	memoryProvider.sessions[sid] = res

	return store, nil
}

// SessionRead 一个Session
func (p *Provider) SessionRead(sid string) (session.Session, error) {
	if v, ok := memoryProvider.sessions[sid]; ok {
		return v.Value.(*Store), nil
	}

	store, err := memoryProvider.SessionInit(sid)
	return store, err

}

// SessionDestroy 一个Session
func (p *Provider) SessionDestroy(sid string) error {
	if v, ok := memoryProvider.sessions[sid]; ok {
		delete(memoryProvider.sessions, sid)
		memoryProvider.list.Remove(v)
		return nil
	}

	return nil
}

// SessionGC 一个Session
func (p *Provider) SessionGC(maxLifeTime int64) {
	memoryProvider.lock.Lock()
	defer memoryProvider.lock.Unlock()

	for {
		v := memoryProvider.list.Back()
		if v == nil {
			break
		}

		if v.Value.(*Store).lastTime.Unix()+maxLifeTime < time.Now().Unix() {
			memoryProvider.list.Remove(v)
			delete(memoryProvider.sessions, v.Value.(*Store).sid)
		} else {
			break
		}
	}
}

// SessionUpdate 一个Session
func (p *Provider) SessionUpdate(sid string) error {
	memoryProvider.lock.Lock()
	defer memoryProvider.lock.Unlock()

	if v, ok := memoryProvider.sessions[sid]; ok {
		v.Value.(*Store).lastTime = time.Now()
		memoryProvider.list.MoveToFront(v)
	}

	return nil
}

func init() {
	memoryProvider.sessions = make(map[string]*list.Element, 0)
	session.RegisterProvider("memory", memoryProvider)
}
```

上面的示例实现了基于内存的Session存储机制。它使用其init()函数将此存储引擎注册到Session管理器。那么我们如何从主程序注册这个引擎呢？

```go
import (
	"github.com/durban89/wiki/session"

	// memory session provider
	_ "github.com/durban89/wiki/session/providers/memory"
)
```

我们使用空白导入机制（它将自动调用包的init()函数）将此引擎注册到Session管理器。然后，我们使用以下代码初始化Session管理器：

```go
var appSession *session.Manager

func init() {
	appSession, _ := session.GetManager("memory", "sessionid", 3600)

	go appSession.SessionGC()
}
```
