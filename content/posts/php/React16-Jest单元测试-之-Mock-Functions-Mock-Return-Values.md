---
title: "React16 Jest单元测试 之 Mock Functions(Mock Return Values)"
date: "2025-07-07 16:41:53"
slug: "react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-return-values"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Mock-Return-Values)/"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Mock-Return-Values).html"
  - "/React16-Jest单元测试-之-Mock-Functions(Mock-Return-Values)/"
  - "/React16-Jest单元测试-之-Mock-Functions(Mock-Return-Values).html"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions-Mock-Return-Values/"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions-Mock-Return-Values.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-return-values/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-return-values.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-return-values.html"
---
项目初始化【这里使用之前的项目，节省时间】

项目初始化地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.20
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.20
npm install
```

**Mock Return Values**

Jest的模拟函数(Mock function)也可以用来在测试中注入测试值到测试的代码中，如下

```js
const myMock = jest.fn();
console.log(myMock);

myMock
  .mockReturnValueOnce(10)
  .mockReturnValueOnce('x')
  .mockReturnValue(true);

console.log(myMock(), myMock(), myMock(), myMock(), myMock());
```

运行npx jest src/\_\_tests\_\_/jest\_mock\_return\_values.test.js --notify --watchman=false 后输出的结果类似如下

```bash
console.log src/__tests__/jest_mock_return_values.test.js:2
{ [Function: mockConstructor]
    _isMockFunction: true,
    getMockImplementation: [Function],
    mock: [Getter/Setter],
    mockClear: [Function],
    mockReset: [Function],
    mockRestore: [Function],
    mockReturnValueOnce: [Function],
    mockResolvedValueOnce: [Function],
    mockRejectedValueOnce: [Function],
    mockReturnValue: [Function],
    mockResolvedValue: [Function],
    mockRejectedValue: [Function],
    mockImplementationOnce: [Function],
    mockImplementation: [Function],
    mockReturnThis: [Function],
    mockName: [Function],
    getMockName: [Function] }

console.log src/__tests__/jest_mock_return_values.test.js:9
10 'x' true true true
```

模拟函数(Mock function)在使用函数continuation-passing风格的代码中也非常有效。以这种风格编写的代码有助于避免需要复杂的存根，以重新创建它们所代表的真实组件的行为，从而倾向于在使用它们之前直接将值注入测试中。具体看如下代码

```js
const filterTestFn = jest.fn();

// 第一次mock返回true,第二次mock返回false
filterTestFn.mockReturnValueOnce(true).mockReturnValueOnce(false);

const result = [11, 12].filter(filterTestFn);

console.log(result);
console.log(filterTestFn.mock.calls);
```

运行npx jest src/\_\_tests\_\_/jest\_mock\_return\_values.test.js --notify --watchman=false 后得到的结果类似如下

```bash
console.log src/__tests__/jest_mock_return_values.test.js:20
[ 11 ]

console.log src/__tests__/jest_mock_return_values.test.js:22
[ [ 11, 0, [ 11, 12 ] ], [ 12, 1, [ 11, 12 ] ] ]
```

现实世界中大多数的例子实际上是在依赖的组件上获取模拟函数并对其进行配置，但技术是相同的。在这些情况下，尽量避免在没有直接测试的任何函数内部实现逻辑。

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.21
```
