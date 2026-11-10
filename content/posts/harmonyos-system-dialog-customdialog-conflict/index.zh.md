+++
title = "HarmonyOS NEXT 系统弹窗与 CustomDialog 冲突：原因分析与 DialogGate 解耦方案"
date = 2026-11-10T11:00:00+08:00
lastmod = 2026-11-10T11:00:00+08:00
slug = "harmonyos-system-dialog-customdialog-conflict"
draft = false
toc = true
tags = ["HarmonyOS", "HarmonyOS NEXT", "ArkUI", "TypeScript", "CustomDialog"]
categories = ["HarmonyOS", "Development"]
description = "解决 HarmonyOS NEXT 系统通知授权弹窗与 ArkUI CustomDialog 并发调用导致自定义弹窗无法显示的问题，通过 DialogGate 实现系统弹窗与业务弹窗的时序隔离和逻辑解耦。"

image = "./cover.png"
image_alt = "HarmonyOS NEXT System Dialog vs CustomDialog – DialogGate solution for dialog scheduling, timing coordination, and module decoupling."
+++

在 HarmonyOS NEXT（API 12+）应用开发过程中，如果系统级弹窗与应用内自定义弹窗在同一时间窗口内被触发，可能出现自定义弹窗无法正常显示的问题。

本文以通知授权弹窗与 ArkUI `CustomDialogController` 之间的冲突为例，分析问题产生的原因，并介绍一种基于全局弹窗闸门（DialogGate）的解耦方案。

该方案不需要让通知模块感知业务弹窗，也不需要让业务弹窗感知通知授权流程。通过统一的弹窗调度入口，可以解决两类弹窗并发调用时的时序冲突。

**适用环境：**

- 系统版本：HarmonyOS NEXT
- API 版本：API 12+
- 通知模块：`@kit.NotificationKit`
- UI 模块：`@kit.ArkUI`
- 涉及 API：`notificationManager`、`CustomDialogController`、`promptAction`
- 项目背景：CoupleWorld（使用 `@amap/amap_lbs_map3d` 2.1.1 等依赖）

---

## 一、问题现象

项目中存在两套相互独立的业务逻辑。

**1. 通知授权逻辑**

应用进入首页后，检查当前应用的通知开关状态。如果用户尚未开启通知，则调用 `notificationManager.requestEnableNotification()` 请求通知授权，并由系统展示通知授权弹窗。

**2. 自定义弹窗逻辑**

业务模块根据实际场景，通过 `CustomDialogController` 展示自定义对话框，例如：

- 新消息提示
- 活动通知
- 业务操作确认
- 其他应用内交互弹窗

两套逻辑分别由不同模块维护，彼此没有直接依赖关系。

但在实际运行过程中，可能出现以下时序：

1. 首页初始化，开始检查通知授权状态。
2. 检查发现通知尚未开启，调用通知授权接口。
3. 系统弹出通知授权窗口。
4. 与此同时，业务模块触发自定义弹窗。
5. 调用 `dialogController.open()`，但自定义弹窗没有显示，也没有明显的异常日志。

问题在于：**两段业务逻辑虽然相互独立，但它们最终都需要使用应用的窗口资源展示交互界面。**

当系统级弹窗正在展示时，直接调用应用内自定义弹窗，可能导致自定义弹窗无法正常显示。

## 二、根因分析

### 2.1 系统弹窗与应用弹窗的窗口层级不同

HarmonyOS 中存在不同类型的弹窗和窗口。

系统权限申请、通知授权以及密码保险箱等安全交互，涉及系统管理的安全窗口。

而以下组件主要用于应用内交互：

- `CustomDialog`
- `openCustomDialog`
- `showAlertDialog`
- `showActionSheet`
- `promptAction` 中的 Toast 等提示组件

两者在窗口管理和显示时序方面存在差异。

系统安全窗口具有更高的显示优先级。在部分系统交互场景中，如果系统窗口正在展示，此时再发起应用内弹窗请求，可能导致应用弹窗无法正常显示。

需要注意，这并不意味着所有系统弹窗和应用弹窗在任何情况下都绝对不能共存，而是需要根据具体窗口类型和系统规定处理显示时序。

### 2.2 为什么 CustomDialog.open() 没有显示？

例如：

```typescript
this.dialogController.open();
```

这段代码本身没有问题。

但如果调用发生在系统安全窗口展示期间，ArkUI 自定义弹窗可能无法按照预期完成显示。

这种情况比较难排查，因为：

- `open()` 调用本身不一定抛出异常。
- 业务代码无法直接判断系统安全窗口是否仍然处于展示状态。
- 通知模块和业务弹窗模块通常由不同的业务组件维护。
- 即使两个模块分别运行正常，同时触发时仍可能出现显示冲突。

因此，问题的核心不是修改 `CustomDialog` 的声明方式，而是**统一管理不同弹窗请求的执行时机**。

### 2.3 官方文档参考

HarmonyOS 官方开发者文档也提供了相关问题的说明：

1. 权限申请弹窗与自定义弹窗冲突问题及解决方案（FAQ：`faqs-arkui-1225`）。
2. 解决安全类窗口和自定义弹窗的调用时序引起的自定义弹窗不显示的问题（FAQ：`faqs-arkui-1069`）。

其中，第二篇 FAQ 明确介绍了系统权限弹窗与 `CustomDialog` 等应用内弹窗之间的调用时序问题，并提供了相应的处理方式。

官方参考：

