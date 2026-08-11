---
title: "React16 Jest单元测试 之 Setup and Teardown(重复设置或重复安装、一次设置或一次安装)"
date: "2025-07-07 16:41:40"
slug: "react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-chong-fu-she-zhi-huo-chong-fu-an-zhuang-yi-ci-she-zhi-huo-yi-ci-an-zhuang"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown(重复设置或重复安装、一次设置或一次安装)/"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown(重复设置或重复安装、一次设置或一次安装).html"
  - "/React16-Jest单元测试-之-Setup-and-Teardown(重复设置或重复安装、一次设置或一次安装)/"
  - "/React16-Jest单元测试-之-Setup-and-Teardown(重复设置或重复安装、一次设置或一次安装).html"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown-重复设置或重复安装-一次设置或一次安装/"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown-重复设置或重复安装-一次设置或一次安装.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-chong-fu-she-zhi-huo-chong-fu-an-zh/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-chong-fu-she-zhi-huo-chong-fu-a.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-chong-fu-she-zhi-huo-chong-fu-an-zhuang-yi.html"
---
### **项目初始化【这里使用之前的项目，节省时间】**

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.17
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.17
npm install
```

一般写单元测试的时候有时候需要在测试运行之前做一个操作，当测试运行完之后有时候也需要执行一些操作，Jest则提供了类似的帮助函数来处理这类问题

### **Repeating Setup For Many Tests 多次安装**

如果在很多测试中需要重复进行某个操作，则可以使用beforeEach和afterEach，

如下，两个测试中都与城市数据进行交互。在每个测试之前调用一个方法initCityDatabase()，并且在每次测试之后调用clearCityDatabase()方法。

```js
let citys = [];
let time = 1;
const isCity = (city) => {
  if (citys.indexOf(city) > -1) {
    return true;
  }
  return false;
};

const initCityDatabase = () => new Promise((resolve, reject) => {
  let promise;

  try {
    setTimeout(() => {
      if (time === 1) {
        citys.push('natasha1');
        time += 1;
      } else if (time === 2) {
        citys.push('natasha2');
        time += 1;
      }
      promise = resolve(citys);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

const clearCityDatabase = () => new Promise((resolve, reject) => {
  let promise;
  try {
    setTimeout(() => {
      citys = [];
      promise = resolve(citys);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

beforeEach(() => initCityDatabase());

afterEach(() => clearCityDatabase());

test('The city database has natasha1', () => {
  expect(isCity('natasha1')).toBeTruthy();
});

test('The city database has natasha2', () => {
  expect(isCity('natasha2')).toBeTruthy();
});
```

执行npm test会得到如下结果

```bash
> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_setup_each_moretime.test.js (5.115s)
  ● Console

    console.log src/__tests__/jest_setup_each_moretime.test.js:16
      moretime -> init time =  1
    console.log src/__tests__/jest_setup_each_moretime.test.js:37
      moretime -> clear time =  1
    console.log src/__tests__/jest_setup_each_moretime.test.js:16
      moretime -> init time =  2
    console.log src/__tests__/jest_setup_each_moretime.test.js:37
      moretime -> clear time =  2

 PASS  src/__tests__/jest_async_callback.test.js
 PASS  src/__tests__/jest_async_promise.test.js (6.436s)
 PASS  src/__tests__/jest_async_await.test.js (6.433s)
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/jest_common.test.js

Test Suites: 7 passed, 7 total
Tests:       24 passed, 24 total
Snapshots:   0 total
Time:        8.91s
Ran all test suites.
```

从上面的例子可以看出有个地方不同

```bash
beforeEach(() => initCityDatabase());

afterEach(() => clearCityDatabase());
```

这里看不出我调用的函数是否进行了针对promise的操作，实际上上面的两行代码等于下面的几行代码

```js
beforeEach(() => {
  return initCityDatabase();
});

afterEach(() => {
  return clearCityDatabase();
});
```

如果initCityDatabase和clearCityDatabase不是promise或者callback的函数完全可以直接调用不需要加return，这里是需要注意的地方，对于函数如果是callbacks方式的话，可以看前面的文章[React16 Jest单元测试 之 Testing Asynchronous Code]了解，还可以看出initCityDatabase和clearCityDatabase的调用次数

### **One-Time Setup 一次安装**

在某些情况下，只需要在文件的开头进行一次安装。当安装的逻辑是异步的时候，这可能会特别麻烦，所以不能直接进行内联。

Jest提供beforeAll和afterAll来处理这种情况。如下，如果initCityDatabase和clearCityDatabase都返回了promise，并且城市数据可以在测试之间重复使用，那么我们可以将我们的测试代码更改为：

```js
let citys = [];
let time1 = 1;
let time2 = 1;
const isCity = (city) => {
  if (citys.indexOf(city) > -1) {
    return true;
  }
  return false;
};

const initCityDatabase = () => new Promise((resolve, reject) => {
  let promise;

  try {
    setTimeout(() => {
      console.log('onetime -> init time = ', time1);
      time1 += 1;
      citys.push('natasha1');
      citys.push('natasha2');
      promise = resolve(citys);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

const clearCityDatabase = () => new Promise((resolve, reject) => {
  let promise;
  try {
    console.log('onetime -> clear time = ', time2);
    time2 += 1;
    setTimeout(() => {
      citys = [];
      promise = resolve(citys);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

beforeAll(() => initCityDatabase());

afterAll(() => clearCityDatabase());

test('The city database has natasha1', () => {
  expect(isCity('natasha1')).toBeTruthy();
});

test('The city database has natasha2', () => {
  expect(isCity('natasha2')).toBeTruthy();
});
```

运行npm test得到类似如下结果

```bash
> webpack4_react16_reactrouter4 @1 .0 .0 test / Users / durban / nodejs / webpack - react - demo >
  jest--notify--watchman = false

PASS src / __tests__ / jest_setup_each_moretime.test.js(5.234 s)
PASS src / __tests__ / jest_async_await.test.js(6.518 s)
PASS src / __tests__ / jest_async_promise.test.js(6.546 s)
PASS src / __tests__ / CheckboxWithLabelComponent.test.jsx
PASS src / __tests__ / jest_common.test.js
PASS src / __tests__ / sum.test.js
PASS src / __tests__ / jest_setup_each_onetime.test.js● Console

console.log src / __tests__ / jest_setup_each_onetime.test.js: 16
onetime - > init time = 1
console.log src / __tests__ / jest_setup_each_onetime.test.js: 32
onetime - > clear time = 1

PASS src / __tests__ / jest_async_callback.test.js

Test Suites: 8 passed, 8 total
Tests: 26 passed, 26 total
Snapshots: 0 total
Time: 10.007 s
Ran all test suites.
```

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.18
```
