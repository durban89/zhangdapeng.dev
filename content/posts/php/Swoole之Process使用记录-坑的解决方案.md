---
title: "Swoole之Process使用记录-坑的解决方案"
date: "2025-07-10 11:52:27"
slug: "swoole-zhi-process-shi-yong-ji-lu-keng-de-jie-jue-fang-an"
categories: ["技术"]
tags: ["PHP", "Swoole"]
aliases:
  - "/2025/07/10/Swoole之Process使用记录-坑的解决方案/"
  - "/2025/07/10/Swoole之Process使用记录-坑的解决方案.html"
  - "/Swoole之Process使用记录-坑的解决方案/"
  - "/Swoole之Process使用记录-坑的解决方案.html"
  - "/2025/07/10/swoole-zhi-process-shi-yong-ji-lu-keng-de-jie-jue-fang-an/"
  - "/2025/07/10/swoole-zhi-process-shi-yong-ji-lu-keng-de-jie-jue-fang-an.html"
  - "/swoole-zhi-process-shi-yong-ji-lu-keng-de-jie-jue-fang-an.html"
---
Swoole之Process使用记录，Swoole自从发布之后，公司项目一直都只是基于http的情况使用，这次在脚本中应用了下，还是踩了些坑，先分享一个简单的

先看下一个简单的创建Process的流程

```php
class SwooleProcessDemo
{
    public $mpid = 0;
    public $works = [];
    public $max_process = 1;
    public $processes = [];
    public $new_index = 0;
    public $ctime = 0;

    public function __construct()
    {
        swoole_async_set(['enable_coroutine' => false]); // Process中仅用协程

        // 由于所有进程是共享使用一个消息队列，所以只需向一个子进程发送消息即可 - 注意队列大小限制
        try {
            if (!preg_match('/Darwin/', php_uname())) {
                swoole_set_process_name(sprintf('php-ps:%s', 'master'));
            }
            $this->mpid = posix_getpid();
            $this->run();

            $process = current($this->processes);

            swoole_timer_tick(1000, function () use ($process) {
                $data = '';
                // $data = $this->getData(); 这里是需要自己是实现的

                // push data
                $process->push(implode(',', $data));
            });

            $this->processWait();
        } catch (\Exception $e) {
            var_dump($e);
        }
    }

    public function run()
    {
        for ($i = 0; $i < $this->max_process; $i++) {
            $this->createProcess($i);
        }
    }

    public function createProcess($index = null)
    {
        $process = new swoole_process(function (swoole_process $worker) use ($index) {
            if (is_null($index)) {
                $index = $this->new_index;
                $this->new_index++;
            }

            if (!preg_match('/Darwin/', php_uname())) {
                try {
                    swoole_set_process_name(sprintf('php-ps:%s', $index));
                } catch (\Exception $e) {
                    var_dump('ALL ERROR:' . $e->getMessage());
                }
            }

            $data = $worker->pop();

            if (!$data) {
                $worker->exit(0);
            }

            if ($data) {
                $this->handleData($data);
                $this->checkMPid($worker);
            }
            unset($userId);
        }, false, false);

        $customMsgKey = 1;
        $mod = 2 | swoole_process::IPC_NOWAIT; //这里设置消息队列为非阻塞模式
        $process->useQueue($customMsgKey, $mod);
        $pid = $process->start();
        $this->works[$index] = $pid;
        $this->processes[$pid] = $process;

        return $pid;
    }

    public function checkMPid(&$worker)
    {
        if (!swoole_process::kill($this->mpid, 0)) {
            $worker->exit();
        }
    }

    public function rebootProcess($ret)
    {
        $pid = $ret['pid'];
        $index = array_search($pid, $this->works);

        if (false !== $index) {
            $index = intval($index);
            $new_pid = $this->createProcess($index);
        }
    }

    public function processWait()
    {
        swoole_timer_tick(1000, function () {
            if (count($this->works)) {
                $ret = swoole_process::wait();
                if ($ret) {
                    $this->rebootProcess($ret);
                }
            }
        });
    }

    private function handleData($data)
    {
        // 你自己的逻辑
    }
}
```

首先swoole\_async\_set(['enable\_coroutine' => false]);这里我关闭了协程，原因是在进行processWait操作的时候，其swoole\_timer\_tick是不允许在其内部创建Process的，这个可以试着启用后看下报错信息

这个例子应该是一个比较完整的例子了，实践当中都有在使用，唯一的问题是在push上，之前一个例子比如发送短信，这个要求实时性，也就push了一些用户的ID，大小的话，可以忽略，但是当我向队列中push足够打的字符串的话，就会提示内存不足，原因可以到这里查看：https://wiki.swoole.com/wiki/page/290.html

```php
swoole_timer_tick(1000, function () use ($process) {
    $data = '';
    // $data = $this->getData(); 这里是需要自己是实现的

    // push data
    $process->push(implode(',', $data));
});
```

解决方案如上代码，

之前的逻辑是for循环，然后直接执行push操作，在你push的时候，队列大小增加，最后直接内存满了，进程退出了，但是当我用上面代码的时候，这就是一个无限循环的永动机了。当然如果pop那边的操作延迟比较久的话，导致内存满了，也是push不进去的。

另外注意一点是swoole\_timer\_tick的函数的调用，不要使用while死循环，会导致swoole\_timer\_tick函数不起作用的，也就是

```php
public function processWait()
{
    swoole_timer_tick(1000, function () {
        if (count($this->works)) {
            $ret = swoole_process::wait();
            if ($ret) {
                $this->rebootProcess($ret);
            }
        }
    });
}
```

这个代码其实也可以用另外一个方式实现的，如下

```php
public function processWait()
{
    while (1) {
        if (count($this->works)) {
            $ret = swoole_process::wait();
            if ($ret) {
                $this->rebootProcess($ret);
            }
        } else {
            break;
        }
    }
}
```

总结如下：

1、swoole\_timer\_tick使用时，不要使用while等类似的死循环阻塞swoole\_timer\_tick的执行

2、Process在进行push的时候，要注意队列的大小
