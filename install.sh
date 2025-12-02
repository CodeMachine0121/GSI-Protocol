#!/bin/bash

# SDD Workflow Installation Script
# This script installs only the .claude/commands files to your project
# without copying examples or other unnecessary files

set -e

echo "🚀 SDD Workflow Installer"
echo "========================="
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
    echo "2) Install globally to ~/.claude/workflows"
    read -p "Enter choice [1-2]: " choice

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
    TARGET_DIR="$HOME/.claude/workflows/sdd-workflow"

    echo "Installing globally to: $TARGET_DIR"
    echo ""

    # Create directory
    mkdir -p "$HOME/.claude/workflows"

    # Clone or update
    if [ -d "$TARGET_DIR" ]; then
        echo "⚠️  SDD Workflow already installed. Updating..."
        cd "$TARGET_DIR"
        git pull
    else
        echo "📦 Cloning repository..."
        git clone "$REPO_URL" "$TARGET_DIR"
    fi

    echo ""
    echo "✅ Global installation complete!"
    echo ""
    echo "You can now use SDD commands in any project:"
    echo "  /sdd-auto <requirement>"
    echo "  /sdd-spec <requirement>"
    echo "  /sdd-arch <feature.feature>"
    echo "  /sdd-impl <feature.feature> <structure>"
    echo "  /sdd-verify <feature.feature> <implementation>"
    echo ""
    exit 0
fi

# Project installation
echo "Installing to current project..."
echo ""

# Check if .claude/commands already exists
if [ -d ".claude/commands" ]; then
    read -p "⚠️  .claude/commands already exists. Overwrite? [y/N]: " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "Installation cancelled."
        exit 0
    fi
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "📦 Downloading SDD Workflow..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR/sdd-workflow"

# Create .claude/commands directory
mkdir -p .claude/commands

# Copy only command files
echo "📋 Copying command files..."
cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md .claude/commands/

# Count files
FILE_COUNT=$(ls -1 .claude/commands/*.md 2>/dev/null | wc -l)

echo ""
echo "✅ Installation complete!"
echo ""
echo "Installed $FILE_COUNT command files:"
ls -1 .claude/commands/
echo ""

# Check if in git repo
if [ -d ".git" ]; then
    echo "📝 Note: You may want to commit these commands:"
    echo "  git add .claude/commands/"
    echo "  git commit -m 'Add SDD workflow commands'"
    echo ""
fi

echo "🎯 Next steps:"
echo "  1. Try: /sdd-auto Create a simple calculator in Python"
echo "  2. Read: QUICKSTART.md for detailed usage"
echo "  3. See: COMMANDS.md for all available commands"
echo ""
echo "Happy coding with SDD Workflow! 🚀"
