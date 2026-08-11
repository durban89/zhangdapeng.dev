---
title: "Proxy Firefox through a SSH tunnel"
date: "2025-07-01 11:54:31"
slug: "proxy-firefox-through-a-ssh-tunnel"
categories: ["技术"]
tags: ["Proxy", "SSH"]
aliases:
  - "/2025/07/01/Proxy-Firefox-through-a-SSH-tunnel/"
  - "/2025/07/01/Proxy-Firefox-through-a-SSH-tunnel.html"
  - "/Proxy-Firefox-through-a-SSH-tunnel/"
  - "/Proxy-Firefox-through-a-SSH-tunnel.html"
  - "/2025/07/01/proxy-firefox-through-a-ssh-tunnel/"
  - "/2025/07/01/proxy-firefox-through-a-ssh-tunnel.html"
  - "/proxy-firefox-through-a-ssh-tunnel.html"
---
**a fast, privately secured tunnel to transfer web pages and dns queries**

Have you ever wanted to visit sites during the day from a location that denied access to those sites? Perhaps the company has denied access due to bandwidth considerations or you might have decided that the site you want to go to might not always be work safe depending on the story or pictures? What you need is the ability to create a secure and encrypted ssh connection to tunnel your browser traffic through.

Using a ssh tunnel to retrieve the data from websites is significantly faster than trying to use X forwarding to open a remote copy of Firefox on the remote machine. If a remote browser is used the connection will be saturated by the graphical front end of the remote browser window. Use the tunnel for the web site's data and leave the rendering of the browser to the local machine. This is the most efficient solution.

If you have access to a remote machine by way of ssh you can set up Firefox, or any other SOCKS v5 enabled application, to tunnel its connection through ssh. This way, if you were at work and wanted to browse your favorite sites like MySpace, Facebook or Maxim that are blocked at the company firewall you could.

Getting Started

First you must have ssh access to the remote machine you want to proxy to. Let it be a home machine or a free shell you signed up for on-line. You must also make sure you can ssh from where your browser is to where you want to tunnel to. No need to set this up if port 22 is not open to you from your location to your destination.

ATTENTION: We are proud to announce our Firefox add-on called, "Calomel SSL Validation". It will grade the security of your SSL connection. The link has screen shots too!

IMPORTANT NOTE: The Firefox tunnel using SOCKS5 (option 1) is the easiest and quickest proxy to setup. If you just want to get the proxy working then follow the SOCKS5 options.

Configure Firefox for the proxy

You need to configure Firefox to use the proxy. Find the section to add a proxy to the browser. On \*nix systems of Firefox you will find the settings in File, Preferences, Advanced, Network, Settings. The setting by default is "Direct Connection to the Internet". We need to setup the "Manual proxy configuration".

You have two(2) options to pick from. You can proxy directly to the remote machine and then connect directly to web sites. This is the SOCKS5 method and is the easiest to setup. Or, you could use a Squid web proxy (if available) on the remote machine to accept the traffic from the ssh tunnel. Squid would then request the traffic from web sites. Pick one of the options below.

NOTE: For our example, ssh is going to listen on localhost (127.0.0.1) and port 8080 of the local machine.

Option 1: ssh and direct connect (SOCKS5) : If you are going to use the ssh tunnel with the option "-D 8080" then you need to setup the browser to use a SOCKS5 proxy. Setup the proxy config page with the following entries and leave the rest of the entries blank.

Manual proxy configuration:

```bash
SOCKS Proxy  127.0.0.1  Port 8080
check the box for "SOCKS v5"
```

Option 2: ssh tunnel to squid proxy (HTTP/SSL Proxy) : If you are going to use the ssh tunnel with the option "-L 8080:localhost:2020" to connect to the remote machine's Squid proxy then configure the browser to use a HTTP/SSL proxy. Setup the proxy config page with the following entries and leave the rest of the entries blank.

Manual proxy configuration:

```bash
HTTP Proxy:  127.0.0.1  Port 8080
SSL Proxy :  127.0.0.1  Port 8080
```

Optional Step: DNS proxying through SOCKS5 is highly recommended

This step is optional, but since we are going to be proxying the data over the ssh tunnel then we should also proxy the DNS requests as well. The purpose of this exercise is to get to a site we might not otherwise be able to retrieve or just to anonymize our browsing from your location. If we tunneled our data through ssh and then asked the local DNS server for the ips it would defeat the purpose. So, add a boolean option into the URL "about:config" page in Firefox. Name the entry "network.proxy.socks_remote_dns" and set it to true.

