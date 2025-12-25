# GSI-Protocol Quick Start Guide

This guide will help you get started with GSI-Protocol in minutes.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10+** installed on your system
- **Git** installed
- **One of the supported AI platforms**:
  - Claude Code CLI
  - Codex (OpenAI)
  - GitHub Copilot

## Installation

### Step 1: Install GSI-Protocol

Choose one of the following methods:

#### Using uvx (Recommended)

```bash
uvx --from gsi-protocol-installer gsi-install
```

#### Using pipx

```bash
pipx run gsi-protocol-installer
```

### Step 2: Follow the Interactive Installer

The installer will ask you several questions:

1. **Select AI Platform(s)**
   - Choose one or more: Claude Code, Codex, GitHub Copilot
   - Default: All platforms

2. **Choose Installation Type**
   - **Project**: Install to current project (`.claude/`, `.codex/`, `.github/`)
   - **Global**: Install to home directory (`~/.claude/`, `~/.codex/`, `~/.github/`)

3. **For Claude Code: Select Components**
   - Commands only
   - Sub-agents only
   - Both (recommended)

### Step 3: Verify Installation

After installation, you should see:

```
✓ Installation complete! Total files installed: X

Claude Code / Codex usage:
  /sdd-auto <requirement>
  /sdd-spec <requirement>
  /sdd-arch <feature.feature>
  /sdd-impl <feature.feature>
  /sdd-verify <feature.feature>
```

## Your First Workflow

Let's create a simple user authentication feature using GSI-Protocol.

### Example: User Authentication

#### Option 1: Automatic Mode (Fastest)

Run the complete workflow with a single command:

```bash
/sdd-auto Add user authentication with email and password, including login and registration
```

This will automatically:
1. Generate a Gherkin specification
2. Design the architecture
3. Implement the code
4. Verify the implementation

#### Option 2: Manual Mode (More Control)

Execute each phase step-by-step:

**Phase 1: Generate Specification**
```bash
/sdd-spec Add user authentication with email and password, including login and registration
```

Output: `features/user_authentication.feature`

**Phase 2: Design Architecture**
```bash
/sdd-arch features/user_authentication.feature
```

Output: `docs/features/user_authentication/architecture.md`

**Phase 3: Implement Code**
```bash
/sdd-impl features/user_authentication.feature
```

Output: Source code files (location specified in architecture.md)

**Phase 4: Verify Implementation**
```bash
/sdd-verify features/user_authentication.feature
```

Output: `docs/features/user_authentication/conclusion.md`

**Optional: Generate Integration Tests**
```bash
/sdd-integration-test features/user_authentication.feature
```

Output: Test files in your project's test directory

## Understanding the Output

After running the workflow, you'll have:

### 1. Gherkin Specification (`features/user_authentication.feature`)

```gherkin
Feature: User Authentication
  Scenario: User registers successfully
    Given the user provides valid email and password
    When the user submits registration
    Then the account is created
    And the user receives confirmation
```

### 2. Architecture Document (`docs/features/user_authentication/architecture.md`)

Contains:
- Project context (tech stack, frameworks)
- Feature overview
- Data models (User, Credentials, etc.)
- Service interfaces (AuthService, UserRepository)
- Architecture decisions
- File structure planning

### 3. Implementation Files

Generated in your project's structure:
- Model files (e.g., `models/User.ts`)
- Service files (e.g., `services/AuthService.ts`)

### 4. Verification Report (`docs/features/user_authentication/conclusion.md`)

Contains:
- Architecture compliance check
- Scenario verification (Given-When-Then)
- Summary (passed/failed)
- Feedback for improvements

## Platform-Specific Usage

### Claude Code

If you installed commands:
```bash
/sdd-auto <requirement>
```

If you installed sub-agents:
```bash
# Sub-agents run automatically when you invoke commands
```

### Codex (OpenAI)

```bash
/sdd-auto <requirement>
/sdd-spec <requirement>
```

### GitHub Copilot

Prefix all commands with `@workspace`:

```bash
@workspace /sdd-auto <requirement>
@workspace /sdd-spec <requirement>
```

## Tips and Best Practices

### 1. Write Clear Requirements

Good:
```bash
/sdd-auto Add user authentication with email/password, including registration, login, and password reset
```

Not optimal:
```bash
/sdd-auto auth stuff
```

### 2. Review Architecture Before Implementation

When using manual mode, review the generated architecture document before proceeding to implementation.

### 3. Iterate on Failed Verifications

If Phase 4 verification fails, review the conclusion report and re-run Phase 3 with corrections.

### 4. Use Integration Tests for TDD

For test-driven development, use this workflow:
```bash
/sdd-spec <requirement>
/sdd-arch features/your_feature.feature
/sdd-integration-test features/your_feature.feature
/sdd-impl features/your_feature.feature
/sdd-verify features/your_feature.feature
```

### 5. Project-Aware Development

GSI-Protocol automatically detects:
- Your tech stack (package.json, requirements.txt, go.mod, etc.)
- Project structure (src/, models/, services/)
- Code samples (*.ts, *.py, *.go)
- Naming conventions

## Common Workflows

### Workflow 1: Quick Feature Addition

```bash
/sdd-auto Add pagination support to the product listing API
```

### Workflow 2: Test-Driven Development

```bash
/sdd-spec Add product search with filters
/sdd-arch features/product_search.feature
/sdd-integration-test features/product_search.feature
# Write tests first, then implement
/sdd-impl features/product_search.feature
/sdd-verify features/product_search.feature
```

### Workflow 3: Architecture Review

```bash
/sdd-spec Implement shopping cart functionality
/sdd-arch features/shopping_cart.feature
# Review docs/features/shopping_cart/architecture.md
# Discuss with team
/sdd-impl features/shopping_cart.feature
/sdd-verify features/shopping_cart.feature
```

## Troubleshooting

### Installation Issues

**Problem**: "Git is not installed"
```bash
# Install git first
# macOS: brew install git
# Ubuntu: sudo apt-get install git
# Windows: Download from https://git-scm.com/downloads
```

**Problem**: "Command not found: /sdd-auto"
- Ensure you selected the correct platform during installation
- Check that commands are installed in the right directory
- For Claude Code: `ls ~/.claude/commands/` or `ls .claude/commands/`

### Workflow Issues

**Problem**: Architecture doesn't match project structure
- Review `docs/features/{feature}/architecture.md`
- Re-run `/sdd-arch` with clearer requirements
- Provide more context about your project structure

**Problem**: Verification fails
- Read the conclusion report: `docs/features/{feature}/conclusion.md`
- Check which scenarios failed
- Re-run `/sdd-impl` with corrections

## Next Steps

1. **Explore the generated files** to understand the workflow
2. **Customize the architecture** design for your needs
3. **Integrate with CI/CD** by running verification in your pipeline
4. **Share specifications** with your team using Gherkin files

## Getting Help

- **GitHub Issues**: https://github.com/CodeMachine0121/GSI-Protocol/issues
- **Documentation**: https://github.com/CodeMachine0121/GSI-Protocol
- **Email**: asdfg55887@gmail.com

## What's Next?

Now that you've completed your first workflow, you can:

- Explore advanced features (sub-agents, custom templates)
- Integrate with your existing CI/CD pipeline
- Collaborate with your team using Gherkin specifications
- Build complex features using the multi-phase workflow

Happy coding with GSI-Protocol!
