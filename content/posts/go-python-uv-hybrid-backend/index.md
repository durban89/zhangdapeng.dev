+++
title = "Building a Hybrid Go and Python Backend with uv"
description = "Learn how to manage Python dependencies with uv, integrate Python AI agents into a Go backend, and handle Unicode JSON output correctly."
image = "./go-python-uv-hybrid-backend.png"
image_alt = "Hybrid Go and Python backend architecture with uv"
date = 2026-11-03T16:00:00+08:00
lastmod = 2026-11-03T16:00:00+08:00
slug = "go-python-uv-hybrid-backend"
categories = ["Development", "Linux"]
tags = ["Go", "Python", "uv", "Backend", "AI Agents"]
keywords = ["Go Python integration", "Python uv", "Go subprocess", "Python dependency management", "Hybrid backend architecture"]
draft = true

toc = true

math = true

+++

# Building a Hybrid Go and Python Backend with uv

Modern backend systems don't always need to rely on a single programming language.

Go is an excellent choice for backend services, offering efficient concurrency, fast execution, and straightforward deployment. Python, meanwhile, has a mature ecosystem for AI agents, LLM integrations, machine learning, and data processing.

Combining these two languages can provide a practical architecture: Go handles backend orchestration, while Python executes specialized AI and data-processing tasks.

However, managing Python dependencies, integrating subprocess execution, and handling JSON output correctly can introduce unnecessary complexity.

In this article, we'll explore how to modernize a Python environment using **uv**, integrate Python scripts into a Go backend, and solve a common Unicode encoding issue.

## 1. Modernizing Python Dependency Management

Traditionally, Python projects often use several independent tools:

- `pip` for installing packages.
- `requirements.txt` for recording dependencies.
- `venv` for managing virtual environments.
- `pyenv` for managing Python versions.

Although this setup works, maintaining multiple configuration files and tools can become inconvenient as a project grows.

### pyproject.toml: A Unified Configuration

The modern Python ecosystem increasingly uses `pyproject.toml` as the central project configuration file.

It is defined through Python packaging standards, including PEP 518 and PEP 621.

A typical project configuration looks like this:

```toml
[project]
name = "ai-agent"
version = "0.1.0"
description = "Python AI agent services"
requires-python = ">=3.11"
dependencies = [
    "openai",
    "pydantic",
]
```

Compared with a standalone `requirements.txt`, `pyproject.toml` provides a structured place to define:

- Project metadata.
- Python version requirements.
- Runtime dependencies.
- Optional dependencies.
- Development dependency groups.
- Build system configuration.

For modern Python applications, it is a good choice as the primary project configuration.

### Why Choose uv?

