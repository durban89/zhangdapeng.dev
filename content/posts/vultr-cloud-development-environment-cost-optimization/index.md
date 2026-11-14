+++
title = "Optimizing Vultr Cloud Development Costs: On-Demand Provisioning with Terraform, Cloud-init, and GitHub"
slug = "vultr-cloud-development-environment-cost-optimization"
date = 2026-11-14T17:20:00+08:00
lastmod = 2026-11-14T17:20:00+08:00
draft = false
description = "Learn how to eliminate idle Vultr Block Storage costs and rebuild your cloud development environment on demand using Terraform, Cloud-init, GitHub Dotfiles, and SSH Agent Forwarding."
summary = "Vultr Block Storage can continue generating charges even when your development environment is idle. This guide explains how to replace persistent storage with automated provisioning using Terraform, Cloud-init, GitHub Dotfiles, and SSH Agent Forwarding, creating a secure and reproducible cloud development environment."
tags = ["Vultr", "Terraform", "Cloud-init", "GitHub", "SSH", "DevOps", "Linux"]
categories = ["Development"]

image = "cover.png"
image_alt = "Optimizing Vultr cloud development costs with Terraform, Cloud-init, and GitHub automated provisioning"

+++

## 1. The Problem: Idle Cloud Storage Still Costs Money

When building a personal cloud development environment with a Vultr VPS, you may purchase additional Block Storage to store development tools, project files, and environment configurations.

This approach has an obvious advantage: even if you rebuild your VPS, your data and development environment can remain intact.

However, there is a downside for developers who only use their cloud servers occasionally.

**Block Storage can continue generating charges as long as the storage resource exists, even when it is not mounted or actively used.**

A typical cloud development environment might include:

- Ubuntu Linux
- Zsh and Oh My Zsh
- Tmux and its plugin configurations
- Android SDK and related development tools
- OpenCode and other AI coding tools
- Git repositories and personal projects

Most of these components can be reinstalled automatically through scripts.

Furthermore, if your project code is already hosted on GitHub, there may be very little data that actually needs to remain on persistent cloud storage.

Instead of paying for idle storage, a more cost-effective approach is to redesign the environment:

**Create the development environment when needed and destroy it when it is no longer in use.**

## 2. Identify Which Data Actually Needs to Persist

Before changing your infrastructure, separate persistent data from components that can be recreated.

| Resource | Needs Persistence? | Recommended Approach |
| --- | --- | --- |
| Project source code | No | GitHub |
| `.zshrc` | No | GitHub Dotfiles |
| `.tmux.conf` | No | GitHub Dotfiles |
| Oh My Zsh | No | Install through initialization scripts |
| Tmux plugins | No | Install through TPM |
| Android SDK | Depends | Reinstall through scripts |
| OpenCode | Depends | Reinstall through scripts |
| OpenCode history | Depends | Back up important records |
| SSH private keys | Yes | Store locally and securely |
| Terraform configuration | Yes | GitHub |

One important consideration is Android SDK.

The SDK can consume a significant amount of disk space, and downloading it every time you recreate a server may increase initialization time and network usage.

However, if you only use the environment occasionally, reinstalling it may still be more economical than maintaining continuously billed Block Storage.

Also, OpenCode configurations, authentication information, and conversation history may be stored in different directories. Do not blindly upload your entire home directory to a public repository.

Decide which data actually needs to be preserved.

## 3. Manage Development Configurations with GitHub Dotfiles

Many Linux development configurations are independent of the underlying server.

For example:

- `.zshrc`
- `.tmux.conf`
- `.gitconfig`
- Oh My Zsh plugin configurations
- Tmux TPM plugin lists

These files can be managed in a dedicated GitHub repository.

A simple structure might look like this:

```text
dotfiles/
├── .zshrc
├── .tmux.conf
├── .gitconfig
└── README.md
```

If the repository contains no sensitive information, consider making it public.

This eliminates the need for SSH keys or GitHub tokens when downloading your configurations.

Simply execute:

```bash
git clone https://github.com/USERNAME/dotfiles.git
```

Then create symbolic links:

```bash
ln -sf ~/dotfiles/.zshrc ~/.zshrc
ln -sf ~/dotfiles/.tmux.conf ~/.tmux.conf
ln -sf ~/dotfiles/.gitconfig ~/.gitconfig
```

