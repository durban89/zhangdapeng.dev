---
title: "React 16 Jest如何进行异步程序测试"
date: "2025-07-07 16:42:11"
slug: "react-16-jest-ru-he-jin-xing-yi-bu-cheng-xu-ce-shi"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest如何进行异步程序测试/"
  - "/2025/07/07/React-16-Jest如何进行异步程序测试.html"
  - "/React-16-Jest如何进行异步程序测试/"
  - "/React-16-Jest如何进行异步程序测试.html"
  - "/2025/07/07/react-16-jest-ru-he-jin-xing-yi-bu-cheng-xu-ce-shi/"
  - "/2025/07/07/react-16-jest-ru-he-jin-xing-yi-bu-cheng-xu-ce-shi.html"
  - "/react-16-jest-ru-he-jin-xing-yi-bu-cheng-xu-ce-shi.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.25
npm install
```

### **异步程序测试**

首先，在Jest中启用Babel支。执行如下安装命令

```bash
npm install babel-jest babel-core regenerator-runtime --save-dev
```

下面实现一个简单的模块，从API中获取用户数据并返回用户名。

src/lib/user.js添加如下代码

```js
import request from './request';

static getUserName(userID) {
  return request(`/users/${userID}`).then(user => user.name);
}
```

在上面的实现中，我们希望request.js模块返回一个promise。然后通过传递用户ID来获取用户信息，最后得到一个用户名称。  
request.js的获取用户信息的实现如下：src/lib/request.js

```js
const http = require('http');

export default function request(url) {
  return new Promise((resolve) => {
    http.get({
      path: url,
    }, (response) => {
      let data = '';
      response.on('data', (o) => {
        data += o;
        return data;
      });
      response.on('end', () => resolve(data));
    });
  });
}
```

这里的话希望在测试中不访问网络，所以在\_\_mocks\_\_文件夹中创建一个request.js，手动模拟网络请求(该文件夹区分大小写，'\_\_MOCKS\_\_'是不起作用的)。  
它可能看起来像这样src/lib/\_\_mocks\_\_/request.js

```js
const users = {
  4: {
    name: 'Mark',
  },
  5: {
    name: 'Paul',
  },
};

export default function request(url) {
  return new Promise((resolve, reject) => {
    const userID = parseInt(url.substr('/users/'.length), 10);
    process.nextTick(() => {
      if (users[userID]) {
        return resolve(users[userID]);
      }
      return reject({
        error: `User with ${userID} not found.`,
      });
    });
  });
}
```

现在为这个异步的功能编写一个测试。src/\_\_tests\_\_/user\_async.test.js

```js
import Users from '../lib/user';

jest.mock('../lib/request');

// The assertion for a promise must be returned.
it('works with promises', () =>
  // expect.assertions(1); // 当前版本加了这行总是报错，暂时未注释
  Users
    .getUserName(4)
    .then(data => expect(data).toEqual('Mark')));
```

运行测试，正常通过测试，如果问题可加群沟通

`jest.mock('../lib/request')`会告诉Jest去使用我们手动模拟的mock，'it'期望返回一个Promise，这个Promise的返回结果是resloved。  
只要最后返回一个Promise，我们就可以链接尽可能多的Promise，并且随时调用'expect'。

### **.resolves**

有一种不那么冗长的方式是使用'resolves'，让它与任何其他匹配器一起unwrap一个fulfilled promise的值。  
如果promise是rejected，则断言将失败。如下

```js
it('works with resolves', () => {
  expect.assertions(1);
  return expect(user.getUserName(5)).resolves.toEqual('Paul');
});
```

### **async/await**

使用async/await语法编写测试很容易。可以写一个和上面实例一致的测试。如下

```js
import Users from '../lib/user';

jest.mock('../lib/request');

it('works with async/await', async () => {
  const data = await Users.getUserName(4);
  expect(data).toEqual('Mark');
});

it('works with async/await and resolves', async () => {
  expect.assertions(1);
  await expect(Users.getUserName(5)).resolves.toEqual('Paul');
});
```

为了使得测试中支持 async/await, 需要安装 babel-preset-env 并且在开通这个属性在.babelrc文件中.

### **Error handling**

可以使用.catch方法处理错误。  
确保添加expect.assertions以验证是否调用了一定数量的断言。  
否则，一个fulfilled promise不会使测试失败：如下

```js
import Users from '../lib/user';

jest.mock('../lib/request');

test('tests error with promises', async () => {
  expect.assertions(1);
  return Users.getUserName(2).catch(e =>
    expect(e).toEqual({
      error: 'User with 2 not found.',
    }));
});

it('tests error with async/await', async () => {
  expect.assertions(1);
  try {
    await Users.getUserName(1);
  } catch (e) {
    expect(e).toEqual({
      error: 'User with 1 not found.',
    });
  }
});
```

### **.rejects**

.rejects帮助程序就像.resolves帮助程序一样。  
如果promise是满足的，测试将自动失败。

```js
import Users from '../lib/user';

jest.mock('../lib/request');
it('tests error with rejects', () => {
  expect.assertions(1);
  return expect(Users.getUserName(3)).rejects.toEqual({
    error: 'User with 3 not found.',
  });
});

it('tests error with async/await and rejects', async () => {
  expect.assertions(1);
  await expect(Users.getUserName(3)).rejects.toEqual({
    error: 'User with 3 not found.',
  });
});
```

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.26
```
