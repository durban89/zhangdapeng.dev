---
title: "React16 Jest单元测试 之 Testing Asynchronous Code"
date: "2025-07-07 16:41:24"
slug: "react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-code"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code/"
  - "/2025/07/07/React16-Jest单元测试-之-Testing-Asynchronous-Code.html"
  - "/React16-Jest单元测试-之-Testing-Asynchronous-Code/"
  - "/React16-Jest单元测试-之-Testing-Asynchronous-Code.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-code/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-code.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-testing-asynchronous-code.html"
---
通常Javascript代码很多情况下是异步运行的，当代码异步运行的时候，Jest需要知道什么运行结束，然后进行下一个单元测试，Jest自身就有需要方法来处理这个。下面记录如下

### **项目初始化**【这里还是之前的项目，省的在配置麻烦】

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.15
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.15
npm install
```

### **Callbacks**

一般情况下，Javascript的异步模式是通过Callbacks进行的

比如有一个函数fetchData(callback)是用来获取数据的，获取完数据回调callback(data),这里测试的时候返回的数据是一个字符串"peanut butter"

默认情况下，一旦Jest测试到达执行结束，它就会完成测试。这意味着下面这个测试不会按预期工作：

```js
function fetchData(callback) {
  setTimeout(() => {
    callback('peanut butter');
  }, 1000);
}

// Don't do this!
test('one section the data is peanut butter', () => {
  function callback(data) {
    console.log('one section data = ', data);
    expect(data).toBe('peanut butter');
  }

  fetchData(callback);
});
```

执行 npm test 得到如下结果

```bash
> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_async.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/sum.test.js

Test Suites: 4 passed, 4 total
Tests:       14 passed, 14 total
Snapshots:   0 total
Time:        2.376s, estimated 3s
Ran all test suites.
```

从上面可以看出并没有打印出我们console.log要输出的内容，问题在于，还有没有等到fetchData执行完，测试就已经完成了。

针对这个问题，有一种替代形式的测试可以解决这个问题。就是不要将测试放入带有空参数的函数中，而应使用称为done的单个参数。Jest将在完成测试之前等待完成回调。如下

```js
function fetchData(callback) {
  setTimeout(() => {
    callback('peanut butter');
  }, 1000);
}

test('two section the data is peanut butter', (done) => {
  function callback(data) {
    console.log('two section data = ', data);
    expect(data).toBe('peanut butter');
    done();
  }

  fetchData(callback);
});
```

执行 npm test 得到如下结果

```bash
> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_async.test.js
  ● Console

    console.log src/__tests__/jest_async.test.js:19
      two section data =  peanut butter

 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/sum.test.js

Test Suites: 4 passed, 4 total
Tests:       14 passed, 14 total
Snapshots:   0 total
Time:        3.438s
Ran all test suites.
```

跟上一个对比的话多了如下的输出代码

```bash
● Console

    console.log src/__tests__/jest_async.test.js:19
      two section data =  peanut butter
```

如果done()永远不会被调用，那么测试会失败。

### **Promises**

如果代码里面使用Promises的话，有一个非常简单的方法来进行异步测试，只需要在测试中返回一个promise就可以了，Jest将等到promise调用resolve，如果promise是reject，则测试结果失败。如下例子，将callback的函数替换为promise的函数

```js
const fetchData = (err) => {
  const promise = new Promise((resolve, reject) => {
    if (err) {
      return reject('error');
    }

    return setTimeout(() => resolve('peanut butter'), 3000);
  });
  return promise;
};

test('the data is peanut butter', () => {
  const promise = fetchData().then((data) => {
    // console.log('third section data = ', data);
    expect(data).toBe('peanut butter');
  });

  return promise;
});

test('the fetch fails with an error', () => {
  expect.assertions(1);
  const promise = fetchData(true).catch((err) => {
    expect(err).toMatch('error');
  });

  return promise;
});
```

一定要确定返回的是一个promise，不行Jest会在fetchData完成之前先完成。

如果期望promise是reject，使用.catch方法，确保添加了expect.assertions去验证产生了一定数量的assertions被调用，否则一个fulfilled promise的测试将会失败

### **.resolves / .rejects**

除了上面简单的方法还可以在测试语句中使用.resolves / .rejects

.resolves matcher如下

```js
test('the data is peanut butter', () => {
  const promise = expect(fetchData()).resolves.toBe('peanut butter');
  return promise;
});
```

.rejects matcher如下

```js
test('the fetch fails with an error', () => {
  const promise = expect(fetchData(true)).rejects.toMatch('error');
  return promise;
});
```

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.16
```