- [解决安全类窗口和自定义弹窗的调用时序引起的自定义弹窗不显示的问题](https://developer.huawei.com/consumer/cn/doc/doccenter-dev-faq/faqs-arkui-1069/)
- [HarmonyOS 通知管理 API 参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager/)

## 三、解决方案设计：DialogGate 弹窗闸门

直接在通知授权逻辑中控制业务弹窗，并不是一个理想的解决方案。

例如，让通知模块在授权完成后主动调用业务模块的弹窗方法，会造成模块之间的直接依赖。

后续如果增加相机权限申请、定位权限申请或者其他系统级交互，就需要在多个业务模块中重复处理类似逻辑。

更合理的方式是引入一个全局弹窗调度机制。

### 3.1 核心设计思路

新增一个全局单例工具类：`DialogGate`。

它的职责非常简单：

- `hold()`：暂时阻止新的自定义弹窗请求执行。
- `release()`：解除阻塞，并放行等待中的请求。
- `run()`：统一管理自定义弹窗的打开请求。

整体执行流程：

```text
             系统弹窗请求
                   |
                   v
             DialogGate.hold()
                   |
                   v
          系统通知授权弹窗展示
                   |
                   | 
          业务模块请求打开弹窗
                   |
                   v
            DialogGate.run()
                   |
                   v
             检查闸门状态
                   |
             +-----+-----+
             |           |
          已持有闸门    未持有闸门
             |           |
             v           v
          加入等待队列   立即执行
             |
             v
       系统弹窗结束
             |
             v
       DialogGate.release()
             |
             v
        放行等待中的请求
             |
             v
       CustomDialog.open()
```

这样，通知授权模块只需要负责持有和释放闸门，业务弹窗模块只需要通过闸门执行打开操作。

两个模块不需要相互引用。

### 3.2 实现 DialogGate 工具类

创建文件：

`common/utils/DialogGate.ets`

```typescript
/**
 * 全局弹窗闸门
 *
 * 用于协调系统级弹窗与应用内 CustomDialog 的显示时序。
 */
export class DialogGate {
  private static instance: DialogGate = new DialogGate();

  /**
   * 闸门持有计数。
   *
   * 使用计数而不是简单的 boolean，
   * 避免多个系统弹窗流程并发时提前释放闸门。
   */
  private holdCount: number = 0;

  /**
   * 等待执行的自定义弹窗请求。
   */
  private pending: Array<() => void> = [];

  private constructor() {}

  static getInstance(): DialogGate {
    return DialogGate.instance;
  }

  /**
   * 持有闸门。
   */
  hold(): void {
    this.holdCount++;
  }

  /**
   * 释放闸门。
   */
  release(): void {
    if (this.holdCount <= 0) {
      return;
    }

    this.holdCount--;

    // 仍有其他系统弹窗流程持有闸门，不执行队列。
    if (this.holdCount > 0) {
      return;
    }

    const queue = this.pending;
    this.pending = [];

    // 按请求顺序执行。
    queue.forEach((fn: () => void) => {
      try {
        fn();
      } catch (error) {
        console.error(
          `DialogGate: Failed to execute dialog request: ${JSON.stringify(error)}`
        );
      }
    });
  }

  /**
   * 自定义弹窗统一执行入口。
   *
   * 如果闸门处于持有状态，则将请求加入队列；
   * 否则立即执行。
   */
  run(fn: () => void): void {
    if (this.holdCount > 0) {
      this.pending.push(fn);
      return;
    }

    fn();
  }
}
```

这里有两个值得注意的设计点。

**第一，使用计数代替 boolean。**

如果项目中同时存在通知授权和其他系统权限申请，可能出现多个流程同时持有闸门的情况。

如果使用简单的：

```typescript
private holding: boolean = false;
```

那么其中一个流程执行 `release()` 后，就可能提前放行其他仍在等待系统弹窗结束的业务请求。

通过 `holdCount` 可以避免这种问题。

只有所有持有闸门的流程都完成后，才会真正放行队列。

**第二，使用队列保存弹窗打开请求。**

当闸门被持有时，`run()` 不会立即执行传入的函数，而是将请求保存起来。

等到闸门完全释放后，再按照请求进入队列的顺序执行。

需要说明的是：这里保证的是请求函数的调用顺序，并不等于保证多个自定义弹窗的完整展示生命周期严格串行。如果业务允许同时积累多个不同弹窗，还需要在业务层设计弹窗优先级、合并或关闭后继续展示的机制。

### 3.3 通知授权模块：只负责 hold / release

通知授权模块不需要知道项目中有哪些自定义弹窗，也不需要引用任何业务弹窗组件。

只需要在系统通知授权流程开始前持有闸门，并在异步流程结束后释放。

示例：

```typescript
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { DialogGate } from '../common/utils/DialogGate';

async requestNotificationPermission(): Promise<void> {
  try {
    const enabled = await notificationManager.isNotificationEnabled();

    if (enabled) {
      this.clearNotification();
      return;
    }

    const gate = DialogGate.getInstance();

    // 系统授权弹窗即将展示，先持有闸门。
    gate.hold();

    try {
      const context = getContext(this) as common.UIAbilityContext;

      await notificationManager.requestEnableNotification(context);

      // 授权成功。
      this.clearNotification();

    } catch (err) {
      const error = err as BusinessError;

      if (error.code === 1600004) {
        // 通知未开启，按业务需要进行提示。
        console.info('Notification is disabled.');

        // 根据实际业务状态决定是否提示用户。
      } else {
        console.error(
          `Notification authorization failed: ${error.code}, ${error.message}`
        );
      }

    } finally {
      // 无论授权成功、失败还是发生异常，都释放闸门。
      gate.release();
    }

  } catch (err) {
    console.error(
      `Failed to check notification status: ${JSON.stringify(err)}`
    );
  }
}
```

这里使用 `try / finally` 保证闸门一定能够释放，避免因为授权失败或者异常导致后续业务弹窗一直处于等待状态。

另外，API 12+ 应优先使用带 `UIAbilityContext` 参数的 `requestEnableNotification(context)` 接口，而不是继续使用已经废弃的无 Context 版本。

**关于错误码 1600004：**

该错误码在通知管理 API 中表示 `Notification disabled`，即通知未开启。它本身并不能单独证明用户已经永久拒绝授权。

因此，不能仅凭这个错误码就将用户状态认定为永久拒绝。实际业务应根据系统返回结果及当前通知状态进行判断。

### 3.4 业务弹窗模块：只修改打开入口

这是整个方案中对业务代码影响最小的地方。

原来的代码：

```typescript
this.dialogController.open();
```

修改为：

```typescript
DialogGate.getInstance().run(() => {
  this.dialogController.open();
});
```

除此之外，原有弹窗的声明、UI 结构以及关闭逻辑都不需要修改。

例如：

```typescript
@Entry
@Component
struct Index {
  private dialogController: CustomDialogController =
    new CustomDialogController({
      builder: MessageDialog(),
      autoCancel: true
    });

  showMessageDialog(): void {
    DialogGate.getInstance().run(() => {
      this.dialogController.open();
    });
  }

  build() {
    Column() {
      Button('显示消息弹窗')
        .onClick(() => {
          this.showMessageDialog();
        });
    }
  }
}
```

`@CustomDialog` 对应的 `CustomDialogController` 仍然按照 ArkUI 的组件约束进行声明和初始化。

DialogGate 只负责控制 `open()` 的调用时机，不改变 Controller 的生命周期和初始化方式。

## 四、关键时序与边界情况

实现弹窗闸门之后，还需要考虑一些实际开发中容易忽略的情况。

### 4.1 系统弹窗结束后再放行

不要在通知授权成功的业务处理逻辑中直接调用：

```typescript
this.dialogController.open();
```

因为业务回调和系统窗口实际关闭之间可能存在时序差异。

应该等待授权请求的 Promise 完成，并在 `finally` 中释放闸门。

这样可以统一处理成功、失败和异常情况。

### 4.2 已授权或无需展示授权弹窗时，不引入人为延时

如果 `isNotificationEnabled()` 检查后发现通知已经开启，就不需要持有闸门。

直接执行后续业务逻辑即可。

对于授权接口返回的其他结果，也应以 API 实际返回的 Promise 状态为准。

DialogGate 本身不使用：

```typescript
setTimeout()
```

也不需要通过固定等待时间猜测系统弹窗何时关闭。

需要注意，Promise 的 `then/catch/finally` 属于异步执行机制，即使 Promise 很快完成，也不代表回调一定在当前同步调用栈中执行。这里的零额外等待，是指不人为增加定时延迟，而不是承诺同步执行。

### 4.3 权限申请弹窗可以复用相同机制

除了通知授权，以下系统交互也可能遇到类似问题：

- `abilityAccessCtrl.requestPermissionsFromUser()`
- 相机权限申请
- 定位权限申请
- 麦克风权限申请
- 其他需要系统安全窗口参与的授权流程

可以统一使用相同的闸门机制。

例如：

```typescript
const gate = DialogGate.getInstance();

gate.hold();

try {
  await abilityAccessCtrl.requestPermissionsFromUser(
    context,
    permissions
  );

} catch (err) {
  console.error(`Permission request failed: ${JSON.stringify(err)}`);

} finally {
  gate.release();
}
```

这样，权限申请模块只需要管理自己的系统授权流程，不需要知道业务弹窗的具体实现。

### 4.4 反向时序：自定义弹窗先打开

还有一种情况：

1. 业务模块先调用 `CustomDialogController.open()`。
2. 自定义弹窗已经正常显示。
3. 此时通知授权流程开始。
4. 系统弹窗随后展示。

对于这种情况，系统安全窗口具有更高的显示优先级，可以覆盖应用内的交互界面。

因此，DialogGate 不需要主动关闭已经打开的自定义弹窗，也不需要在系统弹窗结束后重新创建它。

不过，具体表现仍应以目标设备和系统版本的实际窗口行为为准。

### 4.5 多个业务弹窗同时进入等待队列

当前 DialogGate 的实现按照请求进入队列的顺序调用回调。

但需要特别注意：

```typescript
queue.forEach(fn => fn());
```

这只是保证函数调用顺序，并不会等待前一个 `CustomDialog` 关闭后再执行下一个。

如果多个业务弹窗可能同时排队，建议在业务层增加统一的弹窗调度策略，例如：

- 同一时间只允许展示一个业务弹窗。
- 相同类型的重复弹窗进行合并。
- 不同优先级的弹窗按优先级展示。
- 当前弹窗关闭后，再通知调度器展示下一个。

对于只有一个待展示业务弹窗，或者业务侧已经保证弹窗互斥的场景，当前实现即可满足需求。

另外，排队回调持有的是组件及其 Controller 的引用。页面可能在系统弹窗展示期间销毁或跳转，因此在复杂页面场景中，还应检查页面是否仍然有效，避免对已经失效的 Controller 执行 `open()`。

## 五、方案优势与适用范围

与直接在各个业务模块中处理系统弹窗冲突相比，DialogGate 的优势主要体现在以下几个方面。

| 对比维度 | 直接处理 | DialogGate |
| --- | --- | --- |
| 模块耦合 | 可能需要相互引用 | 相互独立 |
| 弹窗调用 | 各模块自行处理 | 统一入口 |
| 并发控制 | 分散处理 | 集中管理 |
| 请求等待 | 需要额外处理 | 内部队列 |
| 扩展性 | 增加系统弹窗时需要修改业务逻辑 | 复用 hold/release |
| 延时处理 | 容易引入固定延时 | 不需要人为延时 |

这套方案尤其适合以下场景：

1. 应用存在多个独立的系统权限申请流程。
2. 多个业务模块都可能触发 CustomDialog。
3. 不希望系统授权模块与 UI 业务模块产生直接依赖。
4. 希望统一管理应用内弹窗的调用入口。
5. 项目规模逐渐扩大，需要集中维护弹窗调度逻辑。

需要注意，DialogGate 解决的是系统弹窗与应用内弹窗之间的调用时序问题，并不替代 ArkUI 自身的弹窗生命周期管理，也不负责解决多个业务弹窗之间的展示优先级问题。

## 六、总结

HarmonyOS NEXT 中，系统级安全窗口与应用内自定义弹窗存在不同的窗口管理机制。当两者在同一时间窗口内并发触发时，可能出现 `CustomDialogController.open()` 调用成功但弹窗未正常显示的情况。

对于这种问题，单纯修改业务弹窗代码并不能从根本上解决问题。

通过引入全局单例 `DialogGate`，可以将系统弹窗的显示时序控制与业务弹窗的展示逻辑分离：

- 系统授权模块负责 `hold()` 和 `release()`。
- 业务弹窗模块统一通过 `run()` 请求打开弹窗。
- 闸门持有期间，新的业务弹窗请求进入等待队列。
- 所有系统弹窗流程结束后，等待队列自动放行。

整个设计只需要一个轻量级工具类，不需要通知模块与业务弹窗模块互相依赖，也不需要通过固定延时来规避系统窗口冲突。

**核心思想：系统弹窗负责控制时序，业务弹窗负责展示内容，中间通过一个统一的 DialogGate 完成协调。**

这种设计也可以扩展到 HarmonyOS 项目中的其他系统级交互场景，为应用内弹窗提供一个更加统一、可维护的调度入口。

---

## 参考资料

- [HarmonyOS 官方 FAQ：解决安全类窗口和自定义弹窗的调用时序引起的自定义弹窗不显示的问题](https://developer.huawei.com/consumer/cn/doc/doccenter-dev-faq/faqs-arkui-1069/)
- [HarmonyOS NotificationKit API 参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager/)
- [HarmonyOS ArkUI：基础自定义弹出框 CustomDialog](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-dialog/)

*本文记录于 2026-11-10。基于 CoupleWorld 项目中的实际问题整理，代码示例需结合项目实际 API 版本及页面生命周期进行验证。*