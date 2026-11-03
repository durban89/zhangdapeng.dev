---
title: "Elegant and Smooth: How to Optimize the Related Content Scrollbar in Hugo Stack Theme"
description: "Learn how to optimize the horizontal related posts carousel in hugo-theme-stack using pure CSS/SCSS. Choose from three styles: minimal hidden, sleek custom style, or scroll snapping."
date: 2026-11-03T01:08:00+08:00
image: "./hugo-scrollbar-opt.jpg"
math: false
hidden: false
comments: true
draft: false
slug: "hugo-stack-scrollbar-optimization"
categories:
    - Linux
    - Development
    - Hugo
tags:
    - Hugo
    - CSS
    - Stack Theme
    - UI UX
---

In modern web design, **hugo-theme-stack** is a top choice for independent bloggers due to its elegant card-based layout and clean responsive design. At the bottom of the article detail page, the Stack theme features a native horizontal scrolling card flow for "Related Content."

However, the default system scrollbars (especially on Chrome/Edge for Windows) can look clunky and rigid, often disrupting the aesthetic harmony of the page. In this post, I will share how to smoothly optimize the scrollbar for `hugo-theme-stack` using pure CSS/SCSS across three different design approaches.

---

## 🎯 Finding the Core Class Names

Before jumping into the code, we need to locate the DOM structure of the related content section in the Stack theme. By inspecting the elements, we can find the core classes:
* **Scrollbar Container**: `.related-contents--list`
* **Individual Post Card**: `.article-card`

In Hugo, you do not need to modify the theme's core files. Simply add your custom styles to the **`assets/scss/custom.scss`** file located in your project root.

---

## 🚀 Three Optimization Approaches

### Option 1: Completely Hidden (Minimal Touch Style) — ✨ Recommended

The cards in the Stack theme already have a natural breathing room. Modern devices (such as smartphones, trackpads, and desktops via `Shift + Scroll`) support horizontal swiping natively. **Hiding the scrollbar altogether often yields the cleanest look.**

Add the following code to your `custom.scss`:

```scss
/* Hide default scrollbar for related content while maintaining native smooth scrolling */
.related-contents--list {
    /* Hide scrollbar for Firefox */
    scrollbar-width: none; 
    /* Hide scrollbar for IE/Edge */
    -ms-overflow-style: none; 
    
    /* Optimize momentum scrolling on mobile devices */
    -webkit-overflow-scrolling: touch;

    /* Hide scrollbar for Chrome, Safari, and newer Edge */
    &::-webkit-scrollbar {
        display: none !important; 
    }
}
```

### Option 2: Sleek & Custom (Dark Mode Responsive)

If you prefer keeping a scrollbar to guide your readers visually, you can use CSS pseudo-elements to turn it into a thin, rounded, and elegant indicator. This code utilizes Stack's built-in CSS variables to perfectly adapt to both **Light and Dark modes**:

```scss
/* Fine-tune the horizontal scrollbar style */
.related-contents--list {
    scroll-behavior: smooth;
    padding-bottom: 12px; /* Leave space to prevent the thumb from clipping card shadows */

    /* Set horizontal scrollbar height */
    &::-webkit-scrollbar {
        height: 5px;
    }

    /* Scrollbar track background (keep it transparent to blend with the page) */
    &::-webkit-scrollbar-track {
        background: transparent; 
    }

    /* Scrollbar thumb */
    &::-webkit-scrollbar-thumb {
        background-color: var(--card-background); /* Uses the theme's card background variable */
        filter: brightness(0.9); /* Makes it slightly darker than the card in Light Mode */
        border-radius: 10px;
        border: 1px solid transparent;
        transition: background-color 0.3s ease;
        
        &:hover {
            background-color: var(--accent-color); /* Changes to theme accent color on hover */
        }
    }
}

/* Micro-adjustments for Dark Mode */
html[data-scheme="dark"] .related-contents--list {
    &::-webkit-scrollbar-thumb {
        filter: brightness(1.2); /* Makes it slightly brighter than the background in Dark Mode */
    }
}
```

### Option 3: Card Alignment (Scroll Snapping) — 💡 Bonus Feature

Whether you choose to hide or style the scrollbar, you can always layer on a "magnetic alignment" effect. When users swipe and release their finger or trackpad, the cards won't awkwardly stop halfway. Instead, they will **automatically snap to the left edge**, much like a mobile app slider:

```scss
/* Enable strong horizontal scroll snapping */
.related-contents--list {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory; 
}

/* Set each card as a snap point */
.related-contents--list .article-card {
    scroll-snap-align: start; 
}
```

---

## 🛠️ Quick Deployment

1. Open your Hugo blog root directory.
2. Navigate to the `assets/scss/` folder (create it manually if it doesn't exist).
3. Open or create `custom.scss` and paste your preferred snippet.
4. Run `hugo server` locally, clear your browser cache, and enjoy your smooth new related content slider!

I hope this quick layout hack improves your independent blog's user experience. If you run into any style conflicts or layout glitches, feel free to drop a comment below!
