# GSI-Protocol 文件

GSI-Protocol（Gherkin-Structure-Implementation）工作流程的完整文件。

---

## 📚 文件索引

### 入門

| 文件 | 說明 | 時間 |
|----------|-------------|------|
| **[快速入門指南](QUICKSTART.md)** | 5 分鐘快速開始教學 | 5 分鐘 |
| **[安裝指南](INSTALL.md)** | 所有情境的詳細安裝說明 | 10 分鐘 |
| **[Python 安裝器](PYTHON_INSTALLER.md)** | 使用 uvx 的現代化安裝方式 | 3 分鐘 |
| **[平台支援](PLATFORM_SUPPORT.md)** | Claude Code、Codex、GitHub Copilot 比較 | 5 分鐘 |

### 參考

| 文件 | 說明 |
|----------|-------------|
| **[指令參考](COMMANDS.md)** | 所有指令的完整文件 |
| **[語言指南](LANGUAGE_GUIDE.md)** | 多語言支援和範例 |
| **[工作流程定義](expected_workflow.md)** | 詳細的 SDD 方法論和理念 |

### 社群

| 文件 | 說明 |
|----------|-------------|
| **[貢獻指南](../CONTRIBUTING.md)** | 如何為專案做出貢獻 |
| **[授權](../LICENSE)** | MIT 授權詳情 |

---

## 🚀 建議閱讀順序

### 首次使用者

1. **[快速入門](QUICKSTART.md)** - 了解基礎
2. **[安裝](INSTALL.md)** - 設定工具
3. 試試看：`/sdd-auto Create a calculator in Python`
4. **[指令](COMMANDS.md)** - 學習所有可用指令

### 團隊負責人

1. **[工作流程定義](expected_workflow.md)** - 理解方法論
2. **[語言指南](LANGUAGE_GUIDE.md)** - 查看語言支援
3. **[安裝](INSTALL.md)** - 選擇安裝策略
4. **[指令](COMMANDS.md)** - 規劃團隊工作流程

### 貢獻者

1. **[工作流程定義](expected_workflow.md)** - 理解核心原則
2. **[貢獻](../CONTRIBUTING.md)** - 學習貢獻流程
3. **[語言指南](LANGUAGE_GUIDE.md)** - 新增語言範例

---

## 📖 文件概覽

### 快速入門指南

**檔案**：[QUICKSTART.md](QUICKSTART.md)

5 分鐘學習 GSI-Protocol：
- 30 秒安裝
- 2 分鐘完成第一個功能
- 常見使用模式
- 成功秘訣

**最適合**：想要立即嘗試的開發者

---

### 安裝指南

**檔案**：[INSTALL.md](INSTALL.md)

完整的安裝文件：
- 全域安裝（推薦）
- 專案專用安裝
- 團隊協作設定
- 故障排除

**最適合**：了解所有安裝選項

---

### 指令參考

**檔案**：[COMMANDS.md](COMMANDS.md)

完整的指令文件：
- `/sdd-auto` - 自動工作流程
- `/sdd-spec` - 階段 1：規格
- `/sdd-arch` - 階段 2：架構
- `/sdd-impl` - 階段 3：實作
- `/sdd-verify` - 階段 4：驗證
- 使用範例
- 決策矩陣
- 最佳實踐

**最適合**：日常參考和掌握工具

---

### 語言指南

**檔案**：[LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md)

多語言支援指南：
- 特定語言模式
- Python、TypeScript、Go、Java、Rust、C# 範例
- 選擇正確語言
- 跨語言遷移
- 各語言最佳實踐

**最適合**：多語言團隊和特定語言問題

---

### 工作流程定義

**檔案**：[expected_workflow.md](expected_workflow.md)

深入探討 SDD 方法論：
- 理念和原則
- 4 階段工作流程細節
- PM、架構師、工程師、QA 角色
- BDD 和 Gherkin 用法
- 品質保證

**最適合**：理解 GSI-Protocol 背後的「為什麼」

---

## 🎯 按角色快速連結

### 產品經理
- **[工作流程定義](expected_workflow.md)** - 了解階段 1 中的 PM 角色
- **[指令](COMMANDS.md)** - `/sdd-spec` 指令詳情

### 系統架構師
- **[工作流程定義](expected_workflow.md)** - 了解階段 2 中的架構師角色
- **[語言指南](LANGUAGE_GUIDE.md)** - 各語言的結構模式
- **[指令](COMMANDS.md)** - `/sdd-arch` 指令詳情

### 軟體工程師
- **[快速入門](QUICKSTART.md)** - 快速開始
- **[指令](COMMANDS.md)** - 所有指令參考
- **[語言指南](LANGUAGE_GUIDE.md)** - 實作模式

### QA 工程師
- **[工作流程定義](expected_workflow.md)** - 了解階段 4 中的 QA 角色
- **[指令](COMMANDS.md)** - `/sdd-verify` 指令詳情

### DevOps / 團隊負責人
- **[安裝](INSTALL.md)** - 團隊設定
- **[工作流程定義](expected_workflow.md)** - 流程概覽

---

## 🔍 尋找資訊

### 按任務

**"我想安裝這個工具"**
→ [安裝指南](INSTALL.md)

**"我想選擇 AI 平台"**
→ [平台支援](PLATFORM_SUPPORT.md)

**"我想快速試用"**
→ [快速入門](QUICKSTART.md)

**"我需要了解特定指令"**
→ [指令參考](COMMANDS.md)

**"我想用於 Go/Rust 等"**
→ [語言指南](LANGUAGE_GUIDE.md)

**"我想了解方法論"**
→ [工作流程定義](expected_workflow.md)

**"我想做出貢獻"**
→ [貢獻指南](../CONTRIBUTING.md)

---

### 按問題

**"如何安裝？"**
→ [安裝指南](INSTALL.md)

**"應該選 Claude Code、Codex 還是 GitHub Copilot？"**
→ [平台支援](PLATFORM_SUPPORT.md)

**"有哪些可用指令？"**
→ [指令參考](COMMANDS.md)

**"支援 TypeScript/Go 等嗎？"**
→ [語言指南](LANGUAGE_GUIDE.md)

**"何時使用 /sdd-auto vs 手動階段？"**
→ [指令參考](COMMANDS.md) - 決策矩陣

**"4 階段工作流程如何運作？"**
→ [工作流程定義](expected_workflow.md)

**"我可以在團隊中使用嗎？"**
→ [安裝指南](INSTALL.md) - 團隊設定

---

## 📞 仍有問題？

- 💬 [GitHub Issues](https://github.com/CodeMachine0121/GSI-Protocol/issues)
- 💡 [GitHub Discussions](https://github.com/CodeMachine0121/GSI-Protocol/discussions)
- 📖 [主要 README](../README.md)

---

## 🔄 文件更新

本文件持續改進中。如果您發現：
- ❌ 錯誤或拼寫錯誤
- 📝 缺失資訊
- 💡 改進建議

請：
1. 開啟問題
2. 提交 pull request
3. 開始討論

詳見 [貢獻指南](../CONTRIBUTING.md)。

---

**[⬆ 回到主要 README](../README.md)**
