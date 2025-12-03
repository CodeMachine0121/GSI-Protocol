#!/bin/bash

# SDD Workflow Installation Script
# This script installs commands for Claude Code and/or Codex (OpenAI)
# without copying examples or other unnecessary files

set -e

echo "🚀 SDD Workflow Installer"
echo "========================="
echo ""

# Choose AI platform
echo "Select AI platform(s) to install:"
echo "1) Claude Code only"
echo "2) Codex (OpenAI) only"
echo "3) Both Claude Code and Codex"
read -p "Enter choice [1-3]: " platform_choice < /dev/tty

case $platform_choice in
    1)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=false
        ;;
    2)
        INSTALL_CLAUDE=false
        INSTALL_CODEX=true
        ;;
    3)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=true
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""

# Detect installation type
if [ -d ".git" ]; then
    echo "✅ Git repository detected - Installing to current project"
    INSTALL_TYPE="project"
else
    echo "❌ Not a git repository"
    echo ""
    echo "Please choose installation type:"
    echo "1) Install to current directory (manual project)"
    echo "2) Install globally"
    read -p "Enter choice [1-2]: " choice < /dev/tty

    case $choice in
        1)
            INSTALL_TYPE="project"
            ;;
        2)
            INSTALL_TYPE="global"
            ;;
        *)
            echo "Invalid choice. Exiting."
            exit 1
            ;;
    esac
fi

# Set repository URL
REPO_URL="${SDD_REPO_URL:-https://github.com/CodeMachine0121/GSI-Protocol.git}"
echo ""
echo "Repository: $REPO_URL"
echo "(Set SDD_REPO_URL environment variable to override)"
echo ""

# Global installation
if [ "$INSTALL_TYPE" = "global" ]; then
    # Create temp directory for cloning
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT

    echo "📦 Downloading SDD Workflow..."
    git clone --depth 1 "$REPO_URL" "$TEMP_DIR/sdd-workflow"

    TOTAL_FILES=0

    # Install Claude Code commands
    if [ "$INSTALL_CLAUDE" = true ]; then
        CLAUDE_DIR="$HOME/.claude/commands"
        echo "Installing Claude Code commands to: $CLAUDE_DIR"
        mkdir -p "$CLAUDE_DIR"
        cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md "$CLAUDE_DIR/"
        CLAUDE_COUNT=$(ls -1 "$CLAUDE_DIR"/sdd-*.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
        echo "✅ Installed $CLAUDE_COUNT Claude Code command files"
    fi

    # Install Codex commands
    if [ "$INSTALL_CODEX" = true ]; then
        CODEX_DIR="$HOME/.codex/commands"
        echo "Installing Codex commands to: $CODEX_DIR"
        mkdir -p "$CODEX_DIR"
        cp "$TEMP_DIR/sdd-workflow/.codex/commands"/*.md "$CODEX_DIR/"
        CODEX_COUNT=$(ls -1 "$CODEX_DIR"/sdd-*.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + CODEX_COUNT))
        echo "✅ Installed $CODEX_COUNT Codex command files"
    fi

    echo ""
    echo "✅ Global installation complete!"
    echo "Total files installed: $TOTAL_FILES"
    echo ""
    echo "You can now use SDD commands in any project:"
    echo "  /sdd-auto <requirement>"
    echo "  /sdd-spec <requirement>"
    echo "  /sdd-arch <feature.feature>"
    echo "  /sdd-impl <feature.feature>"
    echo "  /sdd-verify <feature.feature>"
    echo ""
    exit 0
fi

# Project installation
echo "Installing to current project..."
echo ""

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "📦 Downloading SDD Workflow..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR/sdd-workflow"

TOTAL_FILES=0

# Install Claude Code commands
if [ "$INSTALL_CLAUDE" = true ]; then
    if [ -d ".claude/commands" ]; then
        read -p "⚠️  .claude/commands already exists. Overwrite? [y/N]: " confirm < /dev/tty
        if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            echo "Skipping Claude Code installation."
        else
            mkdir -p .claude/commands
            echo "📋 Copying Claude Code command files..."
            cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md .claude/commands/
            CLAUDE_COUNT=$(ls -1 .claude/commands/*.md 2>/dev/null | wc -l)
            TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
            echo "✅ Installed $CLAUDE_COUNT Claude Code files"
        fi
    else
        mkdir -p .claude/commands
        echo "📋 Copying Claude Code command files..."
        cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md .claude/commands/
        CLAUDE_COUNT=$(ls -1 .claude/commands/*.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
        echo "✅ Installed $CLAUDE_COUNT Claude Code files"
    fi
fi

# Install Codex commands
if [ "$INSTALL_CODEX" = true ]; then
    if [ -d ".codex/commands" ]; then
        read -p "⚠️  .codex/commands already exists. Overwrite? [y/N]: " confirm < /dev/tty
        if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            echo "Skipping Codex installation."
        else
            mkdir -p .codex/commands
            echo "📋 Copying Codex command files..."
            cp "$TEMP_DIR/sdd-workflow/.codex/commands"/*.md .codex/commands/
            CODEX_COUNT=$(ls -1 .codex/commands/*.md 2>/dev/null | wc -l)
            TOTAL_FILES=$((TOTAL_FILES + CODEX_COUNT))
            echo "✅ Installed $CODEX_COUNT Codex files"
        fi
    else
        mkdir -p .codex/commands
        echo "📋 Copying Codex command files..."
        cp "$TEMP_DIR/sdd-workflow/.codex/commands"/*.md .codex/commands/
        CODEX_COUNT=$(ls -1 .codex/commands/*.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + CODEX_COUNT))
        echo "✅ Installed $CODEX_COUNT Codex files"
    fi
fi

echo ""
echo "✅ Installation complete!"
echo "Total files installed: $TOTAL_FILES"
echo ""

# Check if in git repo
if [ -d ".git" ]; then
    echo "📝 Note: You may want to commit these commands:"
    if [ "$INSTALL_CLAUDE" = true ]; then
        echo "  git add .claude/commands/"
    fi
    if [ "$INSTALL_CODEX" = true ]; then
        echo "  git add .codex/commands/"
    fi
    echo "  git commit -m 'Add SDD workflow commands'"
    echo ""
fi

echo "🎯 Next steps:"
echo "  1. Try: /sdd-auto Create a simple calculator in Python"
echo "  2. Read: QUICKSTART.md for detailed usage"
echo "  3. See: COMMANDS.md for all available commands"
echo ""
echo "Happy coding with SDD Workflow! 🚀"
