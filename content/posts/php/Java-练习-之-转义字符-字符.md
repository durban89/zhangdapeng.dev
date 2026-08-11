---
title: "Java 练习 之 转义字符 字符"
date: "2025-06-24 15:30:07"
slug: "java-lian-xi-zhi-zhuan-yi-zi-fu-zi-fu"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/24/Java-练习-之-转义字符-字符/"
  - "/2025/06/24/Java-练习-之-转义字符-字符.html"
  - "/Java-练习-之-转义字符-字符/"
  - "/Java-练习-之-转义字符-字符.html"
  - "/2025/06/24/java-lian-xi-zhi-zhuan-yi-zi-fu-zi-fu/"
  - "/2025/06/24/java-lian-xi-zhi-zhuan-yi-zi-fu-zi-fu.html"
  - "/java-lian-xi-zhi-zhuan-yi-zi-fu-zi-fu.html"
---
### [简单的字符处理](#0)

```java
public class ZiFu {
	public static void main(String args[]){
		char a = 'A';
		char b = '\u003a';
		System.out.println("第一个字符类型的值等于"+a);
		System.out.println("第二个字符类型的指等于"+b);
	}
}
```

gowhich得到的结果是：

```bash
第一个字符类型的值等于A
第二个字符类型的指等于:
```

### [做个小小实例](#1)

计算圆的面积：

```java
public class YuanMianJi {
	public static void main(String args[]){
		final double PI = 3.14;
		int R = 5;
		double ymj = PI * R * R;
		System.out.println("圆的面积等于"+ymj);
	}

}
```

得到的结果是:

```bash
圆的面积等于78.5
```

### [转义字符的处理](#2)

```java
public class ZhuanYiZiFu {
	public static void main(String args[]){
		System.out.println("Hello \n World");
		System.out.println("Hello \\n Word");
	}
}
```

得到的结果是：

```bash
Hello 
 World
Hello \n Word
```

