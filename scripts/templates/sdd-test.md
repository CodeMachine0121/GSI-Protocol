---
description: 從 feature file 篩選適合單元測試的業務情境，建立測試方法框架
---

# SDD-TEST: Contract Test 生成器

**角色：** QA 工程師  
**輸入：** **PROMPT** (格式：`<feature_file_path>`)  
**自動讀取：** `docs/features/{feature_name}/architecture.md`  
**輸出：** Contract Test 檔案（所有 Scenario 填充具體數值，可直接執行）

## 核心原則

### 1. 所有 Scenario 皆轉為 Contract Test

不做篩選。每個 Scenario = 一組 contract tests，一個 Then = 一個 test case。  
Contract tests 驗證**行為**（Gherkin 定義的 Given/When/Then），不測試內部實作。

### 2. 數值直接來自 Gherkin

- `Given` → Arrange 的具體輸入值
- `When` → Act 的服務方法呼叫（依 architecture.md 的介面定義）
- `Then` → Assert 的具體預期值

所有數值皆填充完畢，**無任何 TODO**，可直接執行。

### 3. 測試撰寫風格

- **S-{scenario}-{assertion} 編號**：每個 test case 方法上方標注（如 `S-1-1`、`S-1-2`）
- **3A 結構**：Arrange / Act / Assert 以空行區隔並加上行內註解
- **單一 Assertion**：每個 test case 只有一個 Assert
- **Fluent 風格**：method chaining

## 執行步驟

### 1. 讀取輸入

```bash
cat <feature_file_path>
cat docs/features/<feature_name>/architecture.md
```

確認：
- 所有 Scenario 與 Given/When/Then 內容
- 服務介面（方法簽名、參數型別、回傳型別）
- 資料模型（列舉值、實體欄位）

### 2. 掃描測試框架

```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -name "*test*" -o -name "*spec*" | grep -v node_modules | head -5
```

框架優先順序：architecture.md 指定 > 專案既有 > 語言預設

### 3. 對每個 Scenario 生成 Contract Tests

對每個 Scenario 的 Given/When/Then：

1. **解析 Given** → 具體輸入值，對應 architecture.md 的型別定義
2. **解析 When** → 對應的服務方法呼叫（依 architecture.md 介面）
3. **解析 Then** → 具體預期輸出值
4. **每個 Then 獨立一個 test case**，編號 `S-{scenario}-{assertion}`

### 4. 輸出 Contract Test 檔案

依專案既有測試目錄輸出，命名：`{FeatureName}ContractTests.{ext}`

## 品質檢查

- [ ] 所有 Scenario 皆已轉為 contract tests（無篩選、無遺漏）
- [ ] 所有 test case 皆填充具體數值（無 TODO）
- [ ] 每個 test case 有正確的 `S-{scenario}-{assertion}` 編號
- [ ] 方法呼叫對應 architecture.md 定義的服務介面與參數型別
- [ ] 每個 test case 只有一個 Assert
- [ ] 3A 結構清晰，以空行區隔並加上行內註解
- [ ] 測試檔案可直接執行（無編譯錯誤）

開始讀取檔案並生成 contract tests。
