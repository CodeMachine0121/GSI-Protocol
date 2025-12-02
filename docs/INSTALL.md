# 安裝指南

本文件說明如何在您的專案中安裝和使用 SDD Workflow 工具。

---

## ⚠️ 重要提醒

**不要直接 clone 整個 repo 到您的專案！** 這會把 `examples/`、`prompts/` 等範例程式碼也複製進去，污染您的專案。

請使用下面推薦的安裝方式。

---

## 方法一：全域安裝（強烈推薦）✅

這是最乾淨的方式，安裝一次後所有專案都能使用，不會污染任何專案目錄。

```bash
# 1. 創建全域 workflows 目錄
mkdir -p ~/.claude/workflows

# 2. Clone 到全域目錄
cd ~/.claude/workflows
git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-workflow

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

# 使用 SDD workflow
/sdd-auto Create a user authentication system in Python with JWT tokens
```

---

## 方法二：專案內安裝（只複製指令）

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
git commit -m "Add SDD workflow commands"
```

### 使用腳本安裝

#### 選項 A：一鍵 curl 安裝（推薦，需要 Public Repo）

⚠️ **注意**：此方式只在 repo 為 public 時可用

```bash
# 下載並執行安裝腳本
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash

# 或使用 wget
wget -qO- https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/install.sh | bash
```

#### 選項 B：Clone 後安裝（Private Repo 也可用）

```bash
# 1. Clone repo（private repo 會要求 GitHub 認證）
git clone https://github.com/CodeMachine0121/GSI-Protocol.git /tmp/gsi-temp
cd /tmp/gsi-temp

# 2. 執行安裝腳本
./install.sh

# 3. 清理
cd ~ && rm -rf /tmp/gsi-temp
```

**如何選擇**：
- ✅ Repo 是 **public** → 使用選項 A（最快最方便）
- ✅ Repo 是 **private** → 使用選項 B 或「手動複製」方式

---

## 方法三：使用 Git Sparse Checkout（進階）

只 checkout 需要的目錄，不下載 examples。

```bash
cd ~/your-project

# 初始化 sparse checkout
git clone --no-checkout https://github.com/CodeMachine0121/GSI-Protocol.git .sdd-tools
cd .sdd-tools

# 設定只 checkout .claude/commands
git sparse-checkout init --cone
git sparse-checkout set .claude/commands

# checkout
git checkout main

# 複製到專案根目錄
cd ..
cp -r .sdd-tools/.claude .

# 清理
rm -rf .sdd-tools
```

---

## 驗證安裝成功

### 檢查檔案

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

### 測試指令

在 Claude Code 中：

1. 輸入 `/` 應該會看到指令提示
2. 嘗試執行：`/sdd-spec Create a simple calculator`
3. 應該會生成 `features/calculator.feature` 檔案

---

## 第一次使用

### 快速模式

```bash
/sdd-auto Create a shopping cart in TypeScript with add, remove, and checkout functions
```

### 手動模式

```bash
# 步驟 1
/sdd-spec Create a shopping cart with add, remove, checkout

# 步驟 2（審查 features/shopping_cart.feature 後）
/sdd-arch features/shopping_cart.feature

# 步驟 3（審查 structure/ 後）
/sdd-impl features/shopping_cart.feature structure/shopping_cart_structure.ts

# 步驟 4（審查 implementation/ 後）
/sdd-verify features/shopping_cart.feature implementation/shopping_cart_impl.ts
```

---

## 專案結構

使用 SDD workflow 後，您的專案會新增這些目錄：

```
your-project/
├── .claude/
│   └── commands/           # SDD 指令（安裝時建立）
│       ├── sdd-auto.md
│       ├── sdd-spec.md
│       ├── sdd-arch.md
│       ├── sdd-impl.md
│       └── sdd-verify.md
├── features/               # 階段 1：Gherkin 規格（自動生成）
│   └── *.feature
├── structure/              # 階段 2：資料模型（自動生成）
│   └── *_structure.*
└── implementation/         # 階段 3：實作程式碼（自動生成）
    └── *_impl.*
