---
title: "Yii2结合Workerman的websocket"
date: "2025-07-09 10:42:12"
slug: "yii2-jie-he-workerman-de-websocket"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/07/09/Yii2结合Workerman的websocket/"
  - "/2025/07/09/Yii2结合Workerman的websocket.html"
  - "/Yii2结合Workerman的websocket/"
  - "/Yii2结合Workerman的websocket.html"
  - "/2025/07/09/yii2-jie-he-workerman-de-websocket/"
  - "/2025/07/09/yii2-jie-he-workerman-de-websocket.html"
  - "/yii2-jie-he-workerman-de-websocket.html"
---
## 1、安装workerman

```bash
composer require workerman/workerman
```

## 2、启动workerman

创建commands/WorkermanWebSocketController.php文件  
创建actionIndex()函数，用来启动，代码如下

```php
public function actionIndex()
{
    if ('start' == $this->send) {
        try {
            $this->start($this->daemon);
        } catch (\Exception $e) {
            $this->stderr($e->getMessage() . "\n", Console::FG_RED);
        }
    } else if ('stop' == $this->send) {
        $this->stop();
    } else if ('restart' == $this->send) {
        $this->restart();
    } else if ('reload' == $this->send) {
        $this->reload();
    } else if ('status' == $this->send) {
        $this->status();
    } else if ('connections' == $this->send) {
        $this->connections();
    }
}
```

### 添加初始化模块

```php
public function initWorker()
{
    $ip = isset($this->config['ip']) ? $this->config['ip'] : $this->ip;
    $port = isset($this->config['port']) ? $this->config['port'] : $this->port;
    $wsWorker = new Worker("websocket://{$ip}:{$port}");

    // 4 processes
    $wsWorker->count = 4;

    // Emitted when new connection come
    $wsWorker->onConnect = function ($connection) {
        echo "New connection\n";
    };

    // Emitted when data received
    $wsWorker->onMessage = function ($connection, $data) {
        // Send hello $data
        $connection->send('hello ' . $data);
    };

    // Emitted when connection closed
    $wsWorker->onClose = function ($connection) {
        echo "Connection closed\n";
    };
}
```

### 添加启动模块

```php
/**
 * workman websocket start
 */
public function start()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'start';
    if ($this->daemon) {
        $argv[2] = '-d';
    }

    // Run worker
    Worker::runAll();
}
```

### 添加停止模块

```php
/**
 * workman websocket stop
 */
public function stop()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'stop';
    if ($this->gracefully) {
        $argv[2] = '-g';
    }

    // Run worker
    Worker::runAll();
}
```

### 添加重启模块

```php
/**
 * workman websocket restart
 */
public function restart()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'restart';
    if ($this->daemon) {
        $argv[2] = '-d';
    }

    if ($this->gracefully) {
        $argv[2] = '-g';
    }

    // Run worker
    Worker::runAll();
}
```

### 添加重载模块

```php
/**
 * workman websocket reload
 */
public function reload()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'reload';
    if ($this->gracefully) {
        $argv[2] = '-g';
    }

    // Run worker
    Worker::runAll();
}
```

### 添加状态模块

```php
/**
 * workman websocket status
 */
public function status()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'status';
    if ($this->daemon) {
        $argv[2] = '-d';
    }

    // Run worker
    Worker::runAll();
}
```

### 添加链接数模块

```php
/**
 * workman websocket connections
 */
public function connections()
{
    $this->initWorker();
    // 重置参数以匹配Worker
    global $argv;
    $argv[0] = $argv[1];
    $argv[1] = 'connections';

    // Run worker
    Worker::runAll();
}
```

## 3、前端调用

```html
<script>
  // Create WebSocket connection.
  const ws = new WebSocket('ws://{{ app.request.hostName }}:2347/'); // 这里是获取的网站的域名，测试的时候可以改为自己的本地的ip地址

  // Connection opened
  ws.addEventListener('open', function (event) {
      ws.send('Hello Server!');
  });

  // Listen for messages
  ws.addEventListener('message', function (event) {
      console.log('Message from server ', event.data);
  });

  setTimeout(function() {
    ws.send('ssssss');
  }, 10000);

</script>
```

