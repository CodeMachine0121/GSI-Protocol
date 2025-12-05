# GSI-Protocol - 快速入門指南

5 分鐘開始使用 GSI-Protocol（規格驅動開發）！

## 安裝

### 最簡單：使用 uvx（推薦）⚡

```bash
uvx gsi-protocol-installer
```

安裝程式會引導您選擇：
1. AI 平台（Claude Code、Codex、GitHub Copilot 或多個）
2. 安裝位置（全域或當前專案）

### 或者：手動全域安裝

**Claude Code:**
```bash
mkdir -p ~/.claude/commands && cd ~/.claude/commands
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md
```

**Codex (OpenAI):**
```bash
mkdir -p ~/.codex/prompts && cd ~/.codex/prompts
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-auto.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-spec.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-arch.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-integration-test.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-impl.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-verify.md
```

**GitHub Copilot:**
```bash
mkdir -p ~/.github/prompts && cd ~/.github/prompts
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-auto.prompts.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-spec.prompts.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-arch.prompts.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-integration-test.prompts.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-impl.prompts.md
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-verify.prompts.md
```

現在在任何專案都能用！

### 驗證安裝

```bash
# Claude Code 全域安裝驗證
ls ~/.claude/commands/ | grep "sdd.*.prompts.md"

# Codex 全域安裝驗證
ls ~/.codex/prompts/ | grep "sdd.*.prompts.md"

# GitHub Copilot 全域安裝驗證
ls ~/.github/prompts/ | grep "sdd.*.prompts.md"

# 應該看到: sdd-auto.md, sdd-spec.md, sdd-arch.md, sdd-integration-test.md, sdd-impl.md, sdd-verify.md
```

> 📖 詳細安裝說明請參考 [INSTALL.md](INSTALL.md) 或 [Python 安裝器](PYTHON_INSTALLER.md)

---

## 您的第一個 SDD 功能

### 步驟 1：定義需求

想一個您想實作的簡單功能。例如：
> "我需要一個折扣系統，VIP 使用者購買超過 $100 可享 20% 折扣。"

### 步驟 2：執行自動工作流程

在您的 AI 工具（Claude Code、Codex 或 GitHub Copilot）中，使用 `/sdd-auto` 或 `@workspace /sdd-auto` 指令：

**Claude Code / Codex:**
```
/sdd-auto I need a discount system where VIP users get 20% off purchases over $100
```

**GitHub Copilot:**
```
@workspace /sdd-auto I need a discount system where VIP users get 20% off purchases over $100
```

代理會自動：
1. 生成 Gherkin 規格（`features/discount.feature`）
2. 設計架構文件（`docs/features/discount/architecture.md`）
3. 實作程式碼（依 architecture.md 定義的位置）
4. 驗證並生成結論（`docs/features/discount/conclusion.md`）

一次完成，Phase 之間不會停止！

### 步驟 3：審查輸出

檢查生成的檔案：
- `features/` - 您的行為規格
- `docs/features/` - 架構設計與驗證結論
- `src/` (或您的專案目錄) - 實作程式碼

### 步驟 4：執行和測試

```bash
# 對於 Python 實作
python implementation/discount_impl.py

# 內建驗證會執行並顯示結果
```

---

## 使用個別 Phase

您也可以分別執行每個 Phase：

### Phase 1：僅規格
```
/sdd-spec I need a user authentication system
```
這只生成 Gherkin `.feature` 檔案。

### Phase 2：架構設計
```
/sdd-arch features/authentication.feature
```
這讀取您的 Gherkin 並生成語言無關的架構文件（繁中）。

### Phase 3：實作
```
/sdd-impl features/authentication.feature
```
這依據 architecture.md 生成實際的程式碼實作。

### Phase 4：驗證
```
/sdd-verify features/authentication.feature
```
這根據規格與架構驗證您的實作。

---

## 常見模式

### 模式 1：快速原型製作（自動模式）
```
/sdd-auto <完整需求>
# 一次生成所有內容 - 測試想法的最快方式
```

**最適合：** 探索想法、簡單功能、展示

### 模式 2：生產開發（手動模式）
```
/sdd-spec <需求>
# 審查並細化 Gherkin
/sdd-arch features/<feature>.feature
# 審查架構，視需要調整
/sdd-impl features/<feature>.feature
# 仔細審查實作
/sdd-verify features/<feature>.feature
```

**最適合：** 生產程式碼、複雜功能、團隊協作

