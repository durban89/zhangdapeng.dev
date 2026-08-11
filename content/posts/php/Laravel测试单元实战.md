---
title: "Laravel测试单元实战"
date: "2025-07-11 10:29:16"
slug: "laravel-ce-shi-dan-yuan-shi-zhan"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/11/Laravel测试单元实战/"
  - "/2025/07/11/Laravel测试单元实战.html"
  - "/Laravel测试单元实战/"
  - "/Laravel测试单元实战.html"
  - "/2025/07/11/laravel-ce-shi-dan-yuan-shi-zhan/"
  - "/2025/07/11/laravel-ce-shi-dan-yuan-shi-zhan.html"
  - "/laravel-ce-shi-dan-yuan-shi-zhan.html"
---
当执行单元测试的时候，Laravel 会自动将环境配置成testing。另外 Laravel 会在测试环境导入session 和cache 的配置文件。当在测试环境里这两个驱动会被配置为array (空数组)，代表在测试的时候没有 session 或 cache 数据将会被保留。视情况你可以任意的建立你需要的测试环境配置。

testing 环境的变量可以在phpunit.xml 文件中配置。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit backupGlobals="false"
         backupStaticAttributes="false"
         bootstrap="bootstrap/autoload.php"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false">
    <testsuites>
        <testsuite name="Application Test Suite">
            <directory suffix="Test.php">./tests</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory suffix=".php">./app</directory>
            <exclude>
                <file>./app/Http/routes.php</file>
            </exclude>
        </whitelist>
    </filter>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="QUEUE_DRIVER" value="sync"/>
    </php>
</phpunit>
```

创建测试用例，命令如下

```bash
php artisan make:test RouteTest
```

### 测试用例代码示例如下

```php
<?php
namespace Tests;

use Exception;

class RouteTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testExample()
    {
        $host = env('DAODAO_HOST');

        $this->baseUrl = 'http://' . $host;

        $response = $this->call('GET', '/api/gift');
        $content = $response->getContent();

        try {
            $content = json_decode($content, true);

            $this->assertResponseOk();
            $this->assertResponseStatus(200);
            $this->assertTrue(isset($content['message']));
        } catch (Exception $e) {
            \Log::error($e);
            $this->assertTrue(false);
        }
    }
}
```

### 代码解释说明

这一步用来配置baseUrl，如果routes中的配置指定了domain，那就需要根据env中的配置来填写，否则的话可以直接使用默认的‘[http://localhost’](http://localhost%E2%80%99)

```php
$host = env('DAODAO_HOST');

$this->baseUrl = 'http://' . $host;
```

```php
$response = $this->call('GET', '/api/gift');
$content = $response->getContent();
```

调用$this->call直接请求接口，如果有参数的话可以参考下面

```php
$this->call($method, $uri, $parameters, $cookies, $files, $server, $content);
```

这个是可以使用的参数，可以根据具体的参数情况来调用
