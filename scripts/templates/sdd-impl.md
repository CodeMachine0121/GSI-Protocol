---
description: Phase 3 - 根據架構設計實作程式碼，滿足 Gherkin 規格
---

# SDD Phase 3: 實作

**角色：** 資深工程師  
**輸入：** Gherkin 規格檔案 __PROMPT__  
**前置條件：** 已完成 Phase 2，存在 `docs/features/{feature_name}/architecture.md`  
**輸出：** 實作程式碼於專案既有目錄結構

## 核心原則

- **遵循架構**：嚴格依照 architecture.md 定義的資料模型與服務介面
- **情境驅動**：每個 Gherkin 情境對應到程式碼邏輯分支
- **專案整合**：檔案放置於專案既有目錄結構
- **可測試性**：程式碼可直接用於驗證 Gherkin 情境

## 執行步驟

### 1. 偵測測試框架檔案

檢查 `sdd-test` 是否已執行：

```bash
find . -path "*{feature_name}*.test.*" -o -path "*{feature_name}*_test.*" -o -path "*{feature_name}*spec*" | grep -v node_modules | head -5
```

**判斷結果：**
- 找到測試框架檔案 → **TDD 模式**：實作測試程式碼 + production code
- 未找到 → **一般模式**：僅實作 production code

### 2. 讀取架構設計

從 `docs/features/{feature_name}/architecture.md` 讀取：
- 專案上下文（語言、框架、架構模式）
- 資料模型定義（列舉、實體）
- 服務介面定義（方法簽名、參數、回傳值）
- 情境對應關係

### 3. 實作 Production Code

依據架構文件實作：

**資料模型：**
- 實作列舉/常數
- 實作核心實體
- 加入資料驗證（依框架）

**服務介面：**
- 實作服務類別/介面
- 實作所有方法
- 每個方法對應 Gherkin 情境

**情境對應：**
- `Given` → 設定/輸入參數
- `When` → 方法呼叫
- `Then` → 回傳值/驗證

### 4. [TDD 模式] 填充測試程式碼

讀取測試框架檔案，填充每個 test case：
- 依照 3A 結構（Arrange / Act / Assert）實作
- 實作 `given...()` private method（設定 mock 回傳值）
- 實作 `create...()` private method（建立測試物件）
- 執行測試，確認全數通過

### 5. 儲存檔案

依據 architecture.md 的「檔案結構」章節，將檔案放置於正確位置

## 程式碼撰寫要求

### 註解標註
- 每個方法標註對應的 Gherkin 情境與行數
- 關鍵邏輯註明對應的 Given/When/Then

### 錯誤處理
依據專案既有模式處理異常

### 驗證邏輯
依據框架加入資料驗證（如需要）

## 品質檢查

- [ ] 已偵測測試框架檔案（確認 TDD 模式或一般模式）
- [ ] 已讀取 `docs/features/{feature_name}/architecture.md`
- [ ] 所有資料模型已實作
- [ ] 所有服務介面已實作
- [ ] 每個 Gherkin 情境都有對應程式碼邏輯
- [ ] 程式碼符合專案既有命名慣例與架構模式
- [ ] 檔案儲存至正確位置（依 architecture.md）
- [ ] 包含 Gherkin 情境追溯註解
- [ ] 構建成功（無編譯錯誤）
- [ ] 程式碼品質檢查通過（lint、type checking）
- [ ] **[TDD 模式]** 測試程式碼已填充且所有測試通過

## 測試失敗排查指南

### 構建失敗
1. 檢查編譯/語法錯誤信息
2. 驗證引入路徑與檔案位置是否正確
3. 確認依賴項是否已安裝

### 品質檢查失敗（Lint/Type 錯誤）
1. 查看具體的 lint 或 type 檢查報告
2. 根據專案的 linting 規則修正程式碼風格
3. 修正型別不匹配或缺少型別定義

### 測試失敗
1. 檢查失敗的具體情境與錯誤信息
2. 驗證程式碼邏輯是否正確對應 Gherkin 規格
3. 檢查是否有邊界條件未考慮到
4. 確認資料模型與服務實作是否完整
5. 修整程式碼後重新運行測試
6. 循環直到所有測試通過

## 執行流程

1. **偵測測試框架檔案**（決定 TDD 模式或一般模式）
2. 讀取 `docs/features/{feature_name}/architecture.md`
3. 讀取 `features/{feature_name}.feature`
4. 依據架構文件與專案上下文實作 production code
5. **[TDD 模式]** 填充測試程式碼並執行測試，失敗則修整後重試
6. 將檔案儲存至專案既有目錄結構
7. **構建檢查**：確保無編譯錯誤
8. **程式碼品質檢查**：運行 lint 和 type checking
9. 回報已建立的檔案清單與驗證結果

## 下一步

完成後可進行：
- 執行專案既有測試框架驗證
- 進入 Phase 4：測試驗證（如有定義）
- 整合至專案主要程式碼
