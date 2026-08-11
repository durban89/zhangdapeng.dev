---
title: "使用TypeScript开发React应用(四) - Jest单元测试"
date: "2025-07-10 10:57:39"
slug: "shi-yong-typescript-kai-fa-react-ying-yong-si-jest-dan-yuan-ce-shi"
categories: ["技术"]
tags: ["TypeScript", "RequireJS", "Jest"]
aliases:
  - "/2025/07/10/使用TypeScript开发React应用(四)-Jest单元测试/"
  - "/2025/07/10/使用TypeScript开发React应用(四)-Jest单元测试.html"
  - "/使用TypeScript开发React应用(四)-Jest单元测试/"
  - "/使用TypeScript开发React应用(四)-Jest单元测试.html"
  - "/2025/07/10/使用TypeScript开发React应用-四-Jest单元测试/"
  - "/2025/07/10/使用TypeScript开发React应用-四-Jest单元测试.html"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-si-jest-dan-yuan-ce-shi/"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-si-jest-dan-yuan-ce-shi.html"
  - "/shi-yong-typescript-kai-fa-react-ying-yong-si-jest-dan-yuan-ce-shi.html"
---
继续前面的文章[使用TypeScript开发React应用(三)](https://www.gowhich.com/blog/977)介绍了React+TypeScript应用的搭建中如何创建状态组件

下面继续分享组件的单元测试

### 用Jest写测试

我们对Hello组件有一定的假设。 让我们重申它们是什么：

* 当我们编写类似的内容时，组件应该渲染为类似`<div>Hello Durban!!!</div>`的内容。
* 如果未指定passioniasmLevel，则组件应默认显示一个感叹号。
* 如果passioniasmLevel为0或负数，则应该抛出错误。

我们可以使用这些要求为我们的组件编写一些测试。

但首先，让我们安装Enzyme。 [Enzyme](http://airbnb.io/enzyme/)是React生态系统中的常用工具，可以更轻松地编写组件行为方式的测试。 默认情况下，我们的应用程序包含一个名为jsdom的库，允许我们模拟DOM并在没有浏览器的情况下测试其运行时行为。 Enzyme类似，但建立在jsdom上，可以更容易地对我们的组件进行某些查询。

让我们将其安装为开发时依赖项。

```bash
npm install -D enzyme @types/enzyme enzyme-adapter-react-16 @types/enzyme-adapter-react-16 react-test-renderer
```

注意我们安装了包`enzyme`以及`@types/enzyme`。 enzyme包是指包含实际运行的JavaScript代码的包，而`@types/enzyme`是包含声明文件（.d.ts文件）的包，因此TypeScript可以理解如何使用Enzyme。 您可以在[此处](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html)了解有关@types包的更多信息。

我们还必须安装`enzyme-adapter-react-16`和`react-test-renderer`。 这是`enzyme`预期安装的东西。

在编写第一个测试之前，我们必须配置Enzyme以使用React 16的适配器。我们将创建一个名为src/setupTests.ts的文件，在运行测试时自动加载，代码示例如下

```ts
import * as enzyme from 'enzyme';
import * as Adapter from 'enzyme-adapter-react-16';

enzyme.configure({
  adapter: new Adapter()
});
```

现在我们已经设置了enzyme，让我们开始编写测试！ 让我们创建一个名为src/components/Hello.test.tsx的文件，与之前的Hello.tsx文件相邻。

src/components/Hello.test.tsx

```tsx
import * as React from 'react';
import * as enzyme from 'enzyme';
import Hello from './Hello';

it('renders the correct text when no enthusiasm level is given', () => {
  const hello = enzyme.shallow(<Hello name='Durban' />);
  expect(hello.find('.greeting').text()).toEqual('Hello Durban!');
});

it('renders the correct text with an explicit enthusiasm of 1', () => {
  const hello = enzyme.shallow(<Hello name='Durban' enthusiasmLevel={1} />);
  expect(hello.find('.greeting').text()).toEqual('Hello Durban!');
});

it('renders the correct text with an explicit enthusiasm of 5', () => {
  const hello = enzyme.shallow(<Hello name='Durban' enthusiasmLevel={5} />);
  expect(hello.find('.greeting').text()).toEqual('Hello Durban!!!!!');
});

it('throws when the enthusiasm level is 0', () => {
  expect(() => {
    enzyme.shallow(<Hello name="Durban" enthusiasmLevel={0} />);
  }).toThrow();
});

it('throws when the enthusiasm level is negative', () => {
  expect(() => {
    enzyme.shallow(<Hello name='Durban' enthusiasmLevel={-1} />);
  }).toThrow();
});
```

这些测试非常基础，但你应该能够掌握一切。

运行代码

```bash
npm run test
```

即可看到运行通过测试的结果

小提示

如果你在国内的话，建议将test的命令

```json
"test": "react-scripts-ts test --env=jsdom",
```

改为

```json
"test": "react-scripts-ts test --env=jsdom --watchman=false",
```

这个原因是因为。默认启动了watchman，watchman是需要连接国外的，如果在国内的话，会因为连接不上导致，看不到测试结果

运行后的结果类似如下

```bash
PASS  src/App.test.tsx
 PASS  src/components/Hello.test.tsx

Test Suites: 2 passed, 2 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        3.68s
Ran all test suites related to changed files.

Watch Usage
 › Press p to filter by a filename regex pattern.
 › Press t to filter by a test name regex pattern.
 › Press q to quit watch mode.
 › Press Enter to trigger a test run.
```

未完待续...
