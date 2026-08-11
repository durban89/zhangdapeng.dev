---
title: "QQ邮箱这里有破解，Nodejs实现"
date: "2025-06-30 14:31:32"
slug: "qq-you-xiang-zhe-li-you-po-jie-nodejs-shi-xian"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/QQ邮箱这里有破解，Nodejs实现/"
  - "/2025/06/30/QQ邮箱这里有破解，Nodejs实现.html"
  - "/QQ邮箱这里有破解，Nodejs实现/"
  - "/QQ邮箱这里有破解，Nodejs实现.html"
  - "/2025/06/30/QQ邮箱这里有破解-Nodejs实现/"
  - "/2025/06/30/QQ邮箱这里有破解-Nodejs实现.html"
  - "/2025/06/30/qq-you-xiang-zhe-li-you-po-jie-nodejs-shi-xian/"
  - "/2025/06/30/qq-you-xiang-zhe-li-you-po-jie-nodejs-shi-xian.html"
  - "/qq-you-xiang-zhe-li-you-po-jie-nodejs-shi-xian.html"
---
QQ邮箱这里有破解了，只是有几个参数，需要你们自己去寻找了，反正我是找好了，就看你们了。

```js
co(function *(){

  var username = '';
  var password = '';
  var _user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36';
  var ptlogin_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=522005705&daid=4&s_url=https://mail.qq.com/cgi-bin/login?vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&';
  var _verifycode = '!IDB';
  var _pt_verifysession_v1 = '5351f6252b2eb7cd2025d8cef4025f3df8514932545b755fdd2bdb5b10d7008ef6b8f42d5f05e44679d09b4515c1d08f682e0330446f702a';
  var _salt = '\x00\x00\x00\x00\x35\x6d\x62\x13';
  try{
    var _p = Encryption.getEncryption(password, _salt, _verifycode, false);
  }catch(err){
    console.log(err.stack);
  }  
  var _login_sig = 'k1j0ogiCLp94MhQuiqFe0aONqYTewoEAWOVK0yRhXiYZ76YjWOLCwCq1AbgbZlz7';

  //登录提交
  var login_url = 'https://ssl.ptlogin2.qq.com/login';
  var login_data = {
    'u':username,
    'verifycode':_verifycode,
    'pt_vcode_v1':0,
    'pt_verifysession_v1':_pt_verifysession_v1,
    'p':_p,
    'pt_randsalt':0,
    'u1':'https://mail.qq.com/cgi-bin/login?vt=passport&vm=wpt&ft=loginpage&target=&account='+username,
    'ptredirect':1,
    'h':1,
    't':1,
    'g':1,
    'from_ui':1,
    'ptlang':'2052',
    'action':'2-3-1432202218068',
    'js_ver':10123,
    'js_type':1,
    'login_sig':_login_sig,
    'pt_uistyle':25,
    'aid':'522005705',
    'daid':4
  };
  login_url = [login_url,queryString.encode(login_data)].join('?');

  try{
    var res = yield request(login_url,{
      method:'GET',
      headers:{
        'Cookie':'dm_login_weixin_rem=; supertoken=3636424164; ptnick_896360979=e68891e79a84e79b8ae8bebe; u_896360979=@EcEWDEtFk:1432212547:1432212547:e68891e79a84e79b8ae8bebe:1; ptcz=6a74b6275a1dbd3a69b6c3ec83088687dcba3c9669af0b6f6bb658ab3b9b151f; pt2gguin=o0896360979; verifysession=h02OBge6wAzGGePYJ7IwDe7G4vsez16cqYqz0LB0w10HLt2JHNAnoqc-ebhwuZSPznSe7GvKEeJztuJhdD1EPPw9rpFU4Q_j7PS; ptui_loginuin=896360979; ETK=j4KdeJfjqM6ytLCbmoD9MUXVRZSffwLcVz8mvfIpmYxfl-514g-Arqm-RDDO-b92avzT*JKE7AQibxTRZGDl*g__; ptisp=ctc; confirmuin=0; ptvfsession='+_pt_verifysession_v1+'; pt_login_sig='+_login_sig+'; pt_clientip=29587f0000012d41; pt_serverip=b6a20abf06626dff; pt_local_token=176655876; uikey=bc5ce4f96fa16f2d0e69733d6a4128b2de3662b28623eb39db9f65dde69b75bd',
        'Referer':ptlogin_url,
        'Host':'ssl.ptlogin2.qq.com',
        'User-Agent':_user_agent
      }
    });
    console.log(res[0].toString());
  }catch(err){
    console.log(err.stack);
  }
});
```

对了，这里是用来co，是JavaScript的一个新特性，我还是很喜欢的，更喜欢yield，node执行的时候别忘记加--harmony，不然你会说我的，说执行不了。


