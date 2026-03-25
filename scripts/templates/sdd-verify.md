---
description: Phase 4 - 驗證實作（QA 角色）
---

# SDD Phase 4: 驗證

**輸入：** __PROMPT__ (Gherkin 檔案路徑)

**角色：** QA - 驗證實作符合 Gherkin 規格與架構設計，只報告不修改

**自動讀取：**
- `features/{feature}.feature`
- `docs/features/{feature}/architecture.md`
- 實作程式碼（依 architecture.md 定義位置）

## 執行步驟

1. 讀取三個輸入（Gherkin, architecture.md, 實作程式碼）
2. **驗證架構符合性**：資料模型、服務介面、檔案位置、命名慣例
3. **驗證情境**：對每個 Gherkin 情境執行 Given→When→Then
4. **執行單元測試**：偵測測試框架並執行所有單元測試，確認全數綠燈
5. **判斷結果**：
   - 若架構、情境、單元測試**全部通過** → 生成 `docs/features/{feature_name}/conclusion.md`
   - 若有任何**測試失敗** → 不產生 conclusion.md，直接告知開發者錯誤訊息，請修復後重新執行 sdd-verify

### 步驟 4 細節：執行單元測試

依專案現有設定找出測試指令（查看 README、Makefile、package.json scripts 等），然後執行。

執行完畢後記錄：
- 總測試數、通過數、失敗數
- 失敗的測試名稱與錯誤訊息

## 輸出規則

**若全部通過：** 生成 `docs/features/{feature_name}/conclusion.md`

```markdown
# {功能名稱} - 驗證結論

## 1. 架構符合性
| 元件 | 定義 | 實作 | 狀態 |
|---|---|---|---|
| {名稱} | architecture.md:{行} | {路徑} | ✅/❌ |

## 2. 情境驗證
### {情境名稱} (第 X 行)
- **Given:** {設定} → `{值}`
- **When:** {動作} → `{方法調用}`
- **Then:** 預期 `{值}` / 實際 `{值}` → ✅/❌

## 3. 單元測試
- 執行指令：`{command}`
- 結果：{通過數}/{總數} 通過 ✅

## 4. 摘要
- 架構：{通過}/{總數}
- 情境：{通過}/{總數}
- 單元測試：{通過}/{總數}
- **狀態：** ✅ 完成

## 5. 失敗回饋（如有）
- {元件}：預期 {X}，實際 {Y}，建議 {Z}
```

**若測試失敗：** 不產生 conclusion.md，直接輸出以下訊息給開發者：

```
❌ sdd-verify 未通過：單元測試有失敗項目

失敗測試：
- {測試名稱}：{錯誤訊息}
- ...

請修復上述測試後，重新執行 sdd-verify。
```

開始執行驗證。
