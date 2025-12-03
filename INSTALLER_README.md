# GSI-Protocol Installer

快速安裝 GSI-Protocol 工作流程指令到 Claude Code 或 Codex。

## 安裝方式

### 方式 1：使用 uvx（推薦）

```bash
# 直接執行（不需要安裝）
uvx gsi-protocol-installer

# 或從本地
uvx --from . gsi-install
```

### 方式 2：使用 pipx

```bash
# 直接執行
pipx run gsi-protocol-installer

# 或安裝後使用
pipx install gsi-protocol-installer
gsi-install
```

### 方式 3：使用 pip

```bash
pip install gsi-protocol-installer
gsi-install
```

## 功能

- ✅ 互動式安裝流程
- ✅ 支援 Claude Code 和 Codex
- ✅ 自動偵測專案類型
- ✅ 全域或專案安裝
- ✅ 彩色終端輸出
- ✅ 錯誤處理

## 使用說明

執行安裝程式後，會詢問：

1. **選擇 AI 平台**
   - Claude Code only
   - Codex (OpenAI) only
   - Both

2. **選擇安裝位置**
   - 當前專案（如果在 Git repo 中）
   - 全域（`~/.claude/commands` 或 `~/.codex/commands`）

3. 自動下載並安裝指令檔案

## 需求

- Python 3.10+
- Git（用於下載指令檔案）

## License

MIT
