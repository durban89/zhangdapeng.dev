---
title: "Android使用Intent传递数据的方式"
date: "2025-07-03 11:58:47"
slug: "android-shi-yong-intent-chuan-di-shu-ju-de-fang-shi"
categories: ["技术"]
tags: ["Android"]
aliases:
  - "/2025/07/03/Android使用Intent传递数据的方式/"
  - "/2025/07/03/Android使用Intent传递数据的方式.html"
  - "/Android使用Intent传递数据的方式/"
  - "/Android使用Intent传递数据的方式.html"
  - "/2025/07/03/android-shi-yong-intent-chuan-di-shu-ju-de-fang-shi/"
  - "/2025/07/03/android-shi-yong-intent-chuan-di-shu-ju-de-fang-shi.html"
  - "/android-shi-yong-intent-chuan-di-shu-ju-de-fang-shi.html"
---
**第一种，直接使用Intent去传递数据**

```java
//传递数据
Intent intent = new Intent(MainActivity.this, OtherActivity.class);
intent.putExtra("key","value");
startActivity(intent);
//接收数据
Intent intent = getIntent();
String name = intent.getStringExtra("key");
```

**第二种，使用Application/全局变量传递传递数据**

创建一个Application的类

```java
public class MyApp extends Application {
    public String name;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    @Override
    public void onCreate() {
        super.onCreate();
        setName("maomao");
    }
}
//使用并定义myApp;
private MyApp myApp;
//实例化Application，并传递数据
myApp = (MyApp)getApplication();
myApp.setName("maomaomao");
Intent intent = new Intent(MainActivity.this, ShowNameActivity.class);
startActivity(intent);
//接收数据
private MyApp myApp;
myApp = (MyApp) getApplication();
String name = myApp.getName();
```

- 这种方式千万别忘记要配置一下AndroidManifest.xml这个文件

在application 添加

```java
android:name=".MyApp"
```

这里的MyApp 就是上面定义的

**第三种，使用剪切板传递数据**

```java
//传递数据
ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
clipboardManager.setText(name);
Intent intent = new Intent(MainActivity.this, ShowNameActivity.class);
startActivity(intent);
```

//接收数据

```java
ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
String name = clipboardManager.getText();
```

也可以使用剪切板的方式传递对象

```java
//创建对象MyData
public class MyData implements Serializable {
    private int age;
    private String name;
    public MyData(String name, int age){
        super();
        this.name = name;
        this.age = age;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        return "MyData{" +
                "age=" + age +
                ", name='" + name + '\'' +
                '}';
    }
}
//对象方式传数据
MyData myData = new MyData("mao", 23);
//将对象转为字符串
ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
String base64String = "";
try {
    ObjectOutputStream objectOutputStream = new ObjectOutputStream(byteArrayOutputStream);
    objectOutputStream.writeObject(myData);
    base64String = Base64.encodeToString(byteArrayOutputStream.toByteArray(), Base64.DEFAULT);
    objectOutputStream.close();
} catch (Exception e) {
}
clipboardManager.setText(base64String);
Intent intent = new Intent(MainActivity.this, ShowNameActivity.class);
startActivity(intent);
//接收对象数据
ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
String msg = clipboardManager.getText().toString();
byte[] base64Bype = Base64.decode(msg, Base64.DEFAULT);
ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(base64Bype);
try{
    ObjectInputStream objectInputStream = new ObjectInputStream(byteArrayInputStream);
    MyData myData = (MyData) objectInputStream.readObject();
    String str = myData.toString();
}catch (Exception e){
}
```

**第四种，直接使用静态变量传递数据**

这种方式需要在接收数据的Activity中定义自己的属性变量

```java
//定义变量
public static int age;
public static String name;
//传递数据
Intent intent = new Intent();
intent.setClass(MainActivity.this, ShowNameActivity.class);
ShowNameActivity.name = "maomaomaomao";
ShowNameActivity.age = 90;
startActivity(intent);
//接收数据-直接使用变量的数据就好了
Log.in("name >>>" + name + " age>>>" + age);
```


