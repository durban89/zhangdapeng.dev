---
title: "Laravel测试单元这么使用"
date: "2025-07-11 10:29:11"
slug: "laravel-ce-shi-dan-yuan-zhe-me-shi-yong"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/11/Laravel测试单元这么使用/"
  - "/2025/07/11/Laravel测试单元这么使用.html"
  - "/Laravel测试单元这么使用/"
  - "/Laravel测试单元这么使用.html"
  - "/2025/07/11/laravel-ce-shi-dan-yuan-zhe-me-shi-yong/"
  - "/2025/07/11/laravel-ce-shi-dan-yuan-zhe-me-shi-yong.html"
  - "/laravel-ce-shi-dan-yuan-zhe-me-shi-yong.html"
---
Laravel版本信息 `"laravel/framework": "5.2.*"`

在项目根目录tests（如果没有tests目录的话，自己创建）目录下创建TestCase.php

代码如下

```php
<?php
namespace Tests;

use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

class TestCase extends BaseTestCase
{

    protected $baseUrl = 'http://localhost';
    public function createApplication()
    {
        $app = require __DIR__ . '/../bootstrap/app.php';
        $app->make(\Illuminate\Contracts\Console\Kernel::class)->bootstrap();
        return $app;
    }
}
```

修改composer.json，添加下面的配置

```json
"autoload-dev": { "classmap": [ "tests/TestCase.php" ] },
```

再执行`composer update`

创建测试用例，命令如下

```bash
php artisan make:test ControllerActionTest
```

生成的文件如下

```php
<?php

use Illuminate\Foundation\Testing\WithoutMiddleware;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class ControllerActionTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testExample()
    {
        $this->assertTrue(true);
    }
}
```

修改成下面的代码

```php
<?php
namespace Tests;

class ControllerActionTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testExample()
    {
        $this->assertTrue(true);
    }
}
```

执行测试单元命令

```bash
$ ./vendor/bin/phpunit
PHPUnit 4.8.36 by Sebastian Bergmann and contributors.

.

Time: 1.37 seconds, Memory: 18.00MB

OK (1 test, 1 assertion)
```

如果遇到上面的输出则表示单元测试正常运行。