This method will only take affect if you use the SOCKS5 proxy method. If you are proxying using the squid method (HTTP/SSL Proxy) you could always check if you can query another, independent DNS server like OpenDNS.

##Preference Name                 Status     Type      Value

  network.proxy.socks_remote_dns  user set   boolean   true

Making the ssh tunnel

Lastly, we need to start the ssh tunnel. You have two choices depending if you want the packets to be forwarded to squid on the remote machine or not.

Option 1: ssh and direct connect (SOCKS5) : The following line will start the ssh client and connect to username@remote_machine.com. Port 8080 on localhost (127.0.0.1) will listen for requests and send them to the remote machine. The remote machine will then send the packets out as if they originated from itself. The ssh options are in the man page of ssh, but to summarize them in order: Compression, SSH2 only, Quite, Force pseudo-tty allocation, Redirect stdin from /dev/null, and Place the ssh client into "master" mode for connection sharing.

```bash
ssh -C2qTnN -D 8080 username@remote_machine.com
```

Option 2: ssh to squid proxy (HTTP/SSL Proxy) : The following line will also start the ssh client and connect to username@remote_machine.com. Port 8080 on localhost (127.0.0.1) on the current machine will listen for requests and ssh tunnel them to the remote machine. On the remote machine ssh will forward the packets to localhost port 2020. If squid is listening on localhost port 2020 on the remote machine then all requests sent though the ssh tunnel will then be forwarded to squid. You can use squid to block ads and speed up web access. If you need assistance with squid, check out the Calomel.org Squid "how to" page.

```bash
ssh -C2qTnN -L 8080:localhost:2020 username@remote_machine.com
```

Testing the ssh tunnel

Once you execute the ssh line the encrypted and compressed ssh tunnel will be active in the xterm. We used the "quiet" options in ssh so there will not be any logging or output to the terminal.

Make sure Firefox is working by checking the proxy is active and then try to go to a web page. You can also try a site like WhatIsMyIp.com to verify the ip you have with the proxy is different than without.

If everything is working then you can be assured that all of your browsing traffic is being encrypted through the tunnel and no one at your current location will be able to see your traffic over the network.

Once you are done with the proxy just exit the ssh xterm or kill this instance of ssh with Ctrl-c. Remember to set Firefox back to "Direct Connection" if you want to directly browse from your location otherwise you will not be going anywhere.

Interested in setting up Squid or Samba? Check out our guides covering the Squid Proxy and Samba file share servers. We offer clear explanations and fully working example configurations.

**Questions?**

How can I setup two or more ssh tunnels through two or more machines ?

At some point you may need to tunnel through multiple ssh tunnels through multiple machines. This is quite easy to do as long as you have ssh access to every machine you want to tunnel through. In this example we will be tunneling from a desktop machine through a machine called host1 and then to a machine called host2 which will then access the internet. Something like so:

Firefox desktop -> host1 -> host2 -> internet

First, make sure you went through the beginning on this page and know how to get firefox to proxy through a SOCKS5 proxy on localhost port 8080. Then run the following ssh command on the desktop running Firefox. This will setup an encrypted ssh tunnel to host1 from the "Firefox desktop".

```bash
desktop$ ssh -C2qTnN username@host1 -L 8080:localhost:8080
```

Now, you need to ssh to host1 directly. Once you are on host1 run the following. This will collect any data from the first tunnel originating from the "Firefox desktop" to host1 and tunnel that data to host2.

```bash
host1$ ssh -C2qTnN -D 8080 username@host2
```

So, how does this setup work? Firefox on the desktop will initiate a SOCKS5 connection to localhost port 8080 on the desktop machine. Since a ssh tunnel is listening on localhost:8080 it will ssh tunnel the traffic to host1 which will forward this traffic to host1's localhost:8080. On host1 the second ssh command will tunnel all traffic it receives on localhost:8080 from the desktop machine to host2. On host2 the traffic will then be able to go out to the internet at large. If you have DNS SOCKS5 resolution on as well then all web traffic _and_ dns queries will goto host2 through both tunnels. From the view of the internet all queries originating from the "Firefox desktop" will look like they come from host2. Nice and anonymous.

What if I need to tunnel through more then two machines? Then just keep repeating "ssh -C2qTnN username@host1 -L 8080:localhost:8080" command for each incremental host. Once you decide you very last host you want the data to access the internet with then use the "ssh -C2qTnN -D 8080 username@host2" command.

