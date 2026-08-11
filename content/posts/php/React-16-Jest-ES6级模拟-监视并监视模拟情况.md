---
title: "React 16 Jest ES6级模拟 - 监视并监视模拟情况"
date: "2025-07-08 15:15:45"
slug: "react-16-jest-es6-ji-mo-ni-jian-shi-bing-jian-shi-mo-ni-qing-kuang"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/08/React-16-Jest-ES6级模拟-监视并监视模拟情况/"
  - "/2025/07/08/React-16-Jest-ES6级模拟-监视并监视模拟情况.html"
  - "/React-16-Jest-ES6级模拟-监视并监视模拟情况/"
  - "/React-16-Jest-ES6级模拟-监视并监视模拟情况.html"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-jian-shi-bing-jian-shi-mo-ni-qing-kuang/"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-jian-shi-bing-jian-shi-mo-ni-qing-kuang.html"
  - "/react-16-jest-es6-ji-mo-ni-jian-shi-bing-jian-shi-mo-ni-qing-kuang.html"
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

### **跟踪使用情况（监视模拟）(Keeping track of usage (spying on the mock))**

注入测试实现很有帮助，但我们可能还想测试是否使用正确的参数调用类构造函数和方法。

### **监视构造函数(Spying on the constructor)**

为了跟踪对构造函数的调用，用一个Jest模拟函数替换HOF返回的函数。  
使用jest.fn()创建它，然后使用mockImplementation()指定它的实现。如下

```js
import SoundPlayer from '../lib/sound-player';
jest.mock('../lib/sound-player', () => {
  // 检查构造函数的调用
  return jest.fn().mockImplementation(() => {
    return {
      choicePlaySoundFile: () => {},
      playSoundFile: () => {},
    };
  });
});
```

我们使用SoundPlayer.mock.calls来检查我们的模拟类的用法：expect(SoundPlayer).toHaveBeenCalled();  
或接近等价的：expect(SoundPlayer.mock.calls.length).toEqual(1);

### **监视类的方法(Spying on methods of our class)**

我们的模拟类需要提供将在测试期间调用的任何成员函数(示例中为playSoundFile)，否则我们将因调用不存在的函数而出错。  
但是我们可能也希望监视对这些方法的调用，以确保使用预期的参数调用它们。

每次在测试期间调用模拟构造函数时，都会创建一个新对象。  
为了监视所有这些对象中的方法调用，我们使用另一个mock函数填充playSoundFile，并在我们的测试文件中存储对同一个mock函数的引用，因此它在测试期间可用。

```js
import SoundPlayer from '../lib/sound-player';
const mockPlaySoundFile = jest.fn();
const mockChoicePlaySoundFile = jest.fn();
jest.mock('../lib/sound-player', () => {
  return jest.fn().mockImplementation(() => {
    return {
      choicePlaySoundFile: mockChoicePlaySoundFile,
      playSoundFile: mockPlaySoundFile,
    };
  });
});
```

手动模拟等效于此：

```js
export const mockChoicePlaySoundFile = jest.fn();
const mockPlaySoundFile = jest.fn();

const mock = jest.fn().mockImplementation(() => {
  const data = {
    choicePlaySoundFile: mockChoicePlaySoundFile,
    playSoundFile: mockPlaySoundFile,
  };

  return data;
});

export default mock;
```

用法类似于模块工厂函数，除了可以省略jest.mock()中的第二个参数，并且必须将模拟方法导入到测试文件中，因为它不再在那里定义。  
使用原始模块路径;  
不包括\_\_mocks\_\_

### **在测试之间进行清理(Cleaning up between tests)**

要清除对mock构造函数及其方法的调用记录，我们在beforeEach()函数中调用mockClear()：

前面的文章分别做了4个实例,分别是下面四个文件,可以自己打开项目去具体看下，这里就不在展示了

```js
src/__tests/jest_sound_player.test.js
src/__tests/jest_sound_player_2.test.js
src/__tests/jest_sound_player_3.test.js
src/__tests/jest_sound_player_4.test.js
```

### **实践项目地址**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.32
```
