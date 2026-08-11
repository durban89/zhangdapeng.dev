---
title: "新手入门NestJS（十二）- 控制器所有请求方式实例"
date: "2025-07-14 16:21:38"
slug: "xin-shou-ru-men-nestjs-shi-er-kong-zhi-qi-suo-you-qing-qiu-fang-shi-shi-li"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（十二）-控制器所有请求方式实例/"
  - "/2025/07/14/新手入门NestJS（十二）-控制器所有请求方式实例.html"
  - "/新手入门NestJS（十二）-控制器所有请求方式实例/"
  - "/新手入门NestJS（十二）-控制器所有请求方式实例.html"
  - "/2025/07/14/新手入门NestJS-十二-控制器所有请求方式实例/"
  - "/2025/07/14/新手入门NestJS-十二-控制器所有请求方式实例.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-er-kong-zhi-qi-suo-you-qing-qiu-fang-shi-shi-li/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-er-kong-zhi-qi-suo-you-qing-qiu-fang-shi-shi-li.html"
  - "/xin-shou-ru-men-nestjs-shi-er-kong-zhi-qi-suo-you-qing-qiu-fang-shi-shi-li.html"
---
这里记录下使用Nest.js中，在控制器中如何添加所有请求方式的方法

第一种请求方式Get

```javascript
@Get()
findAll() {
  return 'This action will return all dogs';
}

@Get(':id')
findOne(@Param('id') id: string) {
  return `This action will return one ${id} dog`;
}
```

第二种请求方式Post

```javascript
@Post()
create(@Body() createDogDto: CreateDogDto) {
  return `This action will add a dog`;
}
```

第三种请求方式Put

```javascript
@Put(':id')
update(@Param('id') id: string, @Body() updateDogDto: UpdateDogDto) {
  return `This action will update a dog`;
}
```

第四种请求方式Delete

```javascript
@Delete(':id')
remove(@Param('id') id: string) {
  return `This action will remote a dog`;
}
```

完整的代码如下

```javascript
import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
} from '@nestjs/common';
import { CreateDogDto } from 'src/create-dog.dto';
import { UpdateDogDto } from 'src/update-dog.dto';

@Controller('dogs')
export class DogsController {
  @Get()
  findAll() {
    return 'This action will return all dogs';
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return `This action will return one ${id} dog`;
  }

  @Post()
  create(@Body() createDogDto: CreateDogDto) {
    return `This action will add a dog`;
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateDogDto: UpdateDogDto) {
    return `This action will update a dog`;
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return `This action will remote a dog`;
  }
}
```
