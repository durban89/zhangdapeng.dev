+++
title = "解决 Hugo 代码高亮无法跟随 Dark/Light 主题切换的问题"
date = 2026-11-07T08:00:00+08:00
lastmod = 2026-11-07T08:00:00+08:00
description = "通过 Hugo Chroma、SCSS 和 CSS 选择器，实现代码高亮与 hugo-theme-stack 深浅色模式同步切换，无需引入额外的 JavaScript 高亮库。"
categories = ["技术", "Linux"]
tags = ["Hugo", "Chroma", "SCSS", "CSS", "Theme Stack"]
image = "./cover.png"
image_alt = "Hugo code highlighting switching between dark and light themes using Chroma and SCSS"
toc = true
+++

在使用 Hugo 搭建技术博客时，很多现代化主题（例如 `hugo-theme-stack`）都提供了 Dark/Light（深色与浅色）模式切换功能。

但有一个容易被忽略的问题：**页面主体已经切换了颜色，代码块却仍然保持原来的高亮主题。**

例如，切换到深色模式后，页面背景变成了深色，而代码块依然使用白色背景和浅色主题的语法配色。这不仅影响视觉一致性，也会降低代码的可读性。

本文将介绍如何利用 Hugo 内置的 Chroma 高亮引擎、两套静态 CSS 和 SCSS，实现代码高亮与主题模式同步切换。

整个方案不需要额外的 JavaScript 高亮库，也不会增加浏览器端的代码解析开销。

## 1. 为什么代码高亮无法跟随主题切换？

Hugo 默认使用内置的 **Chroma** 代码高亮引擎，在网站构建阶段（Build Time）生成语法高亮 HTML。

Chroma 支持两种主要的样式输出方式：

- **Inline Styles**：将颜色信息直接写入 HTML 元素的 `style` 属性。
- **CSS Classes**：通过 CSS Class 标记不同的语法元素，再由外部 CSS 控制颜色。

如果使用默认的内联样式模式，生成的 HTML 可能类似这样：

```html
<div class="highlight">
    <pre style="color:#24292e;background-color:#fff">
        ...
    </pre>
</div>
```

这会带来一个问题：代码块的颜色已经在 Hugo 构建时写入 HTML，前端主题切换时，即使修改了 CSS Class 或 HTML 属性，也很难通过普通 CSS 规则覆盖这些内联样式。

因此，解决问题的关键是：

**让 Chroma 使用 CSS Classes，而不是 Inline Styles。**

这样，我们就可以完全通过 CSS 控制代码高亮颜色。

## 2. 解决方案：使用两套静态 CSS

整体实现思路：

1. 关闭 Chroma 的内联样式输出。
2. 分别生成浅色和深色代码高亮样式。
3. 利用 Hugo Theme Stack 的主题属性控制样式加载。
4. 通过 SCSS 将深色样式限定在 Dark Mode 下。

下面以 `hugo-theme-stack` 为例。

### 第一步：修改 Hugo 配置

打开项目根目录下的 `hugo.toml`（或 `config.toml`），添加以下配置：

```toml
[markup]
  [markup.highlight]
    noClasses = false
    codeFences = true
    guessSyntax = true
```

其中，最重要的是：

```toml
noClasses = false
```

这个配置告诉 Hugo 使用 CSS Class 输出语法高亮，而不是生成内联颜色样式。

注意：

- `false` 表示使用 CSS Classes。
- `true` 表示使用内联样式。
- 这段配置应该放在 `[markup.highlight]` 节点下，而不是 `[params]` 中。

### 第二步：生成两套 Chroma 样式

Hugo 内置了 Chroma 样式生成命令，可以直接导出不同配色方案对应的 CSS。

在项目根目录执行：

```bash
# 浅色模式
hugo gen chromastyles --style=github > assets/scss/syntax-light.scss

# 深色模式
hugo gen chromastyles --style=github-dark > assets/scss/syntax-dark.scss
```

这里分别使用：

- `github`：适合浅色背景的代码高亮主题。
- `github-dark`：适合深色背景的代码高亮主题。

**注意：** 这里使用 `.scss` 扩展名，而不是 `.css`。这样可以让 Hugo 的 Sass/SCSS 构建流程将样式文件作为 SCSS 内容导入，而不是保留为浏览器端的 CSS `@import`。

如果 `assets/scss/` 目录不存在，请先手动创建：

```bash
mkdir -p assets/scss
```

你也可以根据自己的博客风格选择其他 Chroma 配色方案。

### 第三步：修改 custom.scss

`hugo-theme-stack` 提供了 `assets/scss/custom.scss` 作为自定义样式入口。

打开或创建该文件，添加以下代码：

