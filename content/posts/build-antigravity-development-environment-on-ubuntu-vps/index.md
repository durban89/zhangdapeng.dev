+++
title = "Build an Antigravity Development Environment from Scratch: Ubuntu VPS, Linux Desktop, and tmux"
date = 2026-08-18T12:00:00+09:00
lastmod = 2026-08-18T12:00:00+09:00
description = "Learn how to build a persistent remote AI development workstation on an Ubuntu VPS using XFCE, XRDP, Tailscale, Zsh, Node.js, and tmux. A practical setup guide for independent developers."
summary = "Set up a reliable remote AI development workstation with Ubuntu VPS, XFCE, XRDP, Tailscale, and tmux. Keep your development environment accessible and your CLI sessions running independently of your local computer."
draft = false
slug = "build-antigravity-development-environment"

categories = [
    "Development",
    "Linux"
]

tags = [
    "Antigravity",
    "AI Coding",
    "Ubuntu",
    "VPS",
    "Linux Desktop",
    "tmux",
    "Tailscale",
    "XRDP",
    "Remote Development"
]

keywords = [
    "Antigravity",
    "Antigravity CLI",
    "Ubuntu VPS",
    "AI Coding",
    "AI Development Environment",
    "Remote AI Development",
    "Linux Desktop",
    "XFCE",
    "XRDP",
    "Tailscale",
    "tmux",
    "Remote Development"
]

series = [
    "AI Development Environment"
]

image = "cover.webp"

images = [
    "cover.webp"
]

[article]
toc = true
readingTime = true
+++

# Build an Antigravity Development Environment from Scratch: Ubuntu VPS + Linux Desktop + tmux

*A practical guide to building a persistent remote AI development workstation for independent developers.*

## Introduction

As an independent developer, I've been looking for a more stable and independent environment for AI-assisted development.

Working locally is convenient, but it also comes with several limitations:

- Local network conditions can affect access to AI services.
- Some services, including Google Gemini and Antigravity, may have regional availability restrictions.
- AI development tasks cannot continue running locally once the computer is shut down.
- CLI sessions can be interrupted when terminal connections are closed.
- Migrating and maintaining development environments across different machines can be inconvenient.

To address these issues, I decided to build a dedicated Linux VPS that could serve as my long-term development workstation.

Instead of relying entirely on a local terminal, I installed a lightweight Linux desktop environment and configured remote access. I also integrated common development tools and `tmux` to keep terminal sessions running independently of my local computer.

The overall architecture looks like this:

```text
Local Computer
      |
      | Tailscale / RDP / SSH
      |
      v
Ubuntu VPS
      |
      +-- XFCE Desktop
      +-- XRDP
      +-- Zsh
      +-- Node.js
      +-- Git
      +-- tmux
      +-- Antigravity CLI
              |
              v
       AI Coding Workflow
```

This guide walks through the complete setup process, from preparing the Ubuntu VPS to organizing projects, managing AI coding sessions, and configuring backups.

---

# 1. Why Use a VPS Instead of Developing Locally?

I initially experimented with Gemini CLI and Antigravity in my local Linux environment.

However, I quickly ran into several limitations.

## 1.1 Regional Availability and Network Restrictions

Some AI services determine service availability based on multiple factors, including:

- IP address and network location
- Google Account region
- Google Play country or region
- Account history
- Login environment

Simply switching networks does not necessarily resolve every regional availability issue.

For this reason, I wanted a more stable remote Linux environment that could serve as my primary AI development workspace.

A VPS provides an independent network environment and allows me to keep my development tools in one consistent location.

**Note:** A VPS does not automatically bypass regional restrictions or guarantee access to any particular AI service. Account eligibility and service policies still apply.

## 1.2 Keep the Development Environment Independent

One of the biggest advantages of using a VPS is that:

> Your development environment no longer depends on your local computer.

Even when I shut down my computer:

- Git repositories remain on the VPS.
- Detached tmux sessions continue running.
- AI CLI processes can continue running while the VPS remains online.
- I can reconnect from another device whenever needed.

This makes a significant difference when working with long-running AI coding tasks.

Rather than rebuilding the environment every time I switch devices, I can simply reconnect to the same remote workstation.

---

# 2. Choose an Ubuntu VPS

I chose an Ubuntu VPS as the foundation of this development environment.

The main considerations were:

- Relatively affordable hosting costs.
- Ability to run continuously.
- Native SSH support.
- Compatibility with Linux desktop environments.
- Support for Node.js and modern development tools.
- Compatibility with Tailscale for private networking.

I chose Ubuntu because of its mature software ecosystem and extensive documentation.

Some of its advantages include:

- A large and well-maintained software repository.
- Extensive community documentation.
- Excellent support for Node.js, Git, Docker, and other development tools.
- Broad compatibility with Linux-based AI development tools.

For a remote development workstation, Ubuntu offers a practical balance between compatibility, stability, and ease of maintenance.

---

# 3. Install a Linux Desktop Environment

Most VPS instances come with a command-line-only environment.

To get an experience closer to using a regular desktop computer, I installed XFCE.

Run the following commands:

```bash
sudo apt update
sudo apt install xfce4 xfce4-goodies -y
```

XFCE is particularly suitable for VPS environments.

Compared with heavier desktop environments such as GNOME or KDE, XFCE offers several advantages:

- Lower memory consumption.
- Better compatibility with low-resource VPS instances.
- A responsive remote desktop experience.
- A relatively lightweight and stable desktop environment.

For a remote development machine, minimizing unnecessary resource consumption is important.

XFCE provides the graphical environment I need without placing too much additional load on the server.

---

# 4. Install and Configure XRDP

After installing XFCE, the next step is to configure remote desktop access.

XRDP allows you to connect to your Linux desktop using an RDP client.

Install XRDP:

```bash
sudo apt install xrdp -y
```

Enable the service and start it:

```bash
sudo systemctl enable xrdp
sudo systemctl start xrdp
```

Check its status:

```bash
systemctl status xrdp
```

If the output contains:

```text
active (running)
```

XRDP is running successfully.

By default, XRDP listens on port:

```text
3389
```

You can use an RDP client on your local computer to connect to the VPS and access the XFCE desktop.

**Security recommendation:** Avoid exposing port 3389 directly to the public internet. In the next section, we'll use Tailscale to establish private connectivity. Make sure your VPS firewall and provider-level firewall restrict public access to the RDP port.

---

# 5. Secure Remote Access with Tailscale

Exposing an RDP service directly to the public internet is not an ideal security practice.

Instead, I use Tailscale to create a private network between my local computer and the VPS.

The connection looks like this:

```text
Local Computer
       |
       | Encrypted Private Network
       |
       v
    Tailscale
       |
       v
    Ubuntu VPS
```

Tailscale allows authorized devices to communicate through a private network without requiring the RDP service to be publicly accessible.

After installing and connecting Tailscale on both devices, check the connection status:

```bash
tailscale status
```

To retrieve the current device's Tailscale IP address:

```bash
tailscale ip
```

You can then use the Tailscale IP address for:

- SSH connections.
- RDP connections.
- Accessing other internal services.

For example, instead of connecting to the VPS through its public IP address, you can connect using its Tailscale IP:

```bash
ssh username@100.x.x.x
```

The same private IP can be used in your RDP client.

This approach keeps remote development access within your private network and reduces unnecessary public exposure.

---

# 6. Install and Configure Zsh

For a better terminal experience, I use Zsh instead of the default Bash shell.

Install Zsh:

```bash
sudo apt install zsh -y
```

Set it as the default shell:

```bash
chsh -s $(which zsh)
```

Log out and log back in, then verify the current shell:

```bash
echo $SHELL
```

You should see something similar to:

```text
/usr/bin/zsh
```

Zsh provides a flexible shell environment and supports a wide range of plugins and customization options.

It also works well with development tools such as NVM and Node.js.

---

# 7. Install Node.js with NVM

Antigravity CLI requires a suitable Node.js environment in this setup.

I use NVM (Node Version Manager) to manage Node.js versions.

After installing NVM, install Node.js 22:

```bash
nvm install 22
```

Verify the installation:

```bash
node -v
npm -v
```

My development environment uses:

```text
Node.js v22.x
```

I recommend using NVM rather than installing Node.js directly through the system package manager.

There are several benefits:

- Install multiple Node.js versions.
- Switch between versions easily.
- Keep Node.js dependencies separate from the system environment.
- Manage development environments more flexibly.

For a machine that may host multiple projects, version management becomes particularly useful.

---

# 8. Install Antigravity CLI

Once the Node.js environment is ready, you can prepare Antigravity for your development workflow.

After installing Antigravity CLI using its supported installation method, verify that the command is available:

```bash
antigravity --version
```

If the terminal returns:

```text
command not found
```

The executable may not be available in your current shell environment.

Start by checking its location:

```bash
which antigravity
```

Then inspect your current PATH:

```bash
echo $PATH
```

If the CLI was installed globally through npm, you can also check the global package and executable directories:

```bash
npm root -g
npm config get prefix
```

Common causes of this problem include:

- The Node.js environment has not been loaded.
- NVM has not been initialized in `.zshrc`.
- The npm global binary directory is missing from `$PATH`.

