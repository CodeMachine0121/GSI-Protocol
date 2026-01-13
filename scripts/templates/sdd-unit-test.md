---
description: 從 feature file 篩選適合單元測試的業務情境，建立測試方法框架
---

# SDD-UNIT-TEST: 單元測試框架生成器

**輸入：** **PROMPT** (格式：`<feature_file_path>`)

**目標：**

1. 讀取 feature file 和對應的 architecture.md
2. 從所有 Scenario 中篩選出**適合撰寫單元測試防護**的業務情境
3. 為篩選出的情境建立測試方法框架（只開好 test case method，內容為空或 TODO 註解）

## 核心原則

### 1. 篩選適合單元測試的業務情境

- **單元測試適用**：純邏輯運算、資料轉換、商業規則、邊界條件、錯誤處理
- **單元測試不適用**：跨服務互動、資料庫操作、外部 API、檔案系統、端對端流程
- **篩選標準**：不涉及外部依賴的情境才建立單元測試框架

### 2. 固定測試原則：只測行為，不測狀態

- ✅ **測試行為**：驗證方法呼叫、回傳值、拋出的異常
- ❌ **不測狀態**：不直接檢查物件內部狀態或私有欄位
- **焦點**：「做了什麼」而非「是什麼」

### 3. 測試方法框架要求

- **只建立 test case method**：方法簽名正確，但內容為空或只有 TODO 註解
- **不實作測試邏輯**：不寫任何實作內容
- **結構清晰**：方法命名反映測試情境，易於後續填充

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

### 3. 篩選適合單元測試的業務情境

對每個 Scenario 判斷是否適合單元測試：

#### ✅ 篩選標準：適合單元測試

- 純邏輯運算、資料轉換、商業規則
- 邊界條件、錯誤處理
- **關鍵特徵：不涉及外部依賴（資料庫、外部 API、檔案系統、跨服務）**

#### ⏭️ 跳過：不適合單元測試（建議使用整合測試）

- 跨服務互動、資料庫操作、外部 API、檔案系統
- **特徵：需要真實或模擬的外部依賴**
- 這些情境記錄在分析報告中，但不建立單元測試框架

### 4. 建立測試方法框架

為每個**篩選出的 Scenario** 建立測試方法框架，包含：

- 測試篩選分析註解（說明為何適合單元測試）
- Import 語句（基本測試框架）
- 測試類別宣告
- 測試方法（test case method）（只有方法簽名，內容為空或只有 TODO 註解）
- **重點**：
  - 方法命名清楚反映測試情境
  - 內容為空或只有 `// TODO: implement` 註解
  - 註解說明測試重點：「只測行為，不測狀態」

### 5. 產出篩選分析報告

在測試檔案開頭加入註解說明：

- **已篩選進單元測試的 Scenarios**（含原因：為何適合單元測試）
- **未篩選進單元測試的 Scenarios**（含原因：為何不適合，建議使用整合測試）
- **測試原則提醒**：「本測試只測行為，不測狀態」

## 測試檔案輸出

**檔案位置：**

- 依據 architecture.md 指定的測試目錄
- 或依專案既有測試結構
- 預設：`tests/unit/<feature_name>.test.<ext>`

## 品質檢查

- [ ] 已掃描所有 Scenarios 並完成篩選
- [ ] 只為適合單元測試的 Scenario 建立測試方法框架
- [ ] 測試方法框架內容為空或只有 TODO 註解
- [ ] 方法命名清晰反映測試情境
- [ ] 包含篩選分析報告（已篩選 vs 未篩選的 Scenarios）
- [ ] 測試檔案可編譯（無語法錯誤）
- [ ] 明確標示「只測行為，不測狀態」原則
- [ ] 未篩選的 Scenario 有明確說明不適合單元測試的原因

## 使用範例

```bash
/sdd-spec Create a VIP discount system
/sdd-arch features/vip_discount.feature
/sdd-unit-test features/vip_discount.feature  # 篩選業務情境並建立測試方法框架
# 開發者填充測試方法內容並執行測試
/sdd-impl features/vip_discount.feature
```

## 輸出範例結構

```java
/**
 * 篩選分析報告：
 * 
 * 已篩選進單元測試的 Scenarios：
 * - "VIP user gets 10% discount"（純商業邏輯計算，無外部依賴）
 * - "Invalid amount throws exception"（邊界條件錯誤處理）
 * 
 * 未篩選進單元測試的 Scenarios：
 * - "Save order to database"（需要資料庫操作，建議使用整合測試）
 * 
 * 測試原則：本測試只測行為，不測狀態
 */

public class VipDiscountServiceTest {
    // TODO: Add imports
    
    @Test
    public void testVipUserGets10PercentDiscount() {
        // TODO: implement
    }
    
    @Test
    public void testInvalidAmountThrowsException() {
        // TODO: implement
    }
}
```

開始讀取檔案、篩選業務情境並建立測試方法框架。
