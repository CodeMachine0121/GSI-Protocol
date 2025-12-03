# 安裝指南

本文件說明如何在您的專案中安裝和使用 GSI-Protocol 工作流程。

**支援平台：**
- ✅ Claude Code
- ✅ Codex (OpenAI)

---

## ⚠️ 重要提醒

**不要直接 clone 整個 repo 到您的專案！** 這會把 `examples/`、`prompts/` 等範例程式碼也複製進去，污染您的專案。

請使用下面推薦的安裝方式。

---

## 方法一：一鍵安裝（最推薦）✅

這是最簡單的方式，會自動詢問您要安裝哪個 AI 平台，以及全域安裝或專案內安裝。

```bash
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

安裝腳本會引導您完成：
1. 選擇 AI 平台（Claude Code、Codex 或兩者）
2. 選擇安裝位置（全域或當前專案）
3. 自動完成設定

---

## 方法二：手動全域安裝

這是最乾淨的方式，安裝一次後所有專案都能使用，不會污染任何專案目錄。

```bash
# 1. 創建全域指令目錄
mkdir -p ~/.claude/commands

# 2. 下載 SDD 指令檔案
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md -o ~/.claude/commands/sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md -o ~/.claude/commands/sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md -o ~/.claude/commands/sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md -o ~/.claude/commands/sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md -o ~/.claude/commands/sdd-verify.md

# 3. 完成！現在在任何專案都能使用
cd ~/your-project
# 直接使用指令
```

---

## 📖 安裝流程

### 互動式安裝

執行安裝程式後，您會看到：

```
🚀 GSI-Protocol Installer
============================================================

Select AI platform(s) to install:
1) Claude Code only
2) Codex (OpenAI) only
3) Both Claude Code and Codex
Enter choice [1-3] (default: 3): 3

✓ Git repository detected

Choose installation type:
1) Install to current project
2) Install globally to home directory
Enter choice [1-2] (default: 1): 2

ℹ Downloading GSI-Protocol from GitHub...
✓ Downloaded successfully
✓ Installed 5 Claude Code commands to ~/.claude/commands
✓ Installed 5 Codex commands to ~/.codex/commands

============================================================
✓ Installation complete! Total files installed: 10

You can now use SDD commands:
  /sdd-auto <requirement>
  /sdd-spec <requirement>
  /sdd-arch <feature.feature>
  /sdd-impl <feature.feature>
  /sdd-verify <feature.feature>

📖 Documentation: https://github.com/CodeMachine0121/GSI-Protocol
```

---

## 🔍 手動安裝

如果您偏好手動安裝，或在沒有 Python 的環境：

### 手動全域安裝

**Claude Code:**
```bash
mkdir -p ~/.claude/commands
cd ~/.claude/commands

# 下載所有指令檔案
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md
```

**Codex (OpenAI):**
```bash
mkdir -p ~/.codex/commands
cd ~/.codex/commands

# 下載所有指令檔案
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-verify.md
```

### 手動專案內安裝

**在當前專案中：**
```bash
# Claude Code
mkdir -p .claude/commands
cd .claude/commands
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md

# Codex
mkdir -p .codex/commands
cd .codex/commands
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-verify.md

# 提交到 Git（可選）
git add .claude/commands/ .codex/commands/
git commit -m "Add GSI-Protocol workflow commands"
```

---

## ✅ 驗證安裝

### 檢查檔案

**Claude Code (全域安裝):**
```bash
ls ~/.claude/commands/ | grep sdd
```

**Codex (全域安裝):**
```bash
ls ~/.codex/commands/ | grep sdd
```

**專案內安裝:**
```bash
ls .claude/commands/ | grep sdd
# 或
ls .codex/commands/ | grep sdd
```

應該看到：
```
sdd-auto.md
sdd-spec.md
sdd-arch.md
sdd-impl.md
sdd-verify.md
```

### 測試指令

在您的 AI 工具中：

1. 輸入 `/` 應該會看到指令提示
2. 嘗試執行：`/sdd-spec Create a simple calculator`
3. 應該會生成 `features/calculator.feature` 檔案

---

## 第一次使用

### 快速模式（推薦）

```bash
/sdd-auto Create a shopping cart in TypeScript with add, remove, and checkout functions
```

### 手動模式（逐步執行）

```bash
# 步驟 1：定義規格
/sdd-spec Create a shopping cart with add, remove, checkout

# 步驟 2：設計架構（審查 features/shopping_cart.feature 後）
/sdd-arch features/shopping_cart.feature

# 步驟 3：實作程式碼（審查 docs/ 後）
/sdd-impl features/shopping_cart.feature

# 步驟 4：驗證實作（審查 src/ 後）
/sdd-verify features/shopping_cart.feature
```

---

## 專案結構

使用 GSI-Protocol 工作流程後，您的專案會新增這些內容：

### 全域安裝

**Claude Code:**
```
~/.claude/commands/
├── sdd-auto.md
├── sdd-spec.md
├── sdd-arch.md
├── sdd-impl.md
└── sdd-verify.md
```

**Codex (OpenAI):**
```
~/.codex/commands/
├── sdd-auto.md
├── sdd-spec.md
├── sdd-arch.md
├── sdd-impl.md
└── sdd-verify.md
```

**您的專案保持乾淨，只有生成的程式碼:**
```
your-project/
├── features/
│   └── *.feature
├── docs/
│   └── features/
│       └── {feature}/
│           ├── architecture.md
│           └── conclusion.md
└── src/
    └── （您的實作程式碼）