```

**不會有 examples/ 或 prompts/ 目錄** - 這些只存在於 SDD workflow repo 本身。

---

## 多專案使用建議

### 推薦配置

- ✅ **全域安裝**：`~/.claude/workflows/sdd-workflow`（所有專案共用）
- ✅ **專案目錄**：只有 `features/`、`structure/`、`implementation/`（生成的程式碼）
- ❌ **不要**：把整個 SDD repo clone 到專案裡

### 團隊協作

如果團隊需要統一使用：

```bash
# 方式 1：每個開發者自己全域安裝
每人執行：mkdir -p ~/.claude/workflows && cd ~/.claude/workflows && git clone https://github.com/CodeMachine0121/GSI-Protocol.git

# 方式 2：專案內只包含 commands（Git 管理）
在專案內：mkdir -p .claude/commands && cp <commands>
然後 commit .claude/commands/ 到 Git
```

---

## 更新 SDD Workflow

### 全域安裝的更新

```bash
cd ~/.claude/workflows/sdd-workflow
git pull
```

### 專案內安裝的更新

重新執行安裝步驟，覆蓋 `.claude/commands/` 內容。

---

## 卸載

### 全域安裝

```bash
rm -rf ~/.claude/workflows/sdd-workflow
```

### 專案內安裝

```bash
rm -rf .claude/commands/sdd-*.md
```

---

## 常見問題

### Q：我的專案裡出現了 examples/ 目錄怎麼辦？

**A：** 這表示您錯誤地 clone 了整個 repo 到專案裡。請：
1. 刪除：`rm -rf .sdd-workflow` 或類似目錄
2. 重新按照「方法二」只複製 commands
3. 確認 `git status` 沒有 examples 相關檔案

### Q：全域安裝和專案內安裝有什麼區別？

**A：**
- **全域**：安裝一次，所有專案都能用，專案目錄保持乾淨
- **專案內**：指令隨專案走，團隊成員 clone 後就有，但需要手動複製

### Q：團隊成員需要每個人都安裝嗎？

**A：**
- 如果用全域安裝：是，每人自己裝
- 如果用專案內安裝並 commit 到 Git：不用，clone 專案就有

### Q：如何查看 examples 範例？

**A：**
```bash
# 訪問 SDD workflow repo
cd ~/.claude/workflows/sdd-workflow/examples

# 或直接在 GitHub 上查看
```

### Q：生成的檔案要 commit 到 Git 嗎？

**A：**
- ✅ `features/*.feature` - 建議 commit（需求文件）
- ✅ `structure/*` - 建議 commit（技術設計）
- ⚠️ `implementation/*` - 視情況（如果是最終程式碼則 commit）
- ❌ `verification/*` - 不建議（臨時驗證報告）

---

## 下一步

安裝完成後：

1. 📖 閱讀 [QUICKSTART.md](QUICKSTART.md) - 5 分鐘快速入門
2. 📖 閱讀 [COMMANDS.md](COMMANDS.md) - 完整指令參考
3. 📖 閱讀 [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) - 多語言支援
4. 🔍 查看 examples（在 SDD repo 裡，不在您的專案）

---

**快速安裝指令：**

```bash
# 全域安裝（推薦）
mkdir -p ~/.claude/workflows && cd ~/.claude/workflows && git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-workflow

# 專案內安裝（只複製 commands）
mkdir -p .claude/commands && cd /tmp && git clone https://github.com/CodeMachine0121/GSI-Protocol.git sdd-temp && cp sdd-temp/.claude/commands/* <your-project>/.claude/commands/ && rm -rf sdd-temp
```

開始使用 SDD Workflow，讓 AI 幫您寫結構化的程式碼！🚀
