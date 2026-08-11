---
title: "webapp端完美实现字符截取"
date: "2025-07-14 14:44:46"
slug: "webapp-duan-wan-mei-shi-xian-zi-fu-jie-qu"
categories: ["技术"]
tags: ["H5"]
aliases:
  - "/2025/07/14/webapp端完美实现字符截取/"
  - "/2025/07/14/webapp端完美实现字符截取.html"
  - "/webapp端完美实现字符截取/"
  - "/webapp端完美实现字符截取.html"
  - "/2025/07/14/webapp-duan-wan-mei-shi-xian-zi-fu-jie-qu/"
  - "/2025/07/14/webapp-duan-wan-mei-shi-xian-zi-fu-jie-qu.html"
  - "/webapp-duan-wan-mei-shi-xian-zi-fu-jie-qu.html"
---
webapp端如何完美实现字符截取，常用的方式我们知道有substr，但是这种方式如果用在多种语言的情况下可能会有问题

比如英文字母和中文汉子混在一起的话，截取指定长度的字符串就有点困难了

下面是我实战中用到的

```javascript
function getByteByBinary(binaryCode) {
  /*
    二进制 Binary system,es6表示时以0b开头
    八进制 Octal number system,es5表示时以0开头,es6表示时以0o开头
    十进制 Decimal system
    十六进制 Hexadecimal,es5、es6表示时以0x开头
   */

  var byteLengthDatas = [0, 1, 2, 3, 4];
  var len = byteLengthDatas[Math.ceil(binaryCode.length / 8)];
  return len;
}

function getByteByHex(hexCode) {
  return getByteByBinary(parseInt(hexCode, 16).toString(2));
}
```

获取字符串长度函数

```javascript
function getByteLength(str) {
  var result = "";
  var flag = false;
  var len = 0;
  var length = 0;
  var length2 = 0;
  for (var i = 0; i < str.length; i++) {
    var code = str.codePointAt(i).toString(16);
    if (code.length > 4) {
      i++;
      if ((i + 1) < str.length) {
        flag = str.codePointAt(i + 1).toString(16) == "200d";
      }
    }

    if (flag) {
      len += getByteByHex(code);
      if (i == str.length - 1) {
        length += len;
      }
    } else {
      if (len != 0) {
        length += len;
        length += getByteByHex(code);
        len = 0;
        continue;
      }
      length += getByteByHex(code);
    }
  }
  return length;
}
```

经过上面几个函数的准备，下面这个函数，就完美实现了截取字符串长度的功能

```javascript
function substringByByte(str, maxLength) {
  var result = "";
  var flag = false;
  var len = 0;
  var length = 0;
  var length2 = 0;
  for (var i = 0; i < str.length; i++) {
    var code = str.codePointAt(i).toString(16);
    if (code.length > 4) {
      i++;
      if ((i + 1) < str.length) {
        flag = str.codePointAt(i + 1).toString(16) == "200d";
      }
    }
    if (flag) {
      len += getByteByHex(code);
      if (i == str.length - 1) {
        length += len;
        if (length <= maxLength) {
          result += str.substr(length2, i - length2 + 1);
        } else {
          break
        }
      }
    } else {
      if (len != 0) {
        length += len;
        length += getByteByHex(code);
        if (length <= maxLength) {
          result += str.substr(length2, i - length2 + 1);
          length2 = i + 1;
        } else {
          break
        }
        len = 0;
        continue;
      }
      length += getByteByHex(code);
      if (length <= maxLength) {
        if (code.length <= 4) {
          result += str[i]
        } else {
          result += str[i - 1] + str[i]
        }
        length2 = i + 1;
      } else {
        break
      }
    }
  }
  return result;
}
```
