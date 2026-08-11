---
title: "Java简单的浮点数练习"
date: "2025-06-24 15:29:53"
slug: "java-jian-dan-de-fu-dian-shu-lian-xi"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/24/Java简单的浮点数练习/"
  - "/2025/06/24/Java简单的浮点数练习.html"
  - "/Java简单的浮点数练习/"
  - "/Java简单的浮点数练习.html"
  - "/2025/06/24/java-jian-dan-de-fu-dian-shu-lian-xi/"
  - "/2025/06/24/java-jian-dan-de-fu-dian-shu-lian-xi.html"
  - "/java-jian-dan-de-fu-dian-shu-lian-xi.html"
---
```java
public class FuDian {
	public static void main(String args[]){
		float f = 1.23f;
		double d1 = 1.23;
		double d2 = 1.23D;
		System.out.println("单精度浮点类型数值等于"+f);
		System.out.println("双精度浮点类型数值等于"+d1);
		System.out.println("双精度浮点类型数值等于"+d2);
	}
}
```

输出结果是：

```bash
单精度浮点类型数值等于1.23
双精度浮点类型数值等于1.23
双精度浮点类型数值等于1.23
```

