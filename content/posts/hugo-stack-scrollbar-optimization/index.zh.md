---
title: "优雅永不过时：如何优化 Hugo Stack 主题的关联文章横向滚动条"
description: "通过纯 CSS/SCSS 样式对 hugo-theme-stack 的关联文章卡片流进行丝滑优化，打造极简隐藏、精致美化与磁吸对齐三种不同风格的视觉体验。"
date: 2026-11-03T01:08:00+08:00
image: "./hugo-scrollbar-opt.jpg"
math: false
hidden: false
comments: true
draft: false
slug: "hugo-stack-scrollbar-optimization"
categories:
    - 前端开发
    - Hugo 教程
tags:
    - Hugo
    - CSS
    - Stack 主题
    - 滚动条优化
---

在现代网页设计中，**hugo-theme-stack** 凭借其优雅的卡片式布局和极简的响应式设计，成为了无数独立博主的首选。在文章详情页的底部，Stack 主题自带了“关联文章（Related Content）”的横向卡片流推荐。

然而，原生系统自带的横向滚动条（尤其是 Windows 上的 Chrome/Edge）通常比较生硬且粗笨，容易破坏整体界面的美感。本文将分享如何通过纯 CSS/SCSS 样式对 `hugo-theme-stack` 的滚动条进行丝滑优化，打造三种不同风格的视觉体验。

---

## 🎯 寻找核心类名

在开始修改前，我们需要精确定位 Stack 主题关联文章的 DOM 结构。通过审查元素可以发现，它的核心类名为：
* **滚动条容器**：`.related-contents--list`
* **单个文章卡片**：`.article-card`

在 Hugo 项目中，我们不需要修改主题源码，只需将优化代码写入项目根目录下的 **`assets/scss/custom.scss`** 自定义样式文件中即可。

---

## 🚀 三种优化方案

### 方案一：全面隐藏（极简触控风）—— ✨ 最推荐

Stack 主题的卡片本身就有天然的呼吸感，且现代设备（手机触控、笔记本触控板、甚至按住 `Shift` 滚动鼠标滚轮）都原生支持横向滑动。**直接隐藏滚动条，往往能让页面视觉最纯粹。**

将以下代码加入 `custom.scss`：

```scss
/* 隐藏关联文章的默认滚动条，保留流畅的原生滑动体验 */
.related-contents--list {
    /* 隐藏 Firefox 的滚动条 */
    scrollbar-width: none; 
    /* 隐藏 IE/Edge 的滚动条 */
    -ms-overflow-style: none; 
    
    /* 优化移动端滑动的流畅度 */
    -webkit-overflow-scrolling: touch;

    /* 隐藏 Chrome、Safari 和新版 Edge 的滚动条 */
    &::-webkit-scrollbar {
        display: none !important; 
    }
}
```

### 方案二：精致美化（暗色模式自适应）

如果你希望保留滚动条为用户提供明确的视觉引导，可以通过 CSS 伪元素将其改造成细长、圆润的精致样式。这段代码使用了 Stack 主题内置的 CSS 变量，能够自动完美适配**白天/黑夜模式**：

```scss
/* 精细化自定义横向滚动条 */
.related-contents--list {
    scroll-behavior: smooth;
    padding-bottom: 12px; /* 留出一点空间，避免滑块挤压卡片阴影 */

    /* 定义横向滚动条整体高度 */
    &::-webkit-scrollbar {
        height: 5px;
    }

    /* 滚动条轨道（背景保持透明，隐入大背景中） */
    &::-webkit-scrollbar-track {
        background: transparent; 
    }

    /* 滚动条滑块 */
    &::-webkit-scrollbar-thumb {
        background-color: var(--card-background); /* 使用主题自带的卡片背景色变量 */
        filter: brightness(0.9); /* 白天模式下，比卡片颜色略深一点点 */
        border-radius: 10px;
        border: 1px solid transparent;
        transition: background-color 0.3s ease;
        
        &:hover {
            background-color: var(--accent-color); /* 鼠标悬停时，变为主题高亮色 */
        }
    }
}

/* 针对暗色模式（Dark Mode）的微调 */
html[data-scheme="dark"] .related-contents--list {
    &::-webkit-scrollbar-thumb {
        filter: brightness(1.2); /* 在黑夜模式下，比背景稍微亮一点点，方便辨识 */
    }
}
```

### 方案三：磁吸对齐（Scroll Snapping）—— 💡 加分项

无论你选择隐藏还是美化滚动条，都可以叠加这个“磁吸效果”。当用户滑动卡片松开手指时，卡片不会尴尬地停在正中间，而是像手机 App 里的轮播图一样，**自动向左侧对齐**：

```scss
/* 开启横向强力磁吸对齐 */
.related-contents--list {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory; 
}

/* 单个卡片作为捕捉点 */
.related-contents--list .article-card {
    scroll-snap-align: start; 
}
```

---

## 🛠️ 如何快速部署？

1. 打开你的 Hugo 博客根目录。
2. 导航至 `assets/scss/` 文件夹（如果没有，可以手动创建）。
3. 打开或新建 `custom.scss`，将上面你心仪的方案代码复制进去。
4. 在本地运行 `hugo server`，清理一下浏览器缓存，即可看到全新、丝滑的底部关联文章滑动效果！

希望这篇教程能帮你的独立博客体验更上一层楼。如果你在修改过程中遇到了样式冲突或其他布局问题，欢迎在下方留言交流！