To make sure you tunnel is working correctly using a site like ipchicken.com to see what ip address you are coming from. In the case of our example above ipchicken should report the ip address of host2.

Do you have any recommended modifications for Firefox in "about:config" ?

First, make sure to check out our Firefox Add-on "Calomel SSL Validation".

More open proxy connections: When you use a proxy, Firefox limits the amount of concurrent open connections to 8. This is too small for most users as many people open multiple tabs to many sites. When more then 8 connections are made the browser seems to be "stuck" because Firefox will wait till an open connection is closed before making a new one. To avoid this problem it is highly suggested to increase the persistent connections value from 8 to 25.

```bash
network.http.max-persistent-connections-per-proxy 25
```

Turn off pop-up tips: If you are annoyed by pop up text when your mouse hovers over a web element you can turn that function off.

```bash
browser.chrome.toolbar_tips  false
```

No animations: Stop all animated gifs and pictures like ads and annoying dancing cartoons characters.

```bash
image.animation_mode  none
```

No blinking text: Blinking text is annoying. Webmasters should not use it. In case they do, we will disallow the function in the browser.

```bash
browser.blink_allowed  false
```

Parallel connections: An easy way to speed up Firefox is to increase the amount of parallel connections the browser makes to the server. Open up Firefox and type in "about:config" in the URL. Then search for the string "conn" You should see the following entries listed. Modify them as follows:

```bash
network.http.max-connections                        25
network.http.max-connections-per-server             25
network.http.max-persistent-connections-per-proxy   25
network.http.max-persistent-connections-per-server  25
```

It is _not_ recommended to use more then 25 parallel connections due to abuse of the remote server and concurrency bottlenecks on the local system. Understand that if you have a slow system then more parallel connections can actually slow the browser down considerably. Also, if you try to open too many connections to a server then that server many consider you hostile and block or blacklist you.

Pipelining Enabled: The fastest and most efficient way to implement a browser is to use pipelining. This is where a single persistent connection is used, but instead of waiting for each response before sending the next request, several requests are sent out at a time. This reduces the amount of time the client and server are waiting for requests or responses to cross the network. Pipelined requests with a single connection are faster than multiple HTTP/1.0 requests in parallel, and considerably reduce the number of packets transmitted across the network. Apache supports both HTTP/1.0 keep-alive and HTTP/1.1 persistent connections. Pipelining is implement entirely at the browser end if supported by the remote web server, using persistent connections.

To enable pipelining in Firefox browser goto the url about:config . Then search for "pipe" and set the following:

```bash
network.http.pipelining              true
network.http.pipelining.maxrequests  8
network.http.pipelining.ssl          true
network.http.proxy.pipelining        true
```

TLSv1 with AES256, AES128 and 3DES 168 Only: When connecting to SSL based servers (https) you only want to use the strongest ciphers available. Most web server admins can setup their servers to prefer weak ciphers over strong ciphers for any reason; sometimes they want a less CPU intensive encryption or perhaps they just configured the server wrong. Even Google's encrypted pages prefer RC4 instead of AES and this is not our idea of good security. We want to make sure that our version of Firefox only uses AES 256 bit, AES 128 bit or 3DES 168 bit ciphers.

Open up a window and type "about:config". Then in the "Filter" bar at the top search for the following. Double clicking on each line will change the value.

    tls and set the lines to true.

    ssl2 and set every line entry to false.

    ssl3 and set every line to false _except_ lines containing the strings "aes_256" and "aes_128".

    security.ssl3.rsa_des_ede3_sha and set it to true. This is the weakest cipher and may be needed for some older SSL sites.

Now your browser will _only_ accept the TLSv1 protocol in AES256 bit cipher encryption no matter what previous weaker ciphers a web server prefers. This configuration also makes your browser FIPS 120-2 compliant (year 2030 specs).

Is there any way I can switch proxies faster?There are add-ons, also called extensions, for Firefox called FoxyProxy or SwitchProxyTool you can use. They offer the ability to setup multiple proxy settings and choose the one you want, or turn them off, using a drop down menu.

I noticed you use compression in the ssh tunnel proxy. Why?The majority of the data you are retrieving using the browser is text or HTML data. This type of data compresses very well at up to 80%. Using compression in the tunnel will speed up the delivery of the data considerably.

https://calomel.org/firefox_ssh_proxy.html


