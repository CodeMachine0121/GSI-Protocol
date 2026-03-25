---
description: 從 feature file 篩選適合單元測試的業務情境，建立測試方法框架
---

# SDD-TEST: 單元測試框架生成器

**輸入：** **PROMPT** (格式：`<feature_file_path>`)

**目標：**

1. 讀取 feature file 和對應的 architecture.md
2. 從所有 Scenario 中篩選出**適合撰寫單元測試防護**的業務情境
3. 為篩選出的情境建立測試方法框架（只開好 test case method，內容為空或 TODO 註解）

## 核心原則

### 1. 篩選適合單元測試的業務情境

- **單元測試適用**：純邏輯運算、資料轉換、商業規則、邊界條件、錯誤處理、有外部依賴但可透過介面 mock 的業務邏輯
- **單元測試不適用**：端對端流程、複雜的跨服務協作流程

### 2. 只測行為，不測狀態

- 驗證方法呼叫、回傳值、拋出的異常
- 不直接檢查物件內部狀態或私有欄位

### 3. 測試撰寫風格

- **Fluent 風格**：test code 盡量以 method chaining 方式撰寫
- **3A 結構**：每個 test case 以空行清楚區隔 Arrange / Act / Assert 三段，並加上對應的行內註解
- **單一 Assertion**：每個 test case 只做一個 Assertion
- **Given... 方法**：mock 回傳值的設定必須抽出為 private method，命名以 `given` 開頭，命名格式 `given<描述情境>()`
- **Create... 方法**：受測物件（SUT）以外的物件建立必須抽出為 private method，命名以 `create` 開頭，命名格式 `create<物件描述>()`
- **重用**：同一測試類別中，相同的 Given / Create 方法不重複定義，盡量共用

### 4. 測試方法框架要求

- 只建立 test case method 框架，內容為空或只有 TODO 註解
- 預留 Given / Create private method 框架（含 TODO），讓開發者填充
- 方法命名清楚反映測試情境

## 執行步驟

### 1. 讀取輸入檔案

```bash
cat <feature_file_path>
cat docs/features/<feature_name>/architecture.md
```

### 2. 掃描專案與框架偵測

```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -name "*test*" -o -name "*spec*" | head -5
```

**框架優先順序：** architecture.md 指定 > 專案既有 > 預設

### 3. 篩選業務情境並建立框架

對每個 Scenario 判斷是否適合單元測試，並為適合的情境建立：

- 篩選分析報告（已篩選 / 未篩選的 Scenarios 及原因）
- Import 語句、測試類別宣告、Mock 物件宣告
- test case method 框架（內容空白或 TODO）
- Given / Create private method 框架（含 TODO）

未篩選的 Scenario 記錄在報告中，不建立測試框架，並說明建議改用整合測試。

## 測試檔案輸出

依專案既有測試框架與目錄結構決定輸出位置

## 品質檢查

- [ ] 已掃描所有 Scenarios 並完成篩選
- [ ] 只為適合單元測試的 Scenario 建立測試方法框架
- [ ] 包含篩選分析報告（已篩選 vs 未篩選的 Scenarios 及原因）
- [ ] 每個 test case 只有一個 Assertion
- [ ] 3A 結構清晰，以空行區隔並加上對應行內註解
- [ ] test code 採用 fluent / method chaining 風格
- [ ] Mock 設定已抽出為 `Given...` private method 框架
- [ ] 測試物件建立已抽出為 `Create...` private method 框架
- [ ] 相同的 Given / Create 方法有被重用，無重複定義
- [ ] 測試檔案可編譯（無語法錯誤）

開始讀取檔案、篩選業務情境並建立測試方法框架。
