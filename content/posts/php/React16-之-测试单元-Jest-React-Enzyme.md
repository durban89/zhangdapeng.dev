---
title: "React16 之 测试单元(Jest+React+Enzyme)"
date: "2025-07-07 16:41:15"
slug: "react16-zhi-ce-shi-dan-yuan-jestreactenzyme"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React16-之-测试单元(Jest+React+Enzyme)/"
  - "/2025/07/07/React16-之-测试单元(Jest+React+Enzyme).html"
  - "/React16-之-测试单元(Jest+React+Enzyme)/"
  - "/React16-之-测试单元(Jest+React+Enzyme).html"
  - "/2025/07/07/React16-之-测试单元-Jest-React-Enzyme/"
  - "/2025/07/07/React16-之-测试单元-Jest-React-Enzyme.html"
  - "/2025/07/07/react16-zhi-ce-shi-dan-yuan-jestreactenzyme/"
  - "/2025/07/07/react16-zhi-ce-shi-dan-yuan-jestreactenzyme.html"
  - "/react16-zhi-ce-shi-dan-yuan-jestreactenzyme.html"
---
### **安装 enzyme 相关**

```bash
npm install enzyme enzyme-adapter-react-16 --save-dev

npm install jest babel-jest babel-preset-env react-test-renderer --save-dev

npm install enzyme-to-json
```

### **修改package.json**

```bash
"test": "jest --notify --watchman=false",
```

这里强调记录下，为什么要加--watchman=false，因为在国内watchman连接的会会超时，别问我怎么知道的，我可以给你解释102个小时，反正在国内的话就按照我说的这个来，不然，你会和郁闷

```bash
分别添加jest.config.js和jest.setup.js
```

jest.config.js

```js
module.exports = {
  setupFiles: ['./jest.setup.js'],
  snapshotSerializers: ['enzyme-to-json/serializer'],
};
```

jest.setup.js

```js
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({
  adapter: new Adapter(),
});
```

为什么会有jest.setup.js，官网的是在测试文件中其实是可以直接加

```js
import { configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({
  adapter: new Adapter(),
});
```

这段代码的，但是为了不重复操作，有的人把这段代码提出来，放到一个单独的文件中，这个也是jest配置文件支持的，这点做的很好

### **测试用例**

src/lib/sum.js

```js
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```

src/\_\_tests\_\_/sum.test.js

```js
const sum = require('../lib/sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

### **执行jest进行测试**

```bash
$ npm test

> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/sum.test.js
  ✓ adds 1 + 2 to equal 3 (4ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        2.348s
Ran all test suites.
```

### **为什么要把测试案例放到目录\_\_tests\_\_**

默认jest会扫描testMatch匹配的文件，而忽略testPathIgnorePatterns匹配的文件，具体的可在配置文件更改

```bash
testMatch: **/__tests__/**/*.js?(x),**/?(*.)+(spec|test).js?(x)
testPathIgnorePatterns: /node_modules/
```

### **React组件测试用例**

src/components/CheckboxWithLabelComponent.jsx

```js
import React from 'react';
import PropTypes from 'prop-types';

class CheckboxWithLabelComponent extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      isChecked: false,
    };

    this.onChange = this.onChange.bind(this);
  }

  onChange() {
    this.setState({
      isChecked: !this.state.isChecked,
    });
  }

  render() {
    return (
      <label htmlFor="label">
        <input
          type="checkbox"
          checked={this.state.isChecked}
          onChange={this.onChange}
        />
        {this.state.isChecked ? this.props.labelOn : this.props.labelOff}
      </label>
    );
  }
}

CheckboxWithLabelComponent.propTypes = {
  labelOn: PropTypes.string.isRequired,
  labelOff: PropTypes.string.isRequired,
};

export default CheckboxWithLabelComponent;
```

src/\_\_tests\_\_/CheckboxWithLabelComponent.test.jsx

```js
import React from 'react';
import { shallow } from 'enzyme';
import CheckboxWithLabelComponent from '../components/CheckboxWithLabelComponent';

test('CheckboxWithLabelComponent changes the text after click', () => {
  // Render a checkbox with label in the document
  const checkbox = shallow(<CheckboxWithLabelComponent labelOn="On" labelOff="Off" />);

  expect(checkbox.text()).toEqual('Off');

  checkbox.find('input').simulate('change');

  expect(checkbox.text()).toEqual('On');
});
```

### **执行jest进行测试**

```bash
$ npm test

> xx@xx test /Users/durban/nodejs/webpack-react-demo
> jest --notify --watchman=false

 PASS  src/__tests__/sum.test.js
 PASS  src/__tests__/CheckboxWithLabelComponent.test.jsx

Test Suites: 2 passed, 2 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        2.188s
Ran all test suites.
```

是不是很赞。原来前端也可以这么牛逼。

.babelrc也别忘记修改

presets中添加"env"

```js
"presets": [
    "es2015",
    "react",
    "stage-0",
    "env"
]
```

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.14
```
