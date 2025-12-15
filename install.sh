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
echo "3) GitHub Copilot only"
echo "4) Claude Code + Codex"
echo "5) Claude Code + GitHub Copilot"
echo "6) Codex + GitHub Copilot"
echo "7) All three platforms"
read -p "Enter choice [1-7]: " platform_choice < /dev/tty

case $platform_choice in
    1)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=false
        INSTALL_COPILOT=false
        ;;
    2)
        INSTALL_CLAUDE=false
        INSTALL_CODEX=true
        INSTALL_COPILOT=false
        ;;
    3)
        INSTALL_CLAUDE=false
        INSTALL_CODEX=false
        INSTALL_COPILOT=true
        ;;
    4)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=true
        INSTALL_COPILOT=false
        ;;
    5)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=false
        INSTALL_COPILOT=true
        ;;
    6)
        INSTALL_CLAUDE=false
        INSTALL_CODEX=true
        INSTALL_COPILOT=true
        ;;
    7)
        INSTALL_CLAUDE=true
        INSTALL_CODEX=true
        INSTALL_COPILOT=true
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

# If Claude is selected, ask what to install
if [ "$INSTALL_CLAUDE" = true ]; then
    echo ""
    echo "What would you like to install for Claude Code?"
    echo "1) Commands only"
    echo "2) Sub-agents only"
    echo "3) Both commands and sub-agents"
    read -p "Enter choice [1-3] (default: 3): " claude_type_choice < /dev/tty

    case ${claude_type_choice:-3} in
        1)
            CLAUDE_TYPE="commands"
            ;;
        2)
            CLAUDE_TYPE="agents"
            ;;
        3)
            CLAUDE_TYPE="both"
            ;;
        *)
            echo "Invalid choice. Exiting."
            exit 1
            ;;
    esac
