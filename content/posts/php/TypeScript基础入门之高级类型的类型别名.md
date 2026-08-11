---
title: "TypeScript基础入门之高级类型的类型别名"
date: "2025-07-09 10:42:27"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bie-ming"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的类型别名/"
  - "/2025/07/09/TypeScript基础入门之高级类型的类型别名.html"
  - "/TypeScript基础入门之高级类型的类型别名/"
  - "/TypeScript基础入门之高级类型的类型别名.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bie-ming/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bie-ming.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bie-ming.html"
---
## 高级类型

### 类型别名

类型别名会给一个类型起个新名字。 类型别名有时和接口很像，但是可以作用于原始值，联合类型，元组以及其它任何你需要手写的类型。

```ts
type Name = string;
type NameFunc = () => string;
type NameOrFunc = Name | NameFunc;
function getName(n: NameOrFunc): Name {
    if (typeof n === 'string') {
        return n;
    }

    return n();
}
```

起别名不会新建一个类型 - 它创建了一个新名字来引用那个类型。 给原始类型起别名通常没什么用，尽管可以做为文档的一种形式使用。

同接口一样，类型别名也可以是泛型 - 我们可以添加类型参数并且在别名声明的右侧传入：

```ts
type Container<T> = { value: T };
```

我们也可以使用类型别名来在属性里引用自己：

```ts
type Tree<T> = {
    value: T;
    left: Tree<T>;
    right: Tree<T>;
}
```

与交叉类型一起使用，我们可以创建出一些十分稀奇古怪的类型。

```ts
type LinkedList<T> = T & { next: LinkedList<T> };

interface Person {
    name: string;
}

var people: LinkedList<Person>;
var s = people.name;
var s = people.next.name;
var s = people.next.next.name;
var s = people.next.next.next.name;
```

然而，类型别名不能出现在声明右侧的任何地方。

```ts
type Yikes = Array<Yikes>; // error
```

### 接口 vs. 类型别名

像我们提到的，类型别名可以像接口一样；然而，仍有一些细微差别。

其一，接口创建了一个新的名字，可以在其它任何地方使用。 类型别名并不创建新名字—比如，错误信息就不会使用别名。 在下面的示例代码里，在编译器中将鼠标悬停在 interfaced上，显示它返回的是 Interface，但悬停在 aliased上时，显示的却是对象字面量类型。

```ts
type Alias = { num: number }
interface Interface {
    num: number;
}
declare function aliased(arg: Alias): Alias;
declare function interfaced(arg: Interface): Interface;
```

另一个重要区别是类型别名不能被 extends和 implements（自己也不能 extends和 implements其它类型）。 因为 软件中的对象应该对于扩展是开放的，但是对于修改是封闭的，你应该尽量去使用接口代替类型别名。

另一方面，如果你无法通过接口来描述一个类型并且需要使用联合类型或元组类型，这时通常会使用类型别名。
