# 在新專案中使用 SDD Workflow

本指南教你如何在一個全新的專案中使用 SDD Workflow 工具。

## 前置需求

- ✅ 已安裝 Claude Code CLI
- ✅ 有一個專案目錄（新的或現有的）

---

## 方法一：Global 安裝（推薦）

適合在多個專案中重複使用。

### 步驟 1: Clone 到 Claude Code 全域目錄

```bash
# 創建全域 workflows 目錄
mkdir -p ~/.claude/workflows

# Clone 這個工具
cd ~/.claude/workflows
git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-workflow
```

### 步驟 2: 在任何專案中使用

```bash
# 進入你的專案目錄
cd ~/projects/my-new-project

# 直接使用指令
/sdd-auto Create a user authentication system in TypeScript
```

Claude Code 會自動找到全域安裝的指令。

---

## 方法二：專案內安裝

只在當前專案中使用。

### 步驟 1: Clone 到專案目錄

```bash
# 進入你的專案目錄
cd ~/projects/my-new-project

# Clone 工具到 .claude 目錄
git clone https://github.com/CodeMachine0121/GSI-Protocol.git .sdd-workflow

# 複製 slash commands 到專案
mkdir -p .claude/commands
cp .sdd-workflow/.claude/commands/* .claude/commands/
```

### 步驟 2: （可選）加入 Git 管理

```bash
# 選項 A: 作為 git submodule（推薦）
git submodule add https://github.com/CodeMachine0121/GSI-Protocol.git .sdd-workflow

# 選項 B: 直接 commit
git add .claude/
git commit -m "Add SDD workflow commands"
```

---

## 方法三：只複製 Commands（最輕量）

如果你只需要 slash commands，不需要文檔和範例。

```bash
cd ~/projects/my-new-project

# 創建目錄
mkdir -p .claude/commands

# 下載 commands（手動或用 curl/wget）
# 然後複製所有 .md 檔案到 .claude/commands/
```

---

## 驗證安裝

確認 Claude Code 能看到指令：

```bash
# 在專案目錄中
ls .claude/commands/

# 應該看到：
# sdd-auto.md
# sdd-spec.md
# sdd-arch.md
# sdd-impl.md
# sdd-verify.md
```

在 Claude Code 中輸入 `/` 應該會看到這些指令出現。

---

## 第一次使用

### 情境：你要開始一個新功能

假設你的專案是 TypeScript，要實作「購物車」功能。

#### 快速模式（推薦新手）

```bash
/sdd-auto Create a shopping cart in TypeScript. Users can add items, update quantities, remove items, and calculate total price. Each item has name, price, and quantity.
```

AI 會自動：
1. ✅ 生成 `features/shopping_cart.feature`（Gherkin 規格）
2. ✅ 生成 `structure/shopping_cart_structure.ts`（介面定義）
3. ✅ 生成 `implementation/shopping_cart_impl.ts`（實作程式碼）
4. ✅ 生成驗證報告

#### 手動模式（適合生產環境）

**步驟 1: 生成規格**
```bash
/sdd-spec Create a shopping cart. Users can add items, update quantities, remove items, and calculate total price.
```

審查 `features/shopping_cart.feature`，確認業務邏輯正確。

**步驟 2: 生成結構**
```bash
/sdd-arch features/shopping_cart.feature
```

審查 `structure/shopping_cart_structure.ts`，確認資料結構和介面設計。

**步驟 3: 實作程式碼**
```bash
/sdd-impl features/shopping_cart.feature structure/shopping_cart_structure.ts
```

審查 `implementation/shopping_cart_impl.ts`，確認邏輯正確。

**步驟 4: 驗證**
```bash
/sdd-verify features/shopping_cart.feature implementation/shopping_cart_impl.ts
```

查看驗證報告，確保所有情境都通過。

---

## 專案結構建議

安裝後，你的專案會產生這些檔案：

```
my-project/
├── .claude/
│   └── commands/           # SDD workflow 指令
│       ├── sdd-auto.md
│       ├── sdd-spec.md
│       ├── sdd-arch.md
│       ├── sdd-impl.md
│       └── sdd-verify.md
├── features/               # Phase 1 輸出：Gherkin 規格
│   └── shopping_cart.feature
├── structure/              # Phase 2 輸出：資料模型 & 介面
│   └── shopping_cart_structure.ts
├── implementation/         # Phase 3 輸出：實作程式碼
│   └── shopping_cart_impl.ts
└── verification/           # Phase 4 輸出：驗證報告（可選）
    └── shopping_cart_report.md
```

### 整合到現有專案結構

如果你的專案已有結構，可以調整路徑：

