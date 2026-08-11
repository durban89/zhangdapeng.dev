---
title: "Laravel 给生产环境添加监听事件 - SQL日志监听"
date: "2025-07-03 17:11:33"
slug: "laravel-gei-sheng-chan-huan-jing-tian-jia-jian-ting-shi-jian-sql-ri-zhi-jian-ting"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/03/Laravel-给生产环境添加监听事件-SQL日志监听/"
  - "/2025/07/03/Laravel-给生产环境添加监听事件-SQL日志监听.html"
  - "/Laravel-给生产环境添加监听事件-SQL日志监听/"
  - "/Laravel-给生产环境添加监听事件-SQL日志监听.html"
  - "/2025/07/03/Laravel-给生产环境添加监听事件/"
  - "/2025/07/03/Laravel-给生产环境添加监听事件.html"
  - "/2025/07/03/laravel-gei-sheng-chan-huan-jing-tian-jia-jian-ting-shi-jian-sql-ri-zhi-jian-ting/"
  - "/2025/07/03/laravel-gei-sheng-chan-huan-jing-tian-jia-jian-ting-shi-jian-sql-ri-zhi-jian-ting.html"
  - "/laravel-gei-sheng-chan-huan-jing-tian-jia-jian-ting-shi-jian-sql-ri-zhi-jian-ting.html"
---
**laravel版本：5.2.\***

# 一、创建监听器

```bash
php artisan make:listener QueryListener --event=Illuminate\\Database\\Events\\QueryExecuted
```

or

```bash
sudo /usr/local/bin/php artisan make:listener QueryListener --event=Illuminate\\Database\\Events\\QueryExecuted
```

会自动生成文件 app/Listeners/QueryListener.php

# 二、注册事件

打开 app/Providers/EventServiceProvider.php，在 $listen 中添加 Illuminate\Database\Events\QueryExecuted 事件的监听器为 QueryListener

```php
protected $listen = [  
    'Illuminate\Database\Events\QueryExecuted' => [
        'App\Listeners\QueryListener',
    ],
];
```

最终代码如下

```php
namespace App\Providers;
use Illuminate\Contracts\Events\Dispatcher as DispatcherContract;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;
class EventServiceProvider extends ServiceProvider
{
    /**
     * The event listener mappings for the application.
     *
     * @var array
     */
    protected $listen = [
        'App\Events\SomeEvent' => [
            'App\Listeners\EventListener',
        ],
        'Illuminate\Database\Events\QueryExecuted' => [
            'App\Listeners\QueryListener',
        ],
    ];
    /**
     * Register any other events for your application.
     *
     * @param  \Illuminate\Contracts\Events\Dispatcher  $events
     * @return void
     */
    public function boot(DispatcherContract $events)
    {
        parent::boot($events);
        //
    }
}
```

# 三、添加逻辑

打开 app/Listeners/QueryListener.php

光有一个空的监听器是不够的，我们需要自己实现如何把 $sql 记录到日志中。为此，对 QueryListener 进行改造，完善其 handle 方法如下:

```php
$sql = str_replace("?", "'%s'", $event->sql);
$log = vsprintf($sql, $event->bindings);
Log::info($log);
```

最终代码如下

```php
namespace App\Listeners;
use Log;
use Illuminate\Database\Events\QueryExecuted;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
class QueryListener
{
    /**
     * Create the event listener.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }
    /**
     * Handle the event.
     *
     * @param  QueryExecuted  $event
     * @return void
     */
    public function handle(QueryExecuted $event)
    {
        $sql = str_replace("?", "'%s'", $event->sql);
        $log = vsprintf($sql, $event->bindings);
        Log::info($log);
    }
}
```