fi

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

    # Install Claude Code
    if [ "$INSTALL_CLAUDE" = true ]; then
        # Install commands if requested
        if [ "$CLAUDE_TYPE" = "commands" ] || [ "$CLAUDE_TYPE" = "both" ]; then
            CLAUDE_DIR="$HOME/.claude/commands"
            echo "Installing Claude Code commands to: $CLAUDE_DIR"
            mkdir -p "$CLAUDE_DIR"
            cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md "$CLAUDE_DIR/"
            CLAUDE_COUNT=$(ls -1 "$CLAUDE_DIR"/sdd-*.md 2>/dev/null | wc -l)
            TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
            echo "✅ Installed $CLAUDE_COUNT Claude Code command files"
        fi

        # Install agents if requested
        if [ "$CLAUDE_TYPE" = "agents" ] || [ "$CLAUDE_TYPE" = "both" ]; then
            AGENTS_DIR="$HOME/.claude/agents"
            echo "Installing Claude Code agents to: $AGENTS_DIR"
            mkdir -p "$AGENTS_DIR"
            if [ -d "$TEMP_DIR/sdd-workflow/.claude/agents" ]; then
                cp "$TEMP_DIR/sdd-workflow/.claude/agents"/*.md "$AGENTS_DIR/" 2>/dev/null || true
                AGENTS_COUNT=$(ls -1 "$AGENTS_DIR"/*.md 2>/dev/null | wc -l)
                TOTAL_FILES=$((TOTAL_FILES + AGENTS_COUNT))
                echo "✅ Installed $AGENTS_COUNT Claude Code agent files"
            fi
        fi
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

    # Install GitHub Copilot prompts
    if [ "$INSTALL_COPILOT" = true ]; then
        COPILOT_DIR="$HOME/.github/prompts"
        echo "Installing GitHub Copilot prompts to: $COPILOT_DIR"
        mkdir -p "$COPILOT_DIR"
        cp "$TEMP_DIR/sdd-workflow/.github/prompts"/*.prompt.md "$COPILOT_DIR/"
        COPILOT_COUNT=$(ls -1 "$COPILOT_DIR"/sdd-*.prompt.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + COPILOT_COUNT))
        echo "✅ Installed $COPILOT_COUNT GitHub Copilot prompt files"
    fi

    echo ""
    echo "✅ Global installation complete!"
    echo "Total files installed: $TOTAL_FILES"
    echo ""
    echo "You can now use SDD commands in any project:"
    if [ "$INSTALL_COPILOT" = true ]; then
        echo "  GitHub Copilot:"
        echo "    @workspace /sdd-auto <requirement>"
        echo "    @workspace /sdd-spec <requirement>"
        echo "    @workspace /sdd-arch <feature.feature>"
        echo "    @workspace /sdd-impl <feature.feature>"
        echo "    @workspace /sdd-verify <feature.feature>"
    fi
    if [ "$INSTALL_CLAUDE" = true ] || [ "$INSTALL_CODEX" = true ]; then
        if [ "$INSTALL_COPILOT" = true ]; then
            echo ""
            echo "  Claude Code / Codex:"
        fi
        echo "    /sdd-auto <requirement>"
        echo "    /sdd-spec <requirement>"
        echo "    /sdd-arch <feature.feature>"
        echo "    /sdd-impl <feature.feature>"
        echo "    /sdd-verify <feature.feature>"
    fi
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

# Install Claude Code
if [ "$INSTALL_CLAUDE" = true ]; then
    # Install commands if requested
    if [ "$CLAUDE_TYPE" = "commands" ] || [ "$CLAUDE_TYPE" = "both" ]; then
        if [ -d ".claude/commands" ]; then
            read -p "⚠️  .claude/commands already exists. Overwrite? [y/N]: " confirm < /dev/tty
            if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
                echo "Skipping Claude Code commands installation."
            else
                mkdir -p .claude/commands
                echo "📋 Copying Claude Code command files..."
                cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md .claude/commands/
                CLAUDE_COUNT=$(ls -1 .claude/commands/*.md 2>/dev/null | wc -l)
                TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
                echo "✅ Installed $CLAUDE_COUNT Claude Code command files"
            fi
        else
            mkdir -p .claude/commands
            echo "📋 Copying Claude Code command files..."
            cp "$TEMP_DIR/sdd-workflow/.claude/commands"/*.md .claude/commands/
            CLAUDE_COUNT=$(ls -1 .claude/commands/*.md 2>/dev/null | wc -l)
            TOTAL_FILES=$((TOTAL_FILES + CLAUDE_COUNT))
            echo "✅ Installed $CLAUDE_COUNT Claude Code command files"
        fi
    fi

    # Install agents if requested
    if [ "$CLAUDE_TYPE" = "agents" ] || [ "$CLAUDE_TYPE" = "both" ]; then
        if [ -d ".claude/agents" ]; then
            read -p "⚠️  .claude/agents already exists. Overwrite? [y/N]: " confirm < /dev/tty
            if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
                echo "Skipping Claude Code agents installation."
            else
                mkdir -p .claude/agents
                echo "📋 Copying Claude Code agent files..."
                if [ -d "$TEMP_DIR/sdd-workflow/.claude/agents" ]; then
                    cp "$TEMP_DIR/sdd-workflow/.claude/agents"/*.md .claude/agents/ 2>/dev/null || true
                    AGENTS_COUNT=$(ls -1 .claude/agents/*.md 2>/dev/null | wc -l)
                    TOTAL_FILES=$((TOTAL_FILES + AGENTS_COUNT))
                    echo "✅ Installed $AGENTS_COUNT Claude Code agent files"
                fi
            fi
        else
            mkdir -p .claude/agents
            echo "📋 Copying Claude Code agent files..."
            if [ -d "$TEMP_DIR/sdd-workflow/.claude/agents" ]; then
                cp "$TEMP_DIR/sdd-workflow/.claude/agents"/*.md .claude/agents/ 2>/dev/null || true
                AGENTS_COUNT=$(ls -1 .claude/agents/*.md 2>/dev/null | wc -l)
                TOTAL_FILES=$((TOTAL_FILES + AGENTS_COUNT))
                echo "✅ Installed $AGENTS_COUNT Claude Code agent files"
            fi
        fi
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

# Install GitHub Copilot prompts
if [ "$INSTALL_COPILOT" = true ]; then
    if [ -d ".github/prompts" ]; then
        read -p "⚠️  .github/prompts already exists. Overwrite? [y/N]: " confirm < /dev/tty
        if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            echo "Skipping GitHub Copilot installation."
        else
            mkdir -p .github/prompts
            echo "📋 Copying GitHub Copilot prompt files..."
            cp "$TEMP_DIR/sdd-workflow/.github/prompts"/*.prompt.md .github/prompts/
            COPILOT_COUNT=$(ls -1 .github/prompts/*.prompt.md 2>/dev/null | wc -l)
            TOTAL_FILES=$((TOTAL_FILES + COPILOT_COUNT))
            echo "✅ Installed $COPILOT_COUNT GitHub Copilot files"
        fi
    else
        mkdir -p .github/prompts
        echo "📋 Copying GitHub Copilot prompt files..."
        cp "$TEMP_DIR/sdd-workflow/.github/prompts"/*.prompt.md .github/prompts/
        COPILOT_COUNT=$(ls -1 .github/prompts/*.prompt.md 2>/dev/null | wc -l)
        TOTAL_FILES=$((TOTAL_FILES + COPILOT_COUNT))
        echo "✅ Installed $COPILOT_COUNT GitHub Copilot files"
    fi
fi

echo ""
echo "✅ Installation complete!"
echo "Total files installed: $TOTAL_FILES"
echo ""

# Check if in git repo
if [ -d ".git" ]; then
    echo "📝 Note: You may want to commit these files:"
    if [ "$INSTALL_CLAUDE" = true ]; then
        if [ "$CLAUDE_TYPE" = "commands" ] || [ "$CLAUDE_TYPE" = "both" ]; then
            echo "  git add .claude/commands/"
        fi
        if [ "$CLAUDE_TYPE" = "agents" ] || [ "$CLAUDE_TYPE" = "both" ]; then
            echo "  git add .claude/agents/"
        fi
    fi
    if [ "$INSTALL_CODEX" = true ]; then
        echo "  git add .codex/commands/"
    fi
    if [ "$INSTALL_COPILOT" = true ]; then
        echo "  git add .github/prompts/"
    fi
    echo "  git commit -m 'Add SDD workflow files'"
    echo ""
fi

echo "🎯 Next steps:"
if [ "$INSTALL_COPILOT" = true ]; then
    echo "  1. Try: @workspace /sdd-auto Create a simple calculator in Python"
    echo "     (For Claude/Codex: /sdd-auto Create a simple calculator in Python)"
else
    echo "  1. Try: /sdd-auto Create a simple calculator in Python"
fi
echo "  2. Read: QUICKSTART.md for detailed usage"
echo "  3. See: COMMANDS.md for all available commands"
echo ""
echo "Happy coding with SDD Workflow! 🚀"
