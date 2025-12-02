# GSI-Protocol

> **Gherkin → Structure → Implementation**
>
> A language-agnostic workflow for building verified software features using AI agents and BDD principles.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 What is GSI-Protocol?

GSI-Protocol is a Claude Code workflow plugin that implements **Specification-Driven Development (SDD)**. It transforms vague requirements into verified, production-ready code through a strict 4-phase process.

### Core Philosophy

**"Spec → Structure → Implementation"**

Isolate business logic, technical architecture, and coding into distinct phases to minimize AI hallucination and maximize precision.

### Key Features

- 🌍 **Language Agnostic**: Works with Python, TypeScript, Go, Java, Rust, C#, and more
- 🎯 **Framework Independent**: Not tied to any specific library or framework
- 📝 **BDD-Based**: Uses Gherkin for clear, testable specifications
- ✅ **Verifiable**: Automated verification against specifications
- 🔄 **Modular**: Run phases independently or as a complete workflow

---

## 📦 Quick Start

### Installation (30 seconds)

**Option 1: One-liner (if repo is public):**

```bash
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

**Option 2: Global Installation (Recommended):**

```bash
mkdir -p ~/.claude/workflows
cd ~/.claude/workflows
git clone https://github.com/CodeMachine0121/GSI-Protocol.git gsi-protocol
```

Now use in any project!

**Option 3: Project-Specific Installation:**

```bash
cd /tmp
git clone https://github.com/CodeMachine0121/GSI-Protocol.git gsi-temp
cd ~/your-project
mkdir -p .claude/commands
cp /tmp/gsi-temp/.claude/commands/* .claude/commands/
rm -rf /tmp/gsi-temp
```

> 📖 See [Installation Guide](docs/INSTALL.md) for more options

### First Use (2 minutes)

```bash
cd your-project

# Auto mode - generates everything
/sdd-auto Create a shopping cart in TypeScript with add, remove, checkout functions

# Manual mode - step by step
/sdd-spec Create a shopping cart with add, remove, checkout
/sdd-arch features/shopping_cart.feature
/sdd-impl features/shopping_cart.feature structure/shopping_cart_structure.ts
/sdd-verify features/shopping_cart.feature implementation/shopping_cart_impl.ts
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[Quick Start Guide](docs/QUICKSTART.md)** | 5-minute tutorial |
| **[Installation Guide](docs/INSTALL.md)** | Detailed installation instructions |
| **[Commands Reference](docs/COMMANDS.md)** | Complete command documentation |
| **[Language Guide](docs/LANGUAGE_GUIDE.md)** | Multi-language support guide |
| **[Workflow Definition](docs/expected_workflow.md)** | Detailed methodology |
| **[Contributing](CONTRIBUTING.md)** | How to contribute |

---

## 🔄 Workflow Overview

### The 4 Phases

```
Phase 1: Specification (PM)
    ↓
    Gherkin .feature file
    ↓
Phase 2: Structure (Architect)
    ↓
    Data models + Interfaces
    ↓
Phase 3: Implementation (Engineer)
    ↓
    Working code
    ↓
Phase 4: Verification (QA)
    ↓
    ✅ Verified feature
```

### Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/sdd-auto` | Run all 4 phases automatically | Quick prototyping, simple features |
| `/sdd-spec` | Generate Gherkin specification | Define requirements |
| `/sdd-arch` | Design data models & interfaces | Review structure |
| `/sdd-impl` | Implement the logic | Write code |
| `/sdd-verify` | Verify against spec | Test implementation |

---

## 💡 Example

### Input

```
/sdd-auto Implement a VIP discount system in Python where VIP users get 20% off purchases over $100
```

### Output

**Phase 1: Specification** (`features/vip_discount.feature`)
```gherkin
Feature: VIP Discount
  Scenario: Apply discount to VIP user
    Given user is VIP
    When user makes a purchase of 1000 USD
    Then final price should be 800 USD
```

**Phase 2: Structure** (`structure/vip_discount_structure.py`)
```python
from dataclasses import dataclass
from enum import Enum

class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

@dataclass
class DiscountResult:
    final_price: float
    discount: float
```

**Phase 3: Implementation** (`implementation/vip_discount_impl.py`)
```python
def calculate_discount(amount: float, user_type: UserType) -> DiscountResult:
    if user_type == UserType.VIP and amount >= 100:
        discount = amount * 0.2
        return DiscountResult(amount - discount, discount)
    return DiscountResult(amount, 0)
```

**Phase 4: Verification**
```
✅ All scenarios passed
✅ Feature complete
```

---

## 🌐 Multi-Language Support

Same workflow, different languages:

<details>
<summary><b>Python</b></summary>

```python
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class User:
    id: str
    type: UserType

class IUserService(ABC):
    @abstractmethod
    def authenticate(self, credentials: Credentials) -> User:
        pass
```
</details>

<details>
<summary><b>TypeScript</b></summary>

```typescript
interface User {
  id: string;
  type: UserType;
}

interface IUserService {
  authenticate(credentials: Credentials): User;
}
```
</details>

<details>
<summary><b>Go</b></summary>

```go
type User struct {
    ID   string
    Type UserType
}

type UserService interface {
    Authenticate(credentials Credentials) (User, error)
}
```
</details>

See [Language Guide](docs/LANGUAGE_GUIDE.md) for Rust, Java, C#, and more.

---

## 🎓 Use Cases

### 1. API Development
```bash
/sdd-spec Design a RESTful API for blog posts (CRUD operations)
/sdd-arch features/blog_api.feature
# Get clear API contracts and data structures
```

### 2. Feature Implementation
```bash
/sdd-auto Implement user authentication with JWT tokens in TypeScript
# Get working, tested code in minutes
```

### 3. Legacy Code Refactoring
```bash
/sdd-spec The payment module should support credit card, PayPal, and crypto
# Define clear requirements before refactoring
```

### 4. Team Collaboration
```bash
# PM: Define requirements
/sdd-spec User registration with email verification

# Architect: Review and design
/sdd-arch features/user_registration.feature

# Engineer: Implement
/sdd-impl features/user_registration.feature structure/user_registration_structure.py

# QA: Verify
/sdd-verify features/user_registration.feature implementation/user_registration_impl.py
```

---

## 📁 Project Structure

```
GSI-Protocol/
├── README.md                    # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── install.sh                   # Installation script
├── .claude/
│   └── commands/                # Claude Code slash commands
│       ├── gsi-auto.md         # Auto workflow
│       ├── gsi-spec.md         # Phase 1
│       ├── gsi-arch.md         # Phase 2
│       ├── gsi-impl.md         # Phase 3
│       └── gsi-verify.md       # Phase 4
├── docs/                        # Documentation
│   ├── QUICKSTART.md           # Quick start guide
│   ├── INSTALL.md              # Installation guide
│   ├── COMMANDS.md             # Commands reference
│   ├── LANGUAGE_GUIDE.md       # Language support
│   └── expected_workflow.md    # Workflow details
├── prompts/                     # Agent prompts
│   ├── pm_agent.md
│   ├── architect_agent.md
│   ├── engineer_agent.md
│   └── qa_agent.md
└── examples/                    # Working examples
    ├── referral_bonus/         # Python example
    └── vip_discount_typescript/ # TypeScript example
```

---

## 🚀 Benefits

### For Developers
- ✅ **Faster Development**: Auto-generate boilerplate and structure
- ✅ **Better Quality**: Systematic approach reduces bugs
- ✅ **Clear Requirements**: Gherkin specs eliminate ambiguity

### For Teams
- ✅ **Shared Language**: BDD specs everyone understands
- ✅ **Better Communication**: Clear phases for PM, Architect, Engineer, QA
- ✅ **Maintainable Code**: Every line traces to a requirement

### For Projects
- ✅ **Language Flexibility**: Switch languages without changing methodology
- ✅ **Framework Agnostic**: Use any library or framework
- ✅ **Scalable**: Works for simple features to complex systems

---

## 🔧 Requirements

- Claude Code CLI
- Git
- Target language runtime (Python 3.8+, Node.js 16+, Go 1.19+, etc.)

---

## 📖 Learn More

- 📝 [Quick Start (5 min)](docs/QUICKSTART.md)
- 📚 [Full Documentation](docs/)
- 🌍 [Language Support](docs/LANGUAGE_GUIDE.md)
- 💬 [GitHub Discussions](https://github.com/CodeMachine0121/GSI-Protocol/discussions)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🌍 Add language examples
- 🔧 Submit pull requests

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Built with:
- [Claude Code](https://claude.ai/claude-code) - AI-powered development
- [Gherkin](https://cucumber.io/docs/gherkin/) - BDD specification language
- Inspired by Test-Driven Development and Behavior-Driven Development principles

---

## 📞 Support

- 📖 [Documentation](docs/)
- 💬 [GitHub Issues](https://github.com/CodeMachine0121/GSI-Protocol/issues)
- 💡 [Discussions](https://github.com/CodeMachine0121/GSI-Protocol/discussions)

---

<div align="center">

**[⬆ Back to Top](#gsi-protocol)**

Made with ❤️ by developers, for developers

</div>
