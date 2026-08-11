---
title: "React 16 Jest ES6 Class Mocks(使用ES6语法类的模拟) 实例一"
date: "2025-07-07 16:42:26"
slug: "react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-yi"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例一/"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例一.html"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例一/"
  - "/React-16-Jest-ES6-Class-Mocks(使用ES6语法类的模拟)-实例一.html"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例一/"
  - "/2025/07/07/React-16-Jest-ES6-Class-Mocks-使用ES6语法类的模拟-实例一.html"
  - "/2025/07/07/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-yi/"
  - "/2025/07/07/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-yi.html"
  - "/react-16-jest-es6-class-mocks-shi-yong-es6-yu-fa-lei-de-mo-ni-shi-li-yi.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.29
npm install
```

### **ES6 Class Mocks(使用ES6语法类的模拟)**

Jest可用于模拟导入到要测试的文件中的ES6语法的类。

ES6语法的类是具有一些语法糖的构造函数。因此，ES6语法的类的任何模拟都必须是函数或实际的ES6语法的类(这也是另一个函数)。  
所以可以使用模拟函数来模拟它们。如下

### **一个ES6语法类的实例**

这里的实例我使用官方的例子，SoundPlayer类和SoundPlayerConsumer消费者类。

src/lib/sound-player.js

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

这个测试官方介绍了四种方式来创建一个ES6语法的类测试，今天先使用第一种方式 - 自动模拟(Automatic mock)

调用`jest.mock('../lib/sound-player')`会返回一个有用的“自动模拟”，可以使用它来监视对类构造函数及其所有方法的调用。  
它用模拟构造函数替换ES6语法的类，并使用总是返回undefined的mock函数替换它的所有方法。  
方法调用保存在AutomaticMock.mock.instances [index] .methodName.mock.calls中。  
请注意，如果在类中使用箭头功能，它们将不会成为模拟的一部分。  
原因是箭头函数不存在于对象的原型上，它们只是包含对函数的引用的属性。  
如果不需要替换类的实现，这是最简单的设置选项。测试用例如下：



```javascript src/__tests__/jest_sound_player.test.js
import SoundPlayer from '../lib/sound-player';
import SoundPlayerConsumer from '../lib/sound-player-consumer';

jest.mock('../lib/sound-player'); // SoundPlayer 现在是一个模拟构造函数

beforeEach(() => {
  // 清除所有实例并调用构造函数和所有方法：
  SoundPlayer.mockClear();
});

it('我们可以检查SoundPlayerConsumer是否调用了类构造函数', () => {
  const soundPlayerConsumer = new SoundPlayerConsumer();
  expect(SoundPlayer).toHaveBeenCalledTimes(1);
});

it('我们可以检查SoundPlayerConsumer是否在类实例上调用了一个方法', () => {
  // 检查 mockClear() 会否起作用:
  expect(SoundPlayer).not.toHaveBeenCalled();

  const soundPlayerConsumer = new SoundPlayerConsumer();
  // 类构造函数再次被调用
  expect(SoundPlayer).toHaveBeenCalledTimes(1);

  const coolSoundFileName = 'song.mp3';
  soundPlayerConsumer.play();

  // mock.instances可用于自动模拟
  const mockSoundPlayerInstance = SoundPlayer.mock.instances[0];
  const mockChoicePlaySoundFile = mockSoundPlayerInstance.choicePlaySoundFile;
  expect(mockChoicePlaySoundFile.mock.calls[0][0]).toEqual(coolSoundFileName);
  // 相当于上面的检查
  expect(mockChoicePlaySoundFile).toHaveBeenCalledWith(coolSoundFileName);
  expect(mockChoicePlaySoundFile).toHaveBeenCalledTimes(1);
});
```

运行会得到类似如下输出

```javascript
 PASS  src/__tests__/jest_sound_player.test.js
  ✓ 我们可以检查SoundPlayerConsumer是否调用了类构造函数 (4ms)
  ✓ 我们可以检查SoundPlayerConsumer是否在类实例上调用了一个方法 (3ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        2.27s
Ran all test suites matching /src\/__tests__\/jest_sound_player.test.js/i.
```

*下次介绍第二种方法 - 手动模拟(Manual mock)*

实践项目地址

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.30
```
