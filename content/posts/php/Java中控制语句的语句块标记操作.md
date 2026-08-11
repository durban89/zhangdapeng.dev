---
title: "Java中控制语句的语句块标记操作"
date: "2025-06-25 10:09:55"
slug: "java-zhong-kong-zhi-yu-ju-de-yu-ju-kuai-biao-ji-cao-zuo"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/25/Java中控制语句的语句块标记操作/"
  - "/2025/06/25/Java中控制语句的语句块标记操作.html"
  - "/Java中控制语句的语句块标记操作/"
  - "/Java中控制语句的语句块标记操作.html"
  - "/2025/06/25/java-zhong-kong-zhi-yu-ju-de-yu-ju-kuai-biao-ji-cao-zuo/"
  - "/2025/06/25/java-zhong-kong-zhi-yu-ju-de-yu-ju-kuai-biao-ji-cao-zuo.html"
  - "/java-zhong-kong-zhi-yu-ju-de-yu-ju-kuai-biao-ji-cao-zuo.html"
---
与break有关的语句块标记操作

第一个示例：

```java
//语句块标记
public class Demo12 {
	public static void main(String args[]){
		first:{
			second:{
				third:{
					for(int i = 0;i < 3;i++){
						System.out.println("third:" + i);
						if(i == 2){
							break second;
						}
					}
				}
				//该语句永远不会被执行
				System.out.println("在second语句块中");
			}
			System.out.println("在first语句块中");
		}
	}
}
```

第二个示例：

```java
//带标记的语句块
//break 退出到语句块
public class Demo13 {
	public static void main(String args[]){
		out:{
			for(int i = 0;i < 20;i++){
				System.out.println("外循环"+i);
				for(int j = 0;j < 20;j++){
					System.out.println("内循环"+j);
					if(j == 10){
						break out;
					}
				}
			}
		}
	}
}
```

与continue有关的语句块标记操作

第一个示例：

```java
//continue操作语句块的标记
public class Demo15 {
	public static void main(String args[]){
		out:for(int i = 0; i<10;i++){
				for(int j = 0;i<10;j++){
					if(j>=i){
						System.out.println("");
						continue out;
					}else{
						System.out.println("i = "+i+" j = " + j);
					}
				}
			}
		
	}
}
```

