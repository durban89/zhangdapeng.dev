---
title: "React 16 Jest ES6 Class Mocks(使用ES6语法类的模拟) 实例二"
date: "2025-07-07 16:42:36"
slug: "react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-er"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例二/"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例二.html"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例二/"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例二.html"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例二/"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例二.html"
  - "/2025/07/07/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-er/"
  - "/2025/07/07/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-er.html"
  - "/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-er.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.30
npm install
```

### **ES6 Class Mocks(使用ES6语法类的模拟)**

Jest可用于模拟导入到要测试的文件中的ES6语法的类。

ES6语法的类是具有一些语法糖的构造函数。因此，ES6语法的类的任何模拟都必须是函数或实际的ES6语法的类(这也是另一个函数)。  
所以可以使用模拟函数来模拟它们。如下

### *ES6语法的类测试实例二，今天使用第二种方式 - 手动模拟(Manual mock)*

### **ES6语法类的实例**

这里的实例我使用官方的例子，SoundPlayer类和SoundPlayerConsumer消费者类。下面部分文件的内容参考上篇文章[React 16 Jest ES6 Class Mocks(使用ES6语法类的模拟)](https://www.gowhich.com/blog/858)src/lib/sound-player.js

```javascript
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

```javascript
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

通过在__mocks__文件夹中创建一个模拟实现来创建手动模拟。  
这个可以指定实现，并且可以通过测试文件使用它。如下  
src/lib/__mocks__/sound-player.js

```javascript
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

然后在测试用例中导入mock和mock方法，具体如下

```javascript
import SoundPlayer, { mockChoicePlaySoundFile } from '../lib/sound-player';
import SoundPlayerConsumer from '../lib/sound-player-consumer';

jest.mock('../lib/sound-player'); // SoundPlayer 现在是一个模拟构造函数

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

运行后得到的结果如下

```javascript
 PASS  src/__tests__/jest_sound_player_2.test.js
  ✓ 我们可以检查SoundPlayerConsumer是否调用了类构造函数 (7ms)
  ✓ 我们可以检查SoundPlayerConsumer是否在类实例上调用了一个方法 (2ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        3.352s
Ran all test suites matching /src\/__tests__\/jest_sound_player_2.test.js/i.
```

下次介绍第三、四种方法 - 使用模块工厂参数调用jest.mock()(Calling jest.mock() with the module factory parameter)和使用mockImplementation()或mockImplementationOnce()替换mock(Replacing the mock using `mockImplementation()` or `mockImplementationOnce()`)

实践项目地址

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.31
```
