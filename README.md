# GSI-Protocol, Gherkin-Structure-Implementation

A Claude Code workflow plugin that implements a strict **Specification-Driven Development (SDD)** process for building new software features using AI Agents.

## Philosophy

**"Spec -> Structure -> Implementation"**

This workflow isolates business logic, technical architecture, and coding into three distinct phases to minimize hallucination and maximize precision.

**🌍 Language & Framework Agnostic:** Works with Python, TypeScript, Go, Java, Rust, C#, and more. The methodology stays the same regardless of your tech stack.

## Installation

> ⚠️ **重要提醒**: 不要直接 clone 整個 repo 到你的專案！這會把 `examples/` 也複製進去。
>
> 📖 **請參考 [INSTALL.md](INSTALL.md) 查看詳細安裝說明**

### 方法一：全域安裝（推薦）✅

所有專案共用，最乾淨的方式：

```bash
mkdir -p ~/.claude/workflows
cd ~/.claude/workflows
git clone <your-repo-url> sdd-workflow
```

完成！現在在任何專案都能使用 `/sdd-auto` 等指令。

### 方法二：使用安裝腳本

自動安裝，只複製需要的 commands 檔案：

```bash
# 下載並執行安裝腳本
curl -sSL <your-repo-url>/raw/main/install.sh | bash

# 或手動執行
wget <your-repo-url>/raw/main/install.sh
chmod +x install.sh
./install.sh
```

### 方法三：手動複製（專案內安裝）

只複製 commands，不包含 examples：

```bash
# 在專案外臨時下載
cd /tmp
git clone <your-repo-url> sdd-temp

# 進入你的專案
cd ~/your-project

# 只複製 commands
mkdir -p .claude/commands
cp /tmp/sdd-temp/.claude/commands/* .claude/commands/

# 清理
rm -rf /tmp/sdd-temp
```

### 驗證安裝

```bash
# 檢查檔案
ls .claude/commands/
# 應該看到: sdd-auto.md, sdd-spec.md, sdd-arch.md, sdd-impl.md, sdd-verify.md

# 確認沒有 examples 目錄
ls examples/
# 應該不存在（或是你自己的 examples）
```

---

> 📖 **完整安裝指南**: [INSTALL.md](INSTALL.md)
>
> 📖 **指令參考**: [COMMANDS.md](COMMANDS.md)
>
> 📖 **快速入門**: [QUICKSTART.md](QUICKSTART.md)

## Usage

### Auto Mode (Full Workflow)

Run the complete 4-phase SDD workflow automatically in any language:

```
/sdd-auto I need to implement a Referral Bonus system in TypeScript. If a user invites a friend, and the friend completes a purchase over $50, the inviter gets 100 points.
```

```
/sdd-auto Implement a discount system in Go where VIP users get 20% off purchases over $100
```

```
/sdd-auto Create a task management system in Rust with create, complete, and delete operations
```

The agent will automatically execute all 4 phases and adapt the output format to your chosen language while maintaining the SDD principles.

### Language Specification

You can specify the language in three ways:

1. **Explicitly in the prompt:** `/sdd-auto Implement user auth in Python`
2. **From project context:** The agent detects your project's language from existing files
3. **When asked:** The agent will ask which language you prefer if unclear

### Manual Mode (Step-by-Step)

For more control, run each phase separately:

```
/sdd-spec <your requirement>     # Phase 1: Generate Gherkin specifications
/sdd-arch <gherkin file>         # Phase 2: Design data models & interfaces
/sdd-impl <gherkin & structure>  # Phase 3: Implement the logic
/sdd-verify <gherkin & impl>     # Phase 4: Verify implementation
```

**When to use Auto vs Manual:**

- **Auto Mode (`/sdd-auto`)**: Quick prototyping, simple features, one-shot development
- **Manual Mode**: Production code, complex features, need to review each phase before proceeding

## Workflow Phases

### Phase 1: Specification (The Soul)

- **Role:** Product Manager
- **Input:** User's natural language requirement
- **Output:** Gherkin `.feature` file with BDD scenarios
- **Goal:** Translate vague requirements into strict behavioral specifications

### Phase 2: Structure (The Skeleton)

- **Role:** System Architect
- **Input:** Gherkin specification from Phase 1
- **Output:** Data models and interface definitions (Python/TypeScript)
- **Goal:** Design the technical skeleton required to support the Gherkin scenarios

### Phase 3: Implementation (The Flesh)

- **Role:** Senior Engineer
- **Input:** Gherkin specification + Structure design
- **Output:** Fully functional code implementing the interfaces
- **Goal:** Implement the logic within the defined structure to satisfy the specs

### Phase 4: Verification (The Check)

- **Role:** QA Automation
- **Input:** Gherkin specification + Implementation
- **Output:** Test results and feedback
- **Goal:** Verify that implementation meets all requirements

## Example Outputs

The workflow adapts to your chosen language while maintaining the same SDD principles.

### Example: VIP Discount System

**Phase 1 - Gherkin (Language-Independent)**

```gherkin
Feature: VIP Discount
  Scenario: Apply discount
    Given User is VIP
    When Purchase amount is 1000
    Then Final price should be 800
```

**Phase 2 & 3 - Python**

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

# Implementation
def calculate_discount(amount: float, user_type: UserType) -> DiscountResult:
    if user_type == UserType.VIP and amount >= 100:
        discount = amount * 0.2
        return DiscountResult(amount - discount, discount)
    return DiscountResult(amount, 0)
```

**Phase 2 & 3 - TypeScript**

```typescript
enum UserType {
  VIP = "VIP",
  NORMAL = "NORMAL",
}

interface DiscountResult {
  finalPrice: number;
  discount: number;
}

// Implementation
function calculateDiscount(amount: number, userType: UserType): DiscountResult {
  if (userType === UserType.VIP && amount >= 100) {
    const discount = amount * 0.2;
    return { finalPrice: amount - discount, discount };
  }
  return { finalPrice: amount, discount: 0 };
}
```

**Phase 2 & 3 - Go**

```go
type UserType string

const (
    UserTypeVIP    UserType = "VIP"
    UserTypeNormal UserType = "NORMAL"
)

type DiscountResult struct {
    FinalPrice float64
    Discount   float64
}

// Implementation
func CalculateDiscount(amount float64, userType UserType) DiscountResult {
    if userType == UserTypeVIP && amount >= 100 {
        discount := amount * 0.2
        return DiscountResult{FinalPrice: amount - discount, Discount: discount}
    }
    return DiscountResult{FinalPrice: amount, Discount: 0}
}
```

## Project Structure

```
.
├── README.md                           # This file
├── QUICKSTART.md                       # Quick start guide
├── expected_workflow.md                # Detailed workflow definition
├── .claude/
│   └── commands/
│       ├── sdd-auto.md                # Auto mode: run all phases
│       ├── sdd-spec.md                # Phase 1: Specification
│       ├── sdd-arch.md                # Phase 2: Architecture
│       ├── sdd-impl.md                # Phase 3: Implementation
│       └── sdd-verify.md              # Phase 4: Verification
├── prompts/
│   ├── pm_agent.md                    # PM Agent prompt template
│   ├── architect_agent.md             # Architect Agent prompt template
│   ├── engineer_agent.md              # Engineer Agent prompt template
│   └── qa_agent.md                    # QA Agent prompt template
└── examples/
    ├── referral_bonus/                # Python example
    │   ├── spec.feature
    │   ├── structure.py
    │   ├── implementation.py
    │   └── README.md
    └── vip_discount_typescript/       # TypeScript example
        ├── spec.feature
        ├── structure.ts
        ├── implementation.ts
        ├── package.json
        └── README.md
```

## Benefits

1. **Language Agnostic**: Works with any programming language - Python, TypeScript, Go, Java, Rust, C#, and more
2. **Framework Independent**: Not tied to any specific framework or library - use what fits your project
3. **Reduced Hallucination**: Each phase has clear constraints and inputs, minimizing AI confusion
4. **Traceability**: Every code line traces back to a Gherkin scenario for complete auditability
5. **Modularity**: Phases can be run independently or as a complete workflow
6. **Clarity**: Business logic separated from technical implementation
7. **Verifiable**: Automated verification against specifications
8. **Consistent Methodology**: Same proven approach regardless of your tech stack

## Requirements

- Claude Code CLI
- Target language runtime (Python 3.8+, Node.js 16+, Go 1.19+, Java 11+, Rust 1.65+, etc.)
- Language-specific dependencies (if any - see examples for details)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
