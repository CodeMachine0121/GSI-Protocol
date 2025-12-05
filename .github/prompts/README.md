# GSI-Protocol for GitHub Copilot

本目錄包含 GitHub Copilot CLI 的 SDD (Specification-Driven Development) 工作流程 prompts。

## 目錄結構

```
.github/prompts/
├── README.md                           # 本檔案
├── sdd-auto.prompts.md                 # 自動工作流程
├── sdd-spec.prompts.md                 # Phase 1: 規格
├── sdd-arch.prompts.md                 # Phase 2: 架構
├── sdd-integration-test.prompts.md     # Phase 2.5: 整合測試（選用）
├── sdd-impl.prompts.md                 # Phase 3: 實作
└── sdd-verify.prompts.md               # Phase 4: 驗證
```

## 安裝

### 全域安裝（推薦）

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

### 專案安裝

將 `.github/prompts/` 目錄複製到您的專案根目錄。

## 使用方式

GitHub Copilot 使用 `@workspace /command` 格式：

### 自動模式
```bash
@workspace /sdd-auto Create a shopping cart in TypeScript with add, remove, checkout functions
```

### 手動模式（逐步執行）
```bash
# Phase 1: 生成 Gherkin 規格
@workspace /sdd-spec Create a shopping cart with add, remove, checkout

# Phase 2: 設計架構
@workspace /sdd-arch features/shopping_cart.feature

# Phase 2.5: 生成整合測試（選用）
@workspace /sdd-integration-test features/shopping_cart.feature

# Phase 3: 實作程式碼
@workspace /sdd-impl features/shopping_cart.feature

# Phase 4: 驗證實作
@workspace /sdd-verify features/shopping_cart.feature
```

## 可用指令

| 指令 | 說明 | 使用範例 |
|------|------|----------|
| `/sdd-auto` | 自動執行完整 4 階段 | `@workspace /sdd-auto <需求>` |
| `/sdd-spec` | Phase 1: 生成 Gherkin 規格 | `@workspace /sdd-spec <需求>` |
| `/sdd-arch` | Phase 2: 設計架構 | `@workspace /sdd-arch <feature.feature>` |
| `/sdd-integration-test` | Phase 2.5: 整合測試（選用） | `@workspace /sdd-integration-test <feature.feature>` |
| `/sdd-impl` | Phase 3: 實作程式碼 | `@workspace /sdd-impl <feature.feature>` |
| `/sdd-verify` | Phase 4: 驗證實作 | `@workspace /sdd-verify <feature.feature>` |

## 工作流程

```
Phase 1: 規格（PM）
    ↓
    features/{feature}.feature
    ↓
Phase 2: 架構（架構師）
    ↓
    docs/features/{feature}/architecture.md
    ↓
Phase 2.5: 整合測試（選用）
    ↓
    tests/integration/{feature}.test.{ext}
    ↓
Phase 3: 實作（工程師）
    ↓
    實作檔案（依 architecture.md）
    ↓
Phase 4: 驗證（QA）
    ↓
    docs/features/{feature}/conclusion.md
```

## 支援語言

- TypeScript / JavaScript
- Python
- Go
- Java
- Rust
- C#
- 更多...

## 命名規範

GitHub Copilot 的 prompt 檔案使用 `.prompts.md` 副檔名：
- ✅ `sdd-auto.prompts.md`
- ✅ `sdd-spec.prompts.md`
- ❌ `sdd-auto.md` （不正確）

## 詳細文檔

完整說明請參閱：https://github.com/CodeMachine0121/GSI-Protocol

## 平台比較

| 平台 | 檔案位置 | 檔案命名 |
|------|---------|---------|
| Claude Code | `~/.claude/commands/` | `sdd-*.md` |
| Codex (OpenAI) | `~/.codex/prompts/` | `sdd-*.md` |
| GitHub Copilot | `~/.github/prompts/` | `sdd-*.prompts.md` |
