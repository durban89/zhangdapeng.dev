+++
title = "Laravel 12 Docker Deployment: Troubleshooting Missing Storage Directories"
date = 2026-11-20T15:00:00+08:00
lastmod = 2026-11-20T15:00:00+08:00
draft = false
description = "Learn why Laravel 12 storage directories disappear during Git and Docker deployments, how Git ignore rules and Docker volume mounts cause the problem, and how to fix it reliably."
slug = "laravel-12-docker-storage-directory-missing"
tags = ["Laravel", "Laravel 12", "Docker", "Git", "DevOps"]
categories = ["Development"]

image = "cover.png"
image_alt = "Laravel 12 Docker deployment troubleshooting, illustrating missing storage directories, Git ignore rules, Docker volumes, and deployment best practices."
+++

## 1. Background

While working with Laravel projects, I repeatedly encountered a strange issue:

Some subdirectories under the `storage` directory were missing after pulling code from Git or rebuilding and starting Docker containers.

For example:

- `storage/framework/cache/data`
- `storage/framework/sessions`
- `storage/framework/views`
- `storage/app/private`
- `storage/app/public`
- `storage/logs`

These directories usually exist when a Laravel project is initialized locally, but they may disappear after deployment.

When Laravel tries to write cache files, sessions, compiled Blade templates, or application logs, this can result in errors such as:

```text
Please provide a valid cache path.
```

After investigating the issue, I found that it is usually not caused by a Laravel initialization failure. Instead, it is related to how Git handles empty directories and how Docker volume mounts work.

## 2. Why Doesn't Git Preserve Empty Storage Directories?

Git does not track empty directories. It only tracks files.

Many subdirectories inside Laravel's `storage` directory are initially empty. They are intended to store runtime-generated files such as caches, logs, sessions, and temporary data.

If a directory does not contain any tracked files, Git will not include it in the repository.

For example:

```text
storage/
├── app/
│   ├── private/
│   └── public/
├── framework/
│   ├── cache/
│   │   └── data/
│   ├── sessions/
│   └── views/
└── logs/
```

If these directories are empty, Git will not preserve their structure when committing the project.

As a result, some required directories may be missing after running `git clone` or `git pull` on a server.

### Solution: Use .gitignore Files to Preserve Empty Directories

The recommended approach is to place a `.gitignore` file inside each directory that needs to be preserved.

For example:

```gitignore
*
!.gitignore
```

This configuration means:

- `*`: Ignore all files and subdirectories in the current directory.
- `!.gitignore`: Explicitly keep the `.gitignore` file itself.

This allows Git to preserve the directory structure without committing runtime-generated files.

## 3. Recommended Storage Directory Structure for Laravel 12

For a typical Laravel 12 application, the following directory structure should be preserved:

```text
storage/
├── app/
│   ├── .gitignore
│   ├── private/
│   │   └── .gitignore
│   └── public/
│       └── .gitignore
├── framework/
│   ├── cache/
│   │   ├── .gitignore
│   │   └── data/
│   │       └── .gitignore
│   ├── sessions/
│   │   └── .gitignore
│   └── views/
│       └── .gitignore
└── logs/
    └── .gitignore
```

Different directories require slightly different ignore rules.

### 3.1 storage/app/.gitignore

```gitignore
*
!private/
!public/
!.gitignore
```

This preserves the `private` and `public` directories while ignoring their contents.

### 3.2 storage/framework/cache/.gitignore

```gitignore
*
!data/
!.gitignore
```

This ensures that the `data` directory remains in the repository.

### 3.3 Other Runtime Directories

Create a `.gitignore` file in each of the following directories:

- `storage/app/private/`
- `storage/app/public/`
- `storage/framework/cache/data/`
- `storage/framework/sessions/`
- `storage/framework/views/`
- `storage/logs/`

Use the following content:

```gitignore
*
!.gitignore
```

### 3.4 Create Everything with One Command

Run the following commands from your Laravel project root:

```bash
mkdir -p storage/app/private \
         storage/app/public \
         storage/framework/cache/data \
         storage/framework/sessions \
         storage/framework/views \
         storage/logs

printf "*\n!private/\n!public/\n!.gitignore\n" \
    > storage/app/.gitignore

printf "*\n!data/\n!.gitignore\n" \
    > storage/framework/cache/.gitignore

printf "*\n!.gitignore\n" | tee \
    storage/app/private/.gitignore \
    storage/app/public/.gitignore \
    storage/framework/cache/data/.gitignore \
    storage/framework/sessions/.gitignore \
    storage/framework/views/.gitignore \
    storage/logs/.gitignore > /dev/null
```

After creating these files, check whether Git recognizes them:

```bash
git status --short
```

If some files are still ignored because of global Git ignore rules, you can force-add them:

```bash
git add -f storage/app/.gitignore
git add -f storage/app/private/.gitignore
git add -f storage/app/public/.gitignore
git add -f storage/framework/cache/.gitignore
git add -f storage/framework/cache/data/.gitignore
git add -f storage/framework/sessions/.gitignore
git add -f storage/framework/views/.gitignore
git add -f storage/logs/.gitignore
```

Note that force-adding only addresses the immediate issue. You should still inspect your global Git ignore configuration to avoid unintentionally ignoring other project files.

## 4. Docker Volume Mounts Can Hide Existing Directories

This is another important issue to consider when deploying Laravel with Docker.

For example, your `docker-compose.yml` might contain:

