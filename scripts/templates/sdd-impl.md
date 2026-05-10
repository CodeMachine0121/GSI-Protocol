---
description: Phase 3 - 根據架構設計實作程式碼，以 unit tests 驅動 TDD
---

# SDD Phase 3: 實作

**角色：** 資深工程師  
**輸入：** __PROMPT__ (feature 檔案路徑)  
**前置條件：** 已完成 Phase 2，存在 `.gsi/{feature_name}/architecture.md`

**輸出：** Production code + unit tests（TDD 過程產出）

## 核心原則

- **遵循架構**：嚴格依照 architecture.md 定義的資料模型與服務介面
- **Unit Test 驅動**：先寫 unit test（紅燈），再實作 production code（綠燈），再 refactor
- **Contract 由 SpecBridge 驗證**：不需撰寫 contract test 程式碼，Phase 4 由 `specbridge verify` 負責

## 執行步驟

### 1. 讀取輸入

```bash
cat .gsi/<feature_name>/architecture.md
cat .gsi/<feature_name>/PRD.md
```

確認：
- 服務介面（方法簽名、參數型別、回傳型別）
- 資料模型（列舉值、實體欄位）
- 業務規則（PRD.md 的情境）

### 2. 掃描測試框架

```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -name "*test*" -o -name "*spec*" | grep -v node_modules | head -5
```

框架優先順序：architecture.md 指定 > 專案既有 > 語言預設

### 3. TDD 循環：Red → Green → Refactor

依 PRD.md 的業務情境逐一執行：

**Red：** 依業務規則撰寫 unit test，執行確認失敗

**Green：** 實作最小 production code 讓此 test 通過
- 依據 architecture.md 實作資料模型與服務方法
- 只寫讓當前 test 通過所需的邏輯，不過度設計

**Refactor：** 確保所有已通過的 tests 仍為綠燈後再繼續下一個

### 4. 程式碼撰寫要求

**資料模型：**
- 實作列舉/常數（依 architecture.md §3.1）
- 實作核心實體（依 architecture.md §3.2）

**服務介面：**
- 實作服務類別與所有方法（依 architecture.md §4）
- 方法簽名必須與 architecture.md 完全一致

**Unit Tests：**
- 驗證方法回傳值、拋出的異常與邊界條件
- 不直接檢查物件內部狀態或私有欄位
- 3A 結構（Arrange / Act / Assert）以空行區隔
- 命名清楚反映測試情境

### 5. 構建與品質檢查

```bash
# 執行構建
# 執行 lint / type checking
# 執行所有 unit tests
```

確認全數通過後儲存檔案。

## 品質檢查

- [ ] 已讀取 `.gsi/{feature_name}/architecture.md` 與 `PRD.md`
- [ ] 所有 unit tests 通過（green）
- [ ] 所有資料模型已實作（依 architecture.md §3）
- [ ] 所有服務介面已實作（依 architecture.md §4）
- [ ] 方法簽名與 architecture.md 完全一致
- [ ] 檔案儲存至正確位置（依 architecture.md §7）
- [ ] 構建成功（無編譯錯誤）
- [ ] 程式碼品質檢查通過（lint、type checking）

## 下一步

完成後執行 `sdd-verify` 進行最終驗證（specbridge contract + unit tests）。
