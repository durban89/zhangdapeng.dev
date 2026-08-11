---
title: "Fixing the htmlspecialchars UTF-8 Error"
date: "2025-06-20 14:33:42"
slug: "fixing-the-htmlspecialchars-utf-8-error"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/Fixing-the-htmlspecialchars-UTF-8-Error/"
  - "/2025/06/20/Fixing-the-htmlspecialchars-UTF-8-Error.html"
  - "/Fixing-the-htmlspecialchars-UTF-8-Error/"
  - "/Fixing-the-htmlspecialchars-UTF-8-Error.html"
  - "/2025/06/20/fixing-the-htmlspecialchars-utf-8-error/"
  - "/2025/06/20/fixing-the-htmlspecialchars-utf-8-error.html"
  - "/fixing-the-htmlspecialchars-utf-8-error.html"
---
If you’ve ever come across the infuriating error

```bash
htmlspecialchars(): Invalid multibyte sequence in argument
```

I have a simple solution for you: Turn `display_errors` on in your php.ini file!  
It turns out there’s a weird bug that doesn’t appear to be getting fixed any time soon that causes `htmlspecialchars()` to display this error only when `display_errors` is set to Off.

