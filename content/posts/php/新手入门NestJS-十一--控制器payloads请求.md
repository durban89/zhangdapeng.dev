---
title: "新手入门NestJS（十一）- 控制器payloads请求"
date: "2025-07-14 16:21:34"
slug: "xin-shou-ru-men-nestjs-shi-yi-kong-zhi-qi-payloads-qing-qiu"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（十一）-控制器payloads请求/"
  - "/2025/07/14/新手入门NestJS（十一）-控制器payloads请求.html"
  - "/新手入门NestJS（十一）-控制器payloads请求/"
  - "/新手入门NestJS（十一）-控制器payloads请求.html"
  - "/2025/07/14/新手入门NestJS-十一-控制器payloads请求/"
  - "/2025/07/14/新手入门NestJS-十一-控制器payloads请求.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-yi-kong-zhi-qi-payloads-qing-qiu/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-yi-kong-zhi-qi-payloads-qing-qiu.html"
  - "/xin-shou-ru-men-nestjs-shi-yi-kong-zhi-qi-payloads-qing-qiu.html"
---
#### 控制器payloads请求

如果通过Post请求来接收客户端的payloads参数

Nest.js通过使用`@Body`装饰器

首先创建一个DTO类，create-cats.dto.ts

```javascript
export class CreateCatDto {
  name: string;
  age: number;
  bread: string;
}
```

然后修改create方法

```javascript
import { CreateCatDto } from 'src/create-cats.dto';

@Post()
async create(@Body() createCatDto: CreateCatDto) {
  console.log(createCatDto);
  return 'This action will create a new cat';
}
```

运行npm run start:dev

我们测试下

```apache
$ curl -d 'name=durban&age=12&bread=ddd' http://127.0.0.1:3000/cats
This action will create a new cat
```

可以看到console.log的输出结果如下

```bash
{ name: 'durban', age: '12', bread: 'ddd' }
```
