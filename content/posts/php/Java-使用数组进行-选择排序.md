---
title: "Java 使用数组进行 选择排序"
date: "2025-06-26 14:55:19"
slug: "java-shi-yong-shu-zu-jin-xing-xuan-ze-pai-xu"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/26/Java-使用数组进行-选择排序/"
  - "/2025/06/26/Java-使用数组进行-选择排序.html"
  - "/Java-使用数组进行-选择排序/"
  - "/Java-使用数组进行-选择排序.html"
  - "/2025/06/26/java-shi-yong-shu-zu-jin-xing-xuan-ze-pai-xu/"
  - "/2025/06/26/java-shi-yong-shu-zu-jin-xing-xuan-ze-pai-xu.html"
  - "/java-shi-yong-shu-zu-jin-xing-xuan-ze-pai-xu.html"
---
Java 使用数组进行 选择排序，简单的实现过程是这样子的

```java
public class SelectionSort {
	public static void main (String[] args){
		int[] intArray = {12,11,45,6,8,43,40,57,3,20};
		int keyValue;
		int index;
		int temp;
		System.out.println("排序前的数组");
		for(int i=0; i<intArray.length;i++){
			System.out.print(intArray[i]+" ");
		}
		System.out.println();
		for(int i=0; i < intArray.length; i++){
			index = i;
			keyValue = intArray[i];
			for(int j=i;j<intArray.length;j++){
				if(intArray[j] < keyValue){
					index = j;
					keyValue = intArray[j];
				}
			}
			temp = intArray[i];
			intArray[i] = intArray[index];
			intArray[index] = temp;
		}
		System.out.println("排序后的数组");
		for(int i=0; i<intArray.length;i++){
			System.out.print(intArray[i]+" ");
		}
		System.out.println();
	}
}
```

得到的结果是

```
排序前的数组
12 11 45 6 8 43 40 57 3 20 
排序后的数组
3 6 8 11 12 20 40 43 45 57
```

嗯，是这个样子的，

选择排序的特点就是：

效率低，但是实现很简单。