## 4、config参数配置

修改console.php并添加如下代码

```php
'controllerMap' => [
    'workerman-web-socket' => [
        'class' => 'app\commands\WorkermanWebSocketController',
        'config' => [
            'ip' => '127.0.0.1',
            'port' => '2346',
            'daemonize' => true,
        ],
    ],
],
```

## 5、nginx配置

为什么会用 nginx， 我们正常部署上线是不可能直接使用ip的，这个户存在安全隐患，最好是绑定一个域名

```bash
server {
    charset utf-8;
    client_max_body_size 128M;

    listen 2347;

    server_name www.gowhich.com; # 这里改为自己的域名

    access_log   /xxx.workerman.access.log; # 换成自己服务器的nginx日志路径
    error_log    /xxx.workerman.error.log; # 换成自己服务器的nginx日志路径

     location / {
        proxy_pass http://127.0.0.1:2346; # 代理2346 也可以根据项目配置为自己的端口

        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

重新nginx

```bash
nginx -s relad 或者 sudo nginx -s reload
```

然后将第3步的代码加入自己做的视图中，如果没有问题的话，websocket启动后就能正常通讯了。

## 6、启动workerman websocket

```bash
// 启动
./yii workerman-web-socket -s start -d
```

如果没有问题的话会得到类似如下的结果

```bash
$ ./yii workerman-web-socket -s start -d
Workerman[workerman-web-socket] start in DAEMON mode
----------------------- WORKERMAN -----------------------------
Workerman version:3.5.13          PHP version:7.1.16
------------------------ WORKERS -------------------------------
user          worker        listen                      processes status
durban        none          websocket://127.0.0.1:2346   4         [OK] 
----------------------------------------------------------------
Input "php workerman-web-socket stop" to stop. Start success.
```

## 7、其他

commands/WorkermanWebSocketController.php 完整代码如下

```php
<?php
/**
 * WorkmanWebSocket 服务相关
 */

namespace app\commands;

use Workerman\Worker;
use yii\console\Controller;
use yii\helpers\Console;

/**
 *
 * WorkermanWebSocket
 *
 * @author durban.zhang <[email protected]>
 */

class WorkermanWebSocketController extends Controller
{
    public $send;
    public $daemon;
    public $gracefully;

    // 这里不需要设置，会读取配置文件中的配置
    public $config = [];
    private $ip = '127.0.0.1';
    private $port = '2346';

    public function options($actionID)
    {
        return ['send', 'daemon', 'gracefully'];
    }

    public function optionAliases()
    {
        return [
            's' => 'send',
            'd' => 'daemon',
            'g' => 'gracefully',
        ];
    }

    public function actionIndex()
    {
        if ('start' == $this->send) {
            try {
                $this->start($this->daemon);
            } catch (\Exception $e) {
                $this->stderr($e->getMessage() . "\n", Console::FG_RED);
            }
        } else if ('stop' == $this->send) {
            $this->stop();
        } else if ('restart' == $this->send) {
            $this->restart();
        } else if ('reload' == $this->send) {
            $this->reload();
        } else if ('status' == $this->send) {
            $this->status();
        } else if ('connections' == $this->send) {
            $this->connections();
        }
    }

    public function initWorker()
    {
        $ip = isset($this->config['ip']) ? $this->config['ip'] : $this->ip;
        $port = isset($this->config['port']) ? $this->config['port'] : $this->port;
        $wsWorker = new Worker("websocket://{$ip}:{$port}");

        // 4 processes
        $wsWorker->count = 4;

        // Emitted when new connection come
        $wsWorker->onConnect = function ($connection) {
            echo "New connection\n";
        };

        // Emitted when data received
        $wsWorker->onMessage = function ($connection, $data) {
            // Send hello $data
            $connection->send('dddd hello ' . $data);
        };

        // Emitted when connection closed
        $wsWorker->onClose = function ($connection) {
            echo "Connection closed\n";
        };
    }

