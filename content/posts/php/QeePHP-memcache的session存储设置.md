---
title: "QeePHP memcache的session存储设置"
date: "2025-06-20 09:51:54"
slug: "qeephp-memcache-de-session-cun-chu-she-zhi"
categories: ["技术"]
tags: ["PHP", "QeePHP"]
aliases:
  - "/2025/06/20/QeePHP-memcache的session存储设置/"
  - "/2025/06/20/QeePHP-memcache的session存储设置.html"
  - "/QeePHP-memcache的session存储设置/"
  - "/QeePHP-memcache的session存储设置.html"
  - "/2025/06/20/qeephp-memcache-de-session-cun-chu-she-zhi/"
  - "/2025/06/20/qeephp-memcache-de-session-cun-chu-she-zhi.html"
  - "/qeephp-memcache-de-session-cun-chu-she-zhi.html"
---
关于session的memcache的存储，原因为什么要使用它。要看你的项目的需求，网站访问量大的话，默认使用session的文件存储，会导致一个问题就是用户登录不了，原始是，session文件的大量生成，导致读取文件出现问题，就是IO的问题，这时候我们可以考虑使用memcache，还有另外一种是mysql的使用方式。但是目前对于我的这个项目还打不到这种需求，so，还是使用memcache吧。

目前又因为我的项目是使用Qeephp，哈哈，估计现在使用的人少了，不过这里还是说一下，使用他如何进行配置吧。

用过qee的都知道，qee有个文件叫做myapp的文件，ok，解决的问题的办法就在这里。

代码如下

```php
// 打开 session
if (Q::ini('runtime_session_start'))
{
	ini_set("session.save_handler","memcache");
	ini_set("session.save_path","tcp://127.0.0.1:11211");
	session_start();
	            
	// #IFDEF DEBUG
	QLog::log('session_start()', QLog::DEBUG);
	QLog::log('session_id: ' . session_id(), QLog::DEBUG);
	// #ENDIF
}
```

其实就是在打开session的地方加上了关于session的存储设置

```php
ini_set("session.save_handler","memcache");
ini_set("session.save_path","tcp://127.0.0.1:11211");
```

memcache考虑的还是蛮周到。

关于memcache的安装，请使用站内搜索
