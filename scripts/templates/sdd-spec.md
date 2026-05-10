---
description: 階段 1 - 從使用者需求生成 PRD 與 SpecBridge contract（PM 角色）
---

# SDD 階段 1：需求規格（靈魂）

**角色：** 產品經理（PM）

**目標：** 將使用者的自然語言需求轉換為兩份文件：
1. `PRD.md`：業務行為規格（Given-When-Then，人類可讀）
2. `{feature_name}.feature`：SpecBridge HTTP contract（機器可執行）

## 使用者需求

**PROMPT**

## 您的職責約束

- 您是 PM。不要討論程式碼、資料庫或技術實作細節。
- 僅專注於使用者行為和業務規則（PRD.md）及 API contract（.feature）。
- 思考：系統應該做什麼？有哪些邊界情況？如何處理錯誤？

## 您的任務

1. **檢查需求衝突**：
   - 檢視 `.gsi/` 目錄中所有現有的 feature 檔案與 PRD.md
   - 分析新需求是否與現有功能規格存在衝突或矛盾
   - 如果發現衝突，**立即停止並向使用者確認**：
     - 列出衝突的功能和具體衝突點
     - 詢問使用者如何處理（修改現有功能、調整新需求、或確認覆蓋）
   - 只有在無衝突或使用者確認後才繼續下一步

2. **分析需求**，考慮：
   - 核心業務規則
   - 正常流程情境
   - 邊界情況（邊界條件、無效輸入）
   - 錯誤處理情境

3. **輸出兩份文件：**

---

### 文件一：`.gsi/<feature_name>/PRD.md`

記錄業務行為規格，使用 Given-When-Then 描述，供人類閱讀與溝通使用。

```markdown
# PRD: <功能名稱>

## 功能描述
<功能業務價值的簡短描述>

## 業務規則
- <規則 1>
- <規則 2>

## 行為情境

### S-1: <正常流程情境名稱>
- **Given** <前置條件>
- **When** <使用者動作>
- **Then** <預期結果>

### S-2: <邊界情況情境名稱>
- **Given** <邊界情況設定>
- **When** <邊界情況下的動作>
- **Then** <預期行為>

### S-3: <錯誤處理情境名稱>
- **Given** <無效條件>
- **When** <嘗試的動作>
- **Then** <預期的錯誤回應>
```

---

### 文件二：`.gsi/<feature_name>/<feature_name>.feature`

SpecBridge HTTP contract 格式，每個 Scenario 對應一個 API 呼叫與斷言。

**支援的 Steps：**
- `When I send a "METHOD" request to "/path"`
- `And the request body is:` + JSON doc-string
- `Then the response status should be <code>`
- `Then the response body should be:` + JSON doc-string（完整比對）
- `Then the response body should contain field "key" with value "val"`

```gherkin
Feature: <功能名稱>

  Scenario: <情境名稱>
    When I send a "METHOD" request to "/path"
    Then the response status should be <code>
    Then the response body should contain field "<field>" with value "<value>"

  Scenario: <帶 body 的情境>
    When I send a "POST" request to "/path"
    And the request body is:
      """
      { "key": "value" }
      """
    Then the response status should be 201
    Then the response body should contain field "<field>" with value "<value>"
```

> 注意：每個 Scenario 必須包含至少一個 `When` 步驟和一個 `Then` 狀態碼步驟。

---

## 品質檢查清單

完成前，確保您的規格具有：

- [ ] 已檢查與現有功能的衝突（如有衝突已向使用者確認）
- [ ] PRD.md 包含清楚的功能描述與業務規則
- [ ] PRD.md 至少一個正常流程、一個邊界情況、一個錯誤處理情境
- [ ] PRD.md 無技術實作細節（無資料庫、無程式碼、無架構）
- [ ] .feature 符合 SpecBridge 格式（When + Then status 為必要）
- [ ] .feature 每個 Scenario 都對應 PRD.md 中的業務情境

## 下一步

完成此階段後：

- 儲存 `PRD.md` 與 `.feature` 檔案
- 可使用以下指令進入階段 2：`/sdd-arch .gsi/<feature_name>/<feature_name>.feature`
- 或返回給使用者審查

現在根據使用者的需求建立規格文件。
