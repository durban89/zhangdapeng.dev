---
title: "Nodejs - 通过身份证号验证年龄，出生日期和性别"
date: "2025-07-03 11:58:22"
slug: "nodejs-tong-guo-shen-fen-zheng-hao-yan-zheng-nian-ling-chu-sheng-ri-qi-he-xing-bie"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-通过身份证号验证年龄，出生日期和性别/"
  - "/2025/07/03/Nodejs-通过身份证号验证年龄，出生日期和性别.html"
  - "/Nodejs-通过身份证号验证年龄，出生日期和性别/"
  - "/Nodejs-通过身份证号验证年龄，出生日期和性别.html"
  - "/2025/07/03/Nodejs-通过身份证号验证年龄-出生日期和性别/"
  - "/2025/07/03/Nodejs-通过身份证号验证年龄-出生日期和性别.html"
  - "/2025/07/03/nodejs-tong-guo-shen-fen-zheng-hao-yan-zheng-nian-ling-chu-sheng-ri-qi-he-xing-bie/"
  - "/2025/07/03/nodejs-tong-guo-shen-fen-zheng-hao-yan-zheng-nian-ling-chu-sheng-ri-qi-he-xing-bie.html"
  - "/nodejs-tong-guo-shen-fen-zheng-hao-yan-zheng-nian-ling-chu-sheng-ri-qi-he-xing-bie.html"
---
想要知道自己的年龄，出生日期和性别，或者是别人的，给我个身份证号，我就可以知道，看下面代码。

```js
static validateIdNumberToAgeYear(str){
  let date = new Date();
  let currentYear = date.getFullYear();
  let currentMonth = date.getMonth() + 1;
  let currentDate = date.getDate();
  
  let idxSexStart = str.length == 18 ? 16 : 14;
  let birthYearSpan = str.length == 18 ? 4 : 2;

  let year;
  let month;
  let day;
  let sex;
  let birthday;
  let age;

  //性别
  let idxSex = 1 - str.substr(idxSexStart, 1) % 2;  
  sex = idxSex == '1' ? '女' : '男';  
  //生日
  year = (birthYearSpan == 2 ? '19' : '') + str.substr(6, birthYearSpan);  
  month = str.substr(6 + birthYearSpan, 2);  
  day = str.substr(8 + birthYearSpan, 2);  
  birthday = year + '-' + month + '-' + day;  
  //年龄
  let monthFloor = (currentMonth < parseInt(month,10) || (currentMonth == parseInt(month,10) && currentDate < parseInt(day,10))) ? 1 : 0;
  age = currentYear - parseInt(year,10) - monthFloor;  

  // console.log("我的出生日期是"+year+"年"+month+"月"+day+"日"+",今年"+age+"岁了"+",性别是"+sex);

  if(age >= 18){
    return true;  
  }
  
  return false;
}
```

我这里只是做了一个年龄的判断。