[uv](https://docs.astral.sh/uv/) is a Python package and project management tool developed by Astral.

Written in Rust, it provides a fast alternative to several traditional Python tools.

| Feature | Traditional tools | uv |
|---|---|---|
| Package installation | pip | Built-in |
| Virtual environments | venv | Built-in |
| Python version management | pyenv | Built-in |
| Dependency locking | Additional tools | Built-in |
| Project configuration | Multiple files | pyproject.toml |
| Dependency resolution | pip | Integrated resolver |

One of its biggest advantages is that it brings these workflows together in a single command-line tool.

It also supports dependency locking through `uv.lock`, helping developers reproduce consistent environments across machines.

## 2. Introducing uv into an Existing Python Project

You don't need to create a new repository to adopt uv.

It can be introduced into an existing project without rewriting your Python code.

For example, imagine an existing directory:

```text
my-project/
├── main.go
├── agent_demo.py
├── ai_engine.py
└── .deepseek-env/
```

The project already contains working Python scripts and an older virtual environment.

Here's how to migrate it safely.

### Step 1: Install uv on Linux

Run the official installation command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal or reload your shell configuration if necessary.

Verify the installation:

```bash
uv --version
```

### Step 2: Initialize the Project

Navigate to your existing project directory:

```bash
cd my-project
```

Initialize uv:

```bash
uv init --bare
```

Using `--bare` creates the basic project configuration without generating the usual starter application files.

You should now have:

```text
my-project/
├── main.go
├── agent_demo.py
├── ai_engine.py
├── pyproject.toml
└── .deepseek-env/
```

Your existing source code remains untouched.

### Step 3: Create a New Virtual Environment

Create a new environment:

```bash
uv venv
```

By default, uv creates a `.venv` directory in the project root.

The directory structure becomes:

```text
my-project/
├── main.go
├── agent_demo.py
├── ai_engine.py
├── pyproject.toml
├── uv.lock
├── .venv/
└── .deepseek-env/
```

Keep the old environment temporarily until you've verified that the new environment works correctly.

Once migration is complete, you can remove the obsolete environment.

### Step 4: Install Dependencies

Instead of manually editing `requirements.txt`, use:

```bash
uv add openai pydantic
```

uv will:

1. Add the dependencies to `pyproject.toml`.
2. Resolve compatible package versions.
3. Update `uv.lock`.
4. Install the packages into the project environment.

For development dependencies, you can use:

```bash
uv add --dev pytest ruff
```

You now have a reproducible Python dependency configuration.

To install the project dependencies on another machine:

```bash
uv sync
```

This uses the project's configuration and lockfile to synchronize the environment.

## 3. Integrating Python AI Agents with a Go Backend

Now let's look at the more interesting part: running Python AI agents from a Go backend.

Consider a hybrid architecture:

```text
                 Go Backend
                     |
                     |
               Task Orchestrator
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Agent A    Agent B    Agent C
          |          |          |
          v          v          v
       Python     Python     Python
       Script     Script     Script
```

Go handles task orchestration and backend operations, while Python handles AI-related workloads.

Go provides the `os/exec` package for launching external processes.

There are two practical ways to execute Python scripts.

### Approach A: Execute Through uv run

This is generally the simplest approach.

```go
package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("uv", "run", "agent_demo.py")

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Execution error: %v\n", err)
		fmt.Println(string(output))
		return
	}

	fmt.Println(string(output))
}
```

The advantage is that you don't need to manually activate the virtual environment.

uv can locate the project configuration, synchronize the environment when needed, and execute the script using the project's environment.

This approach is particularly convenient during development.

One important detail: make sure the Go process runs with the correct working directory. Otherwise, uv may not find the intended `pyproject.toml`.

For production applications, you should also consider controlling when dependency synchronization occurs rather than relying on automatic synchronization for every execution.

### Approach B: Execute the Virtual Environment's Python Directly

If the environment has already been prepared and you want to avoid uv's runtime project checks, invoke the Python executable directly.

```go
package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command(
		"./.venv/bin/python",
		"agent_demo.py",
	)

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Execution error: %v\n", err)
		fmt.Println(string(output))
		return
	}

	fmt.Println(string(output))
}
```

This approach has several advantages:

- No need to activate the virtual environment.
- No need to invoke uv for every execution.
- Direct access to the project's isolated Python environment.
- Predictable execution when the deployment environment is configured correctly.

For production deployments, this is often a good option when the environment is provisioned in advance.

Note that the executable path above is Linux-specific. Windows and macOS deployments may require different paths.

### Which Approach Should You Choose?

| Scenario | Recommended approach |
|---|---|
| Local development | `uv run` |
| Simple script execution | `uv run` |
| Preconfigured production environment | Direct Python executable |
| Frequent subprocess execution | Direct Python executable |
| Automatic environment management | `uv run` |

Both approaches are valid. The right choice depends on how much control you need over the execution environment.

## 4. Fixing Unicode JSON Output Between Python and Go

Another issue that can appear in hybrid Go and Python applications involves Unicode characters.

Suppose a Python agent returns JSON containing Chinese text or emojis.

For example:

```python
import json

data = {
    "agent": "system",
    "content": "🎯 成功接收业务新指令"
}

print(json.dumps(data))
```

The output may look like this:

```json
{
  "agent": "system",
  "content": "\ud83c\udfaf \u6210\u529f\u63a5\u6536\u4e1a\u52a1\u65b0\u6307\u4ee4"
}
```

This is valid JSON, but it isn't particularly convenient when reading logs or debugging subprocess output.

### Understanding the Root Cause

By default, Python's `json.dumps()` uses:

```python
ensure_ascii=True
```

This causes non-ASCII characters to be represented using Unicode escape sequences.

For example:

```text
成功
```

becomes:

```text
\u6210\u529f
```

This behavior is valid and does not mean that the data has been corrupted.

However, when readable UTF-8 output is preferred, we can change the serialization option.

### The Solution: ensure_ascii=False

Update the Python code:

```python
import json

requirement = "Process Q3 Financial Report"

data = {
    "agent": "system",
    "content": f"🎯 成功接收业务新指令: {requirement}"
}

print(
    json.dumps(data, ensure_ascii=False),
    flush=True
)
```

Now the output contains readable Unicode characters:

```json
{
  "agent": "system",
  "content": "🎯 成功接收业务新指令: Process Q3 Financial Report"
}
```

The important setting is:

```python
ensure_ascii=False
```

This tells Python to output non-ASCII characters directly rather than escaping them.

### Reading the JSON in Go

Go's standard JSON library supports UTF-8 JSON strings natively.

You can decode the output directly:

```go
package main

import (
	"encoding/json"
	"fmt"
	"os/exec"
)

type AgentResponse struct {
	Agent   string `json:"agent"`
	Content string `json:"content"`
}

func main() {
	cmd := exec.Command(
		"./.venv/bin/python",
		"agent_demo.py",
	)

	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Execution error:", err)
		return
	}

	var response AgentResponse

	if err := json.Unmarshal(output, &response); err != nil {
		fmt.Println("JSON parsing error:", err)
		return
	}

	fmt.Println("Agent:", response.Agent)
	fmt.Println("Content:", response.Content)
}
```

Go can correctly decode both escaped Unicode JSON and raw UTF-8 JSON.

Therefore, `ensure_ascii=False` is primarily a readability improvement, not a mandatory compatibility fix.

**Important:** If you're using stdout as a machine-readable communication channel, keep it clean. Send diagnostic logs to stderr and reserve stdout for structured JSON responses. This becomes especially important when multiple Python agents communicate with a Go orchestrator.

## 5. Production Considerations

The combination of Go, Python, and uv provides a convenient architecture, but a few additional practices are important before deploying it.

### Keep Dependencies Reproducible

Commit both files to version control:

```text
pyproject.toml
uv.lock
```

This ensures that the project configuration and resolved dependency versions are available to other developers and deployment environments.

### Avoid Installing Dependencies at Runtime

For production, prepare the Python environment during deployment or image building.

For example:

```bash
uv sync --locked
```

This ensures that the installed dependencies are consistent with the committed lockfile.

### Handle Subprocess Errors Properly

Don't ignore errors returned by `exec.Command`.

Consider:

- Process exit codes.
- Standard output and standard error.
- Execution timeouts.
- Process termination.
- Retry strategies where appropriate.

For long-running AI tasks, Go's `context` package can also help control subprocess execution.

### Consider Process Reuse for Heavy Workloads

Launching a new Python process for every request introduces startup overhead.

For lightweight tasks, subprocess execution is often sufficient.

For high-throughput workloads, consider keeping Python workers alive and communicating through a structured protocol such as HTTP, gRPC, or message queues.

This can reduce repeated initialization costs and improve resource management.

## 6. Conclusion

Building a hybrid Go and Python backend doesn't have to mean maintaining two complicated development environments.

With uv and `pyproject.toml`, Python dependency management becomes simpler and more reproducible.

Go's `os/exec` package provides a straightforward way to integrate Python AI agents into an existing backend without manually activating virtual environments.

And by understanding Python's Unicode serialization behavior, you can make communication between the two languages easier to debug and maintain.

The key takeaways are:

1. Use `pyproject.toml` as the central configuration for modern Python projects.
2. Use uv to manage dependencies, virtual environments, and lockfiles.
3. Use `uv run` for convenient development execution.
4. Use the virtual environment's Python executable for preconfigured production execution.
5. Use `ensure_ascii=False` when readable Unicode JSON output is desired.
6. Keep subprocess communication structured and handle errors explicitly.

Combining Go's backend capabilities with Python's AI ecosystem gives developers a flexible foundation for building practical AI-powered applications.

You don't need to force everything into one language. Sometimes, choosing the right tool for each responsibility is the better engineering decision.
