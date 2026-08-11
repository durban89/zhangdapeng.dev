---
title: "PHP7 新特性 学习"
date: "2025-07-03 17:11:22"
slug: "php7-xin-te-xing-xue-xi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP7-新特性-学习/"
  - "/2025/07/03/PHP7-新特性-学习.html"
  - "/PHP7-新特性-学习/"
  - "/PHP7-新特性-学习.html"
  - "/2025/07/03/php7-xin-te-xing-xue-xi/"
  - "/2025/07/03/php7-xin-te-xing-xue-xi.html"
  - "/php7-xin-te-xing-xue-xi.html"
---
PHP7 的新特性大概浏览下，还是能在工作的效率上有很大益处的。

**1，性能提升**

这个我就不做测试了，哈哈

**2，类型声明**

```php
class Student
{
    public function __construct()
    {
        $this->name = 'durban';
    }
}

$student = new Student();

function enroll(Student $student, array $classes)
{
    foreach ($classes as $class) {
        echo "Enrolling " . $student->name . " in " . $class . "\n";
    }
}

// enroll("name", ["class 1", "class 2"]);// Fatal error: Uncaught TypeError: Argument 1 passed to enroll() must be an instance of Student, string given
// enroll($student, "class"); // Fatal error: Uncaught TypeError: Argument 2 passed to enroll() must be of the type array, string given
enroll($student, array("class 1", "class 2"));

function stringTest(string $string)
{
    echo $string . "\n";
}
stringTest("a string");
```

**3，可以声明严格类型校验模式 , 此声明必须第一个声明**

```php
declare (strict_types = 1);
```

**4, 标量类型提示**

```php
function getTotal(float $a, float $b)
{
    return $a + $b;
}
// getTotal('a', 2); //Argument 1 passed to getTotal() must be of the type float, string given,
$total = getTotal(3, 2);
echo $total . "\n";
```

**5, 返回类型声明**

```php
function getSum(float $a, float $b): int
{
    // return $a + $b; // Fatal error: Uncaught TypeError: Return value of getTotal() must be of the type integer, float returned
    return (int) ($a + $b); // truncate float like non-strict
}
$sum = getSum(3, 6);
echo $sum . "\n";
```

**6, 错误处理**

新的继承如下

> |- Exception implements Throwable
>
>    |- …
>
> |- Error implements Throwable
>
>    |- TypeError extends Error
>
>    |- ParseError extends Error
>
>    |- ArithmeticError extends Error
>
>       |- DivisionByZeroError extends ArithmeticError
>
>    |- AssertionError extends Error

```php
try {
    // Code that may throw an Exception or Error.
} catch (Throwable $t) {
    // Executed only in PHP 7, will not match in PHP 5
} catch (Exception $e) {
    // Executed only in PHP 5, will not be reached in PHP 7
}
```

**7, Null Coalesce Operator**

```php
$name = $firstName ??  "Guest";
```

等同于

```bash
if (!empty($firstName)) {
    $name = $firstName;
} else {
    $name = "Guest";
}
```

还可以像下面这样使用

```php
$name = $firstName ?? $username ?? $placeholder ?? “Guest”;
```

**8, Spaceship Operator**

```php
$compare = 2 <=> 1
```

等同于下面

```php
2 < 1? return -1
2 = 1? return 0
2 > 1? return 1
```

**9，Easy User-land CSPRNG：  random\_int and random\_bytes.**

```php
$int = random_int(1, 2);
var_dump($int);

$bytes = random_bytes(5);
var_dump(bin2hex($bytes));
```
