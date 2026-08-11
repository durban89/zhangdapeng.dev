---
title: "React 16 Jest快照测试"
date: "2025-07-07 16:42:07"
slug: "react-16-jest-kuai-zhao-ce-shi"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/07/React-16-Jest快照测试/"
  - "/2025/07/07/React-16-Jest快照测试.html"
  - "/React-16-Jest快照测试/"
  - "/React-16-Jest快照测试.html"
  - "/2025/07/07/react-16-jest-kuai-zhao-ce-shi/"
  - "/2025/07/07/react-16-jest-kuai-zhao-ce-shi.html"
  - "/react-16-jest-kuai-zhao-ce-shi.html"
---
### **项目初始化**

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git 
cd webpack4-react16-reactrouter-demo
git fetch origin
git checkout v_1.0.24
npm install
```

只要想确保UI不会意外更改，快照测试是非常有用的工具。

移动应用程序的典型呈现UI组件快照测试用例，通过截取屏幕截图，然后将其与存储在测试这边的参考图像进行比较。

如果两个图像不匹配，测试将失败，可能是被意外的更改了，或者需要将屏幕截图更新为新版本的UI组件。

### **Jest快照测试**

在测试React组件时，可以采用类似的方法。  
可以使用测试渲染器快速生成React树的可序列化值，而不是渲染需要构建整个应用程序的图形UI。

下面做一个简单的Link组件的示例测试：  
测试之前先安装下react-test-renderer依赖库

```bash
npm install react-test-renderer --save-dev
```

src/\_\_tests\_\_/react\_link.react.jsx

```jsx
import React from 'react';
import renderer from 'react-test-renderer';
import ALink from '../components/Link.react';

it('正确的渲染', () => {
  const tree = renderer
    .create(<ALink page="https://www.gowhich.com">Gowhich</ALink>)
    .toJSON(); expect(tree).toMatchSnapshot();
});
```

src/components/Link.react.jsx

```jsx
import React from 'react';
import PropTypes from 'prop-types';

const STATUS = {
  HOVERED: 'hovered',
  NORMAL: 'normal',
};

class Link extends React.Component {
  constructor(props) {
    super(props);

    this.onMouseEnter = this.onMouseEnter.bind(this);
    this.onMouseleave = this.onMouseleave.bind(this);
    this.state = {
      class: STATUS.NORMAL,
    };
  }

  onMouseEnter() {
    this.setState({
      class: STATUS.HOVERED,
    });
  }

  onMouseleave() {
    this.setState({
      class: STATUS.NORMAL,
    });
  }

  render() {
    return (
      <a
        className={this.state.class}
        href={this.props.page || '#'}
        onMouseEnter={this.onMouseEnter}
        onMouseLeave={this.onMouseleave}
      >
        {this.props.children}
      </a>
    );
  }
}

Link.propTypes = {
  page: PropTypes.string.isRequired,
  children: PropTypes.oneOfType([
    PropTypes.element,
    PropTypes.string,
  ]).isRequired,
};

export default Link;
```

第一次运行此测试时，Jest会创建一个如下所示的快照文件：  
src/\_\_tests\_\_/\_\_snapshots\_\_/react\_link.test.jsx.snap

```jsx
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`正确的渲染 1`] = `
<a
  className="normal"
  href="https://www.gowhich.com"
  onMouseEnter={[Function]}
  onMouseLeave={[Function]}
>
  Gowhich
</a>
`;
```

快照文件应该与代码更改一起提交，并作为代码审查过程的一部分进行审核。  
Jest使用pretty-format对快照文件进行了处理，当代码在审查期间，会让代码快照变成让人类可阅读的文件。  
在随后的测试运行中，Jest会将渲染的输出的文件与之前的快照进行比较。  
如果匹配，测试将通过。如果它们不匹配，表示代码出问题了。Jest则会告知代码中哪里需要进行修改的错误或者是代码的逻辑需要进行更新，重新生成快照。我们是试着更改下page参数的地址和Gowhich文案，如下  
src/\_\_tests\_\_/react\_link.react.jsx

```jsx
import React from 'react';
import renderer from 'react-test-renderer';
import ALink from '../components/Link.react';

it('正确的渲染', () => {
  const tree = renderer
    .create(<ALink page="https://www.walkerfree.com">Walkerfree</ALink>)
    .toJSON(); expect(tree).toMatchSnapshot();
});
```

再次执行测试，会得到类似如下的输出，这里我就只截取错误这部分的内容

```bash
  ✕ 正确的渲染 (22ms)

  ● 正确的渲染

    expect(value).toMatchSnapshot()

    Received value does not match stored snapshot "正确的渲染 1".

    - Snapshot
    + Received

      <a
        className="normal"
    -   href="https://www.gowhich.com"
    +   href="https://www.walkerfree.com"
        onMouseEnter={[Function]}
        onMouseLeave={[Function]}
      >
    -   Gowhich
    +   Walkerfree
      </a>

       6 |   const tree = renderer
       7 |     .create(<ALink page="https://www.walkerfree.com">Walkerfree</ALink>)
    >  8 |     .toJSON(); expect(tree).toMatchSnapshot();
         |                             ^
       9 | });
      10 |

      at Object.<anonymous> (src/__tests__/react_link.test.jsx:8:29)

 › 1 snapshot failed.
