---
title: "JavaScript 实现Copy动作"
date: "2025-06-27 10:59:46"
slug: "javascript-shi-xian-copy-dong-zuo"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/JavaScript-实现Copy动作/"
  - "/2025/06/27/JavaScript-实现Copy动作.html"
  - "/JavaScript-实现Copy动作/"
  - "/JavaScript-实现Copy动作.html"
  - "/2025/06/27/javascript-shi-xian-copy-dong-zuo/"
  - "/2025/06/27/javascript-shi-xian-copy-dong-zuo.html"
  - "/javascript-shi-xian-copy-dong-zuo.html"
---
1. 实现点击按钮，复制文本框中的的内容

```html
<script type="text/javascript">
function copyUrl2()
{
   var Url2=document.getElementById("biao1");
   Url2.select(); // 选择对象
   document.execCommand("Copy"); // 执行浏览器复制命令
   alert("已复制好，可贴粘。");
}
</script>
<textarea cols="20" rows="10" id="biao1">用户定义的代码区域</textarea>
<input type="button" onClick="copyUrl2()" value="点击复制代码" />
```
2. 复制专题地址和 url 地址，传给 QQ/MSN 上的好友

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
   <title>Js复制代码</title>
</head>
<body>
   <p>
      <input type="button" name="anniu1" onClick='copyToClipBoard()' value="复制专题地址和url地址，传给QQ/MSN上的好友">
      <script language="javascript">
      function copyToClipBoard(){
         var clipBoardContent="";
         clipBoardContent+=document.title;
         clipBoardContent+="";
         clipBoardContent+=this.location.href;
         window.clipboardData.setData("Text",clipBoardContent);
         alert("复制成功，请粘贴到你的QQ/MSN上推荐给你的好友");
      }
      </script>
   </p>
</body>
```
3. 直接复制 url

```html
<input type="button" name="anniu2" onClick='copyUrl()' value="复制URL地址">
<script language="javascript">
function copyUrl()
{
   var clipBoardContent=this.location.href;
   window.clipboardData.setData("Text",clipBoardContent);
   alert("复制成功!");
}
</script>
```
4. 点击文本框时，复制文本框里面的内容

```html
<input onclick="oCopy(this)" value="你好.要copy的内容!">
<script language="javascript">
function oCopy(obj){
   obj.select();
   js=obj.createTextRange();
   js.execCommand("Copy")
   alert("复制成功!");
}
</script>
```
5. 复制文本框或者隐藏域中的内容

```html
<script language="javascript">
function CopyUrl(target){
   target.value=myimg.value;
   target.select();  
   js=myimg.createTextRange();  
   js.execCommand("Copy");
   alert("复制成功!");
}
function AddImg(target){
   target.value="[IMG]"+myimg.value+"[/ img]";
   target.select();
   js=target.createTextRange();  
   js.execCommand("Copy");
   alert("复制成功!");
}
</script>
```
6. 复制 span 标记中的内容

```html
<script type="text/javascript">
function copyText(obj)  
{
   var rng = document.body.createTextRange();
   rng.moveToElementText(obj);
   rng.scrollIntoView();
   rng.select();
   rng.execCommand("Copy");
   rng.collapse(false);
   alert("复制成功!");
}
</script>
```
7. 浏览器兼容  copyToClipboard("拷贝内容")

```js
function copyToClipboard(txt) {
   if (window.clipboardData) {
       window.clipboardData.clearData();
       clipboardData.setData("Text", txt);
       alert("复制成功！");

   } else if (navigator.userAgent.indexOf("Opera") != -1) {
       window.location = txt;
   } else if (window.netscape) {
       try {
           netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
       } catch (e) {
           alert("被浏览器拒绝！\n请在浏览器地址栏输入'about:config'并回车\n然后将 'signed.applets.codebase_principal_support'设置为'true'");
       }
       var clip = Components.classes['@mozilla.org/widget/clipboard;1'].createInstance(Components.interfaces.nsIClipboard);
       if (!clip)
           return;
       var trans = Components.classes['@mozilla.org/widget/transferable;1'].createInstance(Components.interfaces.nsITransferable);
       if (!trans)
           return;
       trans.addDataFlavor("text/unicode");
       var str = new Object();
       var len = new Object();
       var str = Components.classes["@mozilla.org/supports-string;1"].createInstance(Components.interfaces.nsISupportsString);
       var copytext = txt;
       str.data = copytext;
       trans.setTransferData("text/unicode", str, copytext.length * 2);
       var clipid = Components.interfaces.nsIClipboard;
       if (!clip)
           return false;
       clip.setData(trans, null, clipid.kGlobalClipboard);
       alert("复制成功！");
   }
}
```

参考地址：

http://www.cnblogs.com/athens/archive/2013/01/16/2862981.html

