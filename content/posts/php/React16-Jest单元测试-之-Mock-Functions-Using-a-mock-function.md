---
title: "React16 Jest单元测试 之 Mock Functions(Using a mock function)"
date: "2025-07-07 16:41:48"
slug: "react16-jest-dan-yuan-ce-shi-zhi-mock-functionsusing-a-mock-function"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Using-a-mock-function)/"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Using-a-mock-function).html"
  - "/React16-Jest单元测试-之-Mock-Functions(Using-a-mock-function)/"
  - "/React16-Jest单元测试-之-Mock-Functions(Using-a-mock-function).html"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions-Using-a-mock-function/"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions-Using-a-mock-function.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsusing-a-mock-function/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsusing-a-mock-function.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsusing-a-mock-function.html"
---
### **项目初始化【这里使用之前的项目，节省时间】**

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.19
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.19
npm install
```

mock function 可以通过擦除函数的实际实现，捕获对函数的调用（以及在这些调用中传递的参数），在使用new实例化时捕获构造函数的实例，以及允许test-time来轻松测试代码之间的链接返回值的配置。

有两种方法来mock function：通过创建一个mock function来使用测试代码，或者编写一个手动模拟来覆盖模块依赖。

下面先记录下如何使用mock function

### **Using a mock function**

假设我们正在测试一个函数forEach的实现，它调用所提供数组中每个项的回调。如下

```js
function forEach(items, callback) {
  for (let i = 0; i < items.length; i += 1) {
    callback(items[i]);
  }
}

const mockFunction = jest.fn();
forEach([0, 1], mockFunction);

test('mockFunction被调用2次', () => {
  expect(mockFunction.mock.calls.length).toBe(2);
});

test('第一个调用第一个参数是0', () => {
  expect(mockFunction.mock.calls[0][0]).toBe(0);
});

test('第一个调用第一个参数是1', () => {
  expect(mockFunction.mock.calls[1][0]).toBe(1);
});
```

运行

```bash
npx jest src/__tests__/jest_use_mock_function.test.js --notify --watchman=false
```

后输出结果类似如下

```bash
PASS  src/__tests__/jest_use_mock_function.test.js
  ✓ mockFunction被调用2次 (5ms)
  ✓ 第一个调用第一个参数是0
  ✓ 第一个调用第一个参数是1

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        2.341s
Ran all test suites matching /src\/__tests__\/jest_use_mock_function.test.js/i.
```

### **.mock property**

所有模拟函数都有这个特殊的.mock属性，它是关于如何调用函数以及保留函数返回的数据的地方。.mock属性还会跟踪每次调用的值，因此也可以检查它：

```js
const myMock = jest.fn();

const a = new myMock();
const b = {};
const bound = myMock.bind(b);
bound();

console.log(myMock.mock.instances);
```

运行后会看到console.log输出的内容类似如下

```bash
[ mockConstructor {}, {} ]
```

这些模拟成员在测试中非常有用，用于断言这些函数如何被调用，实例化或他们返回了什么，代码如下

```js
// 函数被调用的次数
expect(someMockFunction.mock.calls.length).toBe(1);

// 函数第1次被调用的第一个参数值是'first arg'
expect(someMockFunction.mock.calls[0][0]).toBe('first arg');

// 函数第2次被调用的第一个参数值是'second arg'
expect(someMockFunction.mock.calls[0][1]).toBe('second arg');

// 函数第1次被调用的返回值是'return value'
expect(someMockFunction.mock.results[0].value).toBe('return value');

// 函数被实例化了2次
expect(someMockFunction.mock.instances.length).toBe(2);

// 函数第一次被实例化返回的对象里面有个'name'的属性，它的值为'test'
expect(someMockFunction.mock.instances[0].name).toEqual('test');
```

具体如何使用后面的分享会涉及到多多关注

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.20
```