```yaml
services:
  app:
    volumes:
      - ./storage:/var/www/html/storage
```

This is a Docker Bind Mount.

Docker mounts the host's `./storage` directory into the container at `/var/www/html/storage`.

The important detail is:

**A bind mount hides the existing contents of the corresponding directory inside the container. It does not automatically merge the host directory with the container directory.**

Consider the following scenario:

1. Your Dockerfile copies the complete Laravel project into the image.
2. The image originally contains a complete `storage` directory.
3. However, the host's `./storage` directory is empty or missing some subdirectories.
4. When the container starts, the bind mount hides the original `storage` directory contents inside the image.
5. Laravel sees the incomplete directory structure from the host instead.

This explains why a Docker image can be built successfully but still encounter missing directories after the container starts.

### How to Verify Whether a Volume Mount Is the Cause

First, inspect the resolved Docker Compose configuration:

```bash
docker compose config
```

Then inspect the actual container mounts:

```bash
docker inspect <container_name>
```

You can also enter the running container and check the directory structure:

```bash
docker compose exec app ls -la storage/framework
```

If the directories exist in the image but disappear after the container starts, investigate the volume mount configuration first.

## 5. Add a Startup Fallback for Docker Deployments

Besides preserving directories through Git, I recommend automatically checking and creating the required directories whenever the Docker container starts.

Create a file named `docker/entrypoint.sh`:

```bash
#!/bin/sh

set -e

# Create required Laravel storage directories
mkdir -p /var/www/html/storage/app/private \
         /var/www/html/storage/app/public \
         /var/www/html/storage/framework/cache/data \
         /var/www/html/storage/framework/sessions \
         /var/www/html/storage/framework/views \
         /var/www/html/storage/logs

# Fix directory ownership
chown -R www-data:www-data \
    /var/www/html/storage \
    /var/www/html/bootstrap/cache

# Set appropriate permissions
chmod -R 775 \
    /var/www/html/storage \
    /var/www/html/bootstrap/cache

# Execute the original container command
exec "$@"
```

Then configure your Dockerfile:

```dockerfile
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["php-fpm"]
```

Now, whenever the container starts, the entrypoint script will automatically check and recreate the required directories.

**Important considerations:**

- The example assumes your Laravel application is located at `/var/www/html`.
- It assumes PHP-FPM runs as the `www-data` user.
- If you use Alpine-based images or a custom runtime user, adjust the user and group accordingly.
- If your container uses a read-only filesystem, you must configure writable directories separately.
- For production environments with large persistent directories, avoid recursively changing ownership on every startup. Set the initial permissions during image construction whenever possible.

## 6. Additional Considerations for Docker Deployments

### 6.1 Avoid Mounting the Entire Storage Directory Without a Specific Reason

You do not necessarily need to mount the entire `storage` directory to the host.

If you only need to persist uploaded public files, you can mount that specific directory instead:

```yaml
services:
  app:
    volumes:
      - ./storage/app/public:/var/www/html/storage/app/public
```

However, determine whether uploaded files, logs, caches, and other runtime data need persistence based on your deployment architecture.

### 6.2 Understand Docker Volume Initialization

Named volumes behave somewhat differently from bind mounts.

For example:

```yaml
volumes:
  - storage_data:/var/www/html/storage
```

When Docker mounts a new, empty named volume over a non-empty directory in the container, it normally copies the existing contents into the volume.

However, this does not mean Docker automatically synchronizes directory structures every time the container starts.

Once the volume has been initialized, changes to the corresponding directory in a newly built image are not automatically merged into the existing volume.

### 6.3 Check Directory Permissions

Laravel needs write permissions for the following directories:

```text
storage/
bootstrap/cache/
```

Check their permissions inside the container:

```bash
ls -ld storage bootstrap/cache

ls -la storage/framework
```

If necessary, fix them:

```bash
chown -R www-data:www-data storage bootstrap/cache

chmod -R 775 storage bootstrap/cache
```

Avoid using `chmod -R 777` as a quick fix. Production environments should follow the principle of least privilege.

## 7. Lessons Learned

This issue reminded me that maintaining a Laravel project's directory structure is not just a framework initialization concern. It also involves Git version control and Docker deployment behavior.

Here are the key takeaways:

1. **Git does not track empty directories.** Use directory-level `.gitignore` files to preserve the required Laravel directory structure.
2. **Runtime files should not be committed.** Cache files, sessions, logs, and temporary files should remain excluded from Git.
3. **Docker volumes can hide existing container directories.** In particular, bind mounts can make a complete directory inside an image appear incomplete when the host directory is missing files.
4. **Startup scripts should be resilient.** Use `mkdir -p` to recreate required directories and reduce deployment-related issues.
5. **Directory permissions matter.** Ensure the PHP runtime user has appropriate write permissions for `storage` and `bootstrap/cache`.

### Final Recommendations

For Laravel projects deployed with Docker, I recommend combining the following approaches:

- **Git:** Use directory-level `.gitignore` files to preserve required empty directories.
- **Dockerfile:** Create the required directories and configure initial permissions during image construction.
- **Entrypoint:** Use `mkdir -p` as a fallback whenever the container starts.
- **Docker Compose:** Design volume mounts carefully and avoid unnecessary directory overrides.

By addressing these concerns at the source-control, image-build, and container-startup levels, you can prevent missing `storage` directories and avoid repeatedly troubleshooting the same issue across Laravel deployments.