These issues are particularly common when switching between Bash and Zsh or when opening a new terminal session.

We'll also revisit the NVM configuration in the troubleshooting section.

---

# 9. Use tmux to Keep Antigravity Sessions Running

This is one of the most important components of the entire development environment.

When running an AI coding CLI directly through SSH or a remote terminal:

```bash
antigravity
```

The terminal session may be affected when:

- The network connection drops.
- The SSH session closes.
- The local computer goes to sleep.
- The RDP connection is interrupted.

Using `tmux` helps prevent these connection interruptions from terminating your terminal workflow.

Install tmux:

```bash
sudo apt install tmux -y
```

Create a new session:

```bash
tmux new -s antigravity
```

Start Antigravity inside the session:

```bash
antigravity
```

Now the CLI runs inside a tmux session rather than directly inside your SSH terminal.

## 9.1 Detach from tmux Without Stopping the Process

You can detach from the current tmux session while keeping its processes running.

Press:

```text
Ctrl + B
```

Then press:

```text
D
```

This detaches the current tmux session.

You can now:

- Close your SSH connection.
- Disconnect your RDP session.
- Shut down your local computer.

As long as the VPS remains running and the processes have not exited, the applications inside the detached tmux session will continue running.

This is particularly useful for long-running AI coding tasks.

## 9.2 List Existing tmux Sessions

To see all active tmux sessions:

```bash
tmux ls
```

Example output:

```text
antigravity: 1 windows
```

To reconnect to the existing session:

```bash
tmux attach -t antigravity
```

You can then continue working in the same terminal environment.

**Important:** tmux protects sessions against terminal disconnections, not VPS shutdowns or reboots. If the server restarts, ordinary tmux sessions and their running processes will not automatically return. For reboot recovery, you need additional session restoration or process management mechanisms.

---

# 10. Recommended Antigravity Project Workflow

For multiple projects, I recommend keeping each project in its own directory and using a separate tmux session for each one.

A typical structure might look like this:

```text
~/projects
│
├── project-a
│   └── tmux session: project-a
│
├── project-b
│   └── tmux session: project-b
│
└── project-c
    └── tmux session: project-c
```

Create a dedicated tmux session for a project:

```bash
tmux new -s project-a
```

Navigate to the project directory:

```bash
cd ~/projects/project-a
```

Start Antigravity:

```bash
antigravity
```

Each project now has its own independent terminal session.

To list all sessions:

```bash
tmux ls
```

To reconnect to a specific project:

```bash
tmux attach -t project-a
```

This organization makes it easier to switch between projects without interfering with other development tasks.

It is particularly useful when working on several applications simultaneously.

---

# 11. Back Up Antigravity CLI Data and Development Projects

Another issue that is easy to overlook when using a VPS is data persistence.

A VPS is convenient, but it should not be treated as a replacement for backups.

The server could eventually be:

- Accidentally deleted.
- Affected by filesystem corruption.
- Reinstalled during maintenance.
- Replaced with another VPS instance.

For this reason, I recommend regularly backing up both project files and relevant application data.

Potential directories to investigate include:

```text
~/.cache/
~/.config/
~/.local/
```

You should also back up your project directory:

```text
~/projects/
```

The actual location of Antigravity's session data depends on its implementation and configuration. Identify the directories it actually uses before adding them to a backup script.

For example, if the following cache directory exists:

```text
~/.cache/antigravity
```

You can create a compressed backup:

```bash
tar -czf antigravity-backup.tar.gz \
    ~/.cache/antigravity \
    ~/projects
```

The resulting archive can then be uploaded to secure cloud storage.

For a production environment, I recommend keeping backups outside the VPS itself.

That way, a server failure does not also destroy your backups.

---

# 12. Recommended Directory Structure

I recommend organizing the VPS development environment as follows:

```text
/home/daniel
│
├── projects
│   ├── PulseTimer
│   ├── IndieResizer
│   └── UnixTimestampConverter
│
├── backups
│
├── scripts
│
└── workspace
```

This structure separates project repositories, backup archives, utility scripts, and temporary workspace files.

Create the directories:

```bash
mkdir -p ~/projects
mkdir -p ~/backups
mkdir -p ~/scripts
mkdir -p ~/workspace
```

Keeping everything organized from the beginning makes future maintenance and migration much easier.

---

# 13. Automate Backups with a Shell Script

Instead of creating backups manually, you can write a simple shell script.

Create the script:

```bash
nano ~/scripts/backup.sh
```

Add the following content:

