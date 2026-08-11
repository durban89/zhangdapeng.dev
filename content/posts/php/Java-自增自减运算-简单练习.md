---
title: "Java 自增自减运算 简单练习"
date: "2025-06-24 16:17:35"
slug: "java-zi-zeng-zi-jian-yun-suan-jian-dan-lian-xi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/24/Java-自增自减运算-简单练习/"
  - "/2025/06/24/Java-自增自减运算-简单练习.html"
  - "/Java-自增自减运算-简单练习/"
  - "/Java-自增自减运算-简单练习.html"
  - "/2025/06/24/java-zi-zeng-zi-jian-yun-suan-jian-dan-lian-xi/"
  - "/2025/06/24/java-zi-zeng-zi-jian-yun-suan-jian-dan-lian-xi.html"
  - "/java-zi-zeng-zi-jian-yun-suan-jian-dan-lian-xi.html"
---
### [练习一](#1)

```java
public class ZiZengJian{
	public static void main(String args[]){
		int a = 3;
		int b = ++a;
		int c = 3;
		int d = --c;
		System.out.println("进行自增运算后的值等于:"+b);
		System.out.println("进行自减运算后的值等于:"+d);
			
	}
}
```

gowhich得到的结果是：

```bash
进行自增运算后的值等于:4
进行自减运算后的值等于:2
```

### [练习二](#2)

```java
public class ZiZengJian1{
	public static void main(String args[]){
		byte b1 = 5;
		byte b2 = (byte)(b1 + 1);
		System.out.println("使用加运算符的结果是:"+b2);
		byte b3 = 5;
		byte b4 = ++b3;
		System.out.println("使用自增运算符的结果是:"+b4); 
	}
}
```

gowhich得到的结果是：

```bash
使用加运算符的结果是:6
使用自增运算符的结果是:6
```

### [练习三](#3)

```java
public class ZiZengJian2{
	public static void main(String args[]){
		int a = 5;
		int b = 5;
		int x = 2 * ++a;
		int y = 2 * b++;
		System.out.println("自增运算符前缀运算后 a="+a+"表达式x="+x);
		System.out.println("自增运算符后缀运算后 b="+b+"表达式y="+y);
		
	}
}
```

gowhich得到的结果是：

```bash
自增运算符前缀运算后 a=6表达式x=12
自增运算符后缀运算后 b=6表达式y=10
```

