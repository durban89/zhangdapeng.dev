---
title: "新手入门NestJS（十五）- 连接数据库"
date: "2025-07-15 09:52:03"
slug: "xin-shou-ru-men-nestjs-shi-wu-lian-jie-shu-ju-ku"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/15/新手入门NestJS（十五）-连接数据库/"
  - "/2025/07/15/新手入门NestJS（十五）-连接数据库.html"
  - "/新手入门NestJS（十五）-连接数据库/"
  - "/新手入门NestJS（十五）-连接数据库.html"
  - "/2025/07/15/新手入门NestJS-十五-连接数据库/"
  - "/2025/07/15/新手入门NestJS-十五-连接数据库.html"
  - "/2025/07/15/xin-shou-ru-men-nestjs-shi-wu-lian-jie-shu-ju-ku/"
  - "/2025/07/15/xin-shou-ru-men-nestjs-shi-wu-lian-jie-shu-ju-ku.html"
  - "/xin-shou-ru-men-nestjs-shi-wu-lian-jie-shu-ju-ku.html"
---
Nestjs中为了连接数据库，提供了@nestjs/typeorm包

在使用之前如果没有安装的话，需要安装下，安装命令如下

```bash
npm install --save @nestjs/typeorm typeorm mysql
```

这里使用MySQL，当然TypeORM也是支持其他关系型数据库的，如PostgreSQL，Oracle，Microsoft SQL Server，还有NoSQL数据库如MongoDB

如果TypeORM安装成功之后，就可以导入TypeOrmModule了

```ts
import { TypeOrmModule } from '@nestjs/typeorm';
```

### 如何配置MySQL的参数（比如连接的数据库地址、用户名、密码、数据库）

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'root',
      password: '123456',
      database: 'test',
      entities: [],
      synchronize: true,
    })
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

forRoot方法提供了所有的配置参数给TypeORM包的createConnection方法，除此之外，还有其他的一些配置参数的属性如下

* retryAttempts：默认10，尝试连接数据库的次数
* retryDelay：默认3000，尝试连接数据库延迟时间
* autoLoadEntities：默认false，如果为true，entities将会被自动加载
* keepConnectionAlive：默认false，如果为true，连接在应用被关闭时不会关闭

具体更多的连接配置参数，[点击这里查看](https://typeorm.io/#/connection-options)

数据库配置连接正常之后，就可以正常使用了

app.module.ts完整代码如下

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { Connection } from 'typeorm';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'root',
      password: '123456',
      database: 'test',
      entities: [],
      synchronize: true,
      logging: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {
  constructor(private connection: Connection) {}
}
```

如何连接数据库进行查询和添加

创建Entity

cats/cats.entities.ts代码如下

```ts
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity({ name: 'cats' })
export class Cats {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ name: 'first_name' })
  firstName: string;

  @Column({ name: 'last_name' })
  lastName: string;

  @Column({ name: 'is_active', default: true })
  isActive: boolean;
}
```

创建Service

cats/cats.service.ts代码如下

```ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Cats } from './cats.entity';

@Injectable()
export class CatsService {
  constructor(
    @InjectRepository(Cats)
    private catsRepository: Repository<Cats>,
  ) {}

  findAll(): Promise<Cats[]> {
    return this.catsRepository.find();
  }

  findOne(id: number): Promise<Cats> {
    return this.catsRepository.findOne(id);
  }

  async remove(id: number): Promise<void> {
    await this.catsRepository.delete(id);
  }

  async create(cats: Cats): Promise<void> {
    await this.catsRepository.save(cats);
  }
}
```

创建Controller

cats/cats.controller.ts

```ts
import { Body, Controller, Get, Post, Res } from '@nestjs/common';
import { Response } from 'express';
import { Cats } from './cats.entity';
import { CatsService } from './cats.service';

@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  @Get('/index')
  index(@Res() res: Response): string {
    this.catsService.findAll();

    var cats: Promise<Cats[]> = this.catsService.findAll();

    cats
      .then((data) => {
        return res.render('cats/index', {
          message: 'Cats',
          data: data,
        });
      })
      .catch((error) => {
        console.log(error);
      });

    return '';
  }

  @Post('/create')
  async create(@Body() catsParam: { firstName: string; lastName: string }) {
    let cats = new Cats();
    cats.firstName = catsParam.firstName;
    cats.lastName = catsParam.lastName;
    cats.isActive = true;
    return await this.catsService.create(cats);
  }
}
```

创建Module

cats/cats.module.ts

```javascript
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CatsController } from './cats.controller';
import { Cats } from './cats.entity';
import { CatsService } from './cats.service';

@Module({
  imports: [TypeOrmModule.forFeature([Cats])],
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

修改AppModule

app.module.ts

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsModule } from './cats/cats.module';
import { Connection } from 'typeorm';
import { Cats } from './cats/cats.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'root',
      password: '123456',
      database: 'test',
      entities: [Cats],
      synchronize: true,
      logging: true,
    }),
    CatsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {
  constructor(private connection: Connection) {}
}
```

运行项目

```bash
npm run start:dev
```

启动后如果表不存在的话会自动创建表cats

正常启动没有问题之后，先创建一个数据

```bash
curl -d 'firstName=cats&lastName=1' 'http://localhost:3000/cats/create'
```

然后访问http://localhost:3000/cats/index

会看到创建的数据输出
