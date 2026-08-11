---
title: "ruhoh - Publish Websites Like a BOSS B]（静态博客引擎）"
date: "2025-06-24 11:24:17"
slug: "ruhoh-publish-websites-like-a-boss-b-jing-tai-bo-ke-yin-qing"
categories: ["技术"]
tags: ["Ruhoh"]
aliases:
  - "/2025/06/24/ruhoh-Publish-Websites-Like-a-BOSS-B]（静态博客引擎）/"
  - "/2025/06/24/ruhoh-Publish-Websites-Like-a-BOSS-B]（静态博客引擎）.html"
  - "/ruhoh-Publish-Websites-Like-a-BOSS-B]（静态博客引擎）/"
  - "/ruhoh-Publish-Websites-Like-a-BOSS-B]（静态博客引擎）.html"
  - "/2025/06/24/ruhoh-Publish-Websites-Like-a-BOSS-B-静态博客引擎/"
  - "/2025/06/24/ruhoh-Publish-Websites-Like-a-BOSS-B-静态博客引擎.html"
  - "/2025/06/24/ruhoh-publish-websites-like-a-boss-b-jing-tai-bo-ke-yin-qing/"
  - "/2025/06/24/ruhoh-publish-websites-like-a-boss-b-jing-tai-bo-ke-yin-qing.html"
  - "/ruhoh-publish-websites-like-a-boss-b-jing-tai-bo-ke-yin-qing.html"
---
### [Ruhoh简介](#1)

Ruhoh(http://ruhoh.com/) is a static site generator made for publishing content on the Internet. It's similar to [jekyll](http://jekyllrb.com/), [nanoc](http://nanoc.ws/), and [others](http://nanoc.ws/about/#similar-projects).

**A static site** is a website with no moving parts: no dependencies, no database, no code execution, no admin panel. This is different from a "web application" which requires many layers of software.

**Creating a static site** in ruhoh is done by creating standard HTML, CSS, and javascript files on your local computer as you would normally. Ruhoh does magic based on the way you organize your files and settings. Ruhoh offers baked-in automation, templating, and bindings for powerful features but you don't have to know or touch the underlying programming logic if you don't want to.

**Publish anywhere** by "compiling" your website and hosting the contents on nearly any web-host on the planet. Ruhoh also supports automatic hosting so you don't have to worry about finding or setting up a web-host.

Why a static site?

In terms of publishing textual content and images, a static site is much faster, more secure, costs less, and is highly scalable -- it won't slow to a crawl or crash due to increased traffic.

But maybe you just want to use Wordpress or Tumblr?

There comes a time in your life when as a creator you must create! Your technical curiousity compels you to return to the joy and freedom of using your own tools and owning your content.

You fire up your text-editor and create a masterpiece. A quick switch over to the terminal allows you to execute "publish" like some hipster techno-wizard -- lines of output race down your black terminal screen until finally you see "completed!"

You verify your website is updated, bring up Facebook, twitter, gchat, and snapchat(?), CTRL+V your domain into the appropriate boxes and you pause for three triumphant seconds before finally proclaiming...

"I made that!"

Why ruhoh?

**Ruhoh is straightforward.**

Ruhoh doesn't want you to program your website; it wants you to publish content! Use HTML, CSS, and javascript like you would naturally, but have the power of automation and tooling there when you want it.

**Focus on content not programming.**

Ruhoh is language-agnostic, it's not strictly tied to any one language so you don't need to know ruby or do any programming if you don't want to. However, it turns out to be a good way to learn.

Focus on Web Publishing and nothing else. Ruhoh prioritizes web-publishing specific optimizations like SEO-optimized permalink structures, cononical redirects, microformats, RSS/ATOM feed generation, robust internationalization, textual search, comments, and so on.

**Onions**

Ruhoh should be immediately usable and effective for beginners and experts alike. All functionality should be intuitive and simple to uncover and learn. As your experience grows and you dive deeper into customizations, the layers of power, functionality, and extensibility should elegantly peel away from ruhoh like an onion. You don't have to use them, but they will be there.

Who should use ruhoh?

Ruhoh is built for users looking to publish content online. Publishing content is not the same as creating web apps so ruhoh is not an application framework and you don't have to be a programmer.

You:

* Are technically curious.
* Are interested in basic web programming such as HTML, CSS, and javascript.
* Value owning your own content.
* May be jaded by hosted solutions like Wordpress and Tumblr.
* Are probably not cool with NSA surveillance.

Knowledge of ruby is not required, but since ruby can be a pain to install, it's best if you are capable of setting up a 1.9+ ruby environment locally.

Ruhoh is pretty technical, but the goal is to be accessible and intuitive for beginners.

Beginners are welcomed and encouragd to grow with ruhoh's functionality as experience and curiousity dictates. Experts can immediatelytake full advantage of ruhoh's modular architecture and straightforward APIs. Nearly all features are powered by standalone "service libraries" that can be overloaded or swapped.

## [Core Goals](#2)

1. Prioritize Web Publishing.

   Work will focus on delivering the best publishing experience and utilizing the web's latest standards for maintaining published content on the Internet.
2. Beginner Friendly.

   Simplicity will be the highest meausure of success. Publishing should be modeled from standard HTML, CSS, and javascript workflows. Ruhoh should be a transparent layer that enables power, automatation, and extensibility but only when desired.
3. Language-agnostic.

   A language-specific workflow places focus on the tool rather than the content. Therefore ruhoh's core design and interface should be completely free from language-dependent knowledge or paradigms.
4. Freely Customizable.

   Ruhoh provides many core features such as URL formatting, markdown rendering, tags, automatic summarization, etc. These functions should expose themselves merely as "services" that the user can override, extend, replace, or re-implement without worry.
5. Obsessive Separation of Concerns

   Ruhoh is designed around three principle layers of functionality which are obsessively kept separated as much as possible.

