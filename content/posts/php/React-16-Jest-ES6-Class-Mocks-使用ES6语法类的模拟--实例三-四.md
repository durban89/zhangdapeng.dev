---
title: "React 16 Jest ES6 Class Mocks(使用ES6语法类的模拟) 实例三、四"
date: "2025-07-08 15:15:34"
slug: "react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-san-si"
categories: ["技术"]
tags: ["ReactJS", "Jest"]
aliases:
  - "/2025/07/08/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例三、四/"
  - "/2025/07/08/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例三、四.html"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例三、四/"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例三、四.html"
  - "/2025/07/08/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例三-四/"
  - "/2025/07/08/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例三-四.html"
  - "/2025/07/08/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-san-si/"
  - "/2025/07/08/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-san-si.html"
  - "/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-san-si.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.31
npm install
```

### **ES6 Class Mocks(使用ES6语法类的模拟)**

Jest可用于模拟导入到要测试的文件中的ES6语法的类。

ES6语法的类是具有一些语法糖的构造函数。因此，ES6语法的类的任何模拟都必须是函数或实际的ES6语法的类(这也是另一个函数)。  
所以可以使用模拟函数来模拟它们。如下

### **ES6语法类的实例**

这里的实例我使用官方的例子，SoundPlayer类和SoundPlayerConsumer消费者类。下面部分文件的内容参考上篇文章[React 16 Jest ES6 Class Mocks(使用ES6语法类的模拟)](https://www.gowhich.com/blog/858)src/lib/sound-player.js

```js
export default class SoundPlayer {
  constructor() {
    this.name = 'Player1';
    this.fileName = '';
  }

  choicePlaySoundFile(fileName) {
    this.fileName = fileName;
  }

  playSoundFile() {
    console.log('播放的文件是:', this.fileName);
  }
}
```

src/lib/sound-player-consumer.js

```js
import SoundPlayer from './sound-player';

export default class SoundPlayerConsumer {
  constructor() {
    this.soundPlayer = new SoundPlayer();
  }

  play() {
    const coolSoundFileName = 'song.mp3';
    this.soundPlayer.choicePlaySoundFile(coolSoundFileName);
    this.soundPlayer.playSoundFile();
  }
}
```

### **ES6语法的类测试实例三 - 使用模块工厂参数调用jest.mock()(Calling jest.mock() with the module factory parameter)jest.mock(path，moduleFactory)接受模块工厂参数。**

模块工厂是一个返回模拟的函数。  
为了模拟构造函数，模块工厂必须返回构造函数。  
换句话说，模块工厂必须是返回函数的函数 - 高阶函数（HOF）。测试用例如下  
src/\_\_tests\_\_/jest\_sound\_player\_3.test.js

```js
import SoundPlayer from '../lib/sound-player';
import SoundPlayerConsumer from '../lib/sound-player-consumer';

jest.mock('../lib/sound-player'); // SoundPlayer 现在是一个模拟构造函数

const mockPlaySoundFile = jest.fn();
const mockChoicePlaySoundFile = jest.fn();

jest.mock('../lib/sound-player', () => jest.fn().mockImplementation(() => ({
  choicePlaySoundFile: mockChoicePlaySoundFile,
  playSoundFile: mockPlaySoundFile,
})));

beforeEach(() => {
  // 清除所有实例并调用构造函数和所有方法：
  SoundPlayer.mockClear();
  mockChoicePlaySoundFile.mockClear();
});

it('我们可以检查SoundPlayerConsumer是否调用了类构造函数', () => {
  const soundPlayerConsumer = new SoundPlayerConsumer();
  expect(SoundPlayer).toHaveBeenCalledTimes(1);
});

it('我们可以检查SoundPlayerConsumer是否在类实例上调用了一个方法', () => {
  const soundPlayerConsumer = new SoundPlayerConsumer();
  const coolSoundFileName = 'song.mp3';
  soundPlayerConsumer.play();
  expect(mockChoicePlaySoundFile).toHaveBeenCalledWith(coolSoundFileName);
});
```

注意上面代码中的这段代码

```javascript
const mockPlaySoundFile = jest.fn();
const mockChoicePlaySoundFile = jest.fn();

jest.mock('../lib/sound-player', () => jest.fn().mockImplementation(() => ({
  choicePlaySoundFile: mockChoicePlaySoundFile,
  playSoundFile: mockPlaySoundFile,
})));
```

工厂参数的限制是，由于对jest.mock()的调用被提升到文件的顶部，因此无法首先定义变量然后在工厂中使用它。  
对以"mock"开头的变量进行例外处理。

### **ES6语法的类测试实例四 - 使用mockImplementation（）或mockImplementationOnce（）替换mock(Replacing the mock using mockImplementation() or mockImplementationOnce())**

### 您可以通过在现有模拟上调用mockImplementation()来替换前面所有的模拟，以便更改单个测试或所有测试的实现。 对jest.mock的调用被提升到代码的顶部。 也可以指定模拟，例如在beforeAll()中，通过在现有mock上调用mockImplementation()或mockImplementationOnce()而不是使用factory参数。 如果需要，这还允许在测试之间更改模拟：测试用例如下

```javascript
import SoundPlayer from '../lib/sound-player';
import SoundPlayerConsumer from '../lib/sound-player-consumer';

jest.mock('../lib/sound-player'); // SoundPlayer 现在是一个模拟构造函数

describe('SoundPlayer被调用的时候抛出异常', () => {
  beforeAll(() => {
    SoundPlayer.mockImplementation(() => ({
      playSoundFile: () => {
        throw new Error('Test error');
      },
      choicePlaySoundFile: () => {
        throw new Error('Test error');
      },
    }));
  });

  it('play被调用的收抛出异常', () => {
    const soundPlayerConsumer = new SoundPlayerConsumer();
    expect(() => soundPlayerConsumer.play()).toThrow();
  });
});
```

上面的代码注意这里

```javascript
beforeAll(() => {
  SoundPlayer.mockImplementation(() => ({
    playSoundFile: () => {
      throw new Error('Test error');
    },
    choicePlaySoundFile: () => {
      throw new Error('Test error');
    },
  }));
});
```

实践项目地址

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.32
```
