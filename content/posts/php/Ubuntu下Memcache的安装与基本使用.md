---
title: "Ubuntu下Memcache的安装与基本使用"
date: "2025-06-20 09:51:50"
slug: "ubuntu-xia-memcache-de-an-zhuang-yu-ji-ben-shi-yong"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/20/Ubuntu下Memcache的安装与基本使用/"
  - "/2025/06/20/Ubuntu下Memcache的安装与基本使用.html"
  - "/Ubuntu下Memcache的安装与基本使用/"
  - "/Ubuntu下Memcache的安装与基本使用.html"
  - "/2025/06/20/ubuntu-xia-memcache-de-an-zhuang-yu-ji-ben-shi-yong/"
  - "/2025/06/20/ubuntu-xia-memcache-de-an-zhuang-yu-ji-ben-shi-yong.html"
  - "/ubuntu-xia-memcache-de-an-zhuang-yu-ji-ben-shi-yong.html"
---
关于Memcache与memcached

Memcache是项目名，memcached是服务名。让很多初接触的人感觉很是莫名其妙。个人认为正确的应该是用前者用更为正确一点。

1)安装Memcache服务端

```bash
sudo apt-get install memcached
```

安装完Memcache服务端以后，我们需要启动该服务：

```bash
memcached -d -m 128 -p 11211 -u www
```

> memcached服务的启动参数：
>
> -p 监听的端口  
> -l 连接的IP地址, 默认是本机  
> -d start 启动memcached服务  
> -d restart 重起memcached服务  
> -d stop|shutdown 关闭正在运行的memcached服务  
> -d install 安装memcached服务  
> -d uninstall 卸载memcached服务  
> -u 以的身份运行 (仅在以root运行的时候有效)  
> -m 最大内存使用，单位MB。默认64MB  
> -M 内存耗尽时返回错误，而不是删除项  
> -c 最大同时连接数，默认是1024  
> -f 块大小增长因子，默认是1.25-n 最小分配空间，key+value+flags默认是48  
> -h 显示帮助

我们使用php脚本做一个测试(这个是在qeephp里面做的测试)

```php
public function actionTestMema(){
    ini_set("session.save_handler","memcache");
    ini_set("session.save_path","tcp://127.0.0.1:11211");
    session_start();
    $_SESSION['test0'] = 'my value';
    $_SESSION['test1'] = 'Thisvalue';
    $sid = session_id();
    
    echo "<a href='".url('default/testmemb',array('sid'=>$sid))."'>session</a>";
}

public function actionTestMemb(){
    $mem = new Memcache();
    $mem->connect('127.0.0.1',11211);
    
    if(isset($_REQUEST['sid'])){
            $value = $mem->getstats();
//                var_dump($value);
            $sess_value = $mem->get($_REQUEST['sid']);
            var_dump($sess_value);
            echo $sess_value;
    }else{
            echo "error args";
    }
}
```

其中：

```php
ini_set("session.save_handler","memcache");
ini_set("session.save_path","tcp://127.0.0.1:11211");
session_start();
```

这句话是应该放在myapp.php这个文件中的

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

如果你的输出结果是类似下面这样的话

```bash
string(2044) "test0|s:8:"my value";test1|s:9:"Thisvalue";
```

说明你的安装就成功了，以上是在非命令行模式下测试的。如果你是cli命令行的话，我不能保证。
