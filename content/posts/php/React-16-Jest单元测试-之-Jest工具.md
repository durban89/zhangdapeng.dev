---
title: "React 16 Jest单元测试 之 Jest工具"
date: "2025-07-07 16:42:03"
slug: "react-16-jest-dan-yuan-ce-shi-zhi-jest-gong-ju"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest单元测试-之-Jest工具/"
  - "/2025/07/07/React-16-Jest单元测试-之-Jest工具.html"
  - "/React-16-Jest单元测试-之-Jest工具/"
  - "/React-16-Jest单元测试-之-Jest工具.html"
  - "/2025/07/07/react-16-jest-dan-yuan-ce-shi-zhi-jest-gong-ju/"
  - "/2025/07/07/react-16-jest-dan-yuan-ce-shi-zhi-jest-gong-ju.html"
  - "/react-16-jest-dan-yuan-ce-shi-zhi-jest-gong-ju.html"
---
### **项目初始化【这里使用之前的项目，节省时间】**

项目初始化地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.23
```

拉取

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.23
npm install
```

Jest有很多特定的功能，可以作为单独的包来使用，下面罗列下官网提供的一些有用的包

环境

```bash
node --version
v8.11.3
```

node的安装包方法我就不介绍了，如果看了这么久我的分享还是不知道的话，可以继续看看前面文章，这里简单提示下，安装命令如下

```bash
npm install package_name --save // 生产安装
npm install package_name --save-dev // 开发安装
```

## **1、jest-changed-files**

此工具提供的功能是标识在git或hg中被修改过的文件，提供的方法如下

> getChangedFilesForRoots 返回一个promise，该promise将解析为具有已更改文件和repos的对象。
>
> findRepos 返回一个promise，该promise将解析为指定路径中包含的一组存储库。

演示如下

```js
const { getChangedFilesForRoots } = require('jest-changed-files');

getChangedFilesForRoots(['./'], {
  lastCommit: true,
}).then(result => console.log(result.changedFiles));
```

运行后得到类似如下结果

```bash
Set {
  '/xxx/webpack-react-demo/src/__tests__/jest_mock_names.test.js' }
```

## **2、jest-diff**

用于可视化数据变化的工具。导出一个比较任意类型的两个值的函数，并返回一个"pretty-printed"的字符串，说明两个参数之间的差异。

演示如下

```js
const diff = require('jest-diff');

const a = { a: { b: { c: 5 } } };
const b = { a: { b: { c: 6 } } };

const result = diff(a, b);

console.log(result);
```

运行后输出的结果类似如下

```bash
- Expected
+ Received

  Object {
    "a": Object {
      "b": Object {
-       "c": 5,
+       "c": 6,
      },
    },
  }
```

## 

## **3、jest-docblock**

用于提取和解析JavaScript文件顶部注释的工具。导出各种函数来操作注释块内的数据。

演示如下

```js
const { parseWithComments } = require('jest-docblock');

const code = `
  /**
   * 这是一个例子
   * 
   * @author durban
   *  
   */
  console.log('Hello Jest!');
`;

const parsed = parseWithComments(code);
console.log(parsed);
```

运行后输出结果类似如下

```bash
{ comments: '  /**\n这是一个例子\n\n \n/\n  console.log(\'Hello Jest!\');',
  pragmas: { author: 'durban' } }
```

## **4、jest-get-type**

标识任何JavaScript值的基本类型的模块。导出一个函数，该函数返回一个字符串，其值的类型作为参数传递。

演示如下

```js
const getType = require('jest-get-type');

const array = [1, 2, 3];
const nullvalue = null;
const undefinedValue = undefined;

console.log(getType(array));
console.log(getType(nullvalue));
console.log(getType(undefinedValue));
```

运行后输出结果类似如下

```bash
array
null
undefined
```

## **5、jest-validate**

用于验证用户提交的配置的工具。

导出一个带有两个参数的函数：用户的配置和包含示例配置和其他选项的对象。

返回值是一个具有两个属性的对象，如下：

> hasDeprecationWarnings 一个布尔值，指示提交的配置是否具有弃用警告
>
> isValid 一个布尔值，指示配置是否正确。

演示如下

```js
const { validate } = require('jest-validate');

const configByUser = {
  tranform: '<rootDir>/node_modules/my-custom-packages',
};

const result = validate(configByUser, {
  comment: '  Documentation: http://custom-docs.com',
  exampleConfig: {
    tranform: '<rootDir>/node_modules/jest-validate',
  },
});

console.log(result);
```

运行后输出结果类似如下

```bash
{ hasDeprecationWarnings: false, isValid: true }
```

## **6、jest-worker**

用于并行化任务的模块。

导出一个类Worker，它接受Node.js模块的路径，并允许您调用模块的导出方法，就好像它们在类方法中一样，返回一个promise，当指定的方法在forked进程中完成它的执行时解析。

演示如下

创建一个task.js

```js
module.exports = {
  Task: args => args,
};
```

调用的代码如下

```js
const { default: Worker } = require('jest-worker');

async function main() {
  const worker = new Worker(require.resolve('./task.js'));

  const results = await Promise.all([
    worker.Task({ args: '1' }),
    worker.Task({ args: '2' }),
  ]);

  console.log(results);
}

main();
```

运行后输出结果类似如下

```bash
[ { args: '1' }, { args: '2' } ]
```

这里用了一个看起来很奇怪的用法，其实不然，仔细了解下node包的机制，还是很好理解的

```bash
const { default: Worker } = require('jest-worker');
```

如果你的node版本支持import的话可以替换为，【我试了下10.5.0这个nodejs版本还是不支持呀】

```bash
import Worker from 'jest-worker';
```

## **7、pretty-format**

导出将任何JavaScript值转换为人类可读字符串的函数。

支持开箱即用的所有内置JavaScript类型，并允许通过用户定义的特定应用程序类型的扩展。

演示如下

```js
const prettyFormat = require('pretty-format');

const val = { object: {} };
val.circuleReference = val;
val[Symbol('key')] = 'key';
val.map = new Map([['property', 'value']]);
val.array = [-0, Infinity, NaN];

console.log(prettyFormat(val));
```

运行后输出结果类似如下

```bash
Object {
  "array": Array [
    -0,
    Infinity,
    NaN,
  ],
  "circuleReference": [Circular],
  "map": Map {
    "property" => "value",
  },
  "object": Object {},
  Symbol(key): "key",
}
```

Jest的包远不止这些，有兴趣的可以继续去https://github.com/facebook/jest/tree/master/packages这里观望自己想要的

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.24
```
