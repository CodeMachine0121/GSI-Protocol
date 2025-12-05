# GSI-Protocol（中文）

> **Gherkin → 架構 → 實作**
>
> 一個語言無關的工作流程，使用 AI 代理和 BDD 原則建立可驗證的軟體功能。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 什麼是 GSI-Protocol?

GSI-Protocol 是一個 AI 驅動的工作流程插件，實作了**規格驅動開發（SDD）**。它透過嚴格的四階段流程，將模糊的需求轉化為經過驗證、可用於生產環境的程式碼。

**支援平台：**

- ✅ Claude Code
- ✅ Codex (OpenAI)
- ✅ GitHub Copilot

### 核心理念

**"規格 → 架構 → 實作 → 驗證"**

將業務邏輯、技術架構、程式撰寫和品質保證分離到不同階段，以最小化 AI 幻覺並最大化精確度。

### 主要特性

- 🌍 **語言無關**：支援 Python、TypeScript、Go、Java、Rust、C# 等等
- 🎯 **框架獨立**：不綁定任何特定函式庫或框架
- 📝 **基於 BDD**：使用 Gherkin 撰寫清晰、可測試的規格
- 🏗️ **專案感知**：自動掃描並遵循既有專案架構
- ✅ **可驗證**：自動根據規格進行驗證
- 🔄 **模組化**：可獨立執行各階段或完整工作流程

---

## 📦 快速開始

### 安裝

**選項 1：使用 uvx（最推薦，無需安裝）**

```bash
uvx --from gsi-protocol-installer gsi-install
```

**選項 2：使用 pipx**

```bash
pipx run gsi-protocol-installer
```

**選項 3：直接執行 Python**

```bash
# 下載並執行
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/gsi_installer.py
python3 gsi_installer.py

# 或使用 curl
curl -O https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/gsi_installer.py
python3 gsi_installer.py
```

安裝程式會引導您：

1. 選擇 AI 平台（Claude Code、Codex 或兩者）
2. 選擇安裝位置（全域或當前專案）
3. 自動完成安裝

**選項 4：手動全域安裝**

**Claude Code:**

```bash
mkdir -p ~/.claude/commands
cd ~/.claude/commands
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md -o sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md -o sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md -o sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-integration-test.md -o sdd-integration-test.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md -o sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md -o sdd-verify.md
```

**Codex (OpenAI):**

```bash
mkdir -p ~/.codex/prompts
cd ~/.codex/prompts
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-auto.md -o sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-spec.md -o sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-arch.md -o sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-integration-test.md -o sdd-integration-test.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-impl.md -o sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-verify.md -o sdd-verify.md
```

**GitHub Copilot:**

```bash
mkdir -p ~/.github/prompts
cd ~/.github/prompts
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-auto.prompts.md -o sdd-auto.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-spec.prompts.md -o sdd-spec.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-arch.prompts.md -o sdd-arch.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-integration-test.prompts.md -o sdd-integration-test.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-impl.prompts.md -o sdd-impl.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-verify.prompts.md -o sdd-verify.prompts.md
```

完成後，可在任何專案中使用 `/sdd-auto`、`/sdd-spec` 等全域指令（Claude/Codex）或 `@workspace /sdd-auto`、`@workspace /sdd-spec`（Copilot）。

> 📖 查看 [安裝指南](docs/INSTALL.md) 了解詳細說明

### 第一次使用（2 分鐘）

```bash
# 使用 uvx 安裝
uvx gsi-protocol-installer

# 選擇平台和安裝位置後，進入您的專案
cd your-project

# 自動模式 - 生成所有內容
/sdd-auto Create a shopping cart in TypeScript with add, remove, checkout functions
# 或使用 Copilot
@workspace /sdd-auto Create a shopping cart in TypeScript with add, remove, checkout functions

# 手動模式 - 逐步執行
/sdd-spec Create a shopping cart with add, remove, checkout
/sdd-arch features/shopping_cart.feature
/sdd-impl features/shopping_cart.feature
/sdd-verify features/shopping_cart.feature
# 或使用 Copilot
@workspace /sdd-spec Create a shopping cart with add, remove, checkout
@workspace /sdd-arch features/shopping_cart.feature
@workspace /sdd-impl features/shopping_cart.feature
@workspace /sdd-verify features/shopping_cart.feature
```

---

## 📚 文件

| 文件                                          | 說明                      |
| --------------------------------------------- | ------------------------- |
| **[快速入門指南](docs/QUICKSTART.md)**        | 5 分鐘教學                |
| **[安裝指南](docs/INSTALL.md)**               | 詳細安裝說明              |
| **[Python 安裝器](docs/PYTHON_INSTALLER.md)** | uvx 安裝方式（推薦）      |
| **[平台支援](docs/PLATFORM_SUPPORT.md)**      | Claude Code vs Codex 比較 |
| **[指令參考](docs/COMMANDS.md)**              | 完整指令文件              |
| **[語言指南](docs/LANGUAGE_GUIDE.md)**        | 多語言支援指南            |
| **[工作流程定義](docs/expected_workflow.md)** | 詳細方法論                |
| **[貢獻指南](CONTRIBUTING.md)**               | 如何貢獻                  |