Snapshot Summary
 › 1 snapshot failed from 1 test suite. Inspect your code changes or re-run jest with `-u` to update them.
```

由于刚刚更新了组件以指向不同的地址和文案，而且这次更改是合理的，是我们希望的逻辑，这个时候快照测试会失败，因为刚更新的组件的快照不再与此测试用例的快照相匹配。

为了解决这个问题，我们需要更新快照文件，只需要运行下面的命令，就会重新生成快照

```bash
npx jest src/__tests__/react_link.test.jsx --notify --watchman=false --updateSnapshot
```

这个时候我们就需要同之前一样，将这个新的快照文件同代码的更改一起提交。

### **快照交互模式**

执行如下命令

```bash
npx jest src/__tests__/react_link.test.jsx --notify --watchman=false --updateSnapshot --watch
```

只是加了一个

```bash
--watch
```

运行上面的命令会得到类似如下的输出

```bash
 PASS  src/__tests__/react_link.test.jsx
  ✓ 正确的渲染 (17ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 passed, 1 total
Time:        1.713s
Ran all test suites matching /src\/__tests__\/react_link.test.jsx/i.

Active Filters: filename /src/__tests__/react_link.test.jsx/
 › Press c to clear filters.

Watch Usage
 › Press a to run all tests.
 › Press f to run only failed tests.
 › Press o to only run tests related to changed files.
 › Press p to filter by a filename regex pattern.
 › Press t to filter by a test name regex pattern.
 › Press q to quit watch mode.
 › Press Enter to trigger a test run.
```

而且会对测试文件进行检测。如果有文件改动了，会自动重新启动测试，然后对测试文件，进行重新测试属性匹配器

通常有时候，一个对象的属性的值被生成，但是在进行快照生成时候，这个值就固定了，下载再次执行测试的时候就会报错，如下

```jsx
it('这个快照再次测试的时候会失败', () => {
  const user = {
    createAt: new Date(),
    id: Math.floor(Math.random() * 20),
    name: 'Durban',
  };

  expect(user).toMatchSnapshot();
});
```

执行后生成的快照如下

```jsx
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`这个快照再次测试的时候会失败 1`] = `
Object {
  "createAt": 2018-07-06T06:44:49.429Z,
  "id": 0,
  "name": "Durban",
}
`;
```

其实从下面这里我们就已经能发现问题了

```bash
"createAt": 2018-07-06T06:44:49.429Z,
```

日期是每次执行一次都会变化的。当我们再次执行的时候会发现报出了如下错误

```bash
  ✕ 这个快照再次测试的时候会失败 (14ms)

  ● 这个快照再次测试的时候会失败

    expect(value).toMatchSnapshot()

    Received value does not match stored snapshot "这个快照再次测试的时候会失败 1".

    - Snapshot
    + Received

      Object {
    -   "createAt": 2018-07-06T06:44:49.429Z,
    -   "id": 0,
    +   "createAt": 2018-07-06T06:46:02.245Z,
    +   "id": 10,
        "name": "Durban",
      }

       6 |   };
       7 |
    >  8 |   expect(user).toMatchSnapshot();
         |                ^
       9 | });
      10 |

      at Object.<anonymous> (src/__tests__/jest_snap_property.test.js:8:16)

 › 1 snapshot failed.
Snapshot Summary
 › 1 snapshot failed from 1 test suite. Inspect your code changes or re-run jest with `-u` to update them.
```

针对这个情况我们可以这样解决，在测试里面加入如下代码

```jsx
expect(user).toMatchSnapshot({
  createAt: expect.any(Date),
  id: expect.any(Number),
});
```

修改后代码如下

```jsx
it('检查匹配器并测试通过', () => {
  const user = {
    createAt: new Date(),
    id: Math.floor(Math.random() * 20),
    name: 'Durban',
  };

  expect(user).toMatchSnapshot({
    createAt: expect.any(Date),
    id: expect.any(Number),
  });
});
```

执行更新操作，对快照进行更新得到的快照内容结果如下

```jsx
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`检查匹配器并测试通过 1`] = `
Object {
  "createAt": Any<Date>,
  "id": Any<Number>,
  "name": "Durban",
}
`;
```

项目实践地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.25
```
