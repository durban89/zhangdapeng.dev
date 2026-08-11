---
title: "Nodejs 破解 不规范json字符串的处理方法"
date: "2025-07-01 11:35:53"
slug: "nodejs-po-jie-bu-gui-fan-json-zi-fu-chuan-de-chu-li-fang-fa"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/01/Nodejs-破解-不规范json字符串的处理方法/"
  - "/2025/07/01/Nodejs-破解-不规范json字符串的处理方法.html"
  - "/Nodejs-破解-不规范json字符串的处理方法/"
  - "/Nodejs-破解-不规范json字符串的处理方法.html"
  - "/2025/07/01/nodejs-po-jie-bu-gui-fan-json-zi-fu-chuan-de-chu-li-fang-fa/"
  - "/2025/07/01/nodejs-po-jie-bu-gui-fan-json-zi-fu-chuan-de-chu-li-fang-fa.html"
  - "/nodejs-po-jie-bu-gui-fan-json-zi-fu-chuan-de-chu-li-fang-fa.html"
---
Json字符串如果不是很规范的话,使用nodejs的JSON方法是无法 进行parse的,比如说下面这段代码:

```bash
{'code':'S_OK','result':[0,0,0,0,0],'sessionCount':85,'var':[
{
'mid':'3a010000d4eede56800000b5',
'fid':1,'mailSession':149,
'size':15074,
'sendDate':1433473712,
'receiveDate':1433473712,
'modifyDate':1434356744,
'taskDate':0,
'securityLevel':0,
'meetingFlag':0,
'priority':3,
'color':0,
'antivirusStatus':0,
'rcptFlag':1,
'attachmentNum':0,
'mailNum':1,
'keepDay':0,
'sendId':0,
'sendTotalNum':0,
'sendNewNum':0,
'mailFlag':5,'starType':0,'logoType':68,'denyForward':0, 'auditStatus':0, 'billType':0,'billFlag':0,'subscriptionFlag':0,'secureEncrypt':0,'secureSigned':0,
'flags':{'successed':1,'selfdestruct':1},
'label':[],
'from':'中国移动139邮箱<xx@xx.com>',
'to':'xx@xx.com',
'subject':'邮箱积分新用途？一起积分初体验',
'summary':'邮箱积分新用途知道自己的邮箱积分吗？ 其实你已拥有诸多财富！想了解积分的用途吗？很多人早把积分'},
....... //这里省略了上下类似的代码
{
'mid':'1d0b257e9c2ec6b800000001',
'fid':1,
'mailSession':123,
'size':25633,
'sendDate':1424588244,
'receiveDate':1424588244,
'modifyDate':1433248644,
'taskDate':0,
'securityLevel':0,
'meetingFlag':0,
'priority':3,
'color':0,
'antivirusStatus':0,
'rcptFlag':1,
'attachmentNum':0,
'mailNum':1,
'keepDay':0,
'sendId':0,
'sendTotalNum':0,
'sendNewNum':0,
'mailFlag':5,'starType':0,'logoType':1,'denyForward':0, 'auditStatus':0, 'billType':0,'billFlag':0,'subscriptionFlag':0,'secureEncrypt':0,'secureSigned':0,
'flags':{'successed':1,'selfdestruct':1},
'label':[],
'from':'中国移动<xx@xx>',
'to':'xx@xx',
'subject':'尊敬的客户，您截至2月15日的积分账单已到，请查阅：巧用积分兑换好礼',
'summary':'用户号码：15000711265，尊敬的动感地带（M-Zone）客户：\r截止2月15日您的可兑换积分为：1074\r特别说明：\r1.'}
]
}
```

你可以将此n字符串放到文件内,多复制几个,然后通过JSON的方法试试.

首先肯定要进行读取文件

`fs.readFile`

然后将u读进来的Buffer字节码解析为字符串

`buf.toString()`

下面得到的就是字符串了,试试吧

`JSON.stringify()`

`JSON.parse()`

这两个方法随便搭配.最终还是无解,解析出来的仍然不是你要的对象.

.......................

好吧,如果到了这里,我就只能说,别啥了,获得字符串之后,直接eval吧,哎,笨

```js
json_obj = eval("(" + json_string + ")");
```

可以打印debug(json_obj),试试吧,应该可以不让你那么郁闷了.


