# 平台支援指南

GSI-Protocol 現在支援多個 AI 平台，讓您可以使用您偏好的 AI 工具來執行規格驅動開發工作流程。

---

## 🤖 支援的平台

### Claude Code
- **開發商：** Anthropic
- **特色：** 強大的程式碼理解與生成能力
- **指令格式：** `/sdd-*`
- **指令目錄：** `~/.claude/commands/` (全域) 或 `.claude/commands/` (專案)
- **狀態：** ✅ 完整支援

### Codex (OpenAI)
- **開發商：** OpenAI
- **特色：** 基於 GPT 技術的程式碼生成
- **指令格式：** `/sdd-*`
- **指令目錄：** `~/.codex/prompts/` (全域) 或 `.codex/prompts/` (專案)
- **狀態：** ✅ 完整支援

### GitHub Copilot
- **開發商：** GitHub (Microsoft)
- **特色：** 整合 VS Code 與 CLI 的 AI 程式輔助
- **指令格式：** `@workspace /sdd-*`
- **指令目錄：** `~/.github/prompts/` (全域) 或 `.github/prompts/` (專案)
- **狀態：** ✅ 完整支援

---

## 📊 平台比較

| 特性 | Claude Code | Codex (OpenAI) | GitHub Copilot |
|------|------------|----------------|----------------|
| SDD 工作流程 | ✅ | ✅ | ✅ |
| Gherkin 規格生成 | ✅ | ✅ | ✅ |
| 架構設計 | ✅ | ✅ | ✅ |
| 程式碼實作 | ✅ | ✅ | ✅ |
| 驗證測試 | ✅ | ✅ | ✅ |
| 多語言支援 | ✅ | ✅ | ✅ |
| 框架無關 | ✅ | ✅ | ✅ |
| 專案感知 | ✅ | ✅ | ✅ |
| 指令格式 | `/sdd-*` | `/sdd-*` | `@workspace /sdd-*` |
| VS Code 整合 | - | - | ✅ |

**結論：** 三個平台在 GSI-Protocol 工作流程中功能完全相同，選擇您偏好的平台即可。

---

## 🚀 快速開始

### 選擇您的平台

**只用一個平台：**
```bash
# 安裝時選擇您要使用的平台
uvx gsi-protocol-installer
# 選擇選項 1 (Claude Code)、2 (Codex) 或 3 (GitHub Copilot)
```

**同時使用多個平台：**
```bash
# 安裝時可以選擇多個平台（用逗號分隔）
uvx gsi-protocol-installer
# 輸入 1,2,3 或 all 來安裝所有平台
# 可以在不同專案中使用不同的 AI 工具
```

---

## 💡 使用建議

### 何時使用 Claude Code
- 需要深度程式碼理解
- 複雜的架構設計
- 重構現有程式碼

### 何時使用 Codex
- 快速原型開發
- 標準化程式碼生成
- OpenAI 生態系整合

### 何時使用 GitHub Copilot
- VS Code 開發環境
- CLI 工作流程整合
- 需要 GitHub 生態系整合

### 混合使用
您可以在同一專案中混合使用：
- Phase 1-2 用 Claude Code（規格與架構）
- Phase 3-4 用 Copilot（實作與驗證）
- 或任意組合

---

## 🔄 切換平台

### 已安裝 Claude Code，想加入 Codex

```bash
# 全域安裝
mkdir -p ~/.codex/prompts
cd ~/.codex/prompts
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-auto.md -o sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-spec.md -o sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-arch.md -o sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-integration-test.md -o sdd-integration-test.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-impl.md -o sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.codex/prompts/sdd-verify.md -o sdd-verify.md
```

### 想加入 GitHub Copilot

```bash
# 全域安裝
mkdir -p ~/.github/prompts
cd ~/.github/prompts
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-auto.prompts.md -o sdd-auto.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-spec.prompts.md -o sdd-spec.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-arch.prompts.md -o sdd-arch.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-integration-test.prompts.md -o sdd-integration-test.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-impl.prompts.md -o sdd-impl.prompts.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.github/prompts/sdd-verify.prompts.md -o sdd-verify.prompts.md
```

