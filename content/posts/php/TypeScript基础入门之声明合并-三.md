---
title: "TypeScript基础入门之声明合并(三)"
date: "2025-07-10 10:23:49"
slug: "typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之声明合并(三)/"
  - "/2025/07/10/TypeScript基础入门之声明合并(三).html"
  - "/TypeScript基础入门之声明合并(三)/"
  - "/TypeScript基础入门之声明合并(三).html"
  - "/2025/07/10/TypeScript基础入门之声明合并-三/"
  - "/2025/07/10/TypeScript基础入门之声明合并-三.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-san/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-san.html"
  - "/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-san.html"
---
## 声明合并

### 将命名空间与类，函数和枚举合并

命名空间足够灵活，也可以与其他类型的声明合并。  
为此，命名空间声明必须遵循它将与之合并的声明。  
生成的声明具有两种声明类型的属性。  
TypeScript使用此功能来模拟JavaScript以及其他编程语言中的某些模式。

**将命名空间与类合并**

这为用户提供了一种描述内部类的方法。

```ts
class Album {
    label: Album.AlbumLabel;
}

namespace Album {
    export class AlbumLabel { }
}
```

合并成员的可见性规则与"合并命名空间"部分中描述的相同，因此我们必须导出合并类的AlbumLabel类才能看到它。  
最终结果是在另一个类内部管理的类。  
您还可以使用命名空间向现有类添加更多静态成员。

除了内部类的模式之外，您还可能熟悉创建函数的JavaScript实践，然后通过向函数添加属性来进一步扩展函数。  
TypeScript使用声明合并以类型安全的方式构建这样的定义。

```ts
function buildLabel(name: string): string {
    return buildLabel.prefix + name + buildLabel.suffix;
}

namespace buildLabel {
    export let suffix = "";
    export let prefix = "Hello, ";
}

console.log(buildLabel("Sam Smith"));
```

同样，名称空间可用于扩展具有静态成员的枚举：

```ts
enum Color {
    red = 1,
    green = 2,
    blue = 4
}

namespace Color {
    export function mixColor(colorName: string) {
        if (colorName == "yellow") {
            return Color.red + Color.green;
        }
        else if (colorName == "white") {
            return Color.red + Color.green + Color.blue;
        }
        else if (colorName == "magenta") {
            return Color.red + Color.blue;
        }
        else if (colorName == "cyan") {
            return Color.green + Color.blue;
        }
    }
}
```

### 不允许合并

并非TypeScript中允许所有合并。  
目前，类不能与其他类或变量合并。  
有关模拟类合并的信息，请参阅TypeScript中的Mixins部分。

### 模块扩展

虽然JavaScript模块不支持合并，但您可以通过导入然后更新它们来修补现有对象。  
让我们看一下玩具Observable示例：

```ts
// observable.js
export class Observable<T> {
    // ... implementation left as an exercise for the reader ...
}

// map.js
import { Observable } from "./observable";
Observable.prototype.map = function (f) {
    // ... another exercise for the reader
}
```

这在TypeScript中也可以正常工作，但编译器不了解Observable.prototype.map。  
您可以使用模块扩充来告诉编译器：

```ts
// observable.ts stays the same
// map.ts
import { Observable } from "./observable";
declare module "./observable" {
    interface Observable<T> {
        map<U>(f: (x: T) => U): Observable<U>;
    }
}
Observable.prototype.map = function (f) {
    // ... another exercise for the reader
}

// consumer.ts
import { Observable } from "./observable";
import "./map";
let o: Observable<number>;
o.map(x => x.toFixed());
```

模块名称的解析方式与导入/导出中的模块说明符相同。  
有关更多信息，请参阅模块  
然后合并扩充中的声明，就好像它们在与原始文件相同的文件中声明一样。  
但是，您无法在扩充中声明新的顶级声明 - 只是现有声明的补丁。

**全局扩展**您还可以从模块内部向全局范围添加声明：

```ts
// observable.ts
export class Observable<T> {
    // ... still no implementation ...
}

declare global {
    interface Array<T> {
        toObservable(): Observable<T>;
    }
}

Array.prototype.toObservable = function () {
    // ...
}
```

全局扩展与模块扩展具有相同的行为和限制。
