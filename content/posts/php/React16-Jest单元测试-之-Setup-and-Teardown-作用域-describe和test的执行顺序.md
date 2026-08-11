---
title: "React16 Jest单元测试 之 Setup and Teardown(作用域、describe和test的执行顺序)"
date: "2025-07-07 16:41:44"
slug: "react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-zuo-yong-yu-describe-he-test-de-zhi-xing-shun-xu"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown(作用域、describe和test的执行顺序)/"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown(作用域、describe和test的执行顺序).html"
  - "/React16-Jest单元测试-之-Setup-and-Teardown(作用域、describe和test的执行顺序)/"
  - "/React16-Jest单元测试-之-Setup-and-Teardown(作用域、describe和test的执行顺序).html"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown-作用域-describe和test的执行顺序/"
  - "/2025/07/07/React16-Jest单元测试-之-Setup-and-Teardown-作用域-describe和test的执行顺序.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-zuo-yong-yu-describe-he-test-de-zhi/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-zuo-yong-yu-describe-he-test-de.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-setup-and-teardown-zuo-yong-yu-describe-he-test-de-zhi-xing-s.html"
---
### **项目初始化【这里使用之前的项目，节省时间】**

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.18
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.18
npm install
```

### **Scoping 作用域**

默认情况下，before和after中的代码适用于每个测试模块。

describe可以将测试分组，将多个测分到一个有意义的组里面。

当describe块将测试分组在一起时，before和after中的代码仅适用于describe块内的测试。具体如下

假设有城市数据库和食品数据库。我们分别可以为不同的测试做不同的设置：

```js
const citys = [];
const foods = [];
let time1 = 1;
let time2 = 1;
const isCity = (city) => {
  if (citys.indexOf(city) > -1) {
    return true;
  }
  return false;
};

