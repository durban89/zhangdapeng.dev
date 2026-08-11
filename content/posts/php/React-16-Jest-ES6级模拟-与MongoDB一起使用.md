---
title: "React 16 Jest ES6级模拟 - 与MongoDB一起使用"
date: "2025-07-08 15:15:50"
slug: "react-16-jest-es6-ji-mo-ni-yu-mongodb-yi-qi-shi-yong"
categories: ["技术"]
tags: ["ReactJS", "Jest", "MongoDB"]
aliases:
  - "/2025/07/08/React-16-Jest-ES6级模拟-与MongoDB一起使用/"
  - "/2025/07/08/React-16-Jest-ES6级模拟-与MongoDB一起使用.html"
  - "/React-16-Jest-ES6级模拟-与MongoDB一起使用/"
  - "/React-16-Jest-ES6级模拟-与MongoDB一起使用.html"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-yu-mongodb-yi-qi-shi-yong/"
  - "/2025/07/08/react-16-jest-es6-ji-mo-ni-yu-mongodb-yi-qi-shi-yong.html"
  - "/react-16-jest-es6-ji-mo-ni-yu-mongodb-yi-qi-shi-yong.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.32
npm install
```

### **与MongoDB一起使用(Using with MongoDB)**

通过 Global Setup/Teardown和Async Test EnvironmentAPI，Jest可以与MongoDB一起顺利运行。

jest-mongodb实例  
基本思路是：

> .旋转内存中的mongodb服务器 jest.mongodb.setup.js  
> .使用mongo URI导出全局变量 jest.mongodb.environment.js  
> .使用真实数据库编写查询/聚合测试✨  
> .使用Global Teardown关闭mongodb服务器 jest.mongodb.teardown.js

这是GlobalSetup脚本的一个示例  
在项目根目录添加如下几个文件

jest.mongodb.setup.js

```js
const path = require('path');
const fs = require('fs');
const MongodbMemoryServer = require('mongodb-memory-server');

const globalConfigPath = path.join(__dirname, 'globalConfig.json');
const mongoServer = new MongodbMemoryServer.MongoMemoryServer();

module.exports = async function setupMongodb() {
  console.log('配置Jest Setup调用');
  const mongoConfig = {
    mongoDBName: 'jest',
    mongoUri: await mongoServer.getConnectionString(),
  };

  // 将配置写入本地配置文件以供所有测试都能调用的到
  fs.writeFileSync(globalConfigPath, JSON.stringify(mongoConfig));

  // 设置对mongodb的引用，以便在拆卸期间关闭服务器。
  global.__MONGOD__ = mongoServer;
};
```

jest.mongodb.environment.js

```js
const NodeEnvironment = require('jest-environment-node');
const path = require('path');
const fs = require('fs');

const globalConfigPath = path.join(__dirname, 'globalConfig.json');

class MongoEnvironment extends NodeEnvironment {
  constructor(config) {
    super(config);
  }

  async setup() {
    console.log('设置MongoDB测试环境');

    const globalConfig = JSON.parse(fs.readFileSync(globalConfigPath, 'utf-8'));

    this.global.__MONGO_URI__ = globalConfig.mongoUri;
    this.global.__MONGO_DB_NAME__ = globalConfig.mongoDBName;

    await super.setup();
  }

  async teardown() {
    console.log('卸载MongoDB测试环境');

    await super.teardown();
  }

  runScript(script) {
    return super.runScript(script);
  }
}

module.exports = MongoEnvironment;
```

jest.mongodb.teardown.js

```js
module.exports = async function tearDownMongodb() {
  console.log('配置Jest TearDown调用');
  await global.__MONGOD__.stop();
};
```

执行测试用例之前需要安装以下依赖库（如果还没有安装的情况下）

```bash
npm install mongodb-memory-server --save-dev
npm install mongodb --save-dev
npm install jest-environment-node --save-dev
```

修改jest.config.js文件，添加下面的代码

```js
globalSetup: './jest.mongodb.setup.js',
globalTeardown: './jest.mongodb.teardown.js',
testEnvironment: './jest.mongodb.environment.js',
```

jest.config.js

```js
module.exports = {
  setupFiles: ['./jest.setup.js'],
  snapshotSerializers: ['enzyme-to-json/serializer'],
  globalSetup: './jest.mongodb.setup.js',
  globalTeardown: './jest.mongodb.teardown.js',
  testEnvironment: './jest.mongodb.environment.js',
};
```

下面看测试用例代码  
src/\_\_tests\_\_/jest\_mongodb.test.js

```js
const {
  MongoClient,
} = require('mongodb');

let connection;
let db;

beforeAll(async () => {
  connection = await MongoClient.connect(global.__MONGO_URI__, {
    useNewUrlParser: true,
  });
  db = await connection.db(global.__MONGO_DB_NAME__);
});

afterAll(async () => {
  await connection.close();
});

it('从集合中汇总文档', async () => {
  const files = db.collection('files');

  await files.insertMany([{
    type: 'Document',
  },
  {
    type: 'Video',
  },
  {
    type: 'Image',
  },
  {
    type: 'Document',
  },
  {
    type: 'Image',
  },
  {
    type: 'Document',
  },
  ]);

  const topFiles = await files
    .aggregate([{
      $group: {
        _id: '$type',
        count: {
          $sum: 1,
        },
      },
    },
    {
      $sort: {
        count: -1,
      },
    },
    ])
    .toArray();

  expect(topFiles).toEqual([{
    _id: 'Document',
    count: 3,
  },
  {
    _id: 'Image',
    count: 2,
  },
  {
    _id: 'Video',
    count: 1,
  },
  ]);
});
```

实践项目地址

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git
git checkout v_1.0.33
```