---

## 🔄 工作流程概覽

### 核心四階段（必需）

```
Phase 1：規格（PM）
    ↓
    Gherkin .feature 檔案
    ↓
Phase 2：架構（架構師）
    ↓
    架構設計文件（繁中 Markdown）
    ↓
Phase 3：實作（工程師）
    ↓
    可運行的程式碼（依專案架構）
    ↓
Phase 4：驗證（QA）
    ↓
    ✅ 驗證結論報告
```

### 選用階段：Integration Tests

```
Phase 2.5：整合測試（選用）
    ↓
    在實作前生成 Integration Tests
    ↓
    測試先行開發（紅燈 → 綠燈）
```

**何時使用 `/sdd-integration-test`？**
- ✅ 團隊實踐 BDD 測試先行
- ✅ 需要完整的整合測試覆蓋
- ✅ 複雜的業務邏輯需要驗證
- ❌ 簡單的 CRUD 功能
- ❌ 原型開發階段
- ❌ 時程緊迫的專案

### 指令

| 指令                    | 用途                             | 何時使用           | 是否必需 |
| ----------------------- | -------------------------------- | ------------------ | -------- |
| `/sdd-auto`             | 自動執行全部 4 個階段            | 快速原型、簡單功能 | -        |
| `/sdd-spec`             | 生成 Gherkin 規格                | 定義需求           | ✅ 必需  |
| `/sdd-arch`             | 設計資料模型與介面               | 審查結構           | ✅ 必需  |
| `/sdd-integration-test` | 生成 Integration Tests（紅燈）   | BDD 測試先行開發   | 🔷 選用  |
| `/sdd-impl`             | 實作邏輯                         | 撰寫程式碼         | ✅ 必需  |
| `/sdd-verify`           | 根據規格驗證                     | 測試實作           | ✅ 必需  |

---

## 💡 範例

### 輸入

```
/sdd-auto Implement a VIP discount system in Python where VIP users get 20% off purchases over $100
```

### 輸出

**階段 1：規格** (`features/vip_discount.feature`)

```gherkin
Feature: VIP Discount
  Scenario: Apply discount to VIP user
    Given user is VIP
    When user makes a purchase of 1000 USD
    Then final price should be 800 USD
```

**Phase 2：架構** (`docs/features/vip_discount/architecture.md`)

```markdown
# VIP 折扣系統 - 架構設計

## 1. 專案上下文

- 程式語言：Python
- 架構模式：Service Layer

## 3. 資料模型

- UserType（列舉）：VIP, NORMAL
- DiscountResult（實體）：final_price, discount

## 4. 服務介面

- calculate_discount(amount, user_type) → DiscountResult
```

**Phase 3：實作** （依 architecture.md 指定位置）

```python
# src/services/discount_service.py
def calculate_discount(amount: float, user_type: UserType) -> DiscountResult:
    if user_type == UserType.VIP and amount >= 100:
        discount = amount * 0.2
        return DiscountResult(amount - discount, discount)
    return DiscountResult(amount, 0)
```

**Phase 4：驗證結論** (`docs/features/vip_discount/conclusion.md`)

```markdown
## 3. 摘要

- 架構：2/2 通過
- 情境：2/2 通過
- **狀態：** ✅ 完成
```

---

## 🌐 多語言支援

相同的工作流程，不同的語言：

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

更多語言請參閱 [語言指南](docs/LANGUAGE_GUIDE.md)，包含 Rust、Java、C# 等。

---

## 🎓 使用案例

### 1. API 開發

```bash
/sdd-spec Design a RESTful API for blog posts (CRUD operations)
/sdd-arch features/blog_api.feature
# 獲得清晰的 API 契約和資料結構
```

### 2. 功能實作

```bash
/sdd-auto Implement user authentication with JWT tokens in TypeScript
# 幾分鐘內獲得可運行、已測試的程式碼
```

### 3. 遺留程式碼重構

```bash
/sdd-spec The payment module should support credit card, PayPal, and crypto
# 在重構前定義清晰的需求
```

### 4. 團隊協作

```bash
# PM：定義需求
/sdd-spec User registration with email verification

# 架構師：審查並設計
/sdd-arch features/user_registration.feature

# 工程師：實作
/sdd-impl features/user_registration.feature

# QA：驗證
/sdd-verify features/user_registration.feature
```

---

## 📁 專案結構

執行 SDD 工作流程後的輸出：

```
your-project/
├── features/                    # Phase 1: Gherkin 規格
│   └── {feature}.feature
├── docs/
│   └── features/
│       └── {feature}/
│           ├── architecture.md  # Phase 2: 架構設計（繁中）
│           └── conclusion.md    # Phase 4: 驗證結論
└── src/                         # Phase 3: 實作程式碼
    ├── models/                  # 依專案既有架構
    │   └── {Feature}Model.{ext}
    └── services/
        └── {Feature}Service.{ext}
```

