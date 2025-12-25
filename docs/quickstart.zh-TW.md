# GSI-Protocol 快速開始指南

**語言**: [English](./quickstart.md) | **繁體中文**

本指南將幫助您在幾分鐘內開始使用 GSI-Protocol。

## 前置需求

開始之前，請確保您已安裝：

- **Python 3.10+**
- **Git**
- **以下其中一個支援的 AI 平台**：
  - Claude Code CLI
  - Codex (OpenAI)
  - GitHub Copilot

## 安裝

### 步驟 1：安裝 GSI-Protocol

選擇以下其中一種方法：

#### 使用 uvx（推薦）

```bash
uvx --from gsi-protocol-installer gsi-install
```

#### 使用 pipx

```bash
pipx run gsi-protocol-installer
```

### 步驟 2：依照互動式安裝程式指示

安裝程式會詢問幾個問題：

1. **選擇 AI 平台**
   - 選擇一個或多個：Claude Code、Codex、GitHub Copilot
   - 預設：所有平台

2. **選擇安裝類型**
   - **專案**：安裝到當前專案（`.claude/`、`.codex/`、`.github/`）
   - **全域**：安裝到家目錄（`~/.claude/`、`~/.codex/`、`~/.github/`）

3. **針對 Claude Code：選擇元件**
   - 僅指令
   - 僅子代理
   - 兩者都要（推薦）

### 步驟 3：驗證安裝

安裝完成後，您應該會看到：

```
✓ 安裝完成！已安裝檔案總數：X

Claude Code / Codex 用法：
  /sdd-auto <需求>
  /sdd-spec <需求>
  /sdd-arch <feature.feature>
  /sdd-impl <feature.feature>
  /sdd-verify <feature.feature>
```

## 您的第一個工作流程

讓我們使用 GSI-Protocol 建立一個簡單的使用者認證功能。

### 範例：使用者認證

#### 選項 1：自動模式（最快）

使用單一指令執行完整工作流程：

```bash
/sdd-auto 新增使用者認證功能，包含電子郵件和密碼，支援登入和註冊
```

這將自動：
1. 生成 Gherkin 規格
2. 設計架構
3. 實作程式碼
4. 驗證實作

#### 選項 2：手動模式（更多控制）

逐步執行每個階段：

**階段 1：生成規格**
```bash
/sdd-spec 新增使用者認證功能，包含電子郵件和密碼，支援登入和註冊
```

輸出：`features/user_authentication.feature`

**階段 2：設計架構**
```bash
/sdd-arch features/user_authentication.feature
```

輸出：`docs/features/user_authentication/architecture.md`

**階段 3：實作程式碼**
```bash
/sdd-impl features/user_authentication.feature
```

輸出：原始碼檔案（位置在 architecture.md 中指定）

**階段 4：驗證實作**
```bash
/sdd-verify features/user_authentication.feature
```

輸出：`docs/features/user_authentication/conclusion.md`

**選用：生成整合測試**
```bash
/sdd-integration-test features/user_authentication.feature
```

輸出：專案測試目錄中的測試檔案

## 理解輸出

執行工作流程後，您將獲得：

### 1. Gherkin 規格（`features/user_authentication.feature`）

```gherkin
Feature: 使用者認證
  Scenario: 使用者成功註冊
    Given 使用者提供有效的電子郵件和密碼
    When 使用者提交註冊
    Then 帳戶被建立
    And 使用者收到確認
```

### 2. 架構文件（`docs/features/user_authentication/architecture.md`）

包含：
- 專案上下文（技術棧、框架）
- 功能概述
- 資料模型（User、Credentials 等）
- 服務介面（AuthService、UserRepository）
- 架構決策
- 檔案結構規劃

### 3. 實作檔案

在您的專案結構中生成：
- 模型檔案（例如：`models/User.ts`）
- 服務檔案（例如：`services/AuthService.ts`）

### 4. 驗證報告（`docs/features/user_authentication/conclusion.md`）

包含：
- 架構符合性檢查
- 情境驗證（Given-When-Then）
- 摘要（通過/失敗）
- 改進回饋

