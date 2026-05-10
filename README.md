# GSI-Protocol

> Specification-Driven Development (SDD) Workflow for AI-powered Development

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-1.4.0-green)](https://github.com/CodeMachine0121/GSI-Protocol)

**Language**: English | [繁體中文](./README.zh-TW.md)

GSI-Protocol is an automated Specification-Driven Development (SDD) workflow system that transforms user requirements into production-ready code through a structured 4-phase process: Specification → Architecture → Implementation → Verification.

## Features

- **Multi-Platform Support**: Works with Claude Code, Codex (OpenAI), and GitHub Copilot
- **Language Agnostic**: Architecture design independent of programming language
- **Automated Workflow**: Execute complete development cycle with a single command
- **BDD Integration**: Built-in support for Gherkin specifications
- **Project-Aware**: Automatically detects and adapts to your project's tech stack
- **Role-Based Phases**: PM → Architect → Engineer → QA workflow

## 📚 Learn More

**New to GSI-Protocol?** Start here:

- **[GSI Theory & Methodology](./docs/gsi-theory.md)** - Deep dive into the **G**herkin-**S**tructure-**I**mplement methodology
- **[Quick Start Guide](./docs/quickstart.md)** - Step-by-step tutorial to build your first feature

## Quick Start

### Installation

Install using `uvx` (recommended):

```bash
uvx --from gsi-protocol-installer gsi-install
```

Or using `pipx`:

```bash
pipx run gsi-protocol-installer
```

The installer will guide you through:
1. Selecting AI platform(s) (Claude Code, Codex, GitHub Copilot)
2. Choosing installation type (global or project-specific)
3. Installing workflow commands

### Basic Usage

#### Automatic Mode (Recommended)

Execute the complete 4-phase workflow automatically:

```bash
# For Claude Code / Codex
/sdd-auto <your requirement>

# For GitHub Copilot
@workspace /sdd-auto <your requirement>
```

Example:
```bash
/sdd-auto Add user authentication with email and password
```

#### Manual Mode

For more control over each phase:

1. **Generate Specification** (PM Phase)
   ```bash
   /sdd-spec <requirement>
   ```

2. **Design Architecture** (Architect Phase)
   ```bash
   /sdd-arch <feature_file_path>
   ```

3. **Implement Code** (Engineer Phase)
   ```bash
   /sdd-impl <feature_file_path>
   ```

4. **Verify Implementation** (QA Phase)
   ```bash
   /sdd-verify <feature_file_path>
   ```

## Workflow Overview

The GSI-Protocol follows a structured 4-phase process:

```
User Requirement
      ↓
[Phase 1: Specification (PM)]
   → .gsi/{feature}/PRD.md (business behaviour)
   → .gsi/{feature}/{feature}.feature (SpecBridge HTTP contract)
      ↓
[Phase 2: Architecture (Architect)]
   → .gsi/{feature}/architecture.md
      ↓
[Phase 3: Implementation (Engineer)]
   → Source code + unit tests (TDD)
      ↓
[Phase 4: Verification (QA)]
   → specbridge verify + unit tests
   → .gsi/{feature}/conclusion.md
```

> **Learn the methodology**: Read our [GSI Theory & Methodology guide](./docs/gsi-theory.md) to understand how **Gherkin** (specification), **Structure** (architecture), and **Implement** (code) work together.

## Available Commands

| Command | Description | Phase |
|---------|-------------|-------|
| `/sdd-auto` | Execute complete workflow automatically | All |
| `/sdd-spec` | Generate PRD + SpecBridge contract from requirements | 1 |
| `/sdd-arch` | Design architecture from specification | 2 |
| `/sdd-impl` | Implement code + unit tests (TDD) | 3 |
| `/sdd-verify` | Verify via specbridge + unit tests | 4 |

## Output Structure

After running the workflow, your project will have:

```
project_root/
├── .gsi/{feature_name}/
│   ├── PRD.md                          # Business behaviour spec
│   ├── {feature_name}.feature          # SpecBridge HTTP contract
│   ├── architecture.md                 # Architecture design
│   └── conclusion.md                   # Verification report
└── {your_project_structure}/
    ├── {model_files}                   # Generated models
    ├── {service_files}                 # Generated services
    └── {unit_test_files}               # TDD-produced tests
```

## Platform-Specific Usage

### Claude Code

Commands are available directly in Claude Code CLI:
```bash
/sdd-auto <requirement>
/sdd-spec <requirement>
```

### Codex (OpenAI)

Use prompts with argument placeholders:
```bash
/sdd-auto <requirement>
```

### GitHub Copilot

Prefix commands with `@workspace`:
```bash
@workspace /sdd-auto <requirement>
@workspace /sdd-spec <requirement>
```

## Requirements

- Python 3.10 or higher
- Node.js 18 or higher
- Git
- One of the supported AI platforms:
  - Claude Code CLI
  - Codex (OpenAI)
  - GitHub Copilot

### SpecBridge (Required)

GSI-Protocol integrates [SpecBridge](https://github.com/CodeMachine0121/SpecBridge) in the **Specification** (`/sdd-spec`) and **Verification** (`/sdd-verify`) phases. SpecBridge is a contract testing CLI that validates live HTTP API behavior against Gherkin feature files.

Install it globally before using GSI-Protocol:

```bash
npm install -g @ksz54213/specbridge
```

Verify installation:

```bash
specbridge --version
```

## Documentation

For detailed documentation, see the [docs](./docs) directory:
- [GSI Theory & Methodology](./docs/gsi-theory.md) - Understand the G-S-I pillars
- [Quick Start Guide](./docs/quickstart.md) - Get started in minutes

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**James Hsueh** - [asdfg55887@gmail.com](mailto:asdfg55887@gmail.com)

## Links

- [Landing Page](https://coding-afternoon.com/gsi-protocol/)
- [Homepage](https://github.com/CodeMachine0121/GSI-Protocol)
- [Issues](https://github.com/CodeMachine0121/GSI-Protocol/issues)
- [Repository](https://github.com/CodeMachine0121/GSI-Protocol)

## Changelog

See version history and updates in the project repository.
