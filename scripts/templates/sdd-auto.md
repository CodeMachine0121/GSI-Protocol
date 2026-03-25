---
description: 自動執行完整 SDD 工作流程 (核心 4 階段)
---

# SDD 自動模式

**需求：** __PROMPT__

**目標：** 自動執行完整流程，從需求到驗證完成，無需手動介入

**核心理念：** 規格 → 架構 → 測試框架 → 實作 → 驗證（語言無關，專案感知）

## 開始前：掃描專案

```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -type d -maxdepth 3 | grep -E "src|models|services" | head -10
```

**技術棧判斷優先順序：** Prompt 指定 > 專案既有 > 詢問使用者 > 預設 TypeScript

---

## Phase 1: 規格（PM）

**角色：** PM - 只談業務規則，不談技術
**輸出：** `features/{feature_name}.feature`

1. 檢查 `features/` 目錄是否有與新需求衝突的既有規格，若有則停止並向使用者確認
2. 分析需求，找出業務規則、邊界條件、錯誤處理
3. 撰寫 Gherkin 情境（Given-When-Then），必須涵蓋正常路徑、邊界、錯誤處理

---

## Phase 2: 架構（架構師）

**角色：** 架構師 - 高階設計，語言無關
**輸出：** `docs/features/{feature_name}/architecture.md`（繁體中文）

1. 掃描專案上下文（技術棧、架構模式、命名慣例）
2. 讀取 Phase 1 的 Gherkin
3. 名詞 → 資料模型；動詞 → 服務介面
4. 每個資料模型與服務介面須標注對應的 Gherkin 來源行數
5. 輸出包含：專案上下文、資料模型、服務介面、架構決策、情境對應、檔案結構規劃

---

## Phase 2.5: 單元測試框架（測試生成器）

**角色：** 測試生成器 - 篩選適合單元測試的業務情境，建立測試方法框架
**輸出：** 測試框架檔案（依專案既有測試框架與目錄結構）

1. 讀取 Gherkin + architecture.md
2. 掃描專案測試框架與既有測試結構
3. 篩選適合單元測試的 Scenario（純邏輯、商業規則、邊界條件、可 mock 的外部依賴）
4. 為篩選出的情境建立測試方法框架（只開方法，內容為 TODO，不實作）：
   - 測試類別宣告、mock 物件宣告
   - test case method 框架（3A 結構標注）
   - `given...()` private method 框架
   - `create...()` private method 框架
5. 輸出篩選分析報告（已篩選 vs 未篩選的 Scenario 及原因）

---

## Phase 3: 實作（工程師）

**角色：** 資深工程師 - 依架構實作程式碼（TDD 模式）
**輸出：** 實作檔案（依 architecture.md 定義位置）

1. 讀取 `docs/features/{feature_name}/architecture.md`，依資料模型與服務介面定義實作 production code
2. 每個 Gherkin 情境對應程式碼邏輯分支（Given→輸入 / When→執行 / Then→驗證）
3. 填充 Phase 2.5 產生的測試框架：實作 3A 結構、`given...()`、`create...()` method，執行測試確認全數通過
4. 構建檢查 + 程式碼品質檢查（lint、type checking）
5. 將檔案儲存至 architecture.md 定義的位置

---

## Phase 4: 驗證（QA）

**角色：** QA - 驗證架構、情境符合性，並執行單元測試，只報告不修改
**輸出：** `docs/features/{feature_name}/conclusion.md`（全部通過才產生）

1. 讀取 Gherkin + architecture.md + 實作程式碼
2. 驗證架構符合性（資料模型、服務介面、檔案位置、命名慣例）
3. 逐一驗證每個 Gherkin 情境（Given→When→Then）
4. 依專案現有設定（README、Makefile、package.json scripts 等）找出測試指令並執行所有單元測試
5. 架構、情境、單元測試**全部通過**才輸出結論報告；若任一失敗，列出錯誤並停止

若 Phase 4 發現失敗 → 返回 Phase 3 修正，再重新執行 Phase 4

---

## 輸出結構

```
project_root/
├── features/{feature}.feature              # Phase 1
├── docs/features/{feature}/
│   ├── architecture.md                     # Phase 2
│   └── conclusion.md                       # Phase 4
├── {專案測試目錄}/{feature}.test.{ext}      # Phase 2.5
└── {專案目錄}/
    ├── {模型檔案}                          # Phase 3
    └── {服務檔案}                          # Phase 3
```

開始執行 Phase 1。
