+++
title = "Persist and Restore Tmux Sessions with Tmux-Resurrect and TPM"
date = 2026-11-11T14:30:00+08:00
lastmod = 2026-11-11T14:30:00+08:00
description = "Learn how to install tmux-resurrect and tmux-continuum using Tmux Plugin Manager (TPM) to save, restore, and automatically recover Tmux sessions. Includes installation steps and solutions to common plugin and keybinding issues."
slug = "tmux-resurrect-tpm-session-restore"
image = "./cover.png"
image_alt = "Tmux terminal showing multiple split panes and restored development sessions"
toc = true
draft = false
tags = ["tmux", "linux", "terminal", "development-tools"]
categories = ["Development", "Linux"]
+++

Tmux is an essential tool for developers who frequently work in terminal environments. It allows you to organize multiple tasks into separate sessions, windows, and panes without opening multiple terminal applications.

However, Tmux does not persist session state to disk by default. If your server restarts, the Tmux server crashes, or you accidentally run `tmux kill-server`, your existing sessions, window layouts, and working directories may be lost.

Recreating all those sessions and manually arranging panes every time you restart your environment can quickly become frustrating.

Fortunately, you can solve this problem with **Tmux Plugin Manager (TPM)** and the `tmux-resurrect` plugin. By combining it with `tmux-continuum`, you can also enable automatic session saving and restoration.

This guide walks through the installation, configuration, verification, and troubleshooting process.

<!--more-->

## 1. Understanding Tmux-Resurrect and Tmux-Continuum

Before configuring anything, it is important to understand the roles of these two plugins.

### 1.1 tmux-resurrect: Manual Session Saving and Restoration

[tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) is a plugin that persists your Tmux environment across restarts.

It can save and restore information such as:

- All Tmux sessions, windows, and panes.
- Window and pane ordering.
- The current working directory (CWD) of each pane.
- Pane layouts, including zoomed layouts.
- The currently active session, window, and pane.
- Selected running programs.
- Optional Vim/Neovim sessions and pane history contents.

It provides two default keybindings:

| Keybinding | Action |
|---|---|
| `Prefix + Ctrl-s` | Save the current Tmux environment |
| `Prefix + Ctrl-r` | Restore the previously saved environment |

The default Tmux prefix key is `Ctrl + b`. If you have customized it, use your configured prefix instead.

### 1.2 tmux-continuum: Automatic Saving and Restoration

[tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) builds on top of `tmux-resurrect` to automate session persistence.

Its main features include:

- **Automatic saving:** Saves the Tmux environment every 15 minutes by default.
- **Automatic restoration:** Restores the most recently saved environment when the Tmux server starts.

The relationship between these plugins is straightforward:

- `tmux-resurrect` handles saving and restoring sessions.
- `tmux-continuum` automates periodic saves and restoration when the Tmux server starts.

If you only need manual session recovery, `tmux-resurrect` is sufficient. If you want your sessions to return automatically after a server restart, installing both plugins is recommended.

## 2. Troubleshooting: Why Are the Restore Keybindings Not Working?

A common mistake is adding the following line directly to `~/.tmux.conf`:

```tmux
set -g @plugin 'tmux-plugins/tmux-resurrect'
```

Then pressing:

```text
Ctrl + b
Ctrl + r
```

But nothing happens.

In most cases, the problem is that **TPM has not been installed, initialized, or used to install the actual plugin**.

The following configuration:

```tmux
set -g @plugin 'tmux-plugins/tmux-resurrect'
```

only declares which plugin TPM should manage. It does not download or load the plugin by itself.

TPM must first be cloned to your local machine and initialized through your Tmux configuration. You must then explicitly install the declared plugins.

The complete process is:

1. Install TPM.
2. Declare the plugins in `~/.tmux.conf`.
3. Initialize TPM.
4. Use TPM to install the plugins.

Let's go through each step.

## 3. Installing TPM and Configuring the Plugins

### 3.1 Install Tmux Plugin Manager

First, make sure Git and Tmux are installed.

Check their versions:

```bash
tmux -V
git --version
```

Next, clone TPM into its default plugin directory:

```bash
git clone https://github.com/tmux-plugins/tpm.git ~/.tmux/plugins/tpm
```

After cloning, verify that the directory exists:

