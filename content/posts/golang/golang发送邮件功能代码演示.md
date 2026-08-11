---
title: "golang发送邮件功能代码演示"
date: "2025-08-05 09:48:55"
slug: "golang-fa-song-you-jian-gong-neng-dai-ma-yan-shi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/golang发送邮件功能代码演示/"
  - "/2025/08/05/golang发送邮件功能代码演示.html"
  - "/golang发送邮件功能代码演示/"
  - "/golang发送邮件功能代码演示.html"
  - "/2025/08/05/golang-fa-song-you-jian-gong-neng-dai-ma-yan-shi/"
  - "/2025/08/05/golang-fa-song-you-jian-gong-neng-dai-ma-yan-shi.html"
  - "/golang-fa-song-you-jian-gong-neng-dai-ma-yan-shi.html"
---
```go
import (
	"xxxx/config"
	"github.com/jordan-wright/email"
	"log"
	"net/smtp"
)

// Send smtp send
func Send(senderTitle, mailTo, mailToSubj string, text, html []byte) error {

	emailHost := config.EmailSmtpHost
	emailPort := config.EmailSmtpPort
	emailUser := config.EmailSmtpUsername
	emailAuthPassword := config.EmailSmtpPassword

	//fmt.Printf("emailHost = %s emailPort = %s emailUser = %s emailAuthPassword = %s", emailHost, emailPort, emailUser, emailAuthPassword)

	e := email.NewEmail()
	e.From = senderTitle + " <" + emailUser + ">"
	e.To = []string{mailTo}
	e.Bcc = []string{mailTo}
	e.Cc = []string{mailTo}
	e.Subject = mailToSubj
	e.Text = text //[]byte("Text Body is, of course, supported!")
	e.HTML = html // []byte("<h1>Fancy HTML is supported, too!</h1>")
	err := e.Send(emailHost+":"+emailPort, smtp.PlainAuth("", emailUser, emailAuthPassword, emailHost))

	if err != nil {
		log.Panic(err)

		return err
	}

	return nil
}
```

使用的是github.com/jordan-wright/email

这个比较好用，效果见效快
