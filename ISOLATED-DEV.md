# Isolated Development Environment

This setup provides a **secure, isolated container** for running dangerous AI commands safely.

## Quick Start

```bash
./dev-shell.sh
```

This opens a bash shell inside an isolated container where you can run any commands safely.

## What's Protected

Your Mac is protected from:
- ✅ File system modifications (only this project folder is accessible)
- ✅ Installing system packages
- ✅ Modifying system settings
- ✅ Access to other files on your Mac
- ✅ Resource exhaustion (12GB RAM limit, 4 CPU limit)
- ✅ Privilege escalation (no-new-privileges security option)

## Inside the Container

You run as **`devuser`** (non-root) for security, but have sudo access if needed.

Once inside, you can:

```bash
# Install Python packages (isolated from your Mac)
pip install -r requirements.txt

# Run any Python code
python your_script.py

# Run dangerous AI commands safely
python dangerous_ai_agent.py

# Use Claude Code
npx @anthropic-ai/claude-code --help

# Install system tools if needed (use sudo)
sudo apt-get update && sudo apt-get install -y whatever

# Check your user
whoami  # shows: devuser

# Exit when done
exit
```

## Network Isolation (Optional)

To completely isolate from the internet, edit `dev-shell.sh` and add:

```bash
--network=none \
```

## Container Management

```bash
# See running containers
docker ps

# Stop a container
docker stop <container-id>

# Clean up stopped containers
docker container prune
```

## Safety Features

The container has:
- **No root access to host** - can't modify your Mac
- **Dropped capabilities** - minimal Linux permissions
- **Resource limits** - can't consume all your RAM/CPU
- **Isolated filesystem** - only sees this project folder
- **Destroyed on exit** - no persistent changes (unless in project folder)

## Your Files

- ✅ Files in `/workspace` (this project) are saved on your Mac
- ❌ Everything else in the container is destroyed when you exit

