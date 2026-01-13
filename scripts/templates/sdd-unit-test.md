---
description: 從 feature file 和架構文件生成單元測試空殼，並分析測試策略
---

# SDD-UNIT-TEST: 單元測試空殼生成器

**輸入：** **PROMPT** (格式：`<feature_file_path>`)

**目標：**

1. 讀取 feature file 和對應的 architecture.md
2. 分析每個 Scenario 的測試策略（Unit Test vs Integration Test）
3. 生成單元測試空殼（Test Case structure without implementation）

## 核心原則

- **測試金字塔**：優先單元測試（快速、隔離），必要時使用整合測試
- **單元測試適用**：邏輯運算、資料轉換、商業規則、邊界條件、錯誤處理
- **整合測試適用**：跨服務互動、資料庫操作、外部 API、檔案系統、端對端流程
- **測試空殼**：只產生測試結構與 TODO 標記，不含實作邏輯

## 測試風格約束

### 1. 行為測試 vs 狀態測試

- **只測試行為**：驗證方法呼叫、回傳值、拋出的異常
- **不測試狀態**：不直接檢查物件內部狀態或私有欄位
- 焦點：「做了什麼」而非「是什麼」

### 2. Given 方法抽取規則

- **Mock Return Value**：抽成 `Given...()` 方法
  - 例：`GivenUserRepositoryReturnsVipUser()`
- **建立測試實例**：使用 `new` 建立的物件抽成 `Given...()` 方法
  - 例：`GivenVipUser()`, `GivenInvalidAmount()`
- 目的：提升測試可讀性，重用測試資料

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

### 3. 分析測試策略

對每個 Scenario 判斷測試層級：

#### ✅ 適合單元測試

- 純邏輯運算、資料轉換、商業規則
- 邊界條件、錯誤處理
- **特徵：不涉及外部依賴**

#### ⚠️ 適合整合測試

- 跨服務互動、資料庫、外部 API、檔案系統
- **特徵：需要真實或模擬的外部依賴**

### 4. 生成測試空殼

為每個**適合單元測試**的 Scenario 生成測試空殼，包含：

- 測試策略分析註解
- Import 語句（待填充）
- Setup 方法（初始化受測物件）
- Given...() 輔助方法（mock return value 和測試資料建立）
- 測試案例（使用 Fluent 風格，Given-When-Then 結構）
- TODO 註解標示需要實作的部分
- **重點**：只驗證行為（方法呼叫、回傳值、異常），不驗證狀態

### 5. 產出分析報告

在測試檔案開頭加入：

- 單元測試覆蓋的 Scenarios（含原因）
- 建議使用整合測試的 Scenarios（含原因，建議使用 `/sdd-integration-test`）
- 測試優先順序

## 測試檔案輸出

**檔案位置：**

- 依據 architecture.md 指定的測試目錄
- 或依專案既有測試結構
- 預設：`tests/unit/<feature_name>.test.<ext>`

## 品質檢查

- [ ] 已分析所有 Scenarios 的測試策略
- [ ] 為適合單元測試的 Scenario 生成測試空殼
- [ ] 測試空殼包含 Given-When-Then 結構和 TODO 標記
- [ ] 包含測試策略分析註解
- [ ] 測試檔案可編譯（無語法錯誤）
- [ ] 建議使用整合測試的 Scenario 有明確說明
- [ ] 遵循行為測試原則（不測試狀態）

## 使用範例

```bash
/sdd-spec Create a VIP discount system
/sdd-arch features/vip_discount.feature
/sdd-unit-test features/vip_discount.feature  # 產生單元測試空殼
# 開發者填充測試空殼並執行測試
/sdd-impl features/vip_discount.feature
```

開始讀取檔案並生成單元測試空殼。
