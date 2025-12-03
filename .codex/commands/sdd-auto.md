---
description: 自動執行完整 SDD 工作流程 (4 Phases)
---

# SDD 自動模式

**需求：** {{prompt}}

**目標：** 自動執行 Phase 1-4，從需求到驗證完成，無需手動介入

**核心理念：** 規格 → 架構 → 實作 → 驗證（語言無關，專案感知）

## 開始前：掃描專案

```bash
# 技術棧
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"

# 目錄結構
find . -type d -maxdepth 3 | grep -E "src|models|services" | head -10

# 程式碼樣本
find . -name "*.ts" -o -name "*.py" -o -name "*.go" | head -5
```

**判斷優先順序：** Prompt 指定 > 專案上下文 > 詢問使用者 > 預設 TypeScript

## Phase 1: 規格（PM）

**角色：** PM - 只談業務規則，不談技術  
**輸出：** `features/{feature_name}.feature`

**動作：**
1. 分析需求找出業務規則和邊界情況
2. 用 Gherkin 撰寫情境（Given-When-Then）
3. 必須包含：正常路徑、邊界、錯誤處理

```gherkin
Feature: {功能名稱}
  Scenario: {情境}
    Given {前置條件}
    When {動作}
    Then {預期結果}
```

## Phase 2: 架構（架構師）

**角色：** 架構師 - 高階設計，語言無關  
**輸出：** `docs/features/{feature_name}/architecture.md` (繁中)

**動作：**
1. 掃描專案上下文（技術棧、架構、命名慣例）
2. 讀取 Phase 1 的 Gherkin
3. 名詞 → 資料模型；動詞 → 服務介面
4. 生成繁體中文 Markdown 架構文件

**文件結構：**
```markdown
# {功能} - 架構設計

## 1. 專案上下文
- 語言/框架/架構模式/命名慣例

## 2. 功能概述

## 3. 資料模型
- 列舉/常數
- 核心實體（欄位、型別、說明）

## 4. 服務介面
- 方法簽名（語言無關描述）
- 業務規則

## 5. 架構決策
- 選擇此架構的理由

## 6. 情境對應
| 情境 | 模型 | 方法 |

## 7. 檔案結構規劃
```

## Phase 3: 實作（工程師）

**角色：** 工程師 - 依架構實作程式碼  
**輸出：** 實作檔案（依 architecture.md 定義位置）

**動作：**
1. 讀取 Gherkin + architecture.md
2. 依架構文件實作資料模型與服務
3. 每個 Gherkin 情境對應程式碼邏輯分支
4. 檔案存至 architecture.md 指定位置

**情境對應：** Given→輸入 / When→執行 / Then→驗證

## Phase 4: 驗證（QA）

**角色：** QA - 驗證架構與情境符合性  
**輸出：** `docs/features/{feature_name}/conclusion.md`

**動作：**
1. 讀取 Gherkin + architecture.md + 實作
2. 驗證架構符合性（模型、介面、檔案位置）
3. 驗證每個 Gherkin 情境（Given→When→Then）
4. 生成結論至 `docs/features/{feature_name}/conclusion.md`

**報告格式：**
```markdown
# {功能} - 驗證結論

## 1. 架構符合性
| 元件 | 定義 | 實作 | 狀態 |

## 2. 情境驗證
### {情境} (第 X 行)
- Given/When/Then → ✅/❌

## 3. 摘要
- 架構：{通過}/{總數}
- 情境：{通過}/{總數}
- **狀態：** ✅ 完成 / ❌ 需修正

## 4. 失敗回饋（如有）
```

## 執行流程

1. 掃描專案上下文
2. Phase 1 → `features/{feature}.feature`
3. Phase 2 → `docs/features/{feature}/architecture.md`
4. Phase 3 → 實作檔案（依 architecture.md）
5. Phase 4 → `docs/features/{feature}/conclusion.md`
6. 失敗時返回 Phase 3 重試

**輸出結構：**
```
project_root/
├── features/{feature}.feature
├── docs/features/{feature}/
│   ├── architecture.md
│   └── conclusion.md
└── {專案目錄}/
    ├── {模型檔案}
    └── {服務檔案}
```

**重要：** 
- Phase 2 輸出繁體中文 Markdown（語言無關）
- Phase 3 遵循專案技術棧與架構
- 每個 Phase 必須完成才進入下一個

開始執行 Phase 1。
