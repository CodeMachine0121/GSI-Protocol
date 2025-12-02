---
description: Phase 4 - 驗證實作（QA 角色）
---

# SDD Phase 4: 驗證

**輸入：** {{prompt}} (Gherkin 檔案路徑)

**角色：** QA - 驗證實作符合 Gherkin 規格與架構設計，只報告不修改

**自動讀取：**
- `features/{feature}.feature`
- `docs/features/{feature}/architecture.md`
- 實作程式碼（依 architecture.md 定義位置）

## 執行步驟

1. 讀取三個輸入（Gherkin, architecture.md, 實作程式碼）
2. **驗證架構符合性**：資料模型、服務介面、檔案位置、命名慣例
3. **驗證情境**：對每個 Gherkin 情境執行 Given→When→Then
4. 生成結論報告至 `docs/features/{feature_name}/conclusion.md`

## 報告格式

**唯一輸出：** `docs/features/{feature_name}/conclusion.md`

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

## 3. 摘要
- 架構：{通過}/{總數}
- 情境：{通過}/{總數}  
- **狀態：** ✅ 完成 / ❌ 需修正

## 4. 失敗回饋（如有）
- {元件}：預期 {X}，實際 {Y}，建議 {Z}
```

開始執行驗證。
