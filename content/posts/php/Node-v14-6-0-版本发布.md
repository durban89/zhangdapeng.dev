---
title: "Node v14.6.0 版本发布"
date: "2025-07-11 10:40:30"
slug: "node-v1460-ban-ben-fa-bu"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/11/Node-v14.6.0-版本发布/"
  - "/2025/07/11/Node-v14.6.0-版本发布.html"
  - "/Node-v14.6.0-版本发布/"
  - "/Node-v14.6.0-版本发布.html"
  - "/2025/07/11/Node-v14-6-0-版本发布/"
  - "/2025/07/11/Node-v14-6-0-版本发布.html"
  - "/2025/07/11/node-v1460-ban-ben-fa-bu/"
  - "/2025/07/11/node-v1460-ban-ben-fa-bu.html"
  - "/node-v1460-ban-ben-fa-bu.html"
---
### 发布时间：by Myles Borins, 2020-07-21

### **Notable Changes**

* **deps**:
  + upgrade to libuv 1.38.1 (Colin Ihrig) [#34187](https://github.com/nodejs/node/pull/34187)
  + upgrade npm to 6.14.6 (claudiahdz) [#34246](https://github.com/nodejs/node/pull/34246)
  + **(SEMVER-MINOR)** update V8 to 8.4.371.19 (Michaël Zasso) [#33579](https://github.com/nodejs/node/pull/33579)
* **module**:
  + **(SEMVER-MINOR)** doc only deprecation of module.parent (Antoine du HAMEL) [#32217](https://github.com/nodejs/node/pull/32217)
  + **(SEMVER-MINOR)** package "imports" field (Guy Bedford) [#34117](https://github.com/nodejs/node/pull/34117)
* **src**:
  + **(SEMVER-MINOR)** allow embedders to disable esm loader (Shelley Vohr) [#34060](https://github.com/nodejs/node/pull/34060)
* **tls**:
  + **(SEMVER-MINOR)** make 'createSecureContext' honor more options (Mateusz Krawczuk) [#33974](https://github.com/nodejs/node/pull/33974)
* **vm**:
  + **(SEMVER-MINOR)** add run-after-evaluate microtask mode (Anna Henningsen) [#34023](https://github.com/nodejs/node/pull/34023)
* **worker**:
  + **(SEMVER-MINOR)** add option to track unmanaged file descriptors (Anna Henningsen) [#34303](https://github.com/nodejs/node/pull/34303)
* **New Collaborators**:
  + add danielleadams to collaborators (Danielle Adams) [#34360](https://github.com/nodejs/node/pull/34360)
  + add ruyadorno to collaborators (Ruy Adorno) [#34297](https://github.com/nodejs/node/pull/34297)
  + add sxa as collaborator (Stewart X Addison) [#34338](https://github.com/nodejs/node/pull/34338)

原文地址：<https://nodejs.org/en/blog/release/v14.6.0/>