The main advantage of symbolic links is that you only need to maintain one copy of each configuration file.

Whenever you update a configuration, commit and push the changes to GitHub.

The next time you provision a server, you can restore the latest configurations automatically.

**Important:** Only publish non-sensitive configurations. Never commit API keys, passwords, access tokens, private server information, or SSH private keys.

## 4. Automatically Initialize the Development Environment with Cloud-init

Once your Dotfiles repository is ready, the next step is automating software installation.

Vultr supports Cloud-init, which allows you to execute initialization tasks when a new instance starts for the first time.

You can put the installation commands into a Shell script and pass the Cloud-init configuration to your instance through Terraform's `user_data` attribute.

### 4.1 Create the Initialization Script

Create the following file:

```text
scripts/
└── init.sh
```

Example:

```bash
#!/usr/bin/env bash

set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

DEV_USER="developer"
DEV_HOME="/home/${DEV_USER}"

echo "Starting development environment initialization..."

# 1. Install basic packages
apt-get update

apt-get install -y \
    git \
    curl \
    wget \
    unzip \
    zip \
    zsh \
    tmux \
    ca-certificates \
    build-essential

# 2. Install Oh My Zsh
if [ ! -d "${DEV_HOME}/.oh-my-zsh" ]; then
    su - "${DEV_USER}" -c \
      'RUNZSH=no CHSH=no KEEP_ZSHRC=yes \
      sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
fi

# 3. Clone Dotfiles
if [ ! -d "${DEV_HOME}/dotfiles" ]; then
    su - "${DEV_USER}" -c \
      'git clone https://github.com/USERNAME/dotfiles.git ~/dotfiles'
fi

# 4. Link configuration files
if [ -f "${DEV_HOME}/dotfiles/.zshrc" ]; then
    ln -sf "${DEV_HOME}/dotfiles/.zshrc" "${DEV_HOME}/.zshrc"
fi

if [ -f "${DEV_HOME}/dotfiles/.tmux.conf" ]; then
    ln -sf "${DEV_HOME}/dotfiles/.tmux.conf" "${DEV_HOME}/.tmux.conf"
fi

# 5. Install TPM
if [ ! -d "${DEV_HOME}/.tmux/plugins/tpm" ]; then
    su - "${DEV_USER}" -c \
      'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm'
fi

chown -R "${DEV_USER}:${DEV_USER}" "${DEV_HOME}/dotfiles"
chown -R "${DEV_USER}:${DEV_USER}" "${DEV_HOME}/.tmux"

echo "Development environment initialization completed."
```

Replace `USERNAME` with your actual GitHub username.

This example assumes that the `developer` user has already been created through Cloud-init.

You can extend the script with additional installation steps for Android SDK, OpenCode, and other development tools.

There is no need to install everything if you only need a lightweight development environment.

### 4.2 Create the Development User with Cloud-init

It is a good idea to separate user creation from the initialization script.

Create:

```text
cloud-init.yaml
```

Example:

```yaml
#cloud-config

users:
  - name: developer
    groups:
      - sudo
    shell: /bin/zsh
    sudo: ALL=(ALL) NOPASSWD:ALL

package_update: true

write_files:
  - path: /usr/local/bin/init-dev.sh
    permissions: '0755'
    owner: root:root
    content: |
      #!/usr/bin/env bash
      set -euo pipefail

      # Insert initialization commands here.
      echo "Initializing development environment..."

runcmd:
  - [bash, /usr/local/bin/init-dev.sh]
```

In an actual deployment, you can place the contents of `init.sh` inside the Cloud-init configuration or download and execute the initialization script through another mechanism.

Keep in mind that Cloud-init generally runs its first-boot initialization tasks once per instance. It should not be treated as a regular startup script that executes every time the server reboots.

## 5. Provision Vultr Instances with Terraform

Once the initialization scripts are ready, Terraform can manage the Vultr infrastructure.

A simple project structure might look like this:

```text
vultr-dev-environment/
├── main.tf
├── variables.tf
├── terraform.tfvars
├── cloud-init.yaml
├── scripts/
│   └── init.sh
└── .gitignore
```

### 5.1 Configure Terraform

Create `main.tf`:

