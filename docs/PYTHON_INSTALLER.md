# Python 安裝器使用指南

GSI-Protocol 現在提供了現代化的 Python 安裝工具，參考 GitHub SpecKit 的設計。

## 🚀 為什麼使用 Python 安裝器？

相比手動安裝：
- ✅ **更可靠** - 自動化流程，減少人為錯誤
- ✅ **更友善** - 彩色輸出和更好的互動體驗
- ✅ **跨平台** - Windows、macOS、Linux 都能用
- ✅ **無需安裝** - 使用 `uvx` 直接執行
- ✅ **現代化** - 符合 Python 生態系統最佳實踐

## 📦 安裝方式

### 方式 1：uvx（最推薦）

```bash
# 從 PyPI 執行（發布後）
uvx gsi-protocol-installer

# 從本地執行（開發中）
uvx --from . gsi-install

# 或直接執行 Python 檔案
uvx gsi_installer.py
```

**優點：**
- 不需要安裝到系統
- 每次都使用最新版本
- 不會污染 Python 環境

### 方式 2：pipx

```bash
# 執行（不安裝）
pipx run gsi-protocol-installer

# 或安裝後使用
pipx install gsi-protocol-installer
gsi-install
```

### 方式 3：直接執行 Python 腳本

```bash
# 下載並執行
wget https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/gsi_installer.py
python3 gsi_installer.py

# 或使用 curl
curl -O https://raw.githubusercontent.com/CodeMachine0121/GSI-Protocol/main/gsi_installer.py
python3 gsi_installer.py
```

### 方式 4：傳統 pip

```bash
pip install gsi-protocol-installer
gsi-install
```

## 🎯 使用流程

### 互動式安裝

執行安裝器後：

```
🚀 GSI-Protocol Installer
============================================================

Select AI platform(s) to install:
1) Claude Code
2) Codex (OpenAI)
3) GitHub Copilot
Enter choices (comma-separated, e.g., 1,2,3) or 'all' (default: 1,2,3): 1,3

✓ Git repository detected

Choose installation type:
1) Install to current project
2) Install globally to home directory
Enter choice [1-2] (default: 1): 2

ℹ Downloading GSI-Protocol from GitHub...
✓ Downloaded successfully
✓ Installed 6 Claude Code commands to ~/.claude/commands
✓ Installed 6 GitHub Copilot commands to ~/.copilot/commands

============================================================
✓ Installation complete! Total files installed: 12

Claude Code / Codex usage:
  /sdd-auto <requirement>
  /sdd-spec <requirement>
  /sdd-arch <feature.feature>
  /sdd-impl <feature.feature>
  /sdd-verify <feature.feature>

GitHub Copilot usage:
  @workspace /sdd-auto <requirement>
  @workspace /sdd-spec <requirement>
  @workspace /sdd-arch <feature.feature>
  @workspace /sdd-impl <feature.feature>
  @workspace /sdd-verify <feature.feature>

📖 Documentation: https://github.com/CodeMachine0121/GSI-Protocol
```

### 特色功能

1. **彩色輸出**
   - 成功：綠色 ✓
   - 錯誤：紅色 ✗
   - 警告：黃色 ⚠
   - 資訊：青色 ℹ

2. **智能偵測**
   - 自動偵測是否在 Git repository
   - 根據環境建議最佳安裝方式
   - 支援多平台選擇（可選擇安裝一個或多個平台）

3. **安全確認**
   - 覆蓋現有檔案前會詢問確認
   - 支援 Ctrl+C 隨時取消

4. **錯誤處理**
   - Git 未安裝時給予清楚提示
   - 網路問題時顯示錯誤訊息
   - 輸入驗證

## 🔧 開發者指南

### 本地測試

```bash
# 直接執行
python3 gsi_installer.py

# 使用 uvx 測試
uvx --from . gsi-install

# 建置套件
python -m build

# 檢查建置結果
ls -la dist/
```

### 發布到 PyPI

```bash
# 1. 安裝工具
pip install build twine

# 2. 建置
python -m build

# 3. 檢查
twine check dist/*

# 4. 上傳到 TestPyPI（測試）
twine upload --repository testpypi dist/*

# 5. 測試安裝
uvx --index-url https://test.pypi.org/simple/ gsi-protocol-installer

# 6. 上傳到 PyPI（正式）
twine upload dist/*
```

### 更新版本

編輯 `pyproject.toml`：

```toml
[project]
name = "gsi-protocol-installer"
version = "1.0.1"  # 更新版本號
```

## 📝 技術細節

### 專案結構

```
GSI-Protocol/
├── gsi_installer.py         # 主要安裝腳本
├── pyproject.toml            # Python 專案配置
├── INSTALLER_README.md       # 本文件
├── install.sh                # 傳統 Bash 腳本（向後相容）
└── README.md                 # 主要說明文件
```

### pyproject.toml 說明

- **專案資訊**：名稱、版本、描述、作者
- **依賴需求**：Python 3.10+
- **入口點**：`gsi-install` 命令
- **建置系統**：使用 hatchling
- **打包配置**：只包含必要檔案

### 程式碼特色

- **類型提示**：使用 Python 3.10+ 的現代類型語法
- **Path 物件**：使用 `pathlib` 而非字串操作
- **顏色輸出**：ANSI escape codes
- **錯誤處理**：完整的異常處理和使用者友善的錯誤訊息
- **可測試性**：功能模組化，易於測試

## 🤔 常見問題

### Q: uvx 是什麼？

**A:** `uvx` 是 uv 工具的一部分，用於執行 Python 應用程式而無需安裝。類似於 `npx`（Node.js）或 `pipx`。

安裝 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Q: 為什麼不使用 Bash 腳本？

**A:** Python 安裝器提供更好的體驗：
- Python 有更好的錯誤處理
- 跨平台支援更好（包含 Windows）
- 彩色輸出和互動體驗更佳
- 不會有 stdin/管道的問題

### Q: Python 安裝器和手動安裝有什麼差異？

**A:** 功能完全相同，只是方式不同：
- Python 版本自動化、有進度提示、錯誤處理完整
- 手動安裝更直接，但需要自己執行多個命令
- 兩者都會安裝相同的指令檔案

### Q: 可以離線安裝嗎？

**A:** 目前不行，安裝器需要從 GitHub 下載指令檔案。未來可能會支援離線安裝包。

### Q: 如何卸載？

**A:** 手動刪除指令目錄：
```bash
# 全域安裝
rm -rf ~/.claude/commands/sdd-*
rm -rf ~/.codex/prompts/sdd-*

# 專案安裝
rm -rf .claude/commands/sdd-*
rm -rf .codex/prompts/sdd-*
```

## 📖 相關文件

- [主要 README](../README.md)
- [安裝指南](INSTALL.md)
- [平台支援](PLATFORM_SUPPORT.md)

---

**現代化、可靠、友善的安裝體驗！** 🚀
