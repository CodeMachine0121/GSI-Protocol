# GSI-Protocol 開發工作流程

**中文版本** | [English](./README.md)

## 問題
修改 GSI command 內容時，需要同時維護三個位置：
- `.claude/commands/` (Claude Code)
- `.codex/prompts/` (Codex)
- `.github/prompts/` (GitHub Copilot)

## 解決方案
使用單一來源 + 自動同步腳本

## 目錄結構
```
scripts/
  ├── templates/        # 📝 唯一需要維護的模板來源
  │   ├── sdd-spec.md
  │   ├── sdd-arch.md
  │   ├── sdd-impl.md
  │   ├── sdd-verify.md
  │   ├── sdd-integration-test.md
  │   └── sdd-auto.md
  ├── dev_sync.py       # 🔧 本地開發測試工具（開發者專用）
  └── README.md         # 📖 本文件
```

## 開發工作流程

### 1. 修改模板
只需要修改 `scripts/templates/` 中的檔案，使用通用佔位符：

```markdown
## 使用者需求

__PROMPT__

## 下一步
- 使用指令：`__CMD_PREFIX__sdd-arch features/xxx.feature`
```

**佔位符說明：**
- `__PROMPT__` - 用戶輸入的參數
- `__CMD_PREFIX__` - 命令前綴（會根據平台自動轉換）

### 2. 同步到三個平台
運行開發同步工具：

```bash
python3 scripts/dev_sync.py
```

⚠️ **注意**：此工具僅供開發測試，終端用戶不需要使用

這會自動轉換佔位符並同步：
- 轉換並同步到 `.claude/commands/`：`__PROMPT__` → `{{prompt}}`，`__CMD_PREFIX__` → `/`
- 轉換並同步到 `.codex/prompts/`：`__PROMPT__` → `$1`，`__CMD_PREFIX__` → `/`
- 轉換並同步到 `.github/prompts/`：`__PROMPT__` → `{{ARG}}`，`__CMD_PREFIX__` → `@workspace /`

### 3. 測試
在本地測試各平台的命令是否正常運作

### 4. 提交
提交所有變更到 Git

## 用戶安裝流程

當用戶執行：
```bash
uvx --from gsi-protocol-installer gsi-install
```

`gsi_installer.py` 會：
1. 從 GitHub 下載 repo
2. 讀取 `scripts/templates/` 中的模板
3. 根據用戶選擇的平台自動轉換並安裝

## 佔位符轉換對照表

| 平台 | `__PROMPT__` 轉換為 | `__CMD_PREFIX__` 轉換為 | 檔案副檔名 |
|------|-------------------|----------------------|-----------|
| 模板 | `__PROMPT__` | `__CMD_PREFIX__` | `.md` |
| Claude Code | `{{prompt}}` | `/` | `.md` |
| Codex | `$1` | `/` | `.md` |
| GitHub Copilot | `{{ARG}}` | `@workspace /` | `.prompt.md` |

## 優點

✅ 只需維護一個地方 (`scripts/templates/`)
✅ 自動處理平台差異
✅ 降低維護成本
✅ 減少人為錯誤
