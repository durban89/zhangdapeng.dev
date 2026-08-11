---
title: "React 16 Jest手动模拟(Manual Mocks)"
date: "2025-07-07 16:42:19"
slug: "react-16-jest-shou-dong-mo-ni-manual-mocks"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest手动模拟(Manual-Mocks)/"
  - "/2025/07/07/React-16-Jest手动模拟(Manual-Mocks).html"
  - "/React-16-Jest手动模拟(Manual-Mocks)/"
  - "/React-16-Jest手动模拟(Manual-Mocks).html"
  - "/2025/07/07/React-16-Jest手动模拟-Manual-Mocks/"
  - "/2025/07/07/React-16-Jest手动模拟-Manual-Mocks.html"
  - "/2025/07/07/react-16-jest-shou-dong-mo-ni-manual-mocks/"
  - "/2025/07/07/react-16-jest-shou-dong-mo-ni-manual-mocks.html"
  - "/react-16-jest-shou-dong-mo-ni-manual-mocks.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.27
npm install
```

### **手动模拟(Manual Mocks)**

手动模拟主要功能是用于存储模拟的数据。

例如，我可能希望创建一个允许您使用虚假数据的手动模拟，而不是访问网站或数据库等远程资源。

这可以确保您的测试快速且不易碎(not flaky)。

### **模拟水果模块(Mocking fruit modules)**

通过在紧邻模块的\_\_mocks\_\_/子目录中编写模块来定义手动模拟。这个方式我在前面文章中的实例中也有用到过，具体的可以参考之前的文章，这里我说下大概的流程

例如，要在src/lib目录中模拟一个名为fruit的模块，则分别创建文件src/lib/fruit.js和文件src/lib/\_\_mocks\_\_/fruit.js的文件。

请注意\_\_mocks\_\_文件夹区分大小写。如果命名目录是\_\_MOCKS\_\_，则可能在某些系统上测试的时候会中断。

> 注意点
>
> 当我们在测试中需要该模块时，还需要显式的调用jest.mock('./moduleName')。

### **模拟Node核心模块(Mocking Node modules)**

如果正在模拟的模块是Node module(例如：lodash)，则模拟应放在与node\_modules相邻的\_\_mocks\_\_目录中(除非您将根配置为指向项目根目录以外的文件夹)并将自动模拟。

没有必要显式调用jest.mock('module\_name')。

可以通过在与范围模块的名称匹配的目录结构中创建文件来模拟范围模块。

例如，要模拟名为@scope/project-name的作用域模块，请在\_\_mocks\_\_/@scope/project-name.js创建一个文件，相应地创建@scope/目录。

> 注意点
>
> 如果我们想模拟Node的核心模块（例如：fs或path），那么明确地调用。
>
> 例如：jest.mock('path')是必需的，因为默认情况下不会模拟核心Node模块。

### **实例演示**

当给定模块存在手动模拟时，Jest的模块系统将在显式调用jest.mock('moduleName')时使用该模块。

但是，当automock设置为true时，即使未调用jest.mock('moduleName')，也将使用手动模拟实现而不是自动创建的模拟。

要选择不使用此行为，您需要在应使用实际模块实现的测试中显式调用jest.unmock('moduleName')。

> 注意点
>
> 为了正确模拟，Jest需要jest.mock('moduleName')与require/import语句在同一范围内。

假设我们有一个模块，它提供给定目录中所有文件的摘要。在这种情况下，我们使用核心(内置)fs模块来演示

src/lib/FileSummarizer.js

```javascript
const fs = require('fs');

function summarizeFilesInDirectorySync(directory) {
  return fs.readdirSync(directory).map(fileName => ({
    directory,
    fileName,
  }));
}

exports.summarizeFilesInDirectorySync = summarizeFilesInDirectorySync;
```

由于我们希望我们的测试避免实际操作磁盘(这非常慢且易碎[fragile])，我们通过扩展自动模拟为fs模块创建手动模拟。

我们的手动模拟将实现我们可以为我们的测试构建的fs API的自定义版本：

src/lib/\_\_mocks\_\_/fs.js

```javascript
const path = require('path');

const fs = jest.genMockFromModule('fs');

let mockFiles = Object.create(null);

function __setMockFiles(newMockFiles) {
  mockFiles = Object.create(null);

  const keys = Object.keys(newMockFiles);

  for (let index = 0; index < keys.length; index += 1) {
    const file = keys[index];
    const dir = path.dirname(file);
    if (!mockFiles[dir]) {
      mockFiles[dir] = [];
    }
    mockFiles[dir].push(path.basename(file));
  }
}

function readdirSync(directoryPath) {
  return mockFiles[directoryPath] || [];
}

fs.__setMockFiles = __setMockFiles;
fs.readdirSync = readdirSync;

module.exports = fs;
```

现在我们编写测试。

请注意，我们需要明确告诉我们要模拟fs模块，因为它是一个核心Node模块：

src/\_\_tests\_\_/FileSummarizer-test.js

```javascript
const fs = require('fs');
const FileSummarizer = require('../lib/FileSummarizer');

jest.mock('fs');

describe('listFilesInDirectorySync', () => {
  const MOCK_FILE_INFO = {
    '/path/to/file1.js': 'console.log("file1 contents");',
    '/path/to/file2.txt': 'file2 contents',
  };

  beforeEach(() => {
    // Set up some mocked out file info before each test
    fs.__setMockFiles(MOCK_FILE_INFO);
  });

  test('includes all files in the directory in the summary', () => {
    const fileSummary = FileSummarizer.summarizeFilesInDirectorySync('/path/to');

    expect(fileSummary.length).toBe(2);
  });
});
```

此处显示的示例模拟使用jest.genMockFromModule生成自动模拟，并覆盖其默认行为。

这是推荐的方法，但完全是可选的。

如果您根本不想使用自动模拟，则只需从模拟文件中导出自己的函数即可。

完全手动模拟的一个缺点是它们是手动的 - 这意味着你必须在它们模拟的模块发生变化时手动更新它们。

因此，最好在满足您的需求时使用或扩展自动模拟。

为了确保手动模拟及其实际实现保持同步，在手动模拟中使用require.requireActual(moduleName)并在导出之前使用模拟函数修改它可能是有用的。

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.28
```