## 平台特定用法

### Claude Code

如果您安裝了指令：
```bash
/sdd-auto <需求>
```

如果您安裝了子代理：
```bash
# 子代理在您呼叫指令時自動執行
```

### Codex (OpenAI)

```bash
/sdd-auto <需求>
/sdd-spec <需求>
```

### GitHub Copilot

在所有指令前加上 `@workspace`：

```bash
@workspace /sdd-auto <需求>
@workspace /sdd-spec <需求>
```

## 技巧與最佳實踐

### 1. 撰寫清晰的需求

好的範例：
```bash
/sdd-auto 新增使用者認證功能，包含電子郵件/密碼，支援註冊、登入和密碼重設
```

不夠理想的範例：
```bash
/sdd-auto 認證相關功能
```

### 2. 實作前審查架構

使用手動模式時，在進入實作前先審查生成的架構文件。

### 3. 針對失敗的驗證進行迭代

如果階段 4 驗證失敗，審查結論報告並使用修正重新執行階段 3。

### 4. 使用整合測試進行 TDD

對於測試驅動開發，使用此工作流程：
```bash
/sdd-spec <需求>
/sdd-arch features/your_feature.feature
/sdd-integration-test features/your_feature.feature
/sdd-impl features/your_feature.feature
/sdd-verify features/your_feature.feature
```

### 5. 專案感知開發

GSI-Protocol 自動偵測：
- 您的技術棧（package.json、requirements.txt、go.mod 等）
- 專案結構（src/、models/、services/）
- 程式碼範例（*.ts、*.py、*.go）
- 命名慣例

## 常見工作流程

### 工作流程 1：快速新增功能

```bash
/sdd-auto 為產品列表 API 新增分頁支援
```

### 工作流程 2：測試驅動開發

```bash
/sdd-spec 新增產品搜尋與篩選功能
/sdd-arch features/product_search.feature
/sdd-integration-test features/product_search.feature
# 先寫測試，再實作
/sdd-impl features/product_search.feature
/sdd-verify features/product_search.feature
```

### 工作流程 3：架構審查

```bash
/sdd-spec 實作購物車功能
/sdd-arch features/shopping_cart.feature
# 審查 docs/features/shopping_cart/architecture.md
# 與團隊討論
/sdd-impl features/shopping_cart.feature
/sdd-verify features/shopping_cart.feature
```

## 問題排解

### 安裝問題

**問題**："Git 未安裝"
```bash
# 先安裝 git
# macOS: brew install git
# Ubuntu: sudo apt-get install git
# Windows: 從 https://git-scm.com/downloads 下載
```

**問題**："找不到指令：/sdd-auto"
- 確保您在安裝時選擇了正確的平台
- 檢查指令是否安裝在正確的目錄
- 對於 Claude Code：`ls ~/.claude/commands/` 或 `ls .claude/commands/`

### 工作流程問題

**問題**：架構不符合專案結構
- 審查 `docs/features/{feature}/architecture.md`
- 使用更清晰的需求重新執行 `/sdd-arch`
- 提供更多關於專案結構的上下文

**問題**：驗證失敗
- 閱讀結論報告：`docs/features/{feature}/conclusion.md`
- 檢查哪些情境失敗
- 使用修正重新執行 `/sdd-impl`

## 下一步

1. **探索生成的檔案**以理解工作流程
2. **自訂架構**設計以符合您的需求
3. **整合到 CI/CD**，在管線中執行驗證
4. **與團隊分享規格**，使用 Gherkin 檔案

## 獲得協助

- **GitHub Issues**：https://github.com/CodeMachine0121/GSI-Protocol/issues
- **文件**：https://github.com/CodeMachine0121/GSI-Protocol
- **電子郵件**：asdfg55887@gmail.com

## 接下來？

完成第一個工作流程後，您可以：

- 探索進階功能（子代理、自訂模板）
- 整合到現有的 CI/CD 管線
- 使用 Gherkin 規格與團隊協作
- 使用多階段工作流程建構複雜功能

祝您使用 GSI-Protocol 開發愉快！