```bash
ls -la ~/.tmux/plugins/tpm
```

If you can see the TPM files, the installation was successful.

### 3.2 Configure ~/.tmux.conf

Open your Tmux configuration file:

```bash
vim ~/.tmux.conf
```

If the file does not exist, you can create it.

Add the following configuration:

```tmux
# ==========================================
# TPM Plugin Manager
# ==========================================

# Plugin declarations
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# ==========================================
# Tmux Resurrect
# ==========================================

# Restore pane contents (optional)
set -g @resurrect-capture-pane-contents 'on'

# ==========================================
# Tmux Continuum
# ==========================================

# Enable automatic restoration
set -g @continuum-restore 'on'

# Save the environment every 15 minutes (default)
set -g @continuum-save-interval '15'

# ==========================================
# Initialize TPM
# Keep this line at the very bottom!
# ==========================================

run '~/.tmux/plugins/tpm/tpm'
```

**Configuration details:**

- `@plugin`: Declares the plugins managed by TPM.
- `@resurrect-capture-pane-contents`: Enables saving and restoring pane history contents.
- `@continuum-restore`: Enables automatic restoration when the Tmux server starts.
- `@continuum-save-interval`: Sets the automatic save interval in minutes.
- `run '~/.tmux/plugins/tpm/tpm'`: Initializes TPM.

**Important:** Keep the TPM initialization command at the very bottom of `~/.tmux.conf`. This ensures that plugin declarations and configuration options are processed before TPM initializes.

### 3.3 Reload the Tmux Configuration

After saving the configuration file, switch to an active Tmux session.

Press:

```text
Ctrl + b
:
```

This opens the Tmux command prompt.

Enter:

```bash
source-file ~/.tmux.conf
```

Alternatively, you can execute the following command from a regular terminal:

```bash
tmux source-file ~/.tmux.conf
```

TPM will now read the plugin declarations, but the plugins have not necessarily been downloaded or installed yet.

### 3.4 Install the Plugins Using TPM

This is the most important step.

Inside your Tmux session, press:

```text
Ctrl + b
Shift + i
```

The key combination uses an uppercase `I`, not a lowercase `i`.

TPM will download and load the plugins declared in your configuration file.

Wait until the status message appears:

```text
Plugin(s) installed!
```

Both `tmux-resurrect` and `tmux-continuum` should now be installed and ready to use.

## 4. Verifying Session Saving and Restoration

After installation, it is a good idea to test manual saving and restoration before checking automatic recovery.

### 4.1 Save the Current Tmux Environment

Inside Tmux, press:

```text
Ctrl + b
Ctrl + s
```

If the plugin is working correctly, you should see:

```text
Tmux environment saved!
```

By default, session data is stored in:

```bash
~/.tmux/resurrect/
```

You can inspect the saved files with:

```bash
ls -lah ~/.tmux/resurrect/
```

You should normally see a `last` state file along with timestamped backup files.

### 4.2 Restore a Saved Session Manually

After restarting Tmux, press:

```text
Ctrl + b
Ctrl + r
```

If restoration starts successfully, you should see:

```text
Restoring tmux environment...
```

After a short wait, your previously saved sessions, windows, pane layouts, and working directories should reappear.

### 4.3 Test Recovery After Restarting the Tmux Server

To verify that session recovery works across Tmux server restarts, follow these steps.

**Step 1: Save the current environment**

Start or enter a Tmux session:

```bash
tmux
```

Press:

```text
Ctrl + b
Ctrl + s
```

Make sure the save operation succeeds.

**Step 2: Stop the Tmux server**

Open a regular terminal and execute:

```bash
tmux kill-server
```

Note: This terminates all sessions managed by the current Tmux server. Make sure your session has been saved before running this command.

**Step 3: Start Tmux again**

```bash
tmux
```

If you installed only `tmux-resurrect`, manually trigger restoration:

```text
Ctrl + b
Ctrl + r
```

If you also installed `tmux-continuum` and enabled automatic restoration, it will attempt to restore the most recently saved environment when the Tmux server starts.

One important distinction: `tmux-continuum` does not automatically launch the Tmux process at the operating system level. After a system reboot, you still need a mechanism such as a login script, shell configuration, or systemd service to start Tmux. Automatic restoration only happens after the Tmux server has started.

