---
title: "使用TypeScript开发React应用(五) - 组件状态管理"
date: "2025-07-10 10:57:42"
slug: "shi-yong-typescript-kai-fa-react-ying-yong-wu-zu-jian-zhuang-tai-guan-li"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/使用TypeScript开发React应用(五)-组件状态管理/"
  - "/2025/07/10/使用TypeScript开发React应用(五)-组件状态管理.html"
  - "/使用TypeScript开发React应用(五)-组件状态管理/"
  - "/使用TypeScript开发React应用(五)-组件状态管理.html"
  - "/2025/07/10/使用TypeScript开发React应用-五-组件状态管理/"
  - "/2025/07/10/使用TypeScript开发React应用-五-组件状态管理.html"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-wu-zu-jian-zhuang-tai-guan-li/"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-wu-zu-jian-zhuang-tai-guan-li.html"
  - "/shi-yong-typescript-kai-fa-react-ying-yong-wu-zu-jian-zhuang-tai-guan-li.html"
---
继续前面的文章[使用TypeScript开发React应用(四)](https://www.gowhich.com/blog/978)介绍了React+TypeScript应用的Jest单元测试

下面继续分享如何给组件添加状态管理

### 添加状态管理

此时，如果您使用React只获取一次数据并显示它，您可以认为自己完成了。 但是，如果您正在开发一个更具交互性的应用程序，那么您可能需要添加状态管理。

**一般的状态管理**

React本身就是一个用于创建可组合视图的有用库。 但是，React没有规定在整个应用程序中同步数据的任何特定方法。 就React组件而言，数据通过您在子元素上指定的道具向下流动。 其中一些道具可能是以这种或那种方式更新状态的功能，但是如何发生这是一个悬而未决的问题。

由于React本身并不专注于应用程序状态管理，因此React社区使用Redux和MobX等库。

[Redux](http://redux.js.org/)依赖于通过集中且不可变的数据存储来同步数据，对该数据的更新将触发我们的应用程序的重新呈现。 通过发送必须由称为reducers的函数处理的显式操作消息，以不可变的方式更新状态。 由于具有明确的性质，通常更容易推断某个操作将如何影响您的程序状态。

[MobX](https://mobx.js.org/)依赖于功能反应模式，其中状态通过可观察对象包裹并作为道具传递。 通过简单地将状态标记为可观察状态来保持状态完全同步以用于任何观察者。 作为一个很好的奖励，该库已经用TypeScript编写。

两者都有各种优点和权衡。 通常Redux倾向于看到更广泛的用法，因此为了本教程的目的，我们将专注于添加Redux; 但是，你应该感到鼓励去探索两者。

以下部分可能有一个陡峭的学习曲线。 我们强烈建议您通过其文档熟悉[Redux](http://redux.js.org/)。

**为行动做准备**

除非我们的应用程序状态发生变化，否则添加Redux是没有意义的。 我们需要一个可以触发更改的操作源。 这可以是计时器，也可以是UI中的某个按钮。

出于我们的目的，我们将添加两个按钮来控制Hello组件的enthusiasmLevel。

**安装Redux**

要添加Redux，我们首先将redux和react-redux及其类型安装为依赖项。

```bash
npm install -S redux react-redux @types/react-redux
```

在这种情况下，我们不需要安装@types/redux，因为Redux已经附带了自己的定义文件（.d.ts文件）。

**定义我们的应用程序状态**

我们需要定义Redux将存储的状态的形状。 为此，我们可以创建一个名为src/types/index.tsx的文件，该文件将包含我们可能在整个程序中使用的类型的定义。

```ts
export interface StoreState {
  enthusiasmLevel: number;
  name: string;
}
```

我们的意图是enam将是这个应用程序名称，而enthusiasmLevel的管理将会有所不同。 当我们编写第一个容器时，我们会理解为什么我们故意使我们的状态与我们的道具略有不同。

**添加actions**

让我们从创建一组消息类型开始，我们的应用程序可以在src/constants/index.tsx中响应。

```ts
export const INCREMENT_ENTHUSIASM = 'INCREMENT_ENTHUSIASM';
export type INCREMENT_ENTHUSIASM = typeof INCREMENT_ENTHUSIASM;

export const DECREMENT_ENTHUSIASM = 'DECREMENT_ENTHUSIASM';
export type DECREMENT_ENTHUSIASM = typeof DECREMENT_ENTHUSIASM;
```

这种const/type模式允许我们以易于访问和可重构的方式使用TypeScript的字符串文字类型。

接下来，我们将创建一组可以在src/actions/index.tsx中创建这些操作的操作和函数。

```ts
import * as constants from '../constants';

export interface IncrementEnthusiasm {
  type: constants.INCREMENT_ENTHUSIASM;
}

export interface DecrementEnthusiasm {
  type: constants.DECREMENT_ENTHUSIASM;
}

export type EnthusiasmAction = IncrementEnthusiasm | DecrementEnthusiasm;

export function incrementEnthusiasm(): IncrementEnthusiasm {
  return {
    type: constants.INCREMENT_ENTHUSIASM,
  }
}

export function decrementEnthusiasm(): DecrementEnthusiasm {
  return {
    type: constants.DECREMENT_ENTHUSIASM,
  }
}
```

我们创建了两种类型来描述增量操作和减量操作应该是什么样子。 我们还创建了一个类型（EnthusiasmAction）来描述一个动作可以是增量或减量的情况。 最后，我们制作了两个函数来实际制作我们可以使用的动作，而不是写出庞大的对象文字。

这里有明显的样板，所以一旦你掌握了一些东西，你就可以随意查看像[redux-actions](https://www.npmjs.com/package/redux-actions)这样的库。

**添加一个reducer**

我们准备好写第一个reducer了！ Reducers只是通过创建应用程序状态的修改副本来生成更改的函数，但没有副作用。 换句话说，它们就是我们所谓的纯函数。

我们的reducer将在src/reducers/index.tsx下。 它的功能是确保增量将enthusiasmLevel提高1，而减量将enthusiasmLevel降低1，但水平从不低于1。

```ts
import { EnthusiasmAction } from '../actions';
import { StoreState } from '../types/index';
import { INCREMENT_ENTHUSIASM, DECREMENT_ENTHUSIASM } from '../constants/index';

export function enthusiasm(state: StoreState, action: EnthusiasmAction): StoreState {
  switch (action.type) {
    case INCREMENT_ENTHUSIASM:
      return {
        ...state,
        enthusiasmLevel: state.enthusiasmLevel + 1,
      };
    case DECREMENT_ENTHUSIASM:
      return {
        ...state,
        enthusiasmLevel: Math.max(state.enthusiasmLevel - 1, 1),
      };
  }
  return state;
}
```

请注意，我们正在使用对象展开`(...state)`，它允许我们创建状态的浅赋值，同时替换enthusiasmLevel。 重要的是，enthusiasmLevel属性是最后的，否则它将被旧状态的属性覆盖。

您可能想为reducers编写一些测试。 由于reducer是纯函数，因此可以传递任意数据。 对于每个输入，可以通过检查其新生成的状态来测试reducers。 考虑一下Jest的toEqual方法来实现这一点。

使用Redux编写时，我们经常会编写组件和容器。 组件通常与数据无关，并且主要在表示级别工作。 容器通常包装组件并向其提供显示和修改状态所需的任何数据。 您可以在[Dan Abramov的文章演示和容器组件上](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)阅读有关此概念的更多信息。

首先让我们更新`src/components/Hello.tsx`，以便它可以修改状态。 我们将为名为onIncrement和onDecrement的Props添加两个可选的回调属性：

```ts
export interface Props {
  name: string;
  enthusiasmLevel?: number;
  onIncrement?: () => void;
  onDecrement?: () => void;
}
```

然后我们将这些回调绑定到两个我们将添加到组件中的新按钮。

```ts
function Hello({ name, enthusiasmLevel = 1, onIncrement, onDecrement }: Props) {
  if (enthusiasmLevel <= 0) {
    throw new Error('You could be a little more enthusiastic.');
  }

  return (
    <div className="hello">
      <div className="greeting">
        Hello {name + getExclamationMarks(enthusiasmLevel)}
      </div>
      <div>
        <button onClick={onIncrement}>+</button>
        <button onClick={onDecrement}>-</button>
      </div>
    </div>
  );
}
```

一般来说，为onIncrement编写一些测试并在单击各自的按钮时触发onDecrement是个好主意。 试一试为您的组件编写测试。

现在我们的组件已更新，我们已准备好将其包装到容器中。 让我们创建一个名为src/containers/Hello.tsx的文件，并从以下导入开始。

```tsx
import Hello from '../components/Hello';
import * as actions from '../actions/';
import { StoreState } from '../types';
import { connect } from 'react-redux';
import { Dispatch } from 'redux';
```

这里真正的两个关键部分是原始的Hello组件以及react-redux的connect函数。 connect将能够实际使用我们的原始Hello组件并使用两个函数将其转换为容器：

* mapStateToProps，用于传递当前Sore中的数据到我们组件所需形状的一部分。
* mapDispatchToProps创建回调属性，使用给定的调度函数将操作传送到我们的store。

如果我们回想一下，我们的应用程序状态包含两个属性：name和enthusiasmLevel。 另一方面，我们的Hello组件需要一个名字和一个enthusiasmLevel的管子。 mapStateToProps将从store获取相关数据，并在必要时针对我们组件的属性进行调整。 让我们继续写下来吧。

```tsx
export function mapStateToProps({ enthusiasmLevel, name }: StoreState) {
  return {
    enthusiasmLevel,
    name,
  }
}
```

请注意，mapStateToProps仅创建Hello组件期望的4个属性中的2个。 也就是说，我们仍然希望传入onIncrement和onDecrement回调。 mapDispatchToProps是一个采用调度程序功能的函数。 此调度程序功能可以将操作传递到我们的store以进行更新，因此我们可以创建一对将根据需要调用调度程序的回调。

```tsx
export function mapDispatchToProps(dispatch: Dispatch<actions.EnthusiasmAction>) {
  return {
    onIncrement: () => dispatch(actions.incrementEnthusiasm()),
    onDecrement: () => dispatch(actions.decrementEnthusiasm()),
  }
}
```

最后，我们准备调用connect。 connect将首先获取mapStateToProps和mapDispatchToProps，然后返回另一个我们可以用来包装我们组件的函数。 我们生成的容器使用以下代码行定义：

```tsx
export default connect(mapStateToProps, mapDispatchToProps)(Hello);
```

完成后，我们的文件应如下所示：

```tsx
import Hello from '../components/Hello';
import * as actions from '../actions/';
import { StoreState } from '../types/index';
import { connect } from 'react-redux';
import { Dispatch } from 'redux';

export function mapStateToProps({ enthusiasmLevel, name }: StoreState) {
  return {
    enthusiasmLevel,
    name,
  }
}

export function mapDispatchToProps(dispatch: Dispatch<actions.EnthusiasmAction>) {
  return {
    onIncrement: () => dispatch(actions.incrementEnthusiasm()),
    onDecrement: () => dispatch(actions.decrementEnthusiasm()),
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Hello);
```

**创建store** 我们回到src/index.tsx。 要把这些放在一起，我们需要创建一个具有初始状态的store，并使用我们所有的reducer进行设置。

```tsx
import { createStore } from 'redux';
import { enthusiasm } from './reducers/index';
import { StoreState } from './types/index';
import { EnthusiasmAction } from './actions/index';

const store = createStore<StoreState, EnthusiasmAction, any, any>(enthusiasm, {
  enthusiasmLevel: 1,
  name: 'Durban',  
});
```

正如您可能已经猜到的那样，store是我们应用程序全局状态的中央store。

接下来，我们将把./src/components/Hello与./src/containers/Hello交换使用，并使用react-redux的Provider将我们的道具与我们的容器连接起来。 我们将导入每个：

```tsx
-import Hello from './components/Hello';
+import Hello from './containers/Hello';

import { Provider } from 'react-redux';
```

并将我们的store传递给Provider的属性：

```tsx
ReactDOM.render(
  <Provider store={store}>
    <Hello />
  </Provider>,
  document.getElementById('root') as HTMLElement
);
```

请注意，Hello不再需要props，因为我们使用connect函数来调整我们的应用程序状态，以便包装Hello组件的props。

完整代码请跳转到这里下载 [ts-react-app](https://github.com/durban89/ts-react-app.git)
