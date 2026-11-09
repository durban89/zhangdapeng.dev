+++
title = "Fix Blurry Icons and Input Method Issues in Linux QQ 3.2.35 on Ubuntu KDE"
date = 2026-11-09T10:24:00+08:00
draft = false
description = "Learn how to fix blurry avatars, distorted icons, and Fcitx5 or IBus input method issues in Linux QQ 3.2.35 on Ubuntu KDE using X11 or native Wayland."
tags = ["Linux", "Ubuntu", "KDE", "QQ", "Electron", "Wayland", "X11", "Fcitx5"]
categories = ["Linux", "Development"]

toc = true
lastmod = 2026-11-09T10:24:00+08:00

image = "./cover.png"
image_alt = "Linux QQ 3.2.35 avatar distortion and input method fixes on Ubuntu KDE using X11 and Wayland"
+++

After installing **Linux QQ 3.2.35** on an Ubuntu system running the KDE desktop environment, some users may encounter an annoying display issue: avatars, icons, and images in chat windows appear blurry or heavily pixelated.

Things can become even more frustrating when trying to fix the problem by changing Electron's graphics backend or scaling parameters. The images become sharper, but the input method stops working. After restoring input method support, the display may occasionally become blurry again.

This guide documents the troubleshooting process and presents two possible solutions for running Linux QQ under X11 (Xwayland) or native Wayland.

## 1. Understanding the Problem

Linux QQ 3.2.35 is built on Electron. Its rendering behavior, display scaling, and input method support depend on the interaction between Electron, the graphics backend, and the desktop environment.

On Ubuntu KDE, two areas are particularly worth investigating.

### 1.1 X11 Mode: Clear Images but Potential Input Method Issues

You can force Electron to use X11 with the following launch argument:

```bash
--ozone-platform=x11
```

In my testing environment, this mode resolved the blurry avatar and icon issue.

However, when running an X11 application inside a KDE Wayland session, input method support also depends on the environment configuration between Xwayland and Fcitx5 or IBus.

If the relevant environment variables are missing or incorrectly configured, the application may fail to activate the input method when typing.

### 1.2 Wayland Mode: Working Input Methods but Occasional Blurring

To run QQ using the native Wayland backend, you can try:

```bash
--ozone-platform=wayland
```

This mode can provide better integration with the Wayland input method protocol.

However, additional non-integer scaling parameters, such as:

```bash
--force-device-scale-factor=1.25
```

may cause inconsistencies between Electron's device scale factor and the desktop's actual display scaling, especially on a standard-resolution monitor configured for 100% scaling.

Depending on the Electron version and graphics environment, this may introduce unnecessary image resampling or texture-size mismatches, potentially causing avatars and icons to become blurry during certain rendering updates.

If your display is configured for 100% scaling, it is worth restoring the device scale factor to `1.0` before investigating other causes.

---

## 2. Solution 1: Use X11 Mode (Recommended First)

If your primary concern is blurry avatars, icons, and images, try running QQ in X11 mode first.

Under KDE Wayland, X11 applications generally run through Xwayland. To restore input method support, configure the appropriate environment variables for your input method framework.

### 2.1 For Fcitx5 Users

Open a terminal and run:

```bash
GTK_IM_MODULE=fcitx \
QT_IM_MODULE=fcitx \
XMODIFIERS=@im=fcitx \
qq --ozone-platform=x11 --app-id=qq
```

### 2.2 For IBus Users

If you use IBus instead, run:

```bash
GTK_IM_MODULE=ibus \
QT_IM_MODULE=ibus \
XMODIFIERS=@im=ibus \
qq --ozone-platform=x11 --app-id=qq
```

**Verify the results:**

- Does QQ launch successfully?
- Are avatars and icons displayed clearly?
- Can you switch input methods and type Chinese normally?

If all three checks pass, you can make the configuration permanent by modifying the desktop launcher.

### 2.3 Permanently Modify the Desktop Launcher

First, find the actual QQ executable path:

```bash
command -v qq
```

If the output is `/usr/local/bin/qq`, edit the system desktop entry:

```bash
sudo nano /usr/share/applications/qq.desktop
```

Find the line beginning with `Exec=` and replace it with the following Fcitx5 configuration:

