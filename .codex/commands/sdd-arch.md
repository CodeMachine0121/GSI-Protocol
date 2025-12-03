---
description: Phase 2 - 分析 Gherkin 規格，設計高階架構（資料模型與服務介面），輸出到 docs/features/{feature_name}/
---

# SDD Phase 2: 架構設計

**角色：** 系統架構師  
**輸入：** Gherkin 規格檔案 {{prompt}}  
**輸出：** `docs/features/{feature_name}/architecture.md`

## 核心原則

- **語言無關**：根據專案上下文自動適應
- **專案感知**：掃描技術棧、架構模式、命名慣例
- **架構一致**：遵循專案既有設計
- **高階設計**：定義資料模型與服務介面，不含實作細節

## 執行步驟

### 1. 分析專案上下文

掃描專案以判斷：
- **技術棧**：檢查 `package.json`、`go.mod`、`requirements.txt` 等
- **架構模式**：識別目錄結構（`controllers/`、`services/`、`repositories/` 等）
- **命名慣例**：分析既有程式碼風格（camelCase、snake_case 等）

優先順序：Prompt 指定 > 專案既有架構 > 語言最佳實踐

### 2. 提取功能名稱

從 Gherkin 檔案路徑或 Feature 名稱提取，轉換為專案命名慣例

### 3. 設計架構

- **名詞 → 資料模型**：識別實體、欄位、列舉
- **動詞 → 服務介面**：定義方法簽名、參數、回傳值
- **架構決策**：說明設計理由與整合方式

## 輸出文件結構

```markdown
# {功能名稱} - 架構設計

> 來源：features/{feature_name}.feature  
> 建立日期：{日期}

## 1. 專案上下文

- 程式語言：{language}
- 框架：{framework}
- 架構模式：{pattern}
- 命名慣例：{convention}

## 2. 功能概述

{簡述功能及核心需求}

## 3. 資料模型

### 3.1 列舉/常數

#### {EnumName}
來源："{Gherkin 語句}" (第 X 行)

| 值 | 說明 |
|---|---|
| {VALUE} | {說明} |

### 3.2 核心實體

#### {EntityName}
來源："{Gherkin 語句}" (第 X 行)

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| {field} | {type} | ✅/- | {說明} |

## 4. 服務介面

### {ServiceName}

職責：{服務職責}

#### {methodName}()
來源："{Gherkin 語句}" (第 X-Y 行)

**簽名：** `{signature}`

**參數：**
| 參數 | 型別 | 說明 |
|---|---|---|
| {param} | {type} | {說明} |

**回傳：** {returnType}

**業務規則：**
1. {規則 1}
2. {規則 2}

## 5. 架構決策

- 為何選擇此架構模式：{理由}
- 資料模型設計理由：{理由}
- 整合方式：{與現有系統的整合}

## 6. 情境對應

| 情境 | 行數 | 資料模型 | 服務方法 |
|---|---|---|---|
| {情境} | {行號} | {Model} | {method()} |

## 7. 檔案結構

```
src/
├── {模型目錄}/{FeatureName}Model.{ext}
├── {服務目錄}/{FeatureName}Service.{ext}
└── tests/{FeatureName}.test.{ext}
```
```

## 品質檢查

- [ ] 已掃描專案上下文（技術棧、架構、命名）
- [ ] 所有名詞已轉為資料模型
- [ ] 所有動詞已轉為服務介面
- [ ] 每個元素註明 Gherkin 來源行數
- [ ] 包含架構決策說明
- [ ] 全文使用繁體中文
- [ ] 檔案儲存至 `docs/features/{feature_name}/architecture.md`

## 執行流程

1. 掃描專案（技術棧、架構、命名慣例）
2. 讀取 Gherkin 檔案
3. 提取名詞（實體）與動詞（行為）
4. 生成架構文件（遵循專案上下文）
5. 儲存至 `docs/features/{feature_name}/architecture.md`
6. 回報技術棧與架構決策
