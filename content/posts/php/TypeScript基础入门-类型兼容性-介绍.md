---
title: "TypeScript基础入门 - 类型兼容性 - 介绍"
date: "2025-07-09 10:00:05"
slug: "typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-jie-shao"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-类型兼容性-介绍/"
  - "/2025/07/09/TypeScript基础入门-类型兼容性-介绍.html"
  - "/TypeScript基础入门-类型兼容性-介绍/"
  - "/TypeScript基础入门-类型兼容性-介绍.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-jie-shao/"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-jie-shao.html"
  - "/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-jie-shao.html"
---
## **介绍**

TypeScript中的类型兼容性基于结构子类型。  
结构类型是一种仅根据其成员关联类型的方式。它正好与名义（nominal）类型形成对比。请看如下代码：

```ts
interface Named {
    name: string;
}

class Person {
    name: string;
}

let p: Named;
// OK, because of structural typing
p = new Person();
```

在使用基于名义类型的语言，比如C#或Java中，这段代码会报错，因为Person类没有明确说明其实现了Named接口。

TypeScript的结构性子类型是根据JavaScript代码的典型写法来设计的。 因为JavaScript里广泛地使用匿名对象，例如函数表达式和对象字面量，所以使用结构类型系统来描述这些类型比使用名义类型系统更好。

### 关于可靠性的注意事项

TypeScript的类型系统允许某些在编译阶段无法确认其安全性的操作。当一个类型系统具此属性时，被当做是“不可靠”的。TypeScript允许这种不可靠行为的发生是经过仔细考虑的。通过这篇文章，我们会解释什么时候会发生这种情况和其有利的一面。

## 开始

TypeScript结构化类型系统的基本规则是，如果x要兼容y，那么y至少具有与x相同的属性。比如：

```ts
interface Named {
    name: string;
}

let x: Named;
// y的推断类型 is { name: string; location: string; }
let y = { name: 'Alice', location: 'Seattle' };
x = y;
```

这里要检查y是否能赋值给x，编译器检查x中的每个属性，看是否能在y中也找到对应属性。 在这个例子中， y必须包含名字是name的string类型成员。y满足条件，因此赋值正确。

检查函数参数时使用相同的规则：

```ts
function greet(n: Named) {
    alert('Hello, ' + n.name);
}
greet(y); // OK
```

注意，y有个额外的location属性，但这不会引发错误。 只有目标类型（这里是 Named）的成员会被一一检查是否兼容。

这个比较过程是递归进行的，检查每个成员及子成员。