```ini
Exec=env GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx /usr/local/bin/qq --ozone-platform=x11 --app-id=qq %U
```

For IBus users, replace the three environment variable values with their corresponding IBus settings.

Save the file and launch QQ again from the KDE application menu.

**Note:** The location of the `.desktop` file and the executable path may vary depending on how QQ was installed. Check the actual launcher location before editing it to avoid creating duplicate application entries.

---

## 3. Solution 2: Use Native Wayland Mode

If you prefer running QQ natively on Wayland rather than through Xwayland, try adjusting Electron's launch parameters.

### 3.1 Update the Launch Command

Run:

```bash
qq \
  --enable-features=UseOzonePlatform \
  --ozone-platform=wayland \
  --wayland-text-input-version=3 \
  --force-device-scale-factor=1.0 \
  --app-id=qq
```

The most important parameter to pay attention to is:

```bash
--force-device-scale-factor=1.0
```

### 3.2 Why Use a Scale Factor of 1.0?

If your monitor is already configured for 100% display scaling, Electron generally does not need an additional forced device scale factor.

For example, forcing a scale factor of `1.25` may cause the application to render its interface at a different scale before the desktop compositor adapts it to the actual display configuration.

This can introduce unnecessary image resampling and potentially affect the appearance of bitmap resources such as avatars and icons.

Restoring the scale factor to `1.0` helps avoid this type of scaling inconsistency.

Keep in mind that the actual behavior depends on the Electron version, monitor DPI, KDE scaling configuration, and application implementation. Not every blurry image issue is caused by the device scale factor.

### 3.3 What If the Text Becomes Too Small?

If the chat text looks too small after switching back to `1.0`, avoid immediately increasing Electron's global scale factor.

Instead, try:

- Adjusting the chat font size under **QQ Settings → General**.
- Changing font size or DPI in KDE System Settings.
- Keeping the desktop scaling and Electron device scale factor consistent.

This allows you to adjust text readability without unnecessarily affecting the rendering of the entire application.

---

## 4. Additional Troubleshooting: Clear Old Version Caches

If some avatars remain blurry after changing the launch parameters, the local cache is another area worth investigating.

If the issue started after upgrading QQ, an incompatible cache or configuration left behind by an older version may also be worth ruling out.

You can test this by resetting the QQ configuration and allowing the application to regenerate its local data.

### 4.1 Completely Exit QQ

Make sure QQ is fully closed before modifying its configuration directory. This prevents running processes from continuing to write to the old configuration.

### 4.2 Back Up the Existing Configuration

Run:

```bash
mv ~/.config/QQ ~/.config/QQ.bak
```

This renames the existing configuration directory to `QQ.bak` rather than permanently deleting it.

**Important:** If `QQ.bak` already exists, choose another backup name first. The actual configuration directory may also have a different name depending on the installation package, so verify that the directory exists before running the command.

### 4.3 Restart QQ

Launch QQ again and scan the QR code to log in.

The application should generate a new configuration and cache based on the current environment.

If resetting the configuration does not solve the problem, close QQ and restore the previous configuration before continuing with other troubleshooting steps:

```bash
mv ~/.config/QQ.bak ~/.config/QQ
```

---

## 5. Final Recommendations

When Linux QQ 3.2.35 displays blurry avatars, distorted icons, or input method problems on Ubuntu KDE, start by investigating the graphics backend and display scaling configuration.

| Running Mode | Main Characteristics | Recommended Use Case |
|---|---|---|
| X11 (Xwayland) | May improve image rendering; requires correct input method environment variables | Prioritizing image clarity |
| Native Wayland | Uses the Wayland input method protocol and avoids Xwayland dependency | Preferring native Wayland integration |

**My recommendations:**

- If image clarity is your priority, try Solution 1 first.
- If you prefer native Wayland, try Solution 2 and start with a scale factor of `1.0`.
- If neither solution works, investigate QQ's local cache, Electron version, and KDE display scaling settings.

Keep in mind that Linux distributions, input method frameworks, and Electron versions can behave differently. These launch parameters are not guaranteed to work in every desktop environment or hardware configuration.

Hopefully, this troubleshooting guide helps other Linux users avoid spending hours dealing with the same issues.