```

### 專案內安裝

```
your-project/
├── .claude/               # Claude Code 指令（可選）
│   └── commands/
│       ├── sdd-auto.md
│       ├── sdd-spec.md
│       ├── sdd-arch.md
│       ├── sdd-impl.md
│       └── sdd-verify.md
├── .codex/                # Codex 指令（可選）
│   └── commands/
│       ├── sdd-auto.md
│       ├── sdd-spec.md
│       ├── sdd-arch.md
│       ├── sdd-impl.md
│       └── sdd-verify.md
├── features/              # Phase 1：Gherkin 規格
│   └── *.feature
├── docs/
│   └── features/          # Phase 2：架構設計
│       └── {feature}/
│           ├── architecture.md
│           └── conclusion.md
└── src/                   # Phase 3：實作程式碼
    └── （您的程式碼）
```

**不會有 examples/ 或 prompts/ 目錄** - 這些只存在於 GSI-Protocol repo 本身。

---

## 多專案使用建議

### 推薦配置

- ✅ **全域安裝**：`~/.claude/commands/` 或 `~/.codex/commands/` (所有專案共用)
- ✅ **專案目錄**：只有 `features/`、`docs/features/`、`src/`（生成的程式碼）
- ❌ **不要**：把整個 GSI-Protocol repo clone 到專案裡

### 團隊協作

如果團隊需要統一使用：

**方式 1：每個開發者自己全域安裝（推薦）**
```bash
每人執行：curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

**方式 2：專案內只包含 commands（Git 管理）**
```bash
# 在專案內安裝並 commit
mkdir -p .claude/commands .codex/commands
# 複製命令檔案...
git add .claude/commands/ .codex/commands/
git commit -m "Add SDD workflow commands"
```

---

## 🔄 更新 GSI-Protocol

重新執行安裝程式即可：

```bash
uvx gsi-protocol-installer
```

或手動下載最新的指令檔案（使用上方的 wget 命令）。

---

## 🗑️ 卸載

### 全域安裝

**Claude Code:**
```bash
rm -f ~/.claude/commands/sdd-*.md
```

**Codex (OpenAI):**
```bash
rm -f ~/.codex/commands/sdd-*.md
```

### 專案內安裝

**Claude Code:**
```bash
rm -rf .claude/commands/sdd-*.md
# 或整個目錄
rm -rf .claude/
```

**Codex (OpenAI):**
```bash
rm -rf .codex/commands/sdd-*.md
# 或整個目錄
rm -rf .codex/
```

---

## ❓ 常見問題

### Q：推薦用全域安裝還是專案內安裝？

**A：** 全域安裝更方便：
- ✅ 一次安裝，所有專案都能用
- ✅ 專案目錄保持乾淨
- ✅ 容易更新
- 唯一缺點：團隊成員需要各自安裝

如果整個團隊需要使用，建議全域安裝 + 在文檔中說明安裝步驟。

### Q：我應該選擇 Claude Code 還是 Codex？

**A：** 取決於您的 AI 工具：
- 如果使用 Claude Code → 安裝 `.claude/commands/`
- 如果使用 Codex (OpenAI) → 安裝 `.codex/commands/`
- 可以同時安裝兩者，隨時切換使用

### Q：Claude Code 和 Codex 的指令內容有差異嗎？

**A：** 沒有，兩個平台的指令內容完全相同，只是目錄位置不同。這樣設計是為了讓兩個平台都能使用相同的工作流程。

### Q：需要安裝 Python 嗎？

**A：** 推薦但非必需：
- ✅ **有 Python**：使用 `uvx` 或 `pipx` 安裝（推薦）
- ⚠️ **沒有 Python**：可以手動下載指令檔案

### Q：uvx 是什麼？

**A：** `uvx` 是 uv 工具的一部分，用於執行 Python 應用程式而無需安裝。類似於 `npx`（Node.js）。

安裝 uv：
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Q：全域安裝和專案內安裝有什麼區別？

**A：**
- **全域**：`~/.claude/commands/` 或 `~/.codex/commands/`，所有專案共用，專案保持乾淨
- **專案內**：`.claude/commands/` 或 `.codex/commands/`，指令隨專案走，團隊成員 clone 後就有

### Q：團隊成員需要每個人都安裝嗎？

**A：**
- 如果用全域安裝：是，每人自己執行一遍安裝（推薦：`uvx gsi-protocol-installer`）
- 如果用專案內安裝並 commit 到 Git：不用，clone 專案就有

---

## 下一步

安裝完成後：

1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md) - 5 分鐘快速入門
2. 📖 閱讀 [COMMANDS.md](COMMANDS.md) - 完整指令參考
3. 📖 閱讀 [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) - 多語言支援
4. 🔍 查看 [expected_workflow.md](expected_workflow.md) - 詳細工作流程說明

---

**快速安裝指令：**

**一鍵安裝（推薦）：**
```bash
uvx gsi-protocol-installer
```

**手動全域安裝 - Claude Code：**
```bash
mkdir -p ~/.claude/commands && cd ~/.claude/commands
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md
```

**手動全域安裝 - Codex (OpenAI)：**
```bash
mkdir -p ~/.codex/commands && cd ~/.codex/commands
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/commands/sdd-verify.md
```

開始使用 GSI-Protocol，讓 AI 幫您寫結構化的程式碼！🚀
