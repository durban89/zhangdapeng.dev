---
title: "React 16 Jest ES6级模拟 - 深入：了解模拟构造函数"
date: "2025-07-08 15:15:40"
slug: "react-16-jest-es6-ji-mo-ni-shen-ru-liao-jie-mo-ni-gou-zao-han-shu"
categories: ["技术"]
tags: ["ReactJS", "Jest"]
aliases:
  - "/2025/07/08/React-16-Jest-ES6级模拟-深入：了解模拟构造函数/"
  - "/2025/07/08/React-16-Jest-ES6级模拟-深入：了解模拟构造函数.html"
  - "/React-16-Jest-ES6级模拟-深入：了解模拟构造函数/"
  - "/React-16-Jest-ES6级模拟-深入：了解模拟构造函数.html"
  - "/2025/07/08/React-16-Jest-ES6级模拟-深入-了解模拟构造函数/"
  - "/2025/07/08/React-16-Jest-ES6级模拟-深入-了解模拟构造函数.html"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-shen-ru-liao-jie-mo-ni-gou-zao-han-shu/"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-shen-ru-liao-jie-mo-ni-gou-zao-han-shu.html"
  - "/react-16-jest-es6-ji-mo-ni-shen-ru-liao-jie-mo-ni-gou-zao-han-shu.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.32
npm install
```

### **ES6 Class Mocks(使用ES6语法类的模拟)**

Jest可用于模拟导入到要测试的文件中的ES6语法的类。

ES6语法的类是具有一些语法糖的构造函数。因此，ES6语法的类的任何模拟都必须是函数或实际的ES6语法的类(这也是另一个函数)。  
所以可以使用模拟函数来模拟它们。如下

### **深入：了解模拟构造函数**

使用jest.fn().mockImplementation()构建的构造函数mock，使模拟看起来比实际更复杂。  
那么jest是如何创建一个简单的模拟(simple mocks)并演示下mocking是如何起作用的

### **手动模拟另一个ES6语法的类**

如果使用与\_\_mocks\_\_文件夹中的模拟类相同的文件名定义ES6语法的类，则它将用作模拟。  
这个类将用于代替真正的类。  
我们可以为这个类注入测试实现，但不提供监视调用的方法。如下  
src/\_\_mocks\_\_/sound-player.js

```js
export default class SoundPlayer {
  constructor() {
    console.log('Mock SoundPlayer: constructor was called');
    this.name = 'Player1';
    this.fileName = '';
  }

  choicePlaySoundFile(fileName) {
    console.log('Mock SoundPlayer: choicePlaySoundFile was called');
    this.fileName = fileName;
  }

  playSoundFile() {
    console.log('Mock SoundPlayer: playSoundFile was called');
    console.log('播放的文件是:', this.fileName);
  }
}
```

### **使用模块工厂参数的简单模拟(Simple mock using module factory parameter)**

传递给jest.mock(path，moduleFactory)的模块工厂函数可以是返回函数\*的高阶函数（HOF）。  
这将允许在模拟上调用new。  
同样，这允许为测试注入不同的行为，但不提供监视调用的方法

### **\*模块工厂功能必须返回一个功能(\* Module factory function must return a function)**

为了模拟构造函数，模块工厂必须返回构造函数。  
换句话说，模块工厂必须是返回函数的函数 - 高阶函数（HOF）。如下演示

```js
jest.mock('../lib/sound-player', () => {
  return function() {
    return {
      playSoundFile: () => {}
    };
  };
});
```

### **注意：箭头功能不起作用(Note: Arrow functions won't work)**

请注意，mock不能是箭头函数，因为在JavaScript中不允许在箭头函数上调用new。  
所以这不起作用：

```js
jest.mock('./sound-player', () => {
  return () => {
    // 不起作用 箭头函数不会被调用
    return {playSoundFile: () => {}};
  };
});
```

这将抛出TypeError：\_soundPlayer2.default不是构造函数，除非代码被转换为ES5，例如，  
通过babel-preset-env。（ES5没有箭头函数也没有类，因此两者都将被转换为普通函数。）

实践项目地址

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.32
```
