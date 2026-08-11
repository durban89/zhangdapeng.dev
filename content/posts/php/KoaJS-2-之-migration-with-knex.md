---
title: "KoaJS 2 之 migration with knex"
date: "2025-07-03 16:49:59"
slug: "koajs-2-zhi-migration-with-knex"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/03/KoaJS-2-之-migration-with-knex/"
  - "/2025/07/03/KoaJS-2-之-migration-with-knex.html"
  - "/KoaJS-2-之-migration-with-knex/"
  - "/KoaJS-2-之-migration-with-knex.html"
  - "/2025/07/03/koajs-2-zhi-migration-with-knex/"
  - "/2025/07/03/koajs-2-zhi-migration-with-knex.html"
  - "/koajs-2-zhi-migration-with-knex.html"
---
# 安装knexfile

```bash
npm install -g knex
```

然后在项目的根目录

```bash
knex init
```

将会产生knexfile.js,内容类似如下

```js
// Update with your config settings.
module.exports = {
  development: {
    client: 'mysql',
    connection: {
      host: '127.0.0.1',
      user: 'root',
      password: '',
      database: '<YOUR TEST DB NAME>',
      charset: 'utf8'
    }
  },
  staging: {
    ...
  },
  production: {
    ...
  }
};
```

如果想要根据具体环境来执行具体配置，可以使用如下命令来指定环境

```bash
knex migrate:latest --env production
```

更多的使用可以参考[Knex docs](http://knexjs.org/#Installation-client)

# 创建Migration

```bash
knex migrate:make create_person
```

将会创建migrations目录并且将migration的文件放入文件夹中

默认的内容如下：

```js
exports.up = function(knex, Promise){

}

exports.down = function(knex, Promise){

}
```

接下来我们在这里面实现具体的表信息

```js
exports.up = function(knex, Promise){
    return Promise.all([
        knex.schema.createTable('person', function(table){
            table.increments('id').primary();
            table.integer('parentId').unsigned().references('id').inTable('person');
            table.string('firstName');
            table.string('fullName');
            table.integer('age');
            table.json('address');
        })
    ]);
}

exports.down = function(knex, Promise){
    return Promise.all([
        knex.schema.dropTable('person')
    ]);
}
```

当应用migration的时候up被调用，当执行回滚的时候down被调用

在这些功能中，你可以使用[Knex Schema functions](http://knexjs.org/#Schema)

执行如下命令来使用新的migration

```bash
knex migrate:latest
```

# 更新数据库表

```bash
knex migrate:make update_person
```

内容如下

```js
exports.up = function(knex, Promise) {
    return Promise.all([
        knex.schema.table('person', function(table){
            table.string('twitter');
        })
    ])
}

exports.down = function(knex, Promise) {
    return Promise.all([
        knex.schema.table('person', function(table){
            table.dropColumn('twitter');
        })
    ]);
}
```

# 回滚操作

回滚操作执行下面的命令

```bash
knex migrate:rollback
```

knex对于创建跟修改表变得很容易。