### 已安裝 Codex，想加入 Claude Code

```bash
# 全域安裝
mkdir -p ~/.claude/commands
cd ~/.claude/commands
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-auto.md -o sdd-auto.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-spec.md -o sdd-spec.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-arch.md -o sdd-arch.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-integration-test.md -o sdd-integration-test.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-impl.md -o sdd-impl.md
curl -sSL https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/.claude/commands/sdd-verify.md -o sdd-verify.md
```

---

## 📁 目錄結構

### 全域安裝（推薦）

```
~/.claude/commands/        # Claude Code 全域指令
├── sdd-auto.md
├── sdd-spec.md
├── sdd-arch.md
├── sdd-integration-test.md
├── sdd-impl.md
└── sdd-verify.md

~/.codex/prompts/          # Codex 全域 prompts
├── sdd-auto.md
├── sdd-spec.md
├── sdd-arch.md
├── sdd-integration-test.md
├── sdd-impl.md
└── sdd-verify.md

~/.github/prompts/       # GitHub Copilot 全域 prompts
├── sdd-auto.prompts.md
├── sdd-spec.prompts.md
├── sdd-arch.prompts.md
├── sdd-integration-test.prompts.md
├── sdd-impl.prompts.md
└── sdd-verify.prompts.md

# 專案保持乾淨
your-project/
├── features/              # 生成的規格
├── docs/features/         # 生成的架構與驗證
└── src/                   # 生成的程式碼
```

### 專案內安裝

```
your-project/
├── .claude/commands/      # Claude Code 專案指令（可選）
├── .codex/prompts/        # Codex 專案 prompts（可選）
├── .github/prompts/       # GitHub Copilot 專案 prompts（可選）
├── features/
├── docs/features/
└── src/
```

---

## ❓ 常見問題

### Q: 指令內容有差異嗎？

**A:** 有些許差異。三個平台的**工作流程和輸出格式完全相同**，但指令格式略有不同：

- **Claude Code**: 使用 `{{prompt}}` 變數，指令前綴為 `/sdd-*`
- **Codex**: 使用 `{{prompt}}` 變數，指令前綴為 `/sdd-*`
- **GitHub Copilot**: 使用 `{{ARG}}` 變數，指令前綴為 `@workspace /sdd-*`

這些差異是為了符合各平台的技術規範，但不影響實際使用體驗。

### Q: 可以同時安裝多個平台嗎？

**A:** 可以！您可以同時安裝所有三個平台，然後根據需求選擇使用哪個 AI 工具。

### Q: 哪個平台比較好？

**A:** 三者都很優秀，取決於您的偏好和使用情境：
- 如果您已經在使用 Claude Code → 繼續使用
- 如果您偏好 OpenAI 生態系 → 使用 Codex
- 如果您喜歡 VS Code 與 CLI 整合 → 使用 GitHub Copilot
- 不確定 → 同時安裝，實際使用後再決定

### Q: 生成的檔案格式相容嗎？

**A:** 完全相容！兩個平台生成的檔案（`.feature`, `architecture.md`, `conclusion.md`, 程式碼）格式完全相同，可以互換使用。

### Q: 團隊成員可以用不同平台嗎？

**A:** 可以！因為工作流程和輸出格式都相同，團隊成員可以各自選擇偏好的 AI 工具，不會影響協作。

---

## 🎯 最佳實踐

1. **選擇主要平台**：根據團隊偏好選擇一個主要使用的平台
2. **保持一致性**：在同一專案中盡量使用同一平台（避免混淆）
3. **全域安裝**：優先使用全域安裝，保持專案目錄乾淨
4. **文檔說明**：在專案 README 中說明建議使用哪個平台

---

## 📚 相關文檔

- [安裝指南](INSTALL.md) - 詳細安裝說明
- [快速入門](QUICKSTART.md) - 5 分鐘教學
- [指令參考](COMMANDS.md) - 完整指令文件

---

**支援多平台，選擇更自由！** 🎉
