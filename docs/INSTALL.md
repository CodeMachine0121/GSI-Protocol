# 安裝指南

本文件說明如何在您的專案中安裝和使用 GSI-Protocol 工作流程。

---

## ⚠️ 重要提醒

**不要直接 clone 整個 repo 到您的專案！** 這會把 `examples/`、`prompts/` 等範例程式碼也複製進去，污染您的專案。

請使用下面推薦的安裝方式。

---

## 方法一：一鍵安裝（最推薦）✅

這是最簡單的方式，會自動詢問您是要全域安裝還是專案內安裝。

```bash
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

安裝腳本會詢問您的偏好，然後自動完成設定。

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

### 驗證安裝

在 Claude Code 中輸入 `/sdd` 應該會看到自動補全提示：
- `/sdd-auto`
- `/sdd-spec`
- `/sdd-arch`
- `/sdd-impl`
- `/sdd-verify`

### 使用範例

```bash
# 在任何專案目錄中
cd ~/projects/my-python-api

# 使用 GSI-Protocol 工作流程
/sdd-auto Create a user authentication system in Python with JWT tokens
```

---

## 方法三：手動專案內安裝

如果您只想在特定專案使用，或需要團隊共享這些指令。

### 手動複製（最簡單）

```bash
# 1. 在專案外臨時下載
cd /tmp
git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-temp

# 2. 進入您的專案
cd ~/your-project

# 3. 只複製 commands 目錄
mkdir -p .claude/commands
cp /tmp/sdd-temp/.claude/commands/* .claude/commands/

# 4. 清理臨時檔案
rm -rf /tmp/sdd-temp

# 5. 提交到 Git（可選）
git add .claude/commands/
git commit -m "Add GSI-Protocol workflow commands"
```

### 使用腳本安裝（Clone 方式）

對於 private repo 或需要更多控制的情況：

```bash
# 1. Clone repo（private repo 會要求 GitHub 認證）
git clone https://github.com/CodeMachine0121/GSI-Protocol.git /tmp/gsi-temp
cd /tmp/gsi-temp

# 2. 執行安裝腳本
./install.sh

# 3. 清理
cd ~ && rm -rf /tmp/gsi-temp
```

---

## 驗證安裝成功

### 檢查檔案

```bash
# 全域安裝
ls ~/.claude/commands/ | grep sdd

# 或專案內安裝
ls .claude/commands/ | grep sdd

# 應該看到：
# sdd-auto.md
# sdd-spec.md
# sdd-arch.md
# sdd-impl.md
# sdd-verify.md
```

### 測試指令

在 Claude Code 中：

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

```
~/.claude/commands/
├── sdd-auto.md
├── sdd-spec.md
├── sdd-arch.md
├── sdd-impl.md
└── sdd-verify.md

# 您的專案保持乾淨，只有生成的程式碼
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
├── .claude/
│   └── commands/           # SDD 指令（安裝時建立）
│       ├── sdd-auto.md
│       ├── sdd-spec.md
│       ├── sdd-arch.md
│       ├── sdd-impl.md
│       └── sdd-verify.md
├── features/               # 階段 1：Gherkin 規格
│   └── *.feature
├── docs/
│   └── features/           # 階段 2：架構設計
│       └── {feature}/
│           ├── architecture.md
│           └── conclusion.md
└── src/                    # 階段 3：實作程式碼
    └── （您的程式碼）
```

**不會有 examples/ 或 prompts/ 目錄** - 這些只存在於 GSI-Protocol repo 本身。

---

## 多專案使用建議

### 推薦配置

- ✅ **全域安裝**：`~/.claude/commands/sdd-*.md`（所有專案共用）
- ✅ **專案目錄**：只有 `features/`、`docs/features/`、`src/`（生成的程式碼）
- ❌ **不要**：把整個 GSI-Protocol repo clone 到專案裡

### 團隊協作

如果團隊需要統一使用：

```bash
# 方式 1：每個開發者自己全域安裝
每人執行：curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash

# 方式 2：專案內只包含 commands（Git 管理）
在專案內：mkdir -p .claude/commands && cp <commands>
然後 commit .claude/commands/ 到 Git
```

---

## 更新 GSI-Protocol

### 全域安裝的更新

如果您是從 GitHub repo 直接下載的指令檔案，只需重新執行 curl 命令下載最新版本即可。

```bash
# 或簡單方式：重新執行一鍵安裝
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

### 專案內安裝的更新

重新執行安裝步驟，覆蓋 `.claude/commands/` 內容。

---

## 卸載

### 全域安裝

```bash
rm -f ~/.claude/commands/sdd-*.md
```

### 專案內安裝

```bash
rm -rf .claude/commands/sdd-*.md
```

---

## 常見問題

### Q：推薦用全域安裝還是專案內安裝？

**A：** 全域安裝更方便：
- ✅ 一次安裝，所有專案都能用
- ✅ 專案目錄保持乾淨
- ✅ 容易更新
- 唯一缺點：團隊成員需要各自安裝

如果整個團隊需要使用，建議全域安裝 + 在文檔中說明安裝步驟。

### Q：我的專案裡出現了 examples/ 目錄怎麼辦？

**A：** 這表示您錯誤地 clone 了整個 repo 到專案裡。請：
1. 刪除：`rm -rf .claude/gsi-protocol` 或類似目錄
2. 改為只複製 `.claude/commands/`
3. 確認 `git status` 沒有 examples 相關檔案

### Q：全域安裝和專案內安裝有什麼區別？

**A：**
- **全域**：`~/.claude/commands/sdd-*.md`，所有專案共用，專案保持乾淨
- **專案內**：`.claude/commands/sdd-*.md`，指令隨專案走，團隊成員 clone 後就有

### Q：團隊成員需要每個人都安裝嗎？

**A：**
- 如果用全域安裝：是，每人自己執行一遍安裝
- 如果用專案內安裝並 commit 到 Git：不用，clone 專案就有

### Q：生成的檔案要 commit 到 Git 嗎？

**A：**
- ✅ `features/*.feature` - 建議 commit（需求文件，重要）
- ✅ `docs/features/*/architecture.md` - 建議 commit（技術設計）
- ✅ `src/` - 建議 commit（實作程式碼）
- ❌ `docs/features/*/conclusion.md` - 不建議（臨時驗證報告）

### Q：如何查看 examples 範例？

**A：** 直接訪問 GitHub repo：
```
https://github.com/CodeMachine0121/GSI-Protocol/tree/main/examples
```

---

## 下一步

安裝完成後：

1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md) - 5 分鐘快速入門
2. 📖 閱讀 [COMMANDS.md](COMMANDS.md) - 完整指令參考
3. 📖 閱讀 [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) - 多語言支援
4. 🔍 查看 [expected_workflow.md](expected_workflow.md) - 詳細工作流程說明

---

**快速安裝指令：**

```bash
# 最簡單：一鍵安裝（推薦）
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash

# 或手動全域安裝
mkdir -p ~/.claude/commands
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md -o ~/.claude/commands/sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md -o ~/.claude/commands/sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md -o ~/.claude/commands/sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md -o ~/.claude/commands/sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md -o ~/.claude/commands/sdd-verify.md
```

開始使用 GSI-Protocol，讓 AI 幫您寫結構化的程式碼！🚀
