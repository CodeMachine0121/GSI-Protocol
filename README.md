# GSI-Protocol（中文）

> **Gherkin → 結構 → 實作**
>
> 一個語言無關的工作流程，使用 AI 代理和 BDD 原則建立可驗證的軟體功能。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 什麼是 GSI-Protocol?

GSI-Protocol 是一個 Claude Code 工作流程插件，實作了**規格驅動開發（SDD）**。它透過嚴格的四階段流程，將模糊的需求轉化為經過驗證、可用於生產環境的程式碼。

### 核心理念

**"規格 → 結構 → 實作"**

將業務邏輯、技術架構和程式撰寫分離到不同階段，以最小化 AI 幻覺並最大化精確度。

### 主要特性

- 🌍 **語言無關**：支援 Python、TypeScript、Go、Java、Rust、C# 等等
- 🎯 **框架獨立**：不綁定任何特定函式庫或框架
- 📝 **基於 BDD**：使用 Gherkin 撰寫清晰、可測試的規格
- ✅ **可驗證**：自動根據規格進行驗證
- 🔄 **模組化**：可獨立執行各階段或完整工作流程

---

## 📦 快速開始

### 安裝（30 秒）

**選項 1：一鍵安裝（如果 repo 為 public）：**

```bash
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

**選項 2：全域安裝（推薦）：**

```bash
mkdir -p ~/.claude/workflows
cd ~/.claude/workflows
git clone https://github.com/CodeMachine0121/GSI-Protocol.git gsi-protocol
```

現在可以在任何專案中使用！

**選項 3：專案專用安裝：**

```bash
cd /tmp
git clone https://github.com/CodeMachine0121/GSI-Protocol.git gsi-temp
cd ~/your-project
mkdir -p .claude/commands
cp /tmp/gsi-temp/.claude/commands/* .claude/commands/
rm -rf /tmp/gsi-temp
```

> 📖 查看 [安裝指南](docs/INSTALL.md) 了解更多選項

### 第一次使用（2 分鐘）

```bash
cd your-project

# 自動模式 - 生成所有內容
/sdd-auto Create a shopping cart in TypeScript with add, remove, checkout functions

# 手動模式 - 逐步執行
/sdd-spec Create a shopping cart with add, remove, checkout
/sdd-arch features/shopping_cart.feature
/sdd-impl features/shopping_cart.feature structure/shopping_cart_structure.ts
/sdd-verify features/shopping_cart.feature implementation/shopping_cart_impl.ts
```

---

## 📚 文件

| 文件 | 說明 |
|----------|-------------|
| **[快速入門指南](docs/QUICKSTART.md)** | 5 分鐘教學 |
| **[安裝指南](docs/INSTALL.md)** | 詳細安裝說明 |
| **[指令參考](docs/COMMANDS.md)** | 完整指令文件 |
| **[語言指南](docs/LANGUAGE_GUIDE.md)** | 多語言支援指南 |
| **[工作流程定義](docs/expected_workflow.md)** | 詳細方法論 |
| **[貢獻指南](CONTRIBUTING.md)** | 如何貢獻 |

---

## 🔄 工作流程概覽

### 四個階段

```
階段 1：規格（PM）
    ↓
    Gherkin .feature 檔案
    ↓
階段 2：結構（架構師）
    ↓
    資料模型 + 介面
    ↓
階段 3：實作（工程師）
    ↓
    可運行的程式碼
    ↓
階段 4：驗證（QA）
    ↓
    ✅ 已驗證功能
```

### 指令

| 指令 | 用途 | 何時使用 |
|---------|---------|-------------|
| `/sdd-auto` | 自動執行全部 4 個階段 | 快速原型、簡單功能 |
| `/sdd-spec` | 生成 Gherkin 規格 | 定義需求 |
| `/sdd-arch` | 設計資料模型與介面 | 審查結構 |
| `/sdd-impl` | 實作邏輯 | 撰寫程式碼 |
| `/sdd-verify` | 根據規格驗證 | 測試實作 |

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

**階段 2：結構** (`structure/vip_discount_structure.py`)
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

**階段 3：實作** (`implementation/vip_discount_impl.py`)
```python
def calculate_discount(amount: float, user_type: UserType) -> DiscountResult:
    if user_type == UserType.VIP and amount >= 100:
        discount = amount * 0.2
        return DiscountResult(amount - discount, discount)
    return DiscountResult(amount, 0)
```

**階段 4：驗證**
```
✅ 所有情境通過
✅ 功能完成
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
/sdd-impl features/user_registration.feature structure/user_registration_structure.py

# QA：驗證
/sdd-verify features/user_registration.feature implementation/user_registration_impl.py
```

---

## 📁 專案結構

```
GSI-Protocol/
├── README.md                    # 本檔案
├── CONTRIBUTING.md              # 貢獻指南
├── LICENSE                      # MIT 授權
├── install.sh                   # 安裝腳本
├── .claude/
│   └── commands/                # Claude Code slash 指令
│       ├── gsi-auto.md         # 自動工作流程
│       ├── gsi-spec.md         # 階段 1
│       ├── gsi-arch.md         # 階段 2
│       ├── gsi-impl.md         # 階段 3
│       └── gsi-verify.md       # 階段 4
├── docs/                        # 文件
│   ├── QUICKSTART.md           # 快速入門指南
│   ├── INSTALL.md              # 安裝指南
│   ├── COMMANDS.md             # 指令參考
│   ├── LANGUAGE_GUIDE.md       # 語言支援
│   └── expected_workflow.md    # 工作流程細節
├── prompts/                     # 代理提示
│   ├── pm_agent.md
│   ├── architect_agent.md
│   ├── engineer_agent.md
│   └── qa_agent.md
└── examples/                    # 實作範例
    ├── referral_bonus/         # Python 範例
    └── vip_discount_typescript/ # TypeScript 範例
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

- Claude Code CLI
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