```scss
/* ==========================================
   Chroma Syntax Highlighting Theme Switching
   ========================================== */

// 1. 默认使用浅色代码高亮主题
@import "syntax-light";

// 2. Dark Mode 下切换为深色代码高亮主题
html[data-scheme="dark"] {
    @import "syntax-dark";
}
```

这里的关键是：

```scss
html[data-scheme="dark"] {
    @import "syntax-dark";
}
```

由于 `syntax-dark.scss` 是 SCSS 文件，Sass 会将其中的 CSS 规则展开到对应的选择器作用域中。

最终生成的 CSS 效果类似：

```css
.chroma {
    /* Light Mode styles */
}

html[data-scheme="dark"] .chroma {
    /* Dark Mode styles */
}
```

这样就实现了两套代码高亮样式的隔离：

- Light Mode：使用 `syntax-light.scss`。
- Dark Mode：使用 `syntax-dark.scss`。

切换主题时，浏览器只需要根据 HTML 属性匹配对应的 CSS 规则即可。

**关于背景色：**

如果发现代码块背景色仍然受到主题默认样式影响，可以通过浏览器开发者工具检查最终生效的 CSS。

例如，如果深色代码主题使用 `#24292e` 作为背景色，可以针对实际使用的代码块容器添加覆盖规则：

```scss
html[data-scheme="dark"] {
    .highlight,
    .chroma {
        background-color: #24292e;
    }
}
```

具体选择器和背景颜色应以实际生成的 Chroma CSS 及主题样式为准，不建议一开始就大量使用 `!important`。

### 第四步：重新构建并验证

完成配置后，重新启动 Hugo：

```bash
hugo server --disableFastRender
```

如果需要验证最终生成的 HTML，可以在浏览器中打开开发者工具，检查代码块元素。

正确启用 `noClasses = false` 后，应该能够看到类似：

```html
<div class="highlight">
    <div class="chroma">
        <pre tabindex="0" class="chroma">
            ...
        </pre>
    </div>
</div>
```

具体 HTML 结构可能因 Hugo 版本、Markdown 渲染配置和主题模板而有所不同。

重点是：代码高亮颜色应该由 CSS Class 控制，而不是由大量内联 `style` 属性控制。

接下来，分别切换主题：

- Light Mode：代码块应显示 GitHub 浅色配色。
- Dark Mode：代码块应显示 GitHub Dark 深色配色。

如果切换后没有立即生效，可以尝试浏览器强制刷新（Windows/Linux：`Ctrl + Shift + R`，macOS：`Cmd + Shift + R`），并检查 Hugo 是否成功重新编译了自定义 SCSS。

## 3. 常见问题

### Q1：为什么设置了 `noClasses = false`，代码块还是没有变化？

首先检查 Hugo 是否正确加载了配置文件。

然后查看生成的 HTML：

- 如果仍然存在大量定义语法颜色的内联 `style` 属性，说明配置可能没有生效。
- 如果已经生成 `.chroma`、`.hl` 等 CSS Class，则说明 Chroma 已经切换到 Class 模式，需要进一步检查 CSS 是否正确加载。

### Q2：为什么 Dark Mode 下代码块仍然是白色背景？

通常有两个原因：

1. 深色 CSS 没有正确导入或生成。
2. 主题本身的代码块背景规则覆盖了 Chroma 的背景设置。

可以通过浏览器开发者工具检查 `.highlight` 和 `.chroma` 的最终计算样式，确认究竟是哪条 CSS 规则生效。

### Q3：是否需要引入 Prism.js 或 Highlight.js？

不需要。

Hugo 已经通过 Chroma 在构建阶段完成了代码高亮。只要使用 CSS Classes，就可以通过静态样式控制颜色，不需要再引入额外的客户端代码高亮库。

## 4. 总结

Hugo 代码高亮无法跟随深浅色模式切换，核心原因通常不是主题切换功能本身，而是代码高亮样式的输出方式。

通过以下三个关键步骤：

1. 设置 `noClasses = false`，让 Chroma 使用 CSS Classes。
2. 使用 `hugo gen chromastyles` 生成浅色和深色两套样式。
3. 利用 `html[data-scheme="dark"]` 和 SCSS 控制深色样式的作用范围。

就可以实现代码高亮与网站主题的同步切换。

这种方案具有几个明显优势：

- **纯静态实现**：不需要额外的 JavaScript 高亮库。
- **性能开销低**：代码高亮在 Hugo 构建阶段完成。
- **易于维护**：两套配色独立管理，后续修改也很方便。
- **兼容主题切换**：直接利用 Theme Stack 已有的 `data-scheme` 属性。

对于使用 Hugo 和 hugo-theme-stack 搭建技术博客的开发者来说，这是一个简单、轻量且容易维护的解决方案。