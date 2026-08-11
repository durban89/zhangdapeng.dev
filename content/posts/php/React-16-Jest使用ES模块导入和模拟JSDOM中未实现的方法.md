---
title: "React 16 Jest使用ES模块导入和模拟JSDOM中未实现的方法"
date: "2025-07-07 16:42:23"
slug: "react-16-jest-shi-yong-es-mo-kuai-dao-ru-he-mo-ni-jsdom-zhong-wei-shi-xian-de-fang-fa"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest使用ES模块导入和模拟JSDOM中未实现的方法/"
  - "/2025/07/07/React-16-Jest使用ES模块导入和模拟JSDOM中未实现的方法.html"
  - "/React-16-Jest使用ES模块导入和模拟JSDOM中未实现的方法/"
  - "/React-16-Jest使用ES模块导入和模拟JSDOM中未实现的方法.html"
  - "/2025/07/07/react-16-jest-shi-yong-es-mo-kuai-dao-ru-he-mo-ni-jsdom-zhong-wei-shi-xian-de-fang-fa/"
  - "/2025/07/07/react-16-jest-shi-yong-es-mo-kuai-dao-ru-he-mo-ni-jsdom-zhong-wei-shi-xian-de-fang-.html"
  - "/react-16-jest-shi-yong-es-mo-kuai-dao-ru-he-mo-ni-jsdom-zhong-wei-shi-xian-de-fang-fa.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.28
npm install
```

### **Using with ES module imports(使用ES模块导入)**

我们在使用ES模块时做导入的时候，会习惯性的将导入的语句放在测试文件的顶部。但是在使用Jest的时候，需要指示Jest在模块使用之前进行模拟操作。  
正是由于这个原因，Jest会自动将jest.mock的调用提升到模块的顶部(在任何导入之前)

### **Mocking methods which are not implemented in JSDOM(模拟JSDOM中未实现的方法)**

如果某些代码在使用JSDOM(Jest使用的DOM实现)尚未实现的方法的时候，这个情况在测试时是比较麻烦的。比如我们调用window.matchMedia()的时候，Jest返回TypeError：window.matchMedia不是函数，并且没有正确执行测试。  
在这种情况下，在测试文件中模拟matchMedia就可以解决类似的问题：如下

```javascript
window.matchMedia = jest.fn().mockImplementation(query => {
  return {
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
  };
});
```

如果window.matchMedia()用于在测试中调用的函数(或方法)，则此方法有效。  
如果window.matchMedia()直接在测试文件中执行，则Jest报告相同的错误。  
在这种情况下，解决方案是将手动模拟移动到单独的文件中，并在测试文件之前将其包含在测试中：实例如下

```javascript
import './matchMedia.mock'; // Must be imported before the tested file
import { myMethod } from './file-to-test';

describe('myMethod()', () => {
  // Test the method here...
});
```

这里官方就是简单的介绍了下，导致有些学者可能还是云里雾里的，下面简单的写个实例  
创建文件  
src/lib/matchMedia.mock.js

```javascript
window.matchMedia = jest.fn().mockImplementation((query) => {
  const obj = {
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
  };

  return obj;
});
```

src/lib/useMatchMedia.js

```javascript
const useMatchMedia = () => {
  const res = window.matchMedia;
  return res;
};

module.exports = {
  useMatchMedia,
};
```

创建完文件后，添加测试文件  
src/\_\_tests\_\_/useMatchMedia.test.js  
第一次我们不调用src/lib/matchMedia.mock.js这个文件

```javascript
// import '../lib/matchMedia.mock';
import { useMatchMedia } from '../lib/useMatchMedia';

describe('useMatchMedia()', () => {
  it('useMatchMedia() 被调用', () => {
    const res = useMatchMedia();
    expect(res).toBeUndefined();
    // expect(res).toBeDefined();
  });
});
```

第二次我们调用src/lib/matchMedia.mock.js这个文件

```javascript
import '../lib/matchMedia.mock';
import { useMatchMedia } from '../lib/useMatchMedia';

describe('useMatchMedia()', () => {
  it('useMatchMedia() 被调用', () => {
    const res = useMatchMedia();
    expect(res).toBeDefined();
  });
});
```

从上面的例子大概就能理解基本上官方的意思了，具体如何使用，这个可以自己有发挥。

如果国内的用户还是不知道如何流畅的运行jest的话建议翻翻我前面的文章。  
项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.29
```
