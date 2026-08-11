---
title: "使用TypeScript开发React应用(三) - 创建状态组件"
date: "2025-07-10 10:57:35"
slug: "shi-yong-typescript-kai-fa-react-ying-yong-san-chuang-jian-zhuang-tai-zu-jian"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/使用TypeScript开发React应用(三)-创建状态组件/"
  - "/2025/07/10/使用TypeScript开发React应用(三)-创建状态组件.html"
  - "/使用TypeScript开发React应用(三)-创建状态组件/"
  - "/使用TypeScript开发React应用(三)-创建状态组件.html"
  - "/2025/07/10/使用TypeScript开发React应用-三-创建状态组件/"
  - "/2025/07/10/使用TypeScript开发React应用-三-创建状态组件.html"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-san-chuang-jian-zhuang-tai-zu-jian/"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-san-chuang-jian-zhuang-tai-zu-jian.html"
  - "/shi-yong-typescript-kai-fa-react-ying-yong-san-chuang-jian-zhuang-tai-zu-jian.html"
---
继续前面的文章[使用TypeScript开发React应用(二)](https://www.gowhich.com/blog/976)介绍了React+TypeScript应用的搭建中如何创建组件

下面继续分享创建状态组件

### 状态组件

我们之前提到我们的组件不需要状态。 如果我们希望能够根据用户的交互时间更新我们的组件会怎样？ 那时，状态变得更加重要。

深入了解React中有关组件状态的最佳实践超出了本次分享的范围，但让我们快速查看Hello组件的有状态版本，看看添加状态是什么样的。我们将渲染两个`<button>`来更新Hello组件显示的感叹号的数量。

要做到这一点，我们需要做到下面几个步骤

1. 为我们的状态定义一种类型（即this.state）
2. 根据我们在构造函数中给出的props来初始化this.state。
3. 为我们的按钮创建两个事件处理程序（onIncrement和onDecrement）。

实现代码如下

// src/components/StatefulHello.tsx

```tsx
import * as React from 'react';

export interface Props {
  name: string;
  enthusiasmlevel?: number;
}

interface State {
  currentEnthusiasmLevel: number;
}

class Hello extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      currentEnthusiasmLevel: props.enthusiasmlevel || 1,
    };
  }

  onIncrement = () => this.updateEnthusiasmLevel(this.state.currentEnthusiasmLevel + 1);

  onDecrement = () => this.updateEnthusiasmLevel(this.state.currentEnthusiasmLevel - 1);

  render() {
    const {
      name,
    } = this.props;

    if (this.state.currentEnthusiasmLevel <= 0) {
      throw new Error('You could be a little more enthusiastic.');
    }

    return (
      <div className="hello">
        <div className="greeting">
          Hello {name + getExclamationMarks(this.state.currentEnthusiasmLevel)}
        </div>
        <button onClick={this.onDecrement}>-</button>
        <button onClick={this.onIncrement}>+</button>
      </div>
    );
  }

  updateEnthusiasmLevel(currentEnthusiasmLevel: number) {
    this.setState({
      currentEnthusiasmLevel,
    });
  }
}

export default Hello;

function getExclamationMarks(numberMarks: number) {
  return Array(numberMarks + 1).join('!');
}
```

**小提示**

1. 与Props非常相似，我们必须为我们的状态定义一种新类型：`State`。
2. 要在React中更新状态，我们使用this.setState - 我们不直接在构造函数中设置它。 setState只接受我们感兴趣的属性更新，我们的组件将根据需要重新呈现。
3. 我们正在使用带箭头函数的类属性初始值设定项（例如 `onIncrement = () => ...`）。
4. 将这些声明为箭头函数可避免孤立使用`this`。
5. 将它们设置为实例属性只会创建一次 - 常见的错误是在render方法中初始化它们，每次调用render时都会分配一个闭包。

我们不会在此分享中进一步使用此有状态组件。 有状态组件非常适合创建仅专注于呈现内容的组件（而不是处理核心应用程序状态）。 在某些情况下，它可以用于处理整个应用程序的状态，一个中心组件传递可以适当调用setState的函数; 但是，对于更大的应用程序，可能更喜欢专用的状态管理器（我们将在下面讨论）。

### 添加样式

给一个组件设置样式是很简单的。 要设置Hello组件的样式，我们可以在src/components/Hello.css中创建一个CSS文件。 src/components/Hello.css 内容如下

```css
.hello {
  text-align: center;
  margin: 20px;
  font-size: 48px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.hello button {
  margin-left: 25px;
  margin-right: 25px;
  font-size: 40px;
  min-width: 50px;
}
```

create-react-app使用的工具（即Webpack和各种加载器）允许我们只导入我们感兴趣的样式表。当我们的构建运行时，任何导入的.css文件将被连接成一个输出文件。 所以在src/components/Hello.tsx中，我们将添加以下导入。

```tsx
import './Hello.css';
```

运行`npm run start`看下页面吧，是不是样式也已经加载进去了。

未完待续...
