# GSI-Protocol

> 基於規格驅動開發（SDD）的 AI 輔助開發工作流程

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-1.0.14-green)](https://github.com/CodeMachine0121/GSI-Protocol)

**語言**: [English](./README.md) | **繁體中文**

GSI-Protocol 是一個自動化的規格驅動開發（SDD）工作流程系統，透過結構化的 4 階段流程將使用者需求轉換為可投產的程式碼：規格 → 架構 → 實作 → 驗證。

## 特色

- **多平台支援**：支援 Claude Code、Codex (OpenAI) 和 GitHub Copilot
- **語言無關**：架構設計獨立於程式語言
- **自動化工作流程**：單一命令執行完整開發週期
- **BDD 整合**：內建支援 Gherkin 規格與整合測試
- **專案感知**：自動偵測並適應您專案的技術棧
- **角色導向階段**：PM → 架構師 → 工程師 → QA 工作流程

## 📚 深入了解

**初次使用 GSI-Protocol？** 從這裡開始：

- **[GSI 理論與方法論](./docs/gsi-theory.zh-TW.md)** - 深入理解 **G**herkin-**S**tructure-**I**mplement 方法論
- **[快速開始指南](./docs/quickstart.zh-TW.md)** - 逐步教學建立您的第一個功能

## 快速開始

### 安裝

使用 `uvx` 安裝（推薦）：

```bash
uvx --from gsi-protocol-installer gsi-install
```

或使用 `pipx`：

```bash
pipx run gsi-protocol-installer
```

安裝程式將引導您完成：
1. 選擇 AI 平台（Claude Code、Codex、GitHub Copilot）
2. 選擇安裝類型（全域或專案特定）
3. 安裝工作流程指令

### 基本使用

#### 自動模式（推薦）

自動執行完整的 4 階段工作流程：

```bash
# Claude Code / Codex
/sdd-auto <您的需求>

# GitHub Copilot
@workspace /sdd-auto <您的需求>
```

範例：
```bash
/sdd-auto 新增使用者認證功能，包含電子郵件和密碼登入
```

#### 手動模式

更精細地控制每個階段：

1. **生成規格**（PM 階段）
   ```bash
   /sdd-spec <需求>
   ```

2. **設計架構**（架構師階段）
   ```bash
   /sdd-arch <feature_file_path>
   ```

3. **實作程式碼**（工程師階段）
   ```bash
   /sdd-impl <feature_file_path>
   ```

4. **驗證實作**（QA 階段）
   ```bash
   /sdd-verify <feature_file_path>
   ```

5. **生成整合測試**（選用）
   ```bash
   /sdd-integration-test <feature_file_path>
   ```

## 工作流程概覽

GSI-Protocol 遵循結構化的 4 階段流程：

```
使用者需求
      ↓
[階段 1: 規格（PM）]
   → features/{feature}.feature (Gherkin)
      ↓
[階段 2: 架構（架構師）]
   → docs/features/{feature}/architecture.md
      ↓
[階段 3: 實作（工程師）]
   → 原始碼檔案
      ↓
[階段 4: 驗證（QA）]
   → docs/features/{feature}/conclusion.md
```

> **了解方法論**：閱讀我們的 [GSI 理論與方法論指南](./docs/gsi-theory.zh-TW.md) 來理解 **Gherkin**（規格）、**Structure**（架構）和 **Implement**（實作）如何協同運作。

## 可用指令

| 指令 | 說明 | 階段 |
|---------|-------------|-------|
| `/sdd-auto` | 自動執行完整工作流程 | 全部 |
| `/sdd-spec` | 從需求生成 Gherkin 規格 | 1 |
| `/sdd-arch` | 從規格設計架構 | 2 |
| `/sdd-impl` | 基於架構實作程式碼 | 3 |
| `/sdd-verify` | 驗證實作是否符合規格 | 4 |
| `/sdd-integration-test` | 生成 BDD 整合測試 | 選用 |

## 輸出結構

執行工作流程後，您的專案將包含：

```
project_root/
├── features/
│   └── {feature_name}.feature          # Gherkin 規格
├── docs/
│   └── features/
│       └── {feature_name}/
│           ├── architecture.md         # 架構設計
│           └── conclusion.md           # 驗證報告
└── {your_project_structure}/
    ├── {model_files}                   # 生成的模型
    └── {service_files}                 # 生成的服務
```

## 平台特定用法

### Claude Code

指令可直接在 Claude Code CLI 中使用：
```bash
/sdd-auto <需求>
/sdd-spec <需求>
```

### Codex (OpenAI)

使用帶有參數佔位符的提示：
```bash
/sdd-auto <需求>
```

### GitHub Copilot

在指令前加上 `@workspace`：
```bash
@workspace /sdd-auto <需求>
@workspace /sdd-spec <需求>
```

## 系統需求

- Python 3.10 或更高版本
- Git
- 以下其中一個支援的 AI 平台：
  - Claude Code CLI
  - Codex (OpenAI)
  - GitHub Copilot

## 文件

詳細文件請參閱 [docs](./docs) 目錄：
- [GSI 理論與方法論](./docs/gsi-theory.zh-TW.md) - 理解 G-S-I 三大支柱
- [快速開始指南](./docs/quickstart.zh-TW.md) - 數分鐘內開始使用

## 貢獻

歡迎貢獻！請隨時提交問題和拉取請求。

## 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

## 作者

**James Hsueh** - [asdfg55887@gmail.com](mailto:asdfg55887@gmail.com)

## 連結

- [首頁](https://github.com/CodeMachine0121/GSI-Protocol)
- [問題追蹤](https://github.com/CodeMachine0121/GSI-Protocol/issues)
- [程式碼庫](https://github.com/CodeMachine0121/GSI-Protocol)

## 更新日誌

版本歷史和更新請參閱專案儲存庫。
