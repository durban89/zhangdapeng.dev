---
title: "React16 Jest单元测试 之 Mock Functions(Mocking Modules 和 Mock Implementations)"
date: "2025-07-07 16:41:57"
slug: "react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmocking-modules-he-mock-implementations"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Mocking-Modules-和-Mock-Implementations)/"
  - "/2025/07/07/React16-Jest单元测试-之-Mock-Functions(Mocking-Modules-和-Mock-Implementations).html"
  - "/React16-Jest单元测试-之-Mock-Functions(Mocking-Modules-和-Mock-Implementations)/"
  - "/React16-Jest单元测试-之-Mock-Functions(Mocking-Modules-和-Mock-Implementations).html"
  - "/2025/07/07/React-16-Jest单元测试-之-Mock-Functions-Mocking-Modules-和-Mock-Implementations/"
  - "/2025/07/07/React-16-Jest单元测试-之-Mock-Functions-Mocking-Modules-和-Mock-Implementations.html"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmocking-modules-he-mock-implementations/"
  - "/2025/07/07/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmocking-modules-he-mock-implementati.html"
  - "/react16-jest-dan-yuan-ce-shi-zhi-mock-functionsmocking-modules-he-mock-implementations.html"
---
项目初始化【这里使用之前的项目，节省时间】

项目初始化地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.21
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.21
npm install
```

### **Mocking Modules**

假设我们有一个从API中获取用户的类。该类使用axios调用API然后返回包含所有用户的data属性：

因为要用到axios，需要安装下axios,

运行

```bash
npm install axios --save
```

然后创建文件src/lib/user.js

```js
import axios from 'axios';

class Users {
  static all() {
    return axios.get('/user.json').then(resp => resp.data);
  }
}

export default Users;
```

创建文件src/\_\_tests\_\_/user.test.js

```js
import axios from 'axios';
import Users from '../lib/user';

jest.mock('axios');

test('should fetch users', () => {
  const resp = {
    data: [
      {
        name: 'Durban',
      },
    ],
  };

  axios.get.mockResolvedValue(resp);
  // 或者也可以使用下面的代码
  // axios.get.mockImplementation(() => Promise.resolve(resp));

  return Users.all().then(users => expect(users).toEqual(resp.data));
});
```

现在，为了不在实际访问API的情况下测试此方法（从而创建缓慢且脆弱的测试），我们可以使用jest.mock（...）函数自动模拟axios模块。

一旦我们模拟了模块，我们就可以为.get提供一个mockReturnValue，它返回我们测试希望要的断言数据。实际上，我们说我们希望axios.get（'/users.json'）返回一个假响应。

### **Mock Implementations**

尽管如此，有些情况下超出指定返回值的能力和全面替换模拟函数的实现是有用的。这可以使用jest.fn或mock函数上的mockImplementationOnce方法来实现。如下

```js
const myMockFn = jest.fn(cb => cb(null, true));

myMockFn((err, val) => console.log(val));
// > true
myMockFn((err, val) => console.log(val));
// > true
```

当需要定义从另一个模块创建的模拟函数的默认实现时，mockImplementation方法很有用，如下

```js
// foo.js
module.exports = function() {
  // some implementation;
};

// test.js
jest.mock('../foo'); // this happens automatically with automocking
const foo = require('../foo');

// foo is a mock function
foo.mockImplementation(() => 42);
foo();
// > 42
```

当需要重新创建模拟函数的复杂行为，以便多个函数调用产生不同的结果时，请使用mockImplementationOnce方法，如下

```js
const myMockFn = jest
  .fn()
  .mockImplementationOnce(cb => cb(null, true))
  .mockImplementationOnce(cb => cb(null, false));

myMockFn((err, val) => console.log(val));
// > true

myMockFn((err, val) => console.log(val));
// > false
```

当mocked函数超出了mockImplementationOnce定义的实现次数时，它将使用jest.fn执行默认实现集（如果已定义），如下

```js
const myMockFn = jest
  .fn(() => 'default')
  .mockImplementationOnce(() => 'first call')
  .mockImplementationOnce(() => 'second call');

console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
// > 'first call', 'second call', 'default', 'default'
```

对于我们有通常链接的方法（因此总是需要返回这个）的情况，我们有一个含糖API，以.mockReturnThis（）函数的形式简化它，该函数也位于所有模拟上，如下

```js
const myObj = {
  myMethod: jest.fn().mockReturnThis(),
};
```

跟如下是类似的

```js
const otherObj = {
  myMethod: jest.fn(function() {
    return this;
  }),
};
```

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.22
```
