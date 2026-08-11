---
title: "Android中给按钮添加onClick的操作事件"
date: "2025-07-03 11:58:34"
slug: "android-zhong-gei-an-niu-tian-jia-onclick-de-cao-zuo-shi-jian"
categories: ["技术"]
tags: ["Android"]
aliases:
  - "/2025/07/03/Android中给按钮添加onClick的操作事件/"
  - "/2025/07/03/Android中给按钮添加onClick的操作事件.html"
  - "/Android中给按钮添加onClick的操作事件/"
  - "/Android中给按钮添加onClick的操作事件.html"
  - "/2025/07/03/android-zhong-gei-an-niu-tian-jia-onclick-de-cao-zuo-shi-jian/"
  - "/2025/07/03/android-zhong-gei-an-niu-tian-jia-onclick-de-cao-zuo-shi-jian.html"
  - "/android-zhong-gei-an-niu-tian-jia-onclick-de-cao-zuo-shi-jian.html"
---
```java
//第一步：声明一个button
private Button button;
//实例化这个button
button = (Button) this.findViewById(R.id.button);
//给这个button添加onclick事件
button.setOnclickListener(new View.OnClickListener(){
	@Override
	public void onClick(View view){
		Intent intent = new Intent(MainActivity.this, OtherActivity.class);
		intent.putExtra("key","value");
		startActivity(intent);
	}
})
```


