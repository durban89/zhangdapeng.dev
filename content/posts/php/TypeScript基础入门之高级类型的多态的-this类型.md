---
title: "TypeScript基础入门之高级类型的多态的 this类型"
date: "2025-07-09 10:42:39"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-duo-tai-de-this-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的多态的-this类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的多态的-this类型.html"
  - "/TypeScript基础入门之高级类型的多态的-this类型/"
  - "/TypeScript基础入门之高级类型的多态的-this类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-duo-tai-de-this-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-duo-tai-de-this-lei-xing.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-duo-tai-de-this-lei-xing.html"
---
## 高级类型

### 多态的this类型

多态的this类型表示的是某个包含类或接口的子类型。 这被称做F-bounded多态性。 它能很容易的表现连贯接口间的继承，比如。 在下面的例子里，在每个操作之后都返回this类型：

```ts
class Query {
  public whereCon: Array<string> = [];

  public constructor(protected tableName: string = '') { }

  public andWhere(key: string, value: string) {
    this.whereCon.push(`${key}=${value}`);
    return this;
  }

  public orWhere(key: string, value: string) {
    this.whereCon.push(`OR ${key}=${value}`);
    return this;
  }

  public inWhere(key: string, value: string) {
    this.whereCon.push(`AND ${key} IN (${value})`);
    return this;
  }

  public getSQL(): string {
    return `SELECT * FROM ${this.tableName} WHERE ${this.whereCon.join(' ')}`;
  }

  // ... 其他的操作
}

let generateSQL = new Query('table_name')
  .andWhere('key1', 'value1')
  .orWhere('key2','value2')
  .inWhere('key3','value3')
  .getSQL();

console.log(generateSQL);
```

运行后输入结果如下

```bash
$ npx ts-node ./src/advanced_types_5.ts
SELECT * FROM table_name WHERE key1=value1 OR key2=value2 AND key3 IN (value3)
```

这个类当然还是有点缺陷的，但是我们可以看出这个特性的使用方式由于这个类使用了this类型，你可以继承它，新的类可以直接使用之前的方法，不需要做任何的改变。

```ts
class TQuery extends Query {
  public constructor(tableName: string = '') {
    super(tableName);
  }

  public getUpdateSql(key: string, value: string) {
    return `UPDATE ${this.tableName} SET ${key}=${value} WHERE ${this.whereCon.join(' ')}`;
  }

  // ... 其他的操作
}

let generateSQL = new TQuery('table_name')
  .andWhere('key1', 'value1')
  .orWhere('key2', 'value2')
  .inWhere('key3', 'value3')
  .getUpdateSql('key4', 'value4');
console.log(generateSQL);
```

运行后输入结果如下

```bash
$ npx ts-node ./src/advanced_types_5.ts
UPDATE table_name SET key4=value4 WHERE key1=value1 OR key2=value2 AND key3 IN (value3)
```

如果没有this类型，TQuery就不能够在继承Query的同时还保持接口的连贯性。 inWhere将会返回Query，它并没有getUpdateSql方法。 然而，使用this类型，inWhere会返回 this，在这里就是 TQuery。
