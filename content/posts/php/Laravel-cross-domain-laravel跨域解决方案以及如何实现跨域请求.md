---
title: "laravel cross domain - laravel跨域解决方案以及如何实现跨域请求"
date: "2025-07-14 14:45:07"
slug: "laravel-cross-domain-laravel-kua-yu-jie-jue-fang-an-yi-ji-ru-he-shi-xian-kua-yu-qing-qiu"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/14/laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求/"
  - "/2025/07/14/laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求.html"
  - "/laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求/"
  - "/laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求.html"
  - "/2025/07/14/Laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求/"
  - "/2025/07/14/Laravel-cross-domain-laravel跨域解决方案以及如何实现跨域请求.html"
  - "/2025/07/14/laravel-cross-domain-laravel-kua-yu-jie-jue-fang-an-yi-ji-ru-he-shi-xian-kua-yu-qing-qi/"
  - "/2025/07/14/laravel-cross-domain-laravel-kua-yu-jie-jue-fang-an-yi-ji-ru-he-shi-xian-kua-yu-qin.html"
  - "/laravel-cross-domain-laravel-kua-yu-jie-jue-fang-an-yi-ji-ru-he-shi-xian-kua-yu-qing-qiu.html"
---
我们在用 laravel 进行开发的时候，特别是前后端完全分离的时候，由于前端项目运行在自己机器的指定端口 (也可能是其他人的机器) ， 例如 localhost:8000 , 而 laravel 程序又运行在另一个端口，这样就跨域了，而由于浏览器的同源策略，跨域请求是非法的。其实这个问题很好解决，只需要添加一个中间件就可以了。

中间件代码如下

```php
<?php

namespace App\Http\Middleware;

use Closure;

class EnableCrossRequestMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        $response = $next($request);

        $httpWay = config('app.env') == 'local' ? 'http://' : 'https://';
        $domain = config('routes.H5_HOST', 'm.xxx.com');

        $response->header('Access-Control-Allow-Origin', $httpWay . $domain);

        $response->header('Access-Control-Allow-Headers', 'Origin, Content-Type, Cookie, X-CSRF-TOKEN, Accept, Authorization, X-XSRF-TOKEN');
        $response->header('Access-Control-Expose-Headers', 'Authorization, authenticated');
        $response->header('Access-Control-Allow-Methods', 'GET, POST, PATCH, PUT, OPTIONS');
        $response->header('Access-Control-Allow-Credentials', 'true');

        return $response;
    }
}
```

然后在App\Http\Kernel.php中添加对应的配置就可以了

我的是在

```php
protected $routeMiddleware = [
    // ...
    'cross.domain' => \App\Http\Middleware\EnableCrossRequestMiddleware::class,
]
```

这个地方加入的中间件配置

使用的话在路由中直接调用就可以了

```php
// api
Route::group(['domain' => config('routes.API_HOST', 'api.xx.com')], function () {
    Route::group([
        'middleware' => [
            'cross.domain',
        ],
        'prefix' => '/api',
        'namespace' => 'XXX',
    ], function () {
        Route::post('/xxx/xx', 'xxxController@index');
    });
});
```

这样就实现了给指定的接口添加跨域处理的逻辑了

只是补充

1，如何创建中间件

```bash
php artisan make:middleware EnableCrossRequestMiddleware
```