GSI-Protocol 儲存庫結構：

```
GSI-Protocol/
├── README.md                    # 本檔案
├── CONTRIBUTING.md              # 貢獻指南
├── LICENSE                      # MIT 授權
├── gsi_installer.py             # Python 安裝器
├── pyproject.toml               # Python 專案配置
├── .claude/
│   └── commands/                # Claude Code slash 指令
│       ├── sdd-auto.md         # 自動工作流程
│       ├── sdd-spec.md         # Phase 1
│       ├── sdd-arch.md         # Phase 2
│       ├── sdd-integration-test.md  # BDD Integration Tests
│       ├── sdd-impl.md         # Phase 3
│       └── sdd-verify.md       # Phase 4
├── .codex/
│   └── prompts/                 # Codex (OpenAI) prompts
│       ├── sdd-auto.md         # 自動工作流程
│       ├── sdd-spec.md         # Phase 1
│       ├── sdd-arch.md         # Phase 2
│       ├── sdd-integration-test.md  # BDD Integration Tests
│       ├── sdd-impl.md         # Phase 3
│       └── sdd-verify.md       # Phase 4
├── .github/
│   └── prompts/                 # GitHub Copilot prompts
│       ├── sdd-auto.prompts.md         # 自動工作流程
│       ├── sdd-spec.prompts.md         # Phase 1
│       ├── sdd-arch.prompts.md         # Phase 2
│       ├── sdd-integration-test.prompts.md  # BDD Integration Tests
│       ├── sdd-impl.prompts.md         # Phase 3
│       └── sdd-verify.prompts.md       # Phase 4
├── docs/                        # 文件
│   ├── QUICKSTART.md           # 快速入門指南
│   ├── INSTALL.md              # 安裝指南
│   ├── PYTHON_INSTALLER.md     # Python 安裝器說明
│   ├── PLATFORM_SUPPORT.md     # 平台支援說明
│   ├── COMMANDS.md             # 指令參考
│   ├── LANGUAGE_GUIDE.md       # 語言支援
│   └── expected_workflow.md    # 工作流程細節
└── prompts/                     # 代理提示（參考）
    ├── pm_agent.md
    ├── architect_agent.md
    ├── engineer_agent.md
    └── qa_agent.md
```

---

## 🚀 優勢

### 對開發者

- ✅ **更快開發**：自動生成樣板程式碼和結構
- ✅ **更高品質**：系統化方法減少 bug
- ✅ **清晰需求**：Gherkin 規格消除歧義

### 對團隊

- ✅ **共同語言**：所有人都能理解的 BDD 規格
- ✅ **更好溝通**：PM、架構師、工程師、QA 各有明確階段
- ✅ **可維護程式碼**：每一行都可追溯到需求

### 對專案

- ✅ **語言彈性**：切換語言不需改變方法論
- ✅ **框架無關**：使用任何函式庫或框架
- ✅ **可擴展**：適用於簡單功能到複雜系統

---

## 🔧 需求

- **AI 平台（擇一或多個）：**
  - Claude Code CLI，或
  - Codex (OpenAI)，或
  - GitHub Copilot
- **安裝工具：**
  - Python 3.10+
  - uvx/pipx（推薦）或 pip
- Git
- 目標語言執行環境（Python 3.8+、Node.js 16+、Go 1.19+ 等）

---

## 📖 了解更多

- 📝 [快速入門（5 分鐘）](docs/QUICKSTART.md)
- 📚 [完整文件](docs/)
- 🌍 [語言支援](docs/LANGUAGE_GUIDE.md)
- 💬 [GitHub 討論](https://github.com/CodeMachine0121/GSI-Protocol/discussions)

---

## 🤝 貢獻

我們歡迎貢獻！請參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

### 貢獻方式

- 🐛 回報 bug
- 💡 建議功能
- 📝 改善文件
- 🌍 新增語言範例
- 🔧 提交 pull request

---

## 📄 授權

MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

---

## 🙏 致謝

使用以下工具建置：

- [Claude Code](https://claude.ai/claude-code) - AI 驅動開發
- [Codex (OpenAI)](https://openai.com/blog/openai-codex) - AI 程式碼生成
- [GitHub Copilot](https://github.com/features/copilot) - AI 程式輔助
- [Gherkin](https://cucumber.io/docs/gherkin/) - BDD 規格語言
- 靈感來自測試驅動開發和行為驅動開發原則

---

## 📞 支援

- 📖 [文件](docs/)
- 💬 [GitHub Issues](https://github.com/CodeMachine0121/GSI-Protocol/issues)
- 💡 [討論](https://github.com/CodeMachine0121/GSI-Protocol/discussions)

---

<div align="center">

**[⬆ 回到頂端](#gsi-protocol中文)**

由開發者打造，為開發者服務 ❤️

</div>