    /**
     * workman websocket start
     */
    public function start()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'start';
        if ($this->daemon) {
            $argv[2] = '-d';
        }

        // Run worker
        Worker::runAll();
    }

    /**
     * workman websocket restart
     */
    public function restart()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'restart';
        if ($this->daemon) {
            $argv[2] = '-d';
        }

        if ($this->gracefully) {
            $argv[2] = '-g';
        }

        // Run worker
        Worker::runAll();
    }

    /**
     * workman websocket stop
     */
    public function stop()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'stop';
        if ($this->gracefully) {
            $argv[2] = '-g';
        }

        // Run worker
        Worker::runAll();
    }

    /**
     * workman websocket reload
     */
    public function reload()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'reload';
        if ($this->gracefully) {
            $argv[2] = '-g';
        }

        // Run worker
        Worker::runAll();
    }

    /**
     * workman websocket status
     */
    public function status()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'status';
        if ($this->daemon) {
            $argv[2] = '-d';
        }

        // Run worker
        Worker::runAll();
    }

    /**
     * workman websocket connections
     */
    public function connections()
    {
        $this->initWorker();
        // 重置参数以匹配Worker
        global $argv;
        $argv[0] = $argv[1];
        $argv[1] = 'connections';

        // Run worker
        Worker::runAll();
    }
}
```

workerman websocket支持的其他命令

### 重启

```bash
$ ./yii workerman-web-socket -s restart -d
Workerman[workerman-web-socket] restart 
Workerman[workerman-web-socket] is stopping ...
Workerman[workerman-web-socket] stop success
----------------------- WORKERMAN -----------------------------
Workerman version:3.5.13          PHP version:7.1.16
------------------------ WORKERS -------------------------------
user          worker        listen                      processes status
durban        none          websocket://127.0.0.1:2346   4         [OK] 
----------------------------------------------------------------
Input "php workerman-web-socket stop" to stop. Start success.
```

### 重载

```bash
$ ./yii workerman-web-socket -s reload   
Workerman[workerman-web-socket] reload 
```

### 状态

```bash
$ ./yii workerman-web-socket -s status -g
Workerman[workerman-web-socket] status 
----------------------------------------------GLOBAL STATUS----------------------------------------------------
Workerman version:3.5.13          PHP version:7.1.16
start time:2018-09-10 11:22:15   run 0 days 0 hours   
load average: 1.79, 2, 2         event-loop:\Workerman\Events\Swoole
1 workers       4 processes
worker_name  exit_status      exit_count
none         0                12
----------------------------------------------PROCESS STATUS---------------------------------------------------
pid    memory  listening                  worker_name  connections send_fail timers  total_request qps    status
8283    4M      websocket://127.0.0.1:2346 none         0           0         0       0             0      [idle]
8284    4M      websocket://127.0.0.1:2346 none         0           0         0       0             0      [idle]
8285    4M      websocket://127.0.0.1:2346 none         0           0         0       0             0      [idle]
8286    4M      websocket://127.0.0.1:2346 none         0           0         0       0             0      [idle]
----------------------------------------------PROCESS STATUS---------------------------------------------------
Summary    16M     -                          -            0           0         0       0             0      [Summary] 
```

### 连接数

```bash
 ./yii workerman-web-socket -s connections
Workerman[workerman-web-socket] connections 
--------------------------------------------------------------------- WORKERMAN CONNECTION STATUS --------------------------------------------------------------------------------
PID      Worker          CID       Trans   Protocol        ipv4   ipv6   Recv-Q       Send-Q       Bytes-R      Bytes-W       Status         Local Address          Foreign Address
```

我这里暂时连接的，所以没有连接的信息

### 停止

```bash
$ ./yii workerman-web-socket -s stop          
Workerman[workerman-web-socket] stop 
Workerman[workerman-web-socket] is stopping ...
Workerman[workerman-web-socket] stop success
```
