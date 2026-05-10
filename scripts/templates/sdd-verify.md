---
description: Phase 4 - 驗證實作（QA 角色）
---

# SDD Phase 4: 驗證

**輸入：** __PROMPT__ (Gherkin 檔案路徑)

**角色：** QA - 執行 contract tests 與 unit tests，確認全數通過，只報告不修改

**自動讀取：**
- `features/{feature}.feature`
- `docs/features/{feature}/architecture.md`
- Contract test 檔案（`{FeatureName}ContractTests.{ext}`）

## 執行步驟

1. **找出測試指令**：查看 README、Makefile、package.json scripts 等，確認執行方式
2. **執行 Contract Tests**：執行 contract test 檔案，記錄每個 S-{scenario}-{assertion} 的結果
3. **執行 Unit Tests**：執行所有 unit tests，記錄結果
4. **驗證架構符合性**：比對 architecture.md 定義的資料模型、服務介面、檔案位置與實作
5. **判斷結果**：
   - 全部通過 → 生成 `docs/features/{feature_name}/conclusion.md`
   - 任何失敗 → 不產生 conclusion.md，直接告知錯誤，請修復後重新執行

## 輸出規則

**若全部通過：** 生成 `docs/features/{feature_name}/conclusion.md`

```markdown
# {功能名稱} - 驗證結論

## 1. 架構符合性
| 元件 | 定義 | 實作 | 狀態 |
|---|---|---|---|
| {名稱} | architecture.md:{行} | {路徑} | ✅/❌ |

## 2. Contract Tests
| 編號 | 情境 | 狀態 |
|---|---|---|
| S-1-1 | {情境名稱} - {assertion} | ✅/❌ |

- 執行指令：`{command}`
- 結果：{通過數}/{總數} 通過

## 3. Unit Tests
- 執行指令：`{command}`
- 結果：{通過數}/{總數} 通過

## 4. 摘要
- 架構符合性：{通過}/{總數}
- Contract Tests：{通過}/{總數}
- Unit Tests：{通過}/{總數}
- **狀態：** ✅ 完成

## 5. 失敗回饋（如有）
- {元件/測試}：預期 {X}，實際 {Y}，建議 {Z}
```

**若測試失敗：** 不產生 conclusion.md，直接輸出：

```
❌ sdd-verify 未通過

失敗項目：
- {測試名稱}：{錯誤訊息}
- ...

請修復後重新執行 sdd-verify。
```

開始執行驗證。