## 5. Common Issues and Solutions

### 5.1 Prefix + I Does Nothing

Check the following:

- TPM has been cloned into `~/.tmux/plugins/tpm`.
- `~/.tmux.conf` contains the TPM initialization command.
- You have reloaded the Tmux configuration.
- You are pressing uppercase `I`, not lowercase `i`.

You can also verify that the TPM initialization script exists:

```bash
ls ~/.tmux/plugins/tpm/tpm
```

### 5.2 Ctrl + s or Ctrl + r Does Not Work

First, check whether the plugins have been installed:

```bash
ls ~/.tmux/plugins/
```

You should see directories similar to:

```text
tpm/
tmux-resurrect/
tmux-continuum/
```

If the plugin directories are missing, run:

```text
Prefix + I
```

If the plugins are installed but the keybindings still do not work, check for conflicting keybindings:

```bash
tmux list-keys | grep -E 'C-s|C-r'
```

Another possible cause is terminal flow control (XON/XOFF). Some terminal environments interpret `Ctrl + s` as a flow-control shortcut and intercept the key before Tmux receives it.

You can disable this behavior with:

```bash
stty -ixon
```

To make the change persistent, add the command to your `~/.bashrc` or `~/.zshrc`.

### 5.3 Automatic Restoration Is Not Working

If manual restoration works but automatic restoration does not, check the following:

- `tmux-continuum` is installed.
- `set -g @continuum-restore 'on'` is present in your configuration.
- Both plugins have been installed and loaded successfully.
- You have actually restarted the Tmux server.

**Important:** Running `source-file ~/.tmux.conf` does not trigger automatic restoration. `tmux-continuum` performs automatic restoration only when the Tmux server starts.

Automatic saving also requires the Tmux status line to be enabled. If another plugin or theme overwrites the `status-right` configuration, the automatic save mechanism may stop working.

If this happens, try placing `tmux-continuum` at the end of your TPM plugin list.

### 5.4 No Saved Session Files Found

Check the default save directory:

```bash
ls -lah ~/.tmux/resurrect/
```

If the directory does not exist, try manually saving the current environment:

```text
Prefix + Ctrl + s
```

Also make sure the current user has permission to read and write to the directory.

## 6. Understanding the Limitations of Tmux-Resurrect

Although `tmux-resurrect` can restore most of your Tmux environment, it is not a full process snapshot or checkpointing system.

It is important to understand the difference.

**What it can restore:**

- Session, window, and pane structures.
- Pane layouts and ordering.
- Working directories.
- Active windows and panes.
- Selected supported terminal applications.
- Optionally, pane history contents.

**What it cannot guarantee:**

- The complete runtime state of every running process.
- Unsaved in-memory application data.
- Previously established database or SSH connections.
- The execution state of complex interactive scripts.
- Internal application state, such as unsaved editor changes.

For Vim and Neovim users, additional editor session recovery can be configured through `tmux-resurrect`, allowing the editor's own session mechanism to restore files and window layouts.

In other words, `tmux-resurrect` restores your terminal working environment. It does not freeze and resume every application exactly where it left off.

## 7. Conclusion

By combining TPM, `tmux-resurrect`, and `tmux-continuum`, you can build a simple but effective session persistence solution for Tmux.

Each component has a specific responsibility:

| Component | Responsibility |
|---|---|
| TPM | Installs, manages, and loads Tmux plugins |
| tmux-resurrect | Manually saves and restores Tmux environments |
| tmux-continuum | Automatically saves sessions and restores them when Tmux starts |

For developers who frequently connect to remote servers through SSH, manage multiple projects, or maintain long-running development environments, this combination can significantly reduce the repetitive work of rebuilding terminal sessions.

**One final recommendation:** If your development environment is important, periodically check the saved files in `~/.tmux/resurrect/` and keep your essential configuration files under Git version control.

Session restoration is a convenient productivity feature, but it should never replace proper data backups.

## References

- [Tmux Plugin Manager (TPM)](https://github.com/tmux-plugins/tpm)
- [Tmux Resurrect](https://github.com/tmux-plugins/tmux-resurrect)
- [Tmux Continuum](https://github.com/tmux-plugins/tmux-continuum)