```hcl
resource "vultr_instance" "dev_vm" {
  plan        = var.instance_plan
  region      = var.region
  os_id       = var.os_id
  label       = "dev-environment"

  user_data = file("${path.module}/cloud-init.yaml")
}
```

Create `variables.tf`:

```hcl
variable "instance_plan" {
  type    = string
  default = "YOUR_PLAN"
}

variable "region" {
  type    = string
  default = "YOUR_REGION"
}

variable "os_id" {
  type = number
}
```

Use a currently supported Vultr Plan, Region, and Operating System ID.

### 5.2 Create the VPS

Run:

```bash
terraform init

terraform plan

terraform apply
```

Terraform will provision the Vultr instance and pass the Cloud-init configuration to the server.

After the instance starts, Cloud-init will automatically execute the initialization tasks.

Check the initialization status:

```bash
cloud-init status --long
```

Monitor the initialization logs:

```bash
tail -f /var/log/cloud-init-output.log
```

With this setup, your basic development environment can be automatically restored whenever you create a new instance.

## 6. SSH Key Security: How to Push Code from a Cloud Server

The previous steps solve the environment initialization and GitHub repository cloning problems.

However, there is another practical requirement:

**What if you want to modify code on your Vultr VPS and push those changes directly to GitHub?**

This is where SSH key management becomes particularly important.

### 6.1 Avoid Injecting Personal SSH Private Keys Through Terraform user_data

One seemingly straightforward approach is to read your local SSH private key through Terraform:

```hcl
user_data = templatefile(
  "${path.module}/init.tftpl",
  {
    ssh_private_key = file(
      pathexpand("~/.ssh/id_ed25519")
    )
  }
)
```

Then write the key to the remote server:

```bash
mkdir -p ~/.ssh

chmod 700 ~/.ssh

cat > ~/.ssh/id_ed25519 <<'EOF'
${ssh_private_key}
EOF

chmod 600 ~/.ssh/id_ed25519
```

Although this approach works technically, it is not recommended for your primary personal SSH key.

There are several security concerns:

1. Terraform State may contain sensitive instance configuration.
2. Instance initialization data may be accessible through cloud-provider metadata interfaces.
3. Cloud-init and system logs may retain initialization content.
4. Other users with sufficient server privileges may be able to read the private key.

Even if you mark a Terraform variable as `sensitive = true`, that does not prevent its value from being stored in Terraform State.

Therefore, avoid injecting your personal SSH private key directly through `user_data`.

### 6.2 Recommended Approach: SSH Agent Forwarding

If you only need to perform Git Pull and Git Push operations temporarily from a remote server, SSH Agent Forwarding is a better option.

Its working principle is simple:

- Your SSH private key remains on your local computer.
- Your local computer starts `ssh-agent` and loads the SSH key.
- When connecting to the remote server, you enable Agent Forwarding.
- The remote server temporarily uses your local SSH agent for authentication.
- The private key itself is never copied to the remote server.

The architecture looks like this:

```text
Local Computer
    |
    | SSH Private Key
    |
    v
  ssh-agent
    |
    | SSH Agent Forwarding
    |
    v
Vultr VPS
    |
    | Git SSH Authentication
    |
    v
  GitHub
```

#### Step 1: Start ssh-agent Locally

On macOS or Linux:

```bash
eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519
```

On Windows PowerShell:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic

Start-Service ssh-agent

ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

Make sure the corresponding public key has already been added to your GitHub account.

#### Step 2: Connect to the VPS with Agent Forwarding

Run:

```bash
ssh -A developer@YOUR_VULTR_IP
```

Alternatively, configure your local SSH client in `~/.ssh/config`:

```sshconfig
Host vultr-dev
    HostName YOUR_VULTR_IP
    User developer
    IdentityFile ~/.ssh/id_ed25519
    ForwardAgent yes
```

Then connect using:

```bash
ssh vultr-dev
```

#### Step 3: Verify Agent Forwarding

After logging into your Vultr server, run:

```bash
echo $SSH_AUTH_SOCK
```

If a socket path is returned, Agent Forwarding is available in your session.

Next, test GitHub authentication:

```bash
ssh -T git@github.com
```

If authentication succeeds, you can perform normal Git operations:

```bash
git clone git@github.com:USERNAME/PROJECT.git

cd PROJECT

git add .

git commit -m "Update project"

git push
```

**Important security considerations:**

