---
title: "TypeScript基础入门之命名空间(二)"
date: "2025-07-10 10:23:11"
slug: "typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之命名空间(二)/"
  - "/2025/07/10/TypeScript基础入门之命名空间(二).html"
  - "/TypeScript基础入门之命名空间(二)/"
  - "/TypeScript基础入门之命名空间(二).html"
  - "/2025/07/10/TypeScript基础入门之命名空间-二/"
  - "/2025/07/10/TypeScript基础入门之命名空间-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-er.html"
  - "/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-er.html"
---
继续上篇文章[[TypeScript基础入门之命名空间(一)](https://www.gowhich.com/blog/940)]

## 跨文件拆分

当应用变得越来越大时，我们需要将代码分离到不同的文件中以便于维护。

### 多文件名称空间

现在，我们把Validation命名空间分割成多个文件。 尽管是不同的文件，它们仍是同一个命名空间，并且在使用的时候就如同它们在一个文件中定义的一样。 因为不同文件之间存在依赖关系，所以我们加入了引用标签来告诉编译器文件之间的关联。 我们的测试代码保持不变。

Validation.ts

```ts
namespace Validation {
  export interface StringValidator {
    isAcceptable(s: string): boolean;
  }
}
```

LettersOnlyValidator.ts

```ts
/// <reference path="Validation.ts" />

namespace Validation {
  const letterRegexp = /^[A-Za-z]+/;

  export class LettersOnlyValidator implements StringValidator {
    isAcceptable(s: string): boolean {
      return letterRegexp.test(s);
    }
  }
}
```

ZipCodeValidator.ts

```ts
/// <reference path="Validation.ts" />
namespace Validation {
  export const numberRegexp = /^[0-9]+$/;

  export class ZipCodeValidator implements StringValidator {
    isAcceptable(s: string): boolean {
      return s.length === 5 && numberRegexp.test(s);
    }
  }
}
```

Test.ts

```ts
/// <reference path="Validation.ts" />
/// <reference path="LettersOnlyValidator.ts" />
/// <reference path="ZipCodeValidator.ts" />

// 测试数据
let strings = ["Hello", "98052", "101"];
// 
let validators:{ [s: string]: Validation.StringValidator } = {};
validators["zip code validator"] = new Validation.ZipCodeValidator();
validators["letter validator"] = new Validation.LettersOnlyValidator();

strings.forEach((e) => {
  for (let name in validators) {
    console.log(`"${e}" - ${ validators[name].isAcceptable(e) ? "matches" : 'does not match'} ${name}`)
  }
});
```

编译运行后的结果如下

```bash
$ tsc --outFile src/module_demo/Test.js src/module_demo/Test.ts
$ node src/module_demo/Test.js
"Hello" - does not match zip code validator
"Hello" - matches letter validator
"98052" - matches zip code validator
"98052" - does not match letter validator
"101" - does not match zip code validator
"101" - does not match letter validator
```

一旦涉及多个文件，我们需要确保加载所有已编译的代码。  
有两种方法可以做到这一点。  
首先，我们可以使用--outFile标志使用连接输出将所有输入文件编译为单个JavaScript输出文件：

```bash
tsc --outFile sample.js Test.ts
```

编译器将根据文件中存在的引用标记自动排序输出文件。  
您还可以单独指定每个文件：

```bash
tsc --outFile sample.js Validation.ts LettersOnlyValidator.ts ZipCodeValidator.ts Test.ts
```

或者，我们可以使用每个文件编译（默认）为每个输入文件发出一个JavaScript文件。  
如果生成了多个JS文件，我们需要在我们的网页上使用`<script>`标签以适当的顺序加载每个发出的文件，例如：

```html
<script src="Validation.js" type="text/javascript" />
<script src="LettersOnlyValidator.js" type="text/javascript" />
<script src="ZipCodeValidator.js" type="text/javascript" />
<script src="Test.js" type="text/javascript" />
```

未完待续...
