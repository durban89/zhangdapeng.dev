---
title: "Sublime  Text 3 之 MAC版本的 主题设置"
date: "2025-07-03 11:58:54"
slug: "sublime-text-3-zhi-mac-ban-ben-de-zhu-ti-she-zhi"
categories: ["技术"]
tags: ["Sublime"]
aliases:
  - "/2025/07/03/Sublime-Text-3-之-MAC版本的-主题设置/"
  - "/2025/07/03/Sublime-Text-3-之-MAC版本的-主题设置.html"
  - "/Sublime-Text-3-之-MAC版本的-主题设置/"
  - "/Sublime-Text-3-之-MAC版本的-主题设置.html"
  - "/2025/07/03/sublime-text-3-zhi-mac-ban-ben-de-zhu-ti-she-zhi/"
  - "/2025/07/03/sublime-text-3-zhi-mac-ban-ben-de-zhu-ti-she-zhi.html"
  - "/sublime-text-3-zhi-mac-ban-ben-de-zhu-ti-she-zhi.html"
---
配置主题前提条件

安装插件包

1. Material-Theme
2. Material Theme Appbar

然后将配置按照如下配置下，效果界面很爽眼。

```json
{
	"always_show_minimap_viewport": true,
	"bold_folder_labels": true,
	"color_scheme": "Packages/Material Theme/schemes/Material-Theme.tmTheme",
	"font_face": "Source Code Pro for Powerline",
	"font_size": 13,
	"highlight_line": true,
	"ignored_packages":
	[
		"Vintage"
	],
	"indent_guide_options":
	[
		"draw_normal",
		"draw_active"
	],
	"material_theme_accent_red": true,
	"material_theme_bold_tab": true,
	"material_theme_compact_panel": true,
	"material_theme_compact_sidebar": true,
	"material_theme_contrast_mode": true,
	"material_theme_panel_separator": true,
	"material_theme_small_statusbar": true,
	"material_theme_small_tab": true,
	"material_theme_tabs_autowidth": true,
	"material_theme_tabs_separator": true,
	"material_theme_tree_headings": true,
	"overlay_scroll_bars": "enabled",
	"rulers":
	[
		80,
		110
	],
	"show_encoding": true,
	"theme": "Material-Theme.sublime-theme",
	"word_wrap": false
}
```


