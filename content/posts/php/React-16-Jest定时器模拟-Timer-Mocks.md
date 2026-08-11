---
title: "React 16 Jest定时器模拟 Timer Mocks"
date: "2025-07-07 16:42:14"
slug: "react-16-jest-ding-shi-qi-mo-ni-timer-mocks"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest定时器模拟-Timer-Mocks/"
  - "/2025/07/07/React-16-Jest定时器模拟-Timer-Mocks.html"
  - "/React-16-Jest定时器模拟-Timer-Mocks/"
  - "/React-16-Jest定时器模拟-Timer-Mocks.html"
  - "/2025/07/07/react-16-jest-ding-shi-qi-mo-ni-timer-mocks/"
  - "/2025/07/07/react-16-jest-ding-shi-qi-mo-ni-timer-mocks.html"
  - "/react-16-jest-ding-shi-qi-mo-ni-timer-mocks.html"
---
**项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.26
npm install
```

### **定时器模拟(Timer Mocks)**

原生定时器功能(即setTimeout，setInterval，clearTimeout，clearInterval)对于测试环境来说不太理想，因为它们依赖于实时时间。  
Jest可以将定时器换成允许我们自己控制时间的功能。  
示例如下  
src/lib/timerGame.js

```javascript
function timerGame(callback) {
  console.log('Ready....go!');
  setTimeout(() => {
    console.log('Times up -- stop!');
    return callback && callback();
  }, 1000);
}

module.exports = timerGame;
```

src/\_\_tests\_\_/jest\_timerGame.test.js

```javascript
const timerGame = require('../lib/timerGame');

jest.useFakeTimers();

test('等待1秒钟后结束游戏', () => {
  timerGame();

  expect(setTimeout).toHaveBeenCalledTimes(1);
  expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 1000);
});
```

这里我们通过调用jest.useFakeTimers();来启用假定时器。  
这使用模拟函数模拟了setTimeout和其他计时器函数。  
如果在一个文件或描述块中运行多个测试，则jest.useFakeTimers();  
可以在每次测试之前手动调用，也可以使用诸如beforeEach之类的设置函数调用。  
不这样做会导致内部使用计数器不被重置。

### **运行所有计时器(Run All Timers)** 

为上面的模块timerGame写一个测试，这个测试在1秒钟后调用回调callback，示例如下

```javascript
const timerGame = require('../lib/timerGame');
jest.useFakeTimers();

test('1秒钟后调用回调callback', () => {
  const callback = jest.fn();

  timerGame(callback);

  // 在这个时间点上，callback回调函数还没有被调用
  expect(callback).not.toBeCalled();

  // 所有timers被执行
  jest.runAllTimers();

  // 现在我们的callback回调函数被调用
  expect(callback).toBeCalled();
  expect(callback).toHaveBeenCalledTimes(1);
});
```

### **运行待定时间器**

在某些情况下，您可能还有一个递归计时器 - 这是一个在自己的回调中设置新计时器的计时器。  
对于这些，运行所有计时器将是一个无限循环,所以像jest.runAllTimers()这样的东西是不可取的。  
对于这些情况，您可以使用jest.runOnlyPendingTimers()。示例如下  
src/lib/infiniteTimerGame.js

```javascript
function infiniteTimerGame(callback) {
  console.log('Ready....go!');

  setTimeout(() => {
    console.log('Times up! 10 seconds before the next game starts...');

    if (callback) {
      callback();
    }

    // 10秒钟后执行下一个
    setTimeout(() => {
      infiniteTimerGame(callback);
    }, 10000);
  }, 1000);
}

module.exports = infiniteTimerGame;
```

src/\_\_tests\_\_/jest\_infiniteTimerGame.test.js

```javascript
const infiniteTimerGame = require('../lib/infiniteTimerGame');

jest.useFakeTimers();

describe('infiniteTimerGame', () => {
  test('schedules a 10-second timer after 1 second', () => {
    const callback = jest.fn();

    infiniteTimerGame(callback);

    // 在这里，会在意秒钟后执行callback的回调
    expect(setTimeout).toHaveBeenCalledTimes(1);
    expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 1000);

    // 只有当前待定的计时器（但不是在该过程中创建的任何新计时器）
    jest.runOnlyPendingTimers();

    // 此时，1秒钟的计时器应该已经被回调了
    expect(callback).toBeCalled();

    // 它应该创建一个新的计时器，以便在10秒内启动游戏
    expect(setTimeout).toHaveBeenCalledTimes(2);
    expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 10000);
  });
});
```

### **按时间提前计时器(Advance Timers by Time)**

另一种可能性是使用jest.advanceTimersByTime（msToRun）。  
调用此API时，所有计时器都按msToRun毫秒提前。  
将执行已经通过setTimeout()或setInterval()排队并且将在此时间帧期间执行所有待处理"宏任务"。  
此外，如果这些宏任务调度将在同一时间帧内执行的新宏任务，那么将执行这些宏任务，直到队列中不再有宏任务应该在msToRun毫秒内运行。  
示例如下

```javascript
const timerGame = require('../lib/timerGame');

jest.useFakeTimers();

it('1秒钟后通过advanceTimersByTime调用回调函数', () => {
  const callback = jest.fn();

  timerGame(callback);

  // callback还没有被执行
  expect(callback).not.toBeCalled();

  // 提前1秒钟执行
  jest.advanceTimersByTime(1000);

  // 所有的callback被调用
  expect(callback).toBeCalled();
  expect(callback).toHaveBeenCalledTimes(1);
});
```

在某些测试中偶尔可能有用，就是在测试中可以清除所有挂起的计时器。  
为此，可以使用jest.clearAllTimers()。

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.27
```