### 模式 3：規格優先
```
# 手動撰寫您自己的 .feature 檔案
/sdd-arch features/my_feature.feature
/sdd-impl features/my_feature.feature
```

**最適合：** 明確定義的需求、API 契約、既有規格

---

## 成功秘訣

### 撰寫良好需求

✅ **良好：**
> "使用者可以按名稱搜尋產品。結果顯示產品名稱、價格和庫存狀態。如果找不到結果，顯示「找不到產品」訊息。"

❌ **太模糊：**
> "新增搜尋功能。"

❌ **太技術性：**
> "使用 PostgreSQL 全文搜尋建立帶分頁的 REST API 端點。"

### 理解輸出

每個 Phase 建立在前一個之上：
- **Phase 1** = 什麼（業務行為）
- **Phase 2** = 架構（資料模型和服務介面 - 繁中文件）
- **Phase 3** = 如何（實作邏輯 - 依專案架構）
- **Phase 4** = 驗證（它能運作嗎？- 結論報告）

### 何時使用各種方法

**使用 `/sdd-auto`（自動模式）當：**
- 您有清晰、簡單的需求
- 您想快速製作原型
- 您信任 AI 處理所有階段
- 您需要快速獲得可運作的解決方案

**使用手動階段當：**
- 您想仔細審查每個階段
- 需求複雜或模糊
- 您想手動撰寫某些階段
- 您正在學習 SDD 方法論
- 您正在開發生產程式碼

---

## 故障排除

### 找不到指令

確保您的 AI 工具能看到指令：

**Claude Code:**
```bash
ls ~/.claude/commands/ | grep "sdd.*.prompts.md"
# 或專案內
ls .claude/commands/ | grep "sdd.*.prompts.md"
```

**Codex:**
```bash
ls ~/.codex/prompts/ | grep "sdd.*.prompts.md"
# 或專案內
ls .codex/prompts/ | grep "sdd.*.prompts.md"
```

應該顯示：sdd-auto.md、sdd-spec.md、sdd-arch.md 等

### Python 匯入錯誤

確保您在正確的目錄：
```bash
cd implementation/
python -c "import sys; sys.path.insert(0, '..'); from structure.feature_structure import *"
```

或在程式碼中使用絕對匯入。

### Gherkin 語法錯誤

驗證您的 Gherkin 檔案：
- 每個情境需要 Given-When-Then
- 使用 2 個空格縮排
- 以 Feature: 宣告開始

---

## 下一步

1. **閱讀工作流程：** 查看 [expected_workflow.md](expected_workflow.md) 了解詳細方法論
2. **建立您自己的：** 使用 `/sdd-auto` 與您自己的功能需求
3. **探索平台：** 閱讀 [PLATFORM_SUPPORT.md](PLATFORM_SUPPORT.md) 了解 Claude Code vs Codex
4. **進階使用：** 查看 [PYTHON_INSTALLER.md](PYTHON_INSTALLER.md) 了解安裝器功能
5. **貢獻：** 閱讀 [../CONTRIBUTING.md](../CONTRIBUTING.md) 參與改進！

---

## 學習資源

- [README.md](../README.md) - 完整專案文件
- [expected_workflow.md](expected_workflow.md) - 詳細的 SDD 方法論
- [COMMANDS.md](COMMANDS.md) - 完整指令參考
- [PYTHON_INSTALLER.md](PYTHON_INSTALLER.md) - Python 安裝器使用指南
- [PLATFORM_SUPPORT.md](PLATFORM_SUPPORT.md) - AI 平台比較
- [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) - 多語言支援
- [INSTALL.md](INSTALL.md) - 詳細安裝指南
- [../CONTRIBUTING.md](../CONTRIBUTING.md) - 如何貢獻

---

## 獲取幫助

如果您遇到問題：
1. 閱讀 [INSTALL.md](INSTALL.md) 或 [PYTHON_INSTALLER.md](PYTHON_INSTALLER.md) 檢查安裝
2. 查看 [PLATFORM_SUPPORT.md](PLATFORM_SUPPORT.md) 確認平台設定
3. 閱讀 [expected_workflow.md](expected_workflow.md) 了解詳細工作流程
4. 在 [GitHub Issues](https://github.com/CodeMachine0121/GSI-Protocol/issues) 上提問

---

**準備開始了嗎？** 現在試試：
```
/sdd-auto I need a simple todo list where users can add, complete, and delete tasks
```

或逐步執行：
```
/sdd-spec I need a simple todo list where users can add, complete, and delete tasks
```

使用 GSI-Protocol 快樂編碼！🚀