```bash
#!/bin/bash

BACKUP_DIR="$HOME/backups"

mkdir -p "$BACKUP_DIR"

tar -czf \
    "$BACKUP_DIR/projects-$(date +%F).tar.gz" \
    "$HOME/projects"
```

Save the file and grant execution permissions:

```bash
chmod +x ~/scripts/backup.sh
```

Run it manually:

```bash
~/scripts/backup.sh
```

You should now find a dated archive inside your backup directory.

## 13.1 Schedule Daily Backups with Cron

You can use cron to execute the backup script automatically.

Open the crontab editor:

```bash
crontab -e
```

Add the following entry:

```cron
0 3 * * * /home/daniel/scripts/backup.sh
```

This schedules the backup to run every day at 3:00 AM.

With this configuration, your project directory will be backed up automatically without requiring manual execution.

For long-term use, consider adding backup retention policies and uploading archives to an external storage service.

---

# 14. Common Problems and Troubleshooting

Here are some common issues you may encounter when setting up this environment.

## 14.1 `command not found: antigravity`

If the terminal cannot find the Antigravity command, first check whether the executable is available:

```bash
which antigravity
```

Then verify Node.js and npm:

```bash
node -v
npm -v
```

If you use NVM, make sure it is initialized in your `.zshrc` file.

The configuration should look similar to:

```bash
export NVM_DIR="$HOME/.nvm"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

Reload your shell configuration:

```bash
source ~/.zshrc
```

Then check the command again.

If the problem persists, inspect the npm global binary directory and make sure it is included in your PATH.

## 14.2 How to Check Whether You Are Inside tmux

Run:

```bash
echo $TMUX
```

If the output looks similar to:

```text
/tmp/tmux-1000/default,12345,0
```

You are currently inside a tmux session.

If the command returns nothing, you are probably running outside tmux.

## 14.3 How to Restore an Existing tmux Session

First, list the available sessions:

```bash
tmux ls
```

Then attach to the session you want:

```bash
tmux attach -t session-name
```

For example:

```bash
tmux attach -t antigravity
```

This reconnects you to the existing session, provided the VPS is still running and the session has not been terminated.

---

# 15. Final Architecture

After completing the configuration, the overall development environment looks like this:

```text
┌───────────────────────────────────┐
│           Local Computer          │
│                                   │
│   Browser / VS Code / Terminal    │
└─────────────────┬─────────────────┘
                  │
                  │ Tailscale
                  ▼
┌───────────────────────────────────┐
│             Ubuntu VPS            │
│                                   │
│   ┌───────────────────────────┐   │
│   │       XFCE Desktop        │   │
│   └───────────────────────────┘   │
│                                   │
│   ┌───────────────────────────┐   │
│   │           XRDP            │   │
│   └───────────────────────────┘   │
│                                   │
│   ┌───────────────────────────┐   │
│   │           Zsh             │   │
│   │          Node.js          │   │
│   │           Git             │   │
│   │          tmux             │   │
│   └─────────────┬─────────────┘   │
│                 │                 │
│                 ▼                 │
│          Antigravity CLI          │
│                 │                 │
│                 ▼                 │
│          AI Development           │
│                                   │
└───────────────────────────────────┘
```

---

# Conclusion

By combining an Ubuntu VPS, Linux desktop environment, Tailscale, and tmux, I built a relatively independent environment for AI-assisted development.

The biggest advantages of this setup are:

- **Always-on infrastructure:** The VPS can run continuously without depending on my local computer.
- **Environment independence:** Development tools and projects remain on the remote server.
- **Multi-device access:** I can connect to the same development environment from different devices.
- **Persistent terminal sessions:** tmux keeps CLI processes running when terminal connections are interrupted.
- **Private networking:** Tailscale provides secure connectivity without unnecessarily exposing remote desktop services to the public internet.
- **Centralized project management:** All repositories and development tools are organized in one place.
- **Automated backups:** Shell scripts and cron help protect important project files.

For independent developers, this approach provides a practical foundation for maintaining a long-term remote development workstation.

Ultimately, what you get is more than just another VPS.

It is an:

> **AI Development Workspace that you can access anytime, run continuously, maintain independently, and expand as your development needs grow.**

## What's Next?

There is plenty of room to extend this environment in the future.

Some potential additions include:

- Docker for application containerization.
- k3s for lightweight Kubernetes orchestration.
- GitHub Actions for automated workflows.
- Automated deployment pipelines.
- HTTPS and reverse proxy configuration.
- CI/CD integration.
- Remote cloud backups.
- Multi-project AI agent workflows.
- More advanced development automation.

With these additions, a simple VPS can gradually evolve into a personal AI development infrastructure that supports an increasingly sophisticated development workflow.