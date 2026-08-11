---
title: "HTML5实现浏览器的桌面通知 （兼容性多个浏览器）"
date: "2025-06-30 15:15:32"
slug: "html5-shi-xian-liu-lan-qi-de-zhuo-mian-tong-zhi-jian-rong-xing-duo-ge-liu-lan-qi"
categories: ["技术"]
tags: ["HTML", "桌面通知"]
aliases:
  - "/2025/06/30/HTML5实现浏览器的桌面通知-（兼容性多个浏览器）/"
  - "/2025/06/30/HTML5实现浏览器的桌面通知-（兼容性多个浏览器）.html"
  - "/HTML5实现浏览器的桌面通知-（兼容性多个浏览器）/"
  - "/HTML5实现浏览器的桌面通知-（兼容性多个浏览器）.html"
  - "/2025/06/30/HTML5实现浏览器的桌面通知-兼容性多个浏览器/"
  - "/2025/06/30/HTML5实现浏览器的桌面通知-兼容性多个浏览器.html"
  - "/2025/06/30/html5-shi-xian-liu-lan-qi-de-zhuo-mian-tong-zhi-jian-rong-xing-duo-ge-liu-lan-qi/"
  - "/2025/06/30/html5-shi-xian-liu-lan-qi-de-zhuo-mian-tong-zhi-jian-rong-xing-duo-ge-liu-lan-qi.html"
  - "/html5-shi-xian-liu-lan-qi-de-zhuo-mian-tong-zhi-jian-rong-xing-duo-ge-liu-lan-qi.html"
---
HTML5实现浏览器的桌面通知 （兼容性多个浏览器）

提示：需要在服务器上运行才会有效果，直接运行代码是没有效果的

代码如下：

```js
<script type="text/javascript">
	/*
	 * 桌面通知
	 * strNewsContent:通知的内容
	 */
	function windowsNotify(strNewsContent) {
		if (!("Notification" in window) && !window.webkitNotifications && window.webkitNotifications.checkPermission() != 0)
			return;

		if (Notification.permission == null || Notification.permission == undefined)
			windowsNotify360(strNewsContent);
		else if (Notification.permission === "granted")
			windowsNotifyFFAndGE(strNewsContent);
		else if (Notification.permission !== 'denied') {
			Notification.requestPermission(function (permission) {
				if (!('permission' in Notification))
					Notification.permission = permission;

				if (permission === "granted")
					windowsNotifyFFAndGE(strNewsContent);
			});
		}
	}

	//桌面通知(兼容360)
	function windowsNotify360(strNewsContent) {
		if (window.webkitNotifications && window.webkitNotifications.checkPermission() == 0) {
			var notify = window.webkitNotifications.createNotification(
			    "http://www.fx678.com/corp/images/aboutus/htw.jpg",
		            '汇通-新闻中心',
			    strNewsContent
		    );

			//设置定时撤销机制，防止通知长时间显示不被关闭
			notify.ondisplay = function (event) {
				setTimeout(function () {
					event.currentTarget.cancel();
				}, 10000);
			};
			//下面是定义点击事件，类似地还可定义其它事件
			notify.onclick = function () {
				window.focus();
				this.cancel();
			};
			//弹出
			notify.show();
		} else if (window.webkitNotifications) {
			window.webkitNotifications.requestPermission(windowsNotify360);
		}
	}


	//桌面通知(兼容火狐、谷歌)
	function windowsNotifyFFAndGE(strNewsContent) {
		var notification = new Notification('汇通-新闻中心',
							 {
							 	body: strNewsContent,
							 	icon: "http://www.fx678.com/corp/images/aboutus/htw.jpg"
							 });

		//设置定时撤销机制，防止通知长时间显示不被关闭
		notification.ondisplay = function (event) {
			setTimeout(function () {
				event.currentTarget.cancel();
			}, 10000);
		};

		//下面是定义点击事件，类似地还可定义其它事件
		notification.onclick = function () {
			window.focus();
			this.cancel();
		};
		console.log(notification);
	}
	windowsNotify('asdsd');

</script>
```


