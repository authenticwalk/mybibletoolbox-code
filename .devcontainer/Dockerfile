FROM python:3.11

# Install build tools for native npm modules (like better-sqlite3)
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    gnupg \
    sudo \
    build-essential \
    python3-dev \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20 (using NodeSource repository)
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    NODE_MAJOR=20 && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=devuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to non-root user to install tools in user space
USER $USERNAME
WORKDIR /home/$USERNAME

# Configure NPM to use user directory to avoid permission issues with auto-updates
ENV NPM_CONFIG_PREFIX=/home/$USERNAME/.npm-global
ENV PATH=$PATH:/home/$USERNAME/.npm-global/bin

# Install Claude Code globally (as user)
RUN mkdir -p ~/.npm-global && \
    npm install -g @anthropic-ai/claude-code

# Set working directory
WORKDIR /workspace

# Verify installations
RUN python --version && \
    node --version && \
    npm --version && \
    claude --version

# Default command
CMD ["bash"]
