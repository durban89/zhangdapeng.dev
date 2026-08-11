---
title: "使用TypeScript开发React应用(二) - 创建组件"
date: "2025-07-10 10:57:33"
slug: "shi-yong-typescript-kai-fa-react-ying-yong-er-chuang-jian-zu-jian"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/使用TypeScript开发React应用(二)-创建组件/"
  - "/2025/07/10/使用TypeScript开发React应用(二)-创建组件.html"
  - "/使用TypeScript开发React应用(二)-创建组件/"
  - "/使用TypeScript开发React应用(二)-创建组件.html"
  - "/2025/07/10/使用TypeScript开发React应用-二-创建组件/"
  - "/2025/07/10/使用TypeScript开发React应用-二-创建组件.html"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-er-chuang-jian-zu-jian/"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-er-chuang-jian-zu-jian.html"
  - "/shi-yong-typescript-kai-fa-react-ying-yong-er-chuang-jian-zu-jian.html"
---
继续前面的文章[使用TypeScript开发React应用(一)](https://www.gowhich.com/blog/975)介绍了基础的React+TypeScript应用的搭建

下面看下如何进行开发

### 创建组件

我们要写一个Hello组件。 该组件将采用我们想要问候的任何人的名字（我们称之为名称），以及可选的跟踪感叹号的数量（passioniasmLevel）。

当我们编写类似`<Hello name="Daniel" enthusiasmLevel={3} />`的内容时，组件应该渲染为类似`<div>Hello Daniel!!!</div>`的内容。 如果未指定enthusiasmLevel，则组件应默认显示一个感叹号。 如果enthusiasmLevel为0或负数，则应该抛出错误。

我们写一个Hello.tsx：

// src/components/Hello.tsx

```tsx
import * as React from 'react';

export interface Props {
  name: string;
  enthusiasmLevel?: number;
}

function Hello({ name, enthusiasmLevel = 1 }: Props) {
  if (enthusiasmLevel <= 0) {
    throw new Error('You could be a little more enthusiastic.');
  }

  return (
    <div className="hello">
      <div className="greeting">
        Hello {name + getExclamationMarks(enthusiasmLevel)}
      </div>
    </div>
  );
}

export default Hello;

function getExclamationMarks(numberMarks: number) {
  return Array(numberMarks + 1).join('!');
}
```

请注意，我们定义了一个名为Props的类型，它指定了我们的组件将采用的属性。 name是一个必需的字符串，而enthusiasmLevel是一个可选的数字（你可以从我们在其名字后面写出来的？）告诉你。

我们还将Hello编写为无状态函数组件（SFC）。 具体来说，Hello是一个函数，它接受Props对象，并挑选（或"析构"）它将传递的所有属性。 如果我们的Props对象中没有给出enthusiasmLevel，它将默认为1。

编写函数是React允许我们创建组件的两种主要方式之一。 如果我们想要，我们可以把它写成一个类，如下所示：

```tsx
class Hello extends React.Component<Props, object> {
  render() {
    const { name, enthusiasmLevel = 1 } = this.props;

    if (enthusiasmLevel <= 0) {
      throw new Error('You could be a little more enthusiastic. :D');
    }

    return (
      <div className="hello">
        <div className="greeting">
          Hello {name + getExclamationMarks(enthusiasmLevel)}
        </div>
      </div>
    );
  }
}
```

当我们的组件实例具有某种状态或需要处理生命周期钩子时，类很有用。 但是我们并不需要在这个特定的例子中考虑状态 - 事实上，我们在React.Component<Props, object>中将它指定为对象，所以编写SFC在这里更有意义，但重要的是要知道如何 写一个类组件。

请注意，该类扩展了React.Component<Props, object>。 这里的TypeScript特定位是我们传递给React.Component的类型参数：Props和object。 这里，Props是我们类的this.props的类型，object是this.state的类型。 我们将稍微返回组件状态。

现在我们已经编写了我们的组件，让我们将组件导入到index.tsx并用`<Hello ... />`的渲染替换我们的`<App />`渲染。

首先，我们将它导入文件的顶部：

```tsx
import Hello from './components/Hello';
```

然后改变render函数的调用

```tsx
ReactDOM.render(
  <Hello name="Durban" enthusiasmLevel={3} />,
  document.getElementById('root') as HTMLElement
);
```

### 类型断言

`document.getElementById('root') as HTMLElement`这行代码在语法上称为类型断言，有时也称为强制转换。当你比类型检查器更清楚时，这是告诉TypeScript表达式的真实类型的有用方法。

在这种情况下我们需要这样做的原因是getElementById的返回类型是`HTMLElement | null`。 简而言之，当getElementById找不到具有给定id的元素时，它返回null。 我们假设getElementById实际上会成功，所以我们需要使用as语法来说服TypeScript。

TypeScript还有一个尾随的"bang"语法（!），它从前一个表达式中删除null和undefined。 所以我们可以编写document.getElementById('root')!,但在这种情况下我们想要更明确一些。

未完待续...
