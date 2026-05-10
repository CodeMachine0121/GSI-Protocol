---
description: Phase 3 - 根據架構設計實作程式碼，滿足 Gherkin 規格
---

# SDD Phase 3: 實作

**角色：** 資深工程師  
**輸入：** Gherkin 規格檔案 __PROMPT__  
**前置條件：**
- 已完成 Phase 2，存在 `docs/features/{feature_name}/architecture.md`
- 已完成 sdd-test，存在 contract test 檔案  

**輸出：** Production code + unit tests（TDD 過程產出）

## 核心原則

- **遵循架構**：嚴格依照 architecture.md 定義的資料模型與服務介面
- **Contract First**：以 contract tests 為紅燈起點，驅動 production code 實作
- **TDD 循環**：Red → Green → Refactor，每個 contract test 通過才進行下一個
- **Unit Tests 隨行**：實作過程中為內部邏輯補充 unit tests

## 執行步驟

### 1. 讀取輸入

```bash
cat .gsi/<feature_name>/architecture.md
cat <feature_file_path>
```

找出 contract test 檔案：

```bash
find . -name "*ContractTest*" -o -name "*contract_test*" | grep -v node_modules | head -5
```

### 2. 確認 Contract Tests 狀態

執行 contract tests，確認全數為紅燈（未通過）：

```bash
# 依專案框架執行 contract test 檔案
```

若有 contract test 已通過 → 表示部分 production code 已存在，繼續讓剩餘紅燈通過。

### 3. TDD 循環：Red → Green → Refactor

依序對每個 contract test（S-1-1、S-1-2 ... 順序）執行：

**Red：** 確認 test 失敗

**Green：** 實作最小 production code 讓此 test 通過
- 依據 architecture.md 實作資料模型與服務方法
- 只寫讓當前 test 通過所需的邏輯，不過度設計

**Unit Tests：** 若此段邏輯有內部複雜度（邊界條件、計算規則），補充 unit tests
- Unit tests 驗證實作細節，contract tests 驗證行為
- 使用 3A 結構，命名清楚反映測試情境

**Refactor：** 確保所有已通過的 tests 仍為綠燈後再繼續下一個

### 4. 程式碼撰寫要求

**資料模型：**
- 實作列舉/常數（依 architecture.md §3.1）
- 實作核心實體（依 architecture.md §3.2）

**服務介面：**
- 實作服務類別與所有方法（依 architecture.md §4）
- 方法簽名必須與 architecture.md 完全一致

**Unit Tests：**
- 驗證方法回傳值、拋出的異常
- 不直接檢查物件內部狀態或私有欄位
- 命名反映測試情境

### 5. 構建與品質檢查

```bash
# 執行構建
# 執行 lint / type checking
# 執行所有測試（contract tests + unit tests）
```

確認全數通過後儲存檔案。

## 品質檢查

- [ ] 已讀取 `.gsi/{feature_name}/architecture.md` 與 contract test 檔案
- [ ] 所有 contract tests 通過（green）
- [ ] 所有 unit tests 通過（green）
- [ ] 所有資料模型已實作（依 architecture.md §3）
- [ ] 所有服務介面已實作（依 architecture.md §4）
- [ ] 方法簽名與 architecture.md 完全一致
- [ ] 檔案儲存至正確位置（依 architecture.md §7）
- [ ] 構建成功（無編譯錯誤）
- [ ] 程式碼品質檢查通過（lint、type checking）

## 下一步

完成後執行 sdd-verify 進行最終驗證。
