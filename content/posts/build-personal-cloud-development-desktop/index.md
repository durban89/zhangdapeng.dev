+++
title = "Build a Personal Cloud Development Desktop from Scratch: Vultr VPS + XFCE + XRDP + Tailscale + Remmina"
description = "Learn how to build a lightweight Linux remote desktop on a Vultr Ubuntu VPS using XFCE, XRDP, Tailscale, and Remmina. Create a secure, reliable cloud development workstation accessible from multiple devices."
summary = "Build a secure and lightweight cloud-based Linux desktop with Vultr VPS, Ubuntu, XFCE, XRDP, Tailscale, and Remmina. A practical guide to setting up your own remote development workstation."
date = 2026-08-18T12:00:00+09:00
lastmod = 2026-08-18T12:00:00+09:00
draft = false
slug = "build-personal-cloud-development-desktop"

categories = [
    "Linux",
    "Development"
]

tags = [
    "Vultr",
    "Ubuntu",
    "VPS",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "Remmina",
    "Remote Desktop",
    "Remote Development"
]

keywords = [
    "Vultr VPS",
    "Ubuntu VPS",
    "Linux Remote Desktop",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "Remmina",
    "Remote Desktop",
    "Cloud Development",
    "Cloud Development Environment",
    "Remote Development",
    "Personal Development Environment"
]

series = [
    "Remote Development Environment"
]

image = "cover.webp"

images = [
    "cover.webp"
]

[article]
toc = true
readingTime = true
+++

# Build a Personal Cloud Development Desktop from Scratch: Vultr VPS + XFCE + XRDP + Tailscale + Remmina

*A practical guide to building a lightweight Linux desktop on a Vultr VPS and accessing it securely from your local computer using Tailscale and Remmina.*

As an independent developer, I often need a reliable Linux environment for development, testing, and running various tools.

Rather than configuring and maintaining every development tool on my local computer, I wanted a dedicated cloud-based environment with the following capabilities:

- Accessible anytime from different devices.
- A complete Linux desktop environment.
- Support for browsers and graphical development tools.
- Secure remote access without exposing RDP ports to the public internet.
- A consistent development environment independent of my local machine.

After considering different approaches, I settled on the following setup:

```text
Local Linux / Windows / macOS
              |
              |
           Remmina
              |
              |
          Tailscale
              |
              |
       +--------------+
       |  Vultr VPS   |
       |              |
       | Ubuntu Linux |
       |      +       |
       |     XFCE     |
       |      +       |
       |     XRDP     |
       +--------------+
```

The architecture is straightforward:

> **Vultr provides the VPS, Ubuntu provides the operating system, XFCE provides the lightweight desktop, XRDP handles remote desktop connections, Tailscale provides secure private networking, and Remmina acts as the remote desktop client.**

In this guide, I'll walk through the complete setup process, from creating the VPS to connecting to the Linux desktop remotely.

---

# 1. Why Choose a VPS with a Remote Desktop?

A traditional VPS usually provides only SSH access.

For example:

```bash
ssh root@your-server-ip
```

SSH is sufficient for most server administration tasks. However, it becomes less convenient when you need to run graphical applications such as:

- Google Chrome
- Claude
- Gemini
- Antigravity
- VS Code
- GUI-based development tools
- Browser extension testing environments
- Graphical Git clients

If you want to use these applications directly on a remote server, a command-line-only environment is not always enough.

The solution is to install a complete Linux desktop environment on the VPS.

The resulting architecture looks like this:

```text
VPS
 |
 +-- Ubuntu
 |
 +-- XFCE Desktop
 |
 +-- XRDP
 |
 +-- Tailscale
```

Your local computer connects through the following path:

```text
Remmina
   |
   v
Tailscale Private Network
   |
   v
XRDP
   |
   v
XFCE Desktop
```

This gives you a graphical Linux environment that you can access remotely, just like a regular desktop computer.

---

# 2. Create a Vultr Ubuntu VPS

First, create a new VPS through [Vultr](https://www.vultr.com/).

Choose an Ubuntu LTS image as the operating system.

For example:

```text
Ubuntu LTS
```

Select a server configuration based on your expected workload.

For a lightweight desktop, XFCE is a reasonable choice for resource-constrained instances. However, if you plan to run multiple browsers, IDEs, or AI development tools simultaneously, consider allocating more memory and CPU resources.

Once the VPS has been created, connect to it through SSH:

```bash
ssh root@your-server-ip
```

Update the system packages:

```bash
apt update
apt upgrade -y
```

If you are logged in with a regular user account, use:

```bash
sudo apt update
sudo apt upgrade -y
```

Keeping the system updated before installing additional software helps establish a clean starting point.

---

# 3. Install the XFCE Desktop Environment

For a VPS, I generally recommend avoiding heavier desktop environments such as GNOME or KDE when system resources are limited.

They can consume more:

- RAM
- CPU resources
- Graphics resources

For smaller VPS instances with 1–2 GB of RAM, XFCE is often a more practical choice.

Install XFCE:

```bash
sudo apt install xfce4 xfce4-goodies -y
```

During installation, you may be prompted to select a display manager.

If a selection is required, you can choose:

```text
lightdm
```

XFCE offers several advantages for remote desktop environments:

- Relatively low resource consumption.
- Fast startup.
- Good compatibility with VPS instances.
- A responsive remote desktop experience.

After installation, your server has the basic components required to run a Linux graphical desktop.

---

# 4. Install XRDP

XRDP allows Linux systems to accept remote desktop connections using the Microsoft Remote Desktop Protocol (RDP).

Install XRDP:

```bash
sudo apt install xrdp -y
```

Enable the service and start it:

```bash
sudo systemctl enable xrdp
sudo systemctl start xrdp
```

Check the service status:

```bash
sudo systemctl status xrdp
```

If the output shows:

```text
active (running)
```

XRDP is running successfully.

At this point, the remote desktop service is installed, but we still need to configure it to start the XFCE desktop session correctly.

---

# 5. Configure XRDP to Use XFCE

By default, XRDP may not automatically launch the XFCE desktop environment after a remote login.

To specify which desktop session should start, create an `.xsession` file in your user's home directory.

Run:

```bash
nano ~/.xsession
```

Add the following line:

```bash
startxfce4
```

Save the file and make it executable:

```bash
chmod +x ~/.xsession
```

Restart XRDP:

```bash
sudo systemctl restart xrdp
```

Now, when you connect through RDP using that Linux account, XRDP should launch an XFCE session.

**Note:** Run this configuration under the same Linux user account that you will use for remote desktop login. Display manager and session configuration can vary between Ubuntu versions and XRDP setups.

---

# 6. Avoid Exposing Port 3389 to the Public Internet

By default, XRDP listens on:

```text
3389
```

You could theoretically connect directly using this configuration:

```text
Your Computer
      |
      v
Public IP Address
      |
      v
VPS:3389
```

However, exposing RDP directly to the public internet introduces unnecessary security risks.

Public scanners frequently probe commonly used service ports, including:

```text
3389
22
3306
6379
```

An exposed RDP service may receive:

- Brute-force login attempts.
- Password-guessing attacks.
- Vulnerability scans.
- Unauthorized connection attempts.

For this reason, I decided not to expose XRDP directly to the public internet.

Instead, I use:

> **Tailscale**

Tailscale provides a private network that allows authorized devices to communicate securely without requiring the RDP service to be publicly accessible.

---

# 7. Install Tailscale

Tailscale uses WireGuard-based encrypted networking to connect devices through a private network.

Install Tailscale on the Ubuntu VPS:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Start the authentication process:

```bash
sudo tailscale up
```

The terminal will display a login URL.

Open it in your browser and authenticate with your Tailscale account.

After authentication, retrieve the VPS's Tailscale IP address:

```bash
tailscale ip
```

You should see an address similar to:

```text
100.x.x.x
```

This is the device's Tailscale IP address.

Unlike a public IP address, it is used for communication within your Tailscale network.

You will use this address later when configuring Remmina.

**Important:** You also need to install Tailscale and authenticate your local computer. Both devices must belong to an authorized Tailnet, and the applicable access policies must allow the connection.

---

# 8. Configure the Private Network Architecture

Once Tailscale is installed and authenticated on both devices, the network architecture looks like this:

```text
+----------------------+
|     Local Computer   |
|                      |
|      Tailscale       |
+----------+-----------+
           |
           |
           | Encrypted Connection
           |
           v
+----------------------+
|      Tailscale       |
|     Private Mesh     |
+----------+-----------+
           |
           v
+----------------------+
|       Vultr VPS      |
|                      |
|    Tailscale IP      |
|     100.x.x.x        |
|                      |
|       XRDP           |
|       :3389          |
|                      |
|       XFCE           |
+----------------------+
```

At this point:

- The VPS is connected to your private Tailscale network.
- Your local computer is also connected to the same network.
- XRDP can be accessed through the VPS's Tailscale IP.
- You do not need to expose port 3389 to the public internet.

Only devices authorized by your Tailnet access policies should be able to reach the remote desktop service.

For additional security, configure your VPS firewall and Vultr firewall to block public access to port 3389 while allowing the required private Tailscale traffic.

---

# 9. Install Remmina on Your Local Computer

If your local computer runs Ubuntu or another Linux distribution, Remmina is a convenient remote desktop client.

Install it:

```bash
sudo apt install remmina -y
```

Launch Remmina:

```bash
remmina
```

Create a new remote desktop connection.

Configure the connection as follows:

**Protocol:**

```text
RDP
```

**Server:**

```text
100.x.x.x
```

Make sure you enter the VPS's **Tailscale IP address**, not its public IP address.

For example:

```text
100.64.12.34
```

**Username:**

```text
Your Linux username
```

**Password:**

```text
Your Linux account password
```

After entering the connection details, click Connect.

If everything is configured correctly, Remmina should establish an RDP connection to your VPS.

---

# 10. Understanding the Remote Desktop Connection

The complete connection process looks like this:

```text
Remmina
   |
   | RDP
   v
Tailscale Network
   |
   | Encrypted Connection
   v
Vultr VPS
   |
   v
XRDP
   |
   v
XFCE Desktop
```

The result is simple:

> Open Remmina on your local computer, connect to the VPS, and access its Ubuntu desktop just as you would connect to another remote desktop machine.

You can now use graphical applications running on the VPS without installing all of them locally.

This is particularly useful when you want to maintain a consistent development environment across multiple devices.

---

# 11. Common Problems and Troubleshooting

Here are some common issues you may encounter during the setup process.

## 11.1 XRDP Connection Failed

First, check whether the XRDP service is running:

```bash
sudo systemctl status xrdp
```

If the service is not running, restart it:

```bash
sudo systemctl restart xrdp
```

Next, check whether port 3389 is listening:

```bash
sudo ss -tulpn | grep 3389
```

Under normal conditions, you should see a listening socket:

```text
LISTEN
```

If XRDP is running but connections still fail, check the firewall rules and XRDP logs.

For example:

```bash
sudo journalctl -u xrdp -n 50 --no-pager
```

Also verify that the connection is being made through the correct Tailscale IP.

## 11.2 Remmina Cannot Connect

First, verify that Tailscale is running on both devices.

On your local computer:

```bash
tailscale status
```

On the VPS:

```bash
tailscale status
```

Then test connectivity:

```bash
ping 100.x.x.x
```

If the VPS is unreachable, possible causes include:

- Tailscale is not authenticated.
- The devices are not connected to the same Tailnet.
- Tailscale ACL or grants policies restrict access.
- Network connectivity problems.
- Firewall rules blocking the required traffic.

If ping works but RDP still fails, check whether XRDP is listening and whether the firewall allows connections through the Tailscale interface.

## 11.3 Black Screen After Login

A black screen after authentication may indicate that XRDP failed to start the XFCE desktop session.

Check the session configuration:

```bash
cat ~/.xsession
```

It should contain:

```bash
startxfce4
```

If necessary, recreate the file:

```bash
echo "startxfce4" > ~/.xsession
chmod +x ~/.xsession
```

Restart XRDP:

```bash
sudo systemctl restart xrdp
```

Then reconnect using Remmina.

If the problem persists, inspect the XRDP and Xorg session logs for additional errors.

## 11.4 VPS Running Out of Memory

If your VPS has limited resources, such as:

```text
1 GB RAM
```

Running a full desktop environment alongside browsers and development tools may become difficult.

Check the current memory usage:

```bash
free -h
```

Check whether Swap is configured:

```bash
swapon --show
```

For example:

```text
Memory: 1.6Gi
Swap:   5.8Gi
```

A Swap configuration can help prevent memory pressure from immediately causing application failures.

However, Swap is not a substitute for physical RAM. Heavy swapping can significantly reduce performance.

For a more comfortable development experience, consider upgrading the VPS memory if you regularly run multiple graphical applications.

---

# 12. Why Choose XFCE?

There are several Linux desktop environments worth considering.

Here is a simplified comparison:

| Desktop Environment | Resource Usage | VPS Suitability |
|---|---|---|
| GNOME | High | Limited |
| KDE Plasma | Medium to High | Good |
| XFCE | Low | Excellent |
| LXQt | Very Low | Excellent |

My choice is:

```text
XFCE
```

The reasons are straightforward:

- Lightweight.
- Stable.
- Fast.
- Well suited to remote desktop environments.

A VPS does not need complex desktop animations or unnecessary visual effects.

What matters more is:

> **Stability, responsiveness, and low resource consumption.**

XFCE provides a good balance for a personal cloud development desktop.

---

# 13. Final Environment Overview

After completing the setup, my VPS environment looks like this:

```text
Vultr VPS
|
+-- Ubuntu LTS
|
+-- XFCE Desktop
|
+-- XRDP
|
+-- Tailscale
|
+-- Node.js
|
+-- Git
|
+-- Zsh
|
+-- tmux
|
+-- Chrome / Development Tools
```

My local Linux computer has:

```text
Local Linux Desktop
|
+-- Remmina
|
+-- Tailscale
```

This separation keeps the development environment on the VPS while allowing me to access it remotely through my local computer.

---

# 14. Conclusion

The goal of this setup is not simply to create another Linux VPS.

It is to build a practical:

> **Personal Cloud Development Desktop**

The overall architecture is:

```text
Local Computer
      |
      v
   Remmina
      |
      v
  Tailscale
      |
      v
   Vultr VPS
      |
      v
     XRDP
      |
      v
  XFCE Desktop
```

Compared with exposing RDP directly to the public internet:

```text
Public Internet
       |
       v
    VPS:3389
```

Using Tailscale provides a more secure approach:

```text
Authorized Device
        |
        v
Encrypted Private Network
        |
        v
       VPS
```

This reduces unnecessary public exposure and makes the environment more suitable for long-term personal use.

If you are an independent developer looking for an environment that is:

- Accessible anytime.
- Independently maintained.
- Not dependent on your local computer.
- Capable of running Linux GUI applications.
- Suitable for browsers and development tools.
- Accessible remotely from multiple devices.
- Configured without exposing RDP directly to the public internet.

Then the following combination is worth considering:

> **Vultr + Ubuntu + XFCE + XRDP + Tailscale + Remmina**

It provides a relatively simple foundation for building your own cloud-based Linux workstation.

---

## What's Next?

Once the remote desktop is working, you can gradually expand the VPS into a more complete development infrastructure.

Potential additions include:

```text
VPS
|
+-- Docker
|
+-- k3s
|
+-- GitHub Actions
|
+-- Automated Deployment
|
+-- Nginx / Caddy
|
+-- HTTPS
|
+-- Development Tools
```

Over time, this VPS can evolve into your own:

> **Personal Cloud Development Workstation + Self-Hosted Server + Automated Deployment Platform.**