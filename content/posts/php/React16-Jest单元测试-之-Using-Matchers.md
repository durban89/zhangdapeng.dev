---
title: "React16 Jest单元测试 之 Using Matchers"
date: "2025-07-07 16:41:19"
slug: "react16-jest-dan-yuan-ce-shi-zhi-using-matchers"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Using-Matchers/"
  - "/2025/07/07/React16-Jest单元测试-之-Using-Matchers.html"
  - "/React16-Jest单元测试-之-Using-Matchers/"
  - "/React16-Jest单元测试-之-Using-Matchers.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-using-matchers/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-using-matchers.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-using-matchers.html"
---
### **项目初始化【这里还是之前的项目，省的在配置麻烦】**

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git

tag：v_1.0.14
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git

cd webpack4-react16-reactrouter-demo

git fetch origin

git checkout v_1.0.14

npm install
```

**普通的Matchers**

src/\_\_tests\_\_/jest\_common.test.js

```js
test('two plus two is four', () => {
  expect(2 + 2).toBe(4);
});
```

运行npm test

```bash
$ npm test

> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx

Test Suites: 3 passed, 3 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        2.963s
Ran all test suites.
```

在上面的代码中expect(2+2)返回了一个"expectation"对象，这些"expectation"对象除了调用matchers之外不会做太多其他的事情，上面代码中".toBe(4)"就是一个matchers.当jest运行时，他会捕获所有失败了的matchers,然后打印出比较友好的错误信息。

"toBe"使用Object.is去测试是否相等。如果想要检查对象的值是否相等，可以使用"toEqual"代替.

```js
test('object assignment', () => {
  const data = {one: 1};
  data['two'] = 2;
  expect(data).toEqual({one: 1, two: 2});
});
```

toEqual会用递归的方式检查object或array每个值

也可以使用matchers的相反的方式进行测试

```js
test('adding positive numbers is not zero', () => {
  for (let a = 1; a < 10; a += 1) {
    for (let b = 1; b < 10; b += 1) {
      expect(a + b).not.toBe(0);
    }
  }
});
```

在测试中有时候需要去判断"undefined","null"和"false"的区别，但是有时候又不想区分他们，Jest提供了帮助，从而实现测试中自己想要的情况

* toBeNull只匹配 null
* toBeUndefined只匹配 undefined
* toBeDefined是跟toBeUndefined相反
* toBeTruthy匹配任何if条件认为true的
* toBeFalsy匹配任何if条件认为false的

比如下面

```js
test('null', () => {
  const n = null;
  expect(n).toBeNull();
  expect(n).toBeDefined();
  expect(n).not.toBeUndefined();
  expect(n).not.toBeTruthy();
  expect(n).toBeFalsy();
});

test('zero', () => {
  const z = 0;
  expect(z).not.toBeNull();
  expect(z).toBeDefined();
  expect(z).not.toBeUndefined();
  expect(z).not.toBeTruthy();
  expect(z).toBeFalsy();
});
```

下面看看其他的一些matchers

### **Numbers**

大多数数字的比较方法都有等价的Matchers。

```js
test('two plus two', () => {
  const value = 2 + 2;
  expect(value).toBeGreaterThan(3);
  expect(value).toBeGreaterThanOrEqual(3.5);
  expect(value).toBeLessThan(5);
  expect(value).toBeLessThanOrEqual(4.5);

  // toBe and toEqual are equivalent for numbers
  expect(value).toBe(4);
  expect(value).toEqual(4);
});
```

对于浮点数，我们不希望出现四舍五入的错误情况，因此判断小数的是否相等的时候，使用"toBeCloseTo"代替"toEqual"，如下

```js
test('adding floating point numbers', () => {
  const value = 0.1 + 0.2;
  expect(value).toBeCloseTo(0.3);
});
```

### **Strings**

可以使用toMatch在正则表达式中检查字符串

```js
test('there is no I in team', () => {
  expect('team').not.toMatch(/I/);
});

test('but there is a "stop" in Christoph', () => {
  expect('Christoph').toMatch(/stop/);
});
```

### **Arrays**

可以使用toContain检查数组是否包含特定项目

```js
const shoppingList = [
  'diapers',
  'kleenex',
  'trash bags',
  'paper towels',
  'beer',
];

test('the shopping list has beer on it', () => {
  expect(shoppingList).toContain('beer');
});
```

### **Exceptions**

如果想测试某个特定函数在调用时会抛出错误，请使用toThrow

```js
test('compiling android goes as expected', () => {
  function compileAndroidCode() {
    throw new Error('you are useing the wrong JDK');
  }

  expect(compileAndroidCode).toThrow();
  expect(compileAndroidCode).toThrow(Error);

  // 匹配错误信息
  expect(compileAndroidCode).toThrow('you are useing the wrong JDK');
  expect(compileAndroidCode).toThrow(/JDK/);
});
```

上面的全部测试案例测试结果如下

```bash
$ npm test

> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/sum.test.js

Test Suites: 3 passed, 3 total
Tests:       13 passed, 13 total
Snapshots:   0 total
Time:        2.752s
Ran all test suites.
```

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git

tag：v_1.0.15
```
