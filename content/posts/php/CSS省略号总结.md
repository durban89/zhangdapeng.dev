---
title: "CSS省略号总结"
date: "2025-07-10 11:52:30"
slug: "css-sheng-lve-hao-zong-jie"
categories: ["技术"]
tags: ["CSS", "省略号"]
aliases:
  - "/2025/07/10/CSS省略号总结/"
  - "/2025/07/10/CSS省略号总结.html"
  - "/CSS省略号总结/"
  - "/CSS省略号总结.html"
  - "/2025/07/10/css-sheng-lve-hao-zong-jie/"
  - "/2025/07/10/css-sheng-lve-hao-zong-jie.html"
  - "/css-sheng-lve-hao-zong-jie.html"
---
CSS省略号一直在用，而且用的比较多，这里做下总结，方便日后查用

CSS省略号可以说是前端开发必不可少的。其原理就是将溢出的字符进行覆盖，并通过css的省略号样式表进行填充。

另外的情况可能会用在多行之后添加省略号

参考[这里](https://codepen.io/joelsaupe/pen/ojmLWB?__cf_chl_jschl_tk__=ad2260f8d4282eb686bf94b5680496918201523e-1575267644-0-ATV51Zz3wHoDGlug0fKwsH_7AeJ_jLXzqMBLVtyEOCz0egU2ex35LVMGQdWZG5d_CqXZPP-AheybUivp1kRmEXHN9ZfBMAuivBMYXeocIkJRO0IcrR6sdKWwMkI2A5L5vS9GXi4ruvoZ2yiFb7ljjfslA25u3yKzRgsdcIVBJ2OAOKRqwIUpGEAJQuYC7v3ghGw7pOWk0UhbXUGtC7fodQT4F8WBOdDSAACsAq_b2qpKtx90gfrU9IkTG_QW5-miRvlHkp3eJ1opO4LAD6pGRPlIYI0UDSTzKfrFy99s3MAuTCmIrdSjWlgtoykhN1myCw0cBC3fBzcnfN9QSp56OBxOFW4oiPOtKVqPFC24XJjn)，我这里摘录如下，国内可能有开发者打不开

单行CSS省略号

```css
.ellipsis {
  width: 300px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
```

多行CSS省略号

```css
.block-ellipsis {
  width: 300px;
  display: block;
  display: -webkit-box;
  max-width: 100%;
  height: 43px;
  margin: 0 auto;
  font-size: 14px;
  line-height: 1;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

这里注意下height的值和webkit-line-clamp的值