SSH Agent Forwarding does not copy your private key to the server. However, a malicious process with sufficient access to your remote session may be able to use the forwarded agent while the connection is active.

Therefore:

- Only enable Agent Forwarding for servers you trust.
- Never enable it on untrusted machines.
- Avoid running untrusted applications with root privileges.
- Disconnect the SSH session when you no longer need it.

### 6.3 Alternative: Use a Dedicated SSH Deploy Key

If you want the server to perform Git operations independently without relying on your local computer, consider using a dedicated SSH Deploy Key for a specific repository.

Generate a new key pair:

```bash
ssh-keygen -t ed25519 \
  -f ~/.ssh/github_deploy_key \
  -C "vultr-dev-environment"
```

Add the public key to the corresponding GitHub repository:

Settings → Deploy keys.

If you need to push code, enable:

`Allow write access`

This gives the key access to the specific repository rather than granting it access to all your GitHub repositories.

A Deploy Key does not automatically have write permissions. You must explicitly enable them.

However, remember that a compromised server could potentially use a write-enabled Deploy Key to modify the associated repository.

For development environments that are frequently created and destroyed, SSH Agent Forwarding is generally more suitable for temporary Git operations.

## 7. Destroy Cloud Resources When They Are No Longer Needed

Once the environment is fully automated, you can adopt an on-demand workflow.

When you no longer need your development server, run:

```bash
terraform destroy
```

Terraform will destroy the resources managed by the current configuration.

One important detail:

**Whether Block Storage is destroyed depends on whether it is managed by the current Terraform configuration and how the resources are defined.**

If the Block Storage volume was purchased separately through the Vultr dashboard, you may need to manage and delete it separately.

Before destroying your resources:

1. Make sure all important code has been pushed to GitHub.
2. Check for uncommitted local changes.
3. Back up important OpenCode history and other personal data.
4. Confirm that the Block Storage volume contains nothing you need to retain.
5. Verify exactly which resources will be destroyed.

If you need to preserve a small amount of data from the volume, back it up locally or to another storage location before deleting the original Block Storage.

Snapshots are another possible backup option, but check Vultr's current snapshot pricing and retention charges first. Do not assume snapshots are free.

## 8. Final Architecture: On-Demand Provisioning and Destruction

After these changes, your cloud development environment can follow this architecture:

```text
                 GitHub
                   |
          +--------+--------+
          |                 |
       Projects          Dotfiles
          |                 |
          +--------+--------+
                   |
                   v
              Terraform
                   |
                   v
                Vultr
                   |
             Cloud-init
                   |
          +--------+--------+
          |        |        |
         Zsh     Tmux   Android SDK
          |        |        |
          +--------+--------+
                   |
                OpenCode
                   |
                   v
             Development
```

The workflow is straightforward.

### When You Need the Environment

1. Run `terraform apply`.
2. Terraform provisions a new Vultr instance.
3. Cloud-init automatically installs the required software.
4. GitHub Dotfiles are cloned.
5. Zsh, Tmux, and other development tools are configured.
6. Connect through SSH and start developing.

### When You No Longer Need the Environment

1. Commit and push your changes to GitHub.
2. Back up any personal data that needs to be retained.
3. Run `terraform destroy`.
4. Verify that unnecessary billable resources no longer exist in Vultr.

Whenever you need the environment again, simply provision a new instance.

## 9. Conclusion

For individual developers, there is no reason to keep every cloud development environment running permanently.

There is also no need to pay continuously for persistent storage when most of the environment can be recreated automatically.

If your project code is already hosted on GitHub and your development configurations are managed through Dotfiles, most of your environment can be rebuilt using automation scripts.

The key components of this approach are:

- **GitHub:** Stores project source code and personal configurations.
- **Terraform:** Manages cloud infrastructure.
- **Cloud-init:** Automatically initializes the Linux development environment.
- **SSH Agent Forwarding:** Enables Git authentication without copying your personal private key to the server.
- **Terraform Destroy:** Removes unnecessary cloud resources when the environment is no longer needed.

The goal is not to keep a complete development environment permanently stored on a cloud server.

Instead, it is to make the environment reproducible, portable, and disposable.

**For developers who only use cloud environments occasionally, this approach can significantly reduce idle infrastructure costs while making development environments easier to maintain and rebuild.**