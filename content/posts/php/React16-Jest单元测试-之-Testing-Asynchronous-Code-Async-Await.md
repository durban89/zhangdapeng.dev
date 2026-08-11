---
title: "React16 Jest单元测试 之 Testing Asynchronous Code(Async/Await)"
date: "2025-07-07 16:41:27"
slug: "react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-codeasyncawait"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code(Async/Await)/"
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code(Async/Await).html"
  - "/React16-Jest单元测试-之-Testing-Asynchronous-Code(Async/Await)/"
  - "/React16-Jest单元测试-之-Testing-Asynchronous-Code(Async/Await).html"
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code-Async-Await/"
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code-Async-Await.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-codeasyncawait/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-codeasyncawait.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-codeasyncawait.html"
---
通常Javascript代码很多情况下是异步运行的，当代码异步运行的时候，Jest需要知道什么运行结束，然后进行下一个单元测试，Jest自身就有需要方法来处理这个。下面记录如下

### **项目初始化【这里还是之前的项目，省的在配置麻烦】**

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.16
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.16
npm install
```

### **Async/Await**

上篇文章分享了关于异步测试的，这里继续分享下使用Async/Await进行异步测试

使用Async/Await写测试只需要在写测试的时候在function前面加入async关键字就可以了，比如下面的测试

```js
const fetchData = (err) => {
  const promise = new Promise((resolve, reject) => {
    if (err) {
      return reject('error');
    }

    return setTimeout(() => resolve('gowhich'), 3000);
  });
  return promise;
};

test('data的数据是"gowhich"', async () => {
  const data = await fetchData();
  expect(data).toBe('gowhich');
});

test('获取数据失败', async () => {
  try {
    await fetchData(true);
  } catch (err) {
    expect(err).toBe('error');
  }
});
```

也可以将async/await和.resolves或者.rejects结合来使用，如下

```js
const fetchData = (err) => {
  const promise = new Promise((resolve, reject) => {
    if (err) {
      return reject('error');
    }

    return setTimeout(() => resolve('gowhich'), 3000);
  });
  return promise;
};

test('data的数据是"gowhich"', async () => {
  await expect(fetchData()).resolves.toBe('gowhich');
});

test('获取数据失败', async () => {
  await expect(fetchData(true)).rejects.toMatch('error');
});
```

执行npm test,得到的结果如下

```bash
> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_async_callback.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/jest_async_promise.test.js (6.718s)
 PASS  src/__tests__/jest_async_await.test.js (8.424s)

Test Suites: 6 passed, 6 total
Tests:       22 passed, 22 total
Snapshots:   0 total
Time:        10.927s
Ran all test suites.
```

在这些情况下，async和await实际上只是与promises示例使用的相同逻辑的语法糖。

这些形式都不是特别优于其他形式，您可以在代码库或甚至单个文件中混合使用它们。

这取决于哪种风格可以让你的测试更简单。

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.17
```
