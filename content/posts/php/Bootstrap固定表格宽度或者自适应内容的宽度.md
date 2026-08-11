---
title: "Bootstrap固定表格宽度或者自适应内容的宽度"
date: "2025-07-02 11:31:40"
slug: "bootstrap-gu-ding-biao-ge-kuan-du-huo-zhe-zi-shi-ying-nei-rong-de-kuan-du"
categories: ["技术"]
tags: ["Bootstrap"]
aliases:
  - "/2025/07/02/Bootstrap固定表格宽度或者自适应内容的宽度/"
  - "/2025/07/02/Bootstrap固定表格宽度或者自适应内容的宽度.html"
  - "/Bootstrap固定表格宽度或者自适应内容的宽度/"
  - "/Bootstrap固定表格宽度或者自适应内容的宽度.html"
  - "/2025/07/02/bootstrap-gu-ding-biao-ge-kuan-du-huo-zhe-zi-shi-ying-nei-rong-de-kuan-du/"
  - "/2025/07/02/bootstrap-gu-ding-biao-ge-kuan-du-huo-zhe-zi-shi-ying-nei-rong-de-kuan-du.html"
  - "/bootstrap-gu-ding-biao-ge-kuan-du-huo-zhe-zi-shi-ying-nei-rong-de-kuan-du.html"
---
这个可以通过colgroup来控制单元格的宽度，如果只定义部分宽度，其他的单元格会自适应的调整。  
  
实例代码如下

```html
<thead>
  <colgroup>
    <col></col>
    <col></col>
    <col></col>
    <col></col>
    <col></col>
    <col width='20%'></col>
    <col></col>
    <col></col>
  </colgroup>
  <tr>
    <th>用户名称</th>
    <th>登录方式</th>
    <th>联系方式</th>
    <th>内容</th>
    <th>客户端</th>
    <th>备注</th>
    <th>最后记账时间</th>
    <th>操作</th>
  </tr>
</thead>
```


