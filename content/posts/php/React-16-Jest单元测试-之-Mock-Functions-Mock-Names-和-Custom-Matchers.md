---
title: "React 16 + Jest单元测试 之 Mock Functions(Mock Names 和 Custom Matchers)"
date: "2025-07-07 16:42:01"
slug: "react-16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-names-he-custom-matchers"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-+-Jest单元测试-之-Mock-Functions(Mock-Names-和-Custom-Matchers)/"
  - "/2025/07/07/React-16-+-Jest单元测试-之-Mock-Functions(Mock-Names-和-Custom-Matchers).html"
  - "/React-16-+-Jest单元测试-之-Mock-Functions(Mock-Names-和-Custom-Matchers)/"
  - "/React-16-+-Jest单元测试-之-Mock-Functions(Mock-Names-和-Custom-Matchers).html"
  - "/2025/07/07/React-16-Jest单元测试-之-Mock-Functions-Mock-Names-和-Custom-Matchers/"
  - "/2025/07/07/React-16-Jest单元测试-之-Mock-Functions-Mock-Names-和-Custom-Matchers.html"
  - "/2025/07/07/react-16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-names-he-custom-matchers/"
  - "/2025/07/07/react-16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-names-he-custom-matchers.html"
  - "/react-16-jest-dan-yuan-ce-shi-zhi-mock-functionsmock-names-he-custom-matchers.html"
---
### **项目初始化【这里使用之前的项目，节省时间】**

项目初始化地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.22
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.22
npm install
```

### **Mock Names**

您可以选择为mock function提供一个名称，该名称将在测试错误输出中显示，而不是"jest.fn()"。如果您希望能够快速识别在测试输出中报告错误的mock function，请使用此选项。如下

```js
const myMockFunc = jest
  .fn()
  .mockReturnValue('default')
  .mockImplementation(v => 42 + v)
  .mockName('add42');

test('add 42', () => {
  expect(myMockFunc(1)).toEqual(43);
});
```

### **Custom Matchers**

最后，为了简化断言如何调用mock函数，Jest提供了一些自定义匹配器函数，如下

```js
// mock function至少被调用一次
expect(mockFunc).toBeCalled();

// mock function至少在带有具体参数的情况下被调用一次
expect(mockFunc).toBeCalledWith(arg1, arg2);

// mock function最后在带有具体参数的情况下被调用
expect(mockFunc).lastCalledWith(arg1, arg2);

// 所有的调用和mock被作为snapshot写入到文件
expect(mockFunc).toMatchSnapshot();
```

这些匹配器实际上只是用于检查.mock属性的常见形式的糖。

可以自己手动完成此操作，如果想这更符合自己的口味或者需要做一些更具体的事情，比如如下这些

```js
// mock function至少被调用一次
expect(mockFunc.mock.calls.length).toBeGreaterThan(0);

// mock function至少在带有具体参数的情况下被调用一次
expect(mockFunc.mock.calls).toContain([arg1, arg2]);

// mock function最后在带有具体参数的情况下被调用
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1]).toEqual([
  arg1,
  arg2,
]);

// mock function被最后一次调用传入的第一个参数是`42`
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1][0]).toBe(42);

// 一个snapshot将会检查mock在以同样的参数同样的次数被调用，它也将在名称上断言
expect(mockFunc.mock.calls).toEqual([[arg1, arg2]]);
expect(mockFunc.mock.getMockName()).toBe('a mock name');
```

如果想要一个完成的matchers，可以到官网点击[这里](http://jestjs.io/docs/en/expect)去查看

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.23
```
