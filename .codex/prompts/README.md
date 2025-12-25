# SDD 指令模板管理

## 目錄結構

```
scripts/templates/          # 📝 主要模板源（唯一編輯處）
├── sdd-spec.md
├── sdd-arch.md
├── sdd-impl.md
├── sdd-integration-test.md
├── sdd-verify.md
└── sdd-auto.md

.claude/commands/           # ⚙️ Claude Code CLI 格式（自動生成）
.codex/prompts/             # ⚙️ Codex 格式（自動生成）
.github/prompts/            # ⚙️ GitHub Prompts 格式（自動生成）
```

## 使用方式

### 📝 編輯指令

**只需編輯這裡：** `scripts/templates/*.md`

使用占位符 `$1` 表示參數位置。

### 🔄 同步機制

**方式一：本地開發同步**

```bash
node scripts/sync-commands.js
# 或
npm run sync:commands
```

這會將模板同步到本地的：
- `.claude/commands/` → 使用 `$1`
- `.codex/prompts/` → 使用 `$1` + `argument-hint`
- `.github/prompts/` → 使用 `{{ARG}}` + `@workspace /` 前綴

**方式二：安裝器動態轉換**

`gsi_installer.py` 會在安裝時自動從模板轉換：
- 從 `scripts/templates/` 讀取源模板
- 根據選擇的平台動態轉換格式
- 直接安裝到目標目錄

這意味著 **不需要提交已生成的文件**，只需提交模板即可！

### 🎯 工作流程

**本地開發：**
1. 編輯 `scripts/templates/` 中的模板文件
2. 運行 `npm run sync:commands`（僅用於本地測試）
3. 測試指令
4. 只提交 `scripts/templates/` 的變更

**用戶安裝：**
1. `gsi_installer.py` 從 GitHub 克隆儲存庫
2. 讀取 `scripts/templates/` 中的模板
3. 動態轉換為目標平台格式
4. 安裝到用戶的目錄

## 格式轉換規則

| 工具 | 參數語法 | 命令前綴 | 文件擴展名 |
|------|---------|---------|-----------|
| Claude Code | `$1` | `/` | `.md` |
| Codex | `$1` + frontmatter hint | - | `.md` |
| GitHub Prompts | `{{ARG}}` | `@workspace /` | `.prompt.md` |

## 範例

### 模板源 (scripts/templates/sdd-spec.md)
```markdown
---
description: 階段 1 - 從使用者需求生成 Gherkin 行為規格（PM 角色）
---

## 使用者需求

$1
```

### 生成結果

**Claude Code** (`.claude/commands/sdd-spec.md`):
```markdown
$1
```

**Codex** (`.codex/prompts/sdd-spec.md`):
```markdown
---
description: ...
---

$1
```

**GitHub** (`.github/prompts/sdd-spec.prompt.md`):
```markdown
{{ARG}}

使用 `@workspace /sdd-spec` 呼叫
```

## 注意事項

- ⚠️ **不要直接編輯** `.claude/`, `.codex/`, `.github/` 中的文件
- ✅ **只編輯** `scripts/templates/` 中的源模板
- 🔄 本地測試時運行 `npm run sync:commands`
- 📦 **提交時只需提交** `scripts/templates/` 的變更
- 🚀 已生成的文件（`.claude/`, `.codex/`, `.github/`）可選擇性提交，或加入 `.gitignore`
