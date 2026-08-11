---
title: "laravel^8.0使用laravel-excel^3.1方法记录"
date: "2025-07-15 10:29:07"
slug: "laravel80-shi-yong-laravel-excel31-fang-fa-ji-lu"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/15/laravel^8.0使用laravel-excel^3.1方法记录/"
  - "/2025/07/15/laravel^8.0使用laravel-excel^3.1方法记录.html"
  - "/laravel^8.0使用laravel-excel^3.1方法记录/"
  - "/laravel^8.0使用laravel-excel^3.1方法记录.html"
  - "/2025/07/15/Laravel-8-0使用laravel-excel-3-1方法记录/"
  - "/2025/07/15/Laravel-8-0使用laravel-excel-3-1方法记录.html"
  - "/2025/07/15/laravel80-shi-yong-laravel-excel31-fang-fa-ji-lu/"
  - "/2025/07/15/laravel80-shi-yong-laravel-excel31-fang-fa-ji-lu.html"
  - "/laravel80-shi-yong-laravel-excel31-fang-fa-ji-lu.html"
---
laravel-excel的安装直接看官网

官网地址 https://docs.laravel-excel.com/

使用场景记录：

> 导出一个表格，指定表头，指定对应的数据

需求很简单，不过使用新版本还是有点不知如何下手，不过仔细看了文档还是找到了办法，所以文档是一个好东西

说说以前是如何使用的

首先数据源的获取，这个是一致的，需要什么数据不管新版本旧版本都一样的

```php
$data = [[1,2,3,4],[1,2,3,4]];
```

之前的版本"maatwebsite/excel": "^2.1"

```php
Excel::create('conversion', function($excel) use ($data) {
    $excel->sheet('信息', function($sheet) use ($data) {
        $sheet->rows($data);
        $sheet->prependRow(['header1','header2','header3','header4']);
    });
})->export('xlsx');
```

新版本"maatwebsite/excel": "^3.1"就比较麻烦了

配置数据源

```php
use Maatwebsite\Excel\Facades\Excel;
use Maatwebsite\Excel\Concerns\FromCollection;
use Maatwebsite\Excel\Concerns\WithHeadings;
use Illuminate\Support\Collection;
class DataExport implements FromCollection, WithHeadings
{
    public function collection()
    {
        $data = [[1,2,3,4],[1,2,3,4]];
        return new Collection($data);
    }

    public function headings(): array
    {
        return [
            'header1',
            'header2',
            'header3',
            'header4',
        ];
    }
}
```

导出实现

```php
Excel::store(new DataExport(), "invoices.xlsx");
```

看起来麻烦，不过梳理了之后感觉还是很方便的，应该算是增加了耦合度