```typescript
// 例如將 implementation 整合到現有 src/
my-project/
├── src/
│   ├── services/          # 把生成的 impl 放這裡
│   │   └── shopping_cart.service.ts
│   └── types/             # 把生成的 structure 放這裡
│       └── shopping_cart.types.ts
└── specs/                 # 把 features 放這裡
    └── shopping_cart.feature
```

---

## 多語言專案範例

### Python 專案

```bash
cd my-python-project

# 自動生成
/sdd-auto Implement a user authentication service in Python with login, logout, and token refresh

# 會生成：
# features/user_auth.feature
# structure/user_auth_structure.py
# implementation/user_auth_impl.py
```

### Go 專案

```bash
cd my-go-project

# 自動生成
/sdd-auto Create a REST API handler in Go for managing products (CRUD operations)

# 會生成：
# features/product_api.feature
# structure/product_api_structure.go
# implementation/product_api_impl.go
```

### Rust 專案

```bash
cd my-rust-project

# 自動生成
/sdd-auto Build a configuration parser in Rust that reads TOML files and validates settings

# 會生成：
# features/config_parser.feature
# structure/config_parser_structure.rs
# implementation/config_parser_impl.rs
```

---

## 整合到團隊工作流

### 1. 加入 Git

```bash
# 將 .claude/commands 加入版本控制
git add .claude/
git commit -m "Add SDD workflow tools"

# 團隊成員 clone 後自動有這些指令
```

### 2. 設定 .gitignore

```bash
# 可以選擇性忽略生成的檔案
echo "verification/" >> .gitignore

# 或是全部保留做為文檔
# （features/ 和 structure/ 通常建議保留）
```

### 3. Code Review 流程

```bash
# 開發者
/sdd-auto Implement feature X

# 提交 PR，包含：
# - features/x.feature  （規格，給 PM/QA 審查）
# - structure/x.ts      （架構，給 Tech Lead 審查）
# - implementation/x.ts （程式碼，給工程師審查）
```

---

## 常見使用情境

### 情境 1: 快速原型

```bash
/sdd-auto Create a simple task manager in Python with add, complete, and list tasks
```

幾秒內獲得可運行的程式碼。

### 情境 2: API 設計

```bash
/sdd-spec Design a RESTful API for managing blog posts (create, read, update, delete, list)
/sdd-arch features/blog_api.feature
```

獲得清晰的 API 契約和資料結構。

### 情境 3: 重構現有程式碼

```bash
/sdd-spec The existing payment module should support multiple payment methods (credit card, PayPal, crypto)
# 基於生成的規格重新設計
```

### 情境 4: 文檔驅動開發

```bash
# 先寫規格
/sdd-spec User registration flow with email verification and password strength check

# 審查後再實作
/sdd-arch features/user_registration.feature
/sdd-impl features/user_registration.feature structure/user_registration_structure.py
```

---

## 最佳實踐

### ✅ DO

1. **指定語言**：`/sdd-auto Create X in TypeScript`
2. **描述清楚**：包含輸入、輸出、邊界條件
3. **保留 features/**：作為需求文檔
4. **審查生成的程式碼**：不要盲目使用
5. **逐步學習**：先用 `/sdd-auto`，再學手動模式

### ❌ DON'T

1. **不要跳過 Phase 1**：規格是一切的基礎
2. **不要在生產環境直接用自動模式**：需要人工審查
3. **不要混合多個功能**：一次只做一個 feature
4. **不要忽略驗證結果**：Phase 4 很重要
5. **不要依賴 Python 特定框架**：工具是語言無關的

---

## 故障排除

### 指令找不到

```bash
# 檢查檔案是否存在
ls .claude/commands/

# 確認路徑正確
pwd

# 重啟 Claude Code
```

### 生成的程式碼有錯誤

```bash
# 重新執行該階段
/sdd-impl features/x.feature structure/x.ts

# 或手動修改後再驗證
/sdd-verify features/x.feature implementation/x.ts
```

### 語言選擇錯誤

```bash
# 明確指定語言
/sdd-auto Create X in Go  # 而不是只寫 "Create X"
```

---

## 下一步

1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md) 了解更多範例
2. 📖 閱讀 [COMMANDS.md](COMMANDS.md) 了解所有指令細節
3. 📖 閱讀 [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) 了解特定語言的模式
4. 🔍 查看 `examples/` 目錄的實際範例

---

## 快速參考卡

```bash
# === 新專案快速開始 ===

# 1. 安裝
cd ~/.claude/workflows
git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-workflow

# 2. 進入專案
cd ~/my-project

# 3. 使用（自動模式）
/sdd-auto <你的需求> in <語言>

# 4. 使用（手動模式）
/sdd-spec <需求>
/sdd-arch features/spec.feature
/sdd-impl features/spec.feature structure/struct.py
/sdd-verify features/spec.feature implementation/impl.py
```

---

開始使用 SDD Workflow，讓 AI 幫你寫出結構化、可驗證的程式碼！🚀
