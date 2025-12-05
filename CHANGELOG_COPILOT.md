# GitHub Copilot Support - Changelog

## [New] 2024-12-05

### Added
- ✨ **GitHub Copilot 完整支援**
  - 新增 `.copilot/commands/` 目錄，包含所有 6 個 SDD 工作流程指令
  - 新增 `.copilot/README.md` 使用說明文檔
  - 新增 Copilot 專屬安裝路徑 (`~/.copilot/commands/`)

### Changed
- 🔧 **安裝器升級** (`gsi_installer.py`)
  - 新增 `prompt_multi_choice()` 函數，支援多平台選擇
  - 更新 `install_commands()` 支援 Copilot 平台
  - 改善使用者介面，顯示平台專屬的使用說明
  
- 📖 **文檔更新** (`README.md`)
  - 支援平台清單新增 GitHub Copilot
  - 新增 Copilot 手動安裝指令
  - 更新快速開始範例（包含 `@workspace` 語法）
  - 更新專案結構說明
  - 更新致謝章節

### Technical Details

**指令格式適配：**
- 參數語法：`{{prompt}}` → `{{ARG}}`
- 指令前綴：`/sdd-*` → `@workspace /sdd-*`

**檔案清單：**
```
.copilot/
├── README.md
├── commands/
│   ├── sdd-auto.md             (161 行)
│   ├── sdd-spec.md             (123 行)
│   ├── sdd-arch.md             (139 行)
│   ├── sdd-integration-test.md (123 行)
│   ├── sdd-impl.md             (210 行)
│   └── sdd-verify.md           (50 行)
└── settings.local.json
```

**測試狀態：**
- ✅ Python 語法驗證通過
- ✅ 檔案結構驗證通過
- ✅ 格式轉換驗證通過
- ⏳ 待測試：實際 Copilot CLI 安裝測試
- ⏳ 待測試：端對端工作流程測試

### Usage

**安裝：**
```bash
uvx --from gsi-protocol-installer gsi-install
# 選擇平台 3) GitHub Copilot
```

**使用：**
```bash
# 自動模式
@workspace /sdd-auto Create a user authentication system

# 手動模式
@workspace /sdd-spec Create a user authentication system
@workspace /sdd-arch features/user_auth.feature
@workspace /sdd-impl features/user_auth.feature
@workspace /sdd-verify features/user_auth.feature
```

### Compatibility

| Platform | Status | Command Format | Config Path |
|----------|--------|----------------|-------------|
| Claude Code | ✅ Supported | `/sdd-*` | `~/.claude/commands/` |
| Codex (OpenAI) | ✅ Supported | `/sdd-*` | `~/.codex/prompts/` |
| GitHub Copilot | ✅ **NEW** | `@workspace /sdd-*` | `~/.copilot/commands/` |

---

**維護者備註：**
所有現有功能保持不變，新增 Copilot 支援為附加功能，不影響現有 Claude Code 和 Codex 使用者。