const isCityAndFood = (cityAndFood) => {
  let hasCity = false;
  let hasFood = false;

  if (citys.indexOf(cityAndFood.city) > -1) {
    hasCity = true;
  }

  if (foods.indexOf(cityAndFood.food) > -1) {
    hasFood = true;
  }

  if (hasCity && hasFood) {
    return true;
  }

  return false;
};
const initCityDatabase = () => new Promise((resolve, reject) => {
  let promise;

  try {
    setTimeout(() => {
      console.log('initCityDatabase time = ', time1);
      if (time1 === 1) {
        citys.push('Shanghai');
      } else if (time1 === 2) {
        citys.push('Chifeng');
      }
      time1 += 1;
      promise = resolve(citys);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

const initFoodDatabase = () => new Promise((resolve, reject) => {
  let promise;

  try {
    setTimeout(() => {
      console.log('initFoodDatabase time = ', time2);
      if (time2 === 1) {
        foods.push('Banana');
      } else if (time2 === 2) {
        foods.push('Apple');
      }
      time2 += 1;
      promise = resolve(foods);
    }, 1000);
  } catch (err) {
    return reject(err);
  }

  return promise;
});

beforeEach(() => initCityDatabase());

test('city database has Shanghai', () => {
  expect(isCity('Shanghai')).toBeTruthy();
});

test('city database has Chifeng', () => {
  expect(isCity('Chifeng')).toBeTruthy();
});

describe('matching cities to foods', () => {
  beforeEach(() => initFoodDatabase());

  test('database has Shanghai and Banana', () => {
    expect(isCityAndFood({
      city: 'Shanghai',
      food: 'Banana',
    })).toBe(true);
  });

  test('database has Chifeng and Apple', () => {
    expect(isCityAndFood({
      city: 'Chifeng',
      food: 'Apple',
    })).toBe(true);
  });
});
```

执行npm test得到类似如下结果

```bash
> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_async_promise.test.js (6.41s)
 PASS  src/__tests__/jest_async_await.test.js (6.401s)
 PASS  src/__tests__/jest_setup_describe.js (7.09s)
  ● Console

    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  1
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  2
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  3
    console.log src/__tests__/jest_setup_describe.js:56
      initFoodDatabase time =  1
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  4
    console.log src/__tests__/jest_setup_describe.js:56
      initFoodDatabase time =  2

 PASS  src/__tests__/jest_async_callback.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/jest_setup_each_onetime.test.js
 PASS  src/__tests__/jest_setup_each_moretime.test.js

Test Suites: 9 passed, 9 total
Tests:       30 passed, 30 total
Snapshots:   0 total
Time:        12.94s
Ran all test suites.
```

请注意这里

```bash
● Console

    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  1
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  2
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  3
    console.log src/__tests__/jest_setup_describe.js:56
      initFoodDatabase time =  1
    console.log src/__tests__/jest_setup_describe.js:35
      initCityDatabase time =  4
    console.log src/__tests__/jest_setup_describe.js:56
      initFoodDatabase time =  2
```

initCityDatabase执行了4次，initFoodDatabase执行了2次，这是因为顶级beforeEach在describe块内的beforeEach之前执行。

这可能有助于说明所有钩子的执行顺序。下面来做个比较

```js
beforeAll(() => console.log('1 - beforeAll'));
afterAll(() => console.log('1 - afterAll'));
beforeEach(() => console.log('1 - beforeEach'));
afterEach(() => console.log('1 - afterEach'));
test('', () => console.log('1 - test'));
describe('Scoped / Nested block', () => {
  beforeAll(() => console.log('2 - beforeAll'));
  afterAll(() => console.log('2 - afterAll'));
  beforeEach(() => console.log('2 - beforeEach'));
  afterEach(() => console.log('2 - afterEach'));
  test('', () => console.log('2 - test'));
});
```

运行npm test得到结果如下

```bash
xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/jest_setup_describe_diff.js
  ● Console

    console.log src/__tests__/jest_setup_describe_diff.js:1
      1 - beforeAll
    console.log src/__tests__/jest_setup_describe_diff.js:3
      1 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:5
      1 - test
    console.log src/__tests__/jest_setup_describe_diff.js:4
      1 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:7
      2 - beforeAll
    console.log src/__tests__/jest_setup_describe_diff.js:3
      1 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:9
      2 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:11
      2 - test
    console.log src/__tests__/jest_setup_describe_diff.js:10
      2 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:4
      1 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:8
      2 - afterAll
    console.log src/__tests__/jest_setup_describe_diff.js:2
      1 - afterAll

 PASS  src/__tests__/jest_async_promise.test.js (6.439s)
 PASS  src/__tests__/jest_setup_describe.js (7.13s)
 PASS  src/__tests__/jest_async_await.test.js (6.063s)
 PASS  src/__tests__/jest_async_callback.test.js
 PASS  src/__tests__/jest_common.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx
 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/jest_setup_each_onetime.test.js
 PASS  src/__tests__/jest_setup_each_moretime.test.js

Test Suites: 10 passed, 10 total
Tests:       32 passed, 32 total
Snapshots:   0 total
Time:        12.892s
Ran all test suites.
```

可以从这里看出其执行的顺序

```bash
● Console

    console.log src/__tests__/jest_setup_describe_diff.js:1
      1 - beforeAll
    console.log src/__tests__/jest_setup_describe_diff.js:3
      1 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:5
      1 - test
    console.log src/__tests__/jest_setup_describe_diff.js:4
      1 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:7
      2 - beforeAll
    console.log src/__tests__/jest_setup_describe_diff.js:3
      1 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:9
      2 - beforeEach
    console.log src/__tests__/jest_setup_describe_diff.js:11
      2 - test
    console.log src/__tests__/jest_setup_describe_diff.js:10
      2 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:4
      1 - afterEach
    console.log src/__tests__/jest_setup_describe_diff.js:8
      2 - afterAll
    console.log src/__tests__/jest_setup_describe_diff.js:2
      1 - afterAll
```

### **Order of execution of describe and test blocks - describe和test的执行顺序**

在一个测试文件中Jest在执行真实的测试之前先执行所有describe的handlers。

这是在before\*和after\*的handlers中进行setup和teardown的另一个原因而不是在describe blocks。

一旦describe blocks完成，默认情况下，Jest将按照它们在collection phase遇到的顺序依次运行所有测试，等待每个测试完成并在继续之前进行整理。

理解起来很难，看下下面的例子，考虑下下面的代码猜测下输出的顺序是什么：

```js
describe('outer', () => {
  console.log('describe outer-a');

  describe('describe inner 1', () => {
    console.log('describe inner 1');
    test('test 1', () => {
      console.log('test for describe inner 1');
      expect(true).toEqual(true);
    });
  });

  console.log('describe outer-b');

  test('test 1', () => {
    console.log('test for describe outer');
    expect(true).toEqual(true);
  });

  describe('describe inner 2', () => {
    console.log('describe inner 2');
    test('test for describe inner 2', () => {
      console.log('test for describe inner 2');
      expect(false).toEqual(false);
    });
  });

  console.log('describe outer-c');
});
```

执行npm test，看下下面这块的输出

```bash
● Console

    console.log src/__tests__/jest_setup_describe_order.js:2
      describe outer-a
    console.log src/__tests__/jest_setup_describe_order.js:5
      describe inner 1
    console.log src/__tests__/jest_setup_describe_order.js:12
      describe outer-b
    console.log src/__tests__/jest_setup_describe_order.js:20
      describe inner 2
    console.log src/__tests__/jest_setup_describe_order.js:27
      describe outer-c
    console.log src/__tests__/jest_setup_describe_order.js:7
      test for describe inner 1
    console.log src/__tests__/jest_setup_describe_order.js:15
      test for describe outer
    console.log src/__tests__/jest_setup_describe_order.js:22
      test for describe inner 2
```

从输出中可以看出

```bash
describe outer-a
describe inner 1
describe outer-b
describe inner 2
describe outer-c
```

这几行的输出表示从外到内的执行了describe里面的代码，并没有按照顺序执行测试模块，而是在执行完describe只有，在从上到下的按照顺序执行测试模块，这个顺序要好好理解，对于以后的写测试模块的逻辑非常重要。

### **建议**

如果一个测试失败了，首先要检查的事情应该是当测试单独运行的时候测试是否失败。

在Jest中，只运行一个测试很简单 - 只需暂时将该测试命令更改为test.only，如下

```js
test.only('this will be the only test that runs', () => {
  expect(true).toBe(false);
});

test('this test will not run', () => {
  expect('A').toBe('A');
});
```

这次换个测试命令，不然每次执行npm test会把之前的也一起执行了，命令如下

```bash
npx jest src/__tests__/jest_setup_test_only.js
```

会得到如下的输出

```bash
FAIL  src/__tests__/jest_setup_test_only.js
  ✕ this will be the only test that runs (10ms)
  ○ skipped 1 test

  ● this will be the only test that runs

    expect(received).toBe(expected) // Object.is equality

    Expected: false
    Received: true

      1 | test.only('this will be the only test that runs', () => {
    > 2 |   expect(true).toBe(false);
        |                ^
      3 | });
      4 |
      5 | test('this test will not run', () => {

      at Object.<anonymous> (src/__tests__/jest_setup_test_only.js:2:16)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 skipped, 2 total
Snapshots:   0 total
Time:        2.344s
Ran all test suites matching /src\/__tests__\/jest_setup_test_only.js/i.
```

从这里可以看出

```bash
✕ this will be the only test that runs (10ms)
  ○ skipped 1 test
```

有两个测试的但是其中一个被跳过了。

当有一个比较复杂的测试中有一个小的测试总是事变，但是单独运行的时候又是成功的，可能是的原因是不同的测试中的有一些干扰元素干扰了这个测试。可以通过用beforeEach清除一些共享状态来解决这个问题。如果不确定是共享的转状态是否被修改，可以通过加入一些日志来判断。

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.19
```
