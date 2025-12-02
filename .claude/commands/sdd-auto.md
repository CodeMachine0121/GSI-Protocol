---
description: 自動執行完整 SDD 工作流程 - 從需求到驗證的全部 4 個階段
---

# SDD 自動模式 - 完整 4 階段工作流程

您現在正在執行 **SDD 自動** 模式。這會自動執行規格驅動開發工作流程的全部 4 個階段，將使用者需求轉換為經過驗證、可用於生產環境的程式碼，階段之間無需手動介入。

## 核心理念

**"規格 -> 結構 -> 實作"**

將業務邏輯、技術架構和程式撰寫分離到不同階段，以最小化幻覺並最大化精確度。

**此工作流程與語言和框架無關。** 使用者可以要求使用任何程式語言（Python、TypeScript、Go、Java、Rust 等）和任何框架進行實作。您應該相應調整輸出格式，同時維持 SDD 原則。

## 使用者需求

使用者已要求：{{prompt}}

## 語言偵測

**重要：** 開始前，確定目標語言：
1. 如果使用者在提示中明確指定語言（例如："in Python"、"using TypeScript"），使用該語言
2. 如果專案上下文建議某種語言（檢查現有檔案），使用該語言
3. 如果不清楚，詢問使用者偏好哪種語言
4. 如果沒有表達偏好，預設使用 Python

一旦確定，在所有階段中一致使用該語言。

## 您的任務

按順序執行全部 4 個階段：

### 階段 1：規格（靈魂）
**角色：** 產品經理
**約束：**
- 您是 PM。不要討論程式碼、資料庫或技術實作。
- 僅專注於使用者行為和業務規則。
- 使用 Gherkin 語法（Given-When-Then）。
- 必須包含：正常路徑、邊界情況、錯誤處理。

**動作：**
1. 分析使用者需求，找出業務規則和邊界情況
2. 建立包含完整 Gherkin 情境的 `.feature` 檔案
3. 儲存為 `features/<feature_name>.feature`

**輸出格式：**
```gherkin
Feature: <功能名稱>
  Scenario: <情境名稱>
    Given <前置條件>
    When <動作>
    Then <預期結果>
```

### 階段 2：架構設計（骨架）
**角色：** 系統架構師
**約束：**
- 您是架構師。讀取階段 1 的 Gherkin。
- **首先掃描專案上下文**，理解現有技術棧和架構模式。
- 定義功能架構：服務介面與資料模型。
- 不包含業務邏輯實作，只做架構規劃。
- 從 Gherkin 提取名詞 → 資料模型
- 從 Gherkin 提取動詞 → 服務介面
- **遵循專案既有架構風格**（若專案為新建，則使用最佳實踐）
- **輸出為中文的結構化 Markdown 文件**

**核心原則：**
- ✅ **語言無關**：不預設特定程式語言，根據專案上下文判斷
- ✅ **專案感知**：掃描現有專案結構、技術棧、架構模式
- ✅ **架構一致**：遵循專案既有的設計模式和命名慣例
- ✅ **靈活適應**：支援 prompt 指定或自動偵測架構風格

**動作：**
1. **掃描專案上下文**（必須執行）：
   - 偵測技術棧（package.json, requirements.txt, go.mod 等）
   - 分析現有架構模式（controllers/, services/, repositories/ 等）
   - 識別命名慣例（camelCase, snake_case 等）
   - 檢查配置檔案和依賴

2. 讀取階段 1 建立的 Gherkin 檔案

3. 執行名詞分析以建立資料模型設計

4. 執行動詞分析以建立服務介面設計

5. 生成架構決策說明

6. 儲存為 `docs/features/{feature_name}/architecture.md`（中文 Markdown）

**輸出格式：**

檔案位置：`docs/features/{feature_name}/architecture.md`（中文文件）

文件必須包含：

```markdown
# {功能名稱} - 架構設計

> 來源：features/{feature_name}.feature
> 建立日期：{日期}

## 0. 專案上下文

### 技術棧資訊
- **程式語言**：{偵測或指定的語言}
- **框架**：{偵測或指定的框架}
- **資料庫**：{偵測或指定的資料庫}
- **ORM/ODM**：{偵測或指定的 ORM}
- **架構模式**：{偵測或指定的架構模式}

### 現有專案結構
```
{顯示掃描到的專案目錄結構}
```

### 命名慣例
- 檔案命名：{snake_case / camelCase / PascalCase}
- 類別命名：{PascalCase / camelCase}
- 方法命名：{camelCase / snake_case}

### 設計模式偵測
- [ ] Repository Pattern
- [ ] Service Layer
- [ ] MVC
- [ ] Clean Architecture
- [ ] DDD

## 1. 功能概述

本功能提供 {功能簡述}。

**核心需求：**
- {需求 1}
- {需求 2}

## 2. 資料模型設計

### 2.1 列舉與常數

#### {EnumName}（{描述}）
**來源情境：** "{Gherkin 語句}" (第 X 行)

| 值 | 說明 | 用途 |
|---|---|---|
| {VALUE_1} | {說明} | {用途} |

**實作建議（基於 {語言}）：**
```{language}
{語言特定的列舉實作範例}
```

### 2.2 核心實體

#### {EntityName}（{描述}）
**來源情境：** "{Gherkin 語句}" (第 X 行)

| 欄位名稱 | 資料型別 | 必填 | 預設值 | 說明 |
|---|---|---|---|---|
| {field1} | {type} | ✅/- | {default} | {說明} |

**實作範例（基於 {language} + {orm}）：**
```{language}
{語言和 ORM 特定的模型定義}
```

## 3. 服務介面設計

### 3.1 {ServiceName}（{服務描述}）

**在專案架構中的位置：**
```
src/{path}/{ServiceName}.{ext}
```

#### 方法：{methodName}()

**來源情境：**
- "{Gherkin 語句}" (第 X-Y 行)

**方法簽名（基於 {language}）：**
```{language}
{語言特定的方法簽名}
```

**輸入參數：**

| 參數名稱 | 型別 | 說明 |
|---|---|---|
| {param1} | {type} | {說明} |

**回傳值：**

| 型別 | 說明 |
|---|---|
| {returnType} | {說明} |

**業務規則：**
1. {規則 1}
2. {規則 2}

**與現有服務的整合：**
- 依賴服務：{依賴的現有服務}
- 被依賴於：{可能依賴此服務的其他服務}

## 4. 架構決策

### 4.1 為什麼選擇此架構模式？

**基於專案分析：**
- ✅ 專案現有架構：{偵測到的架構}
- ✅ 保持一致性：{說明如何保持一致}
- ✅ 整合考量：{與現有元件的整合方式}

### 4.2 資料模型設計理由

**與現有模型的關聯：**
- 關聯模型：{現有的相關模型}
- 關聯方式：{One-to-Many, Many-to-Many 等}

### 4.3 技術考量

#### 型別定義（{language}）
{語言特定的型別定義建議}

#### 資料驗證（{framework}）
{框架特定的驗證建議}

#### 錯誤處理（{language}）
{語言特定的錯誤處理模式}

## 5. 情境對應關係

| Gherkin 情境 | 行數 | 相關資料模型 | 相關服務方法 | 驗證重點 |
|---|---|---|---|---|
| {情境描述} | {行號} | {Model} | {method()} | {驗證重點} |

## 6. 檔案結構規劃

**基於專案既有結構，新增以下檔案：**

```
{project_root}/
├── src/
│   ├── {模型目錄}/
│   │   └── {FeatureName}Model.{ext}
│   ├── {服務目錄}/
│   │   └── {FeatureName}Service.{ext}
│   └── {介面目錄}/
│       └── I{FeatureName}Service.{ext}
└── docs/
    └── features/{feature_name}/
        └── architecture.md
```

## 7. 下一步行動

### 階段 3：程式碼實作

**需要實作的元件（基於 {language} + {framework}）：**

1. ✅ 定義列舉/常數
2. ✅ 建立資料模型
3. ✅ 實作服務介面/類別
4. ✅ 整合現有架構
5. ✅ 撰寫單元測試
```

**專案上下文掃描命令：**
```bash
# 1. 檢測技術棧
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml|Cargo.toml"

# 2. 分析目錄結構
find src -type d -maxdepth 2 2>/dev/null || find . -type d -maxdepth 2

# 3. 掃描現有程式碼模式
find . -name "*.service.*" -o -name "*Service.*" 2>/dev/null | head -5
find . -name "*.repository.*" -o -name "*Repository.*" 2>/dev/null | head -5
```

### 階段 3：實作（血肉）
**角色：** 資深工程師
**約束：**
- 您是工程師。您必須使用階段 2 的資料模型。
- 為階段 2 的介面實作邏輯。
- 每個程式碼分支必須對應一個 Gherkin 情境。
- 您的程式碼必須通過階段 1 的所有情境。

**動作：**
1. 讀取階段 1 的 Gherkin 檔案
2. 讀取階段 2 的結構檔案
3. 實作滿足介面的具體類別
4. 確保滿足所有 Gherkin 情境
5. 儲存為 `implementation/<feature_name>_impl.py`（或 `.ts`）

**輸出格式（根據目標語言調整）：**

使用目標語言的慣用語實作階段 2 中定義的介面/特徵：

- 將 Gherkin `Given` 對應 → 設定/前置條件
- 將 Gherkin `When` 對應 → 方法執行
- 將 Gherkin `Then` 對應 → 回傳值/結果

範例（Python）：
```python
from structure import IServiceInterface, Entity, Result

class ServiceImpl(IServiceInterface):
    def method_name(self, param: Entity) -> Result:
        # 情境 1：<名稱>
        if condition_from_scenario:
            return Result(value=expected)
        # 情境 2：<名稱>
        return Result(value=other)
```

範例（TypeScript）：
```typescript
import { IServiceInterface, Entity, Result } from './structure';

export class ServiceImpl implements IServiceInterface {
  methodName(param: Entity): Result {
    // 情境 1：<名稱>
    if (conditionFromScenario) {
      return { value: expected };
    }
    return { value: other };
  }
}
```

範例（Go）：
```go
type ServiceImpl struct {}

func (s *ServiceImpl) MethodName(param Entity) Result {
    // 情境 1：<名稱>
    if conditionFromScenario {
        return Result{Value: expected}
    }
    return Result{Value: other}
}
```

### 階段 4：驗證（檢查）
**角色：** QA 自動化
**約束：**
- 驗證階段 3 的實作是否符合階段 1 的需求。
- 對實作執行每個 Gherkin 情境。
- 報告通過/失敗並提供詳細回饋。

**動作：**
1. 讀取階段 1 的 Gherkin 檔案
2. 讀取階段 3 的實作
3. 對於每個 Gherkin 情境：
   - 設定 Given 條件
   - 執行 When 動作
   - 驗證 Then 結果
4. 建立驗證報告
5. 如果有失敗，為階段 3 重試提供具體回饋

**輸出格式：**
```markdown
# 驗證報告

## 測試結果

### 情境：<名稱>
- 狀態：✅ 通過 / ❌ 失敗
- Given：<條件設定>
- When：<執行的動作>
- Then：<預期 vs 實際>
- 備註：<任何差異>

## 摘要
- 總情境數：X
- 通過：Y
- 失敗：Z

## 下一步
[如果全部通過]：✅ 功能完成
[如果有任何失敗]：階段 3 重試的回饋：<具體問題>
```

## 執行指示

1. **從階段 1 開始**：建立 Gherkin 規格
2. **等待使用者確認**（可選，但對複雜功能建議）
3. **進入階段 2**：設計結構
4. **進入階段 3**：實作邏輯
5. **以階段 4 完成**：驗證實作
6. **如果階段 4 失敗**：帶著具體回饋返回階段 3

## 重要提醒

- 建立待辦清單追蹤全部 4 個階段
- 在進入下一階段前將每個階段標記為已完成
- 將所有產出儲存在指定的目錄結構中
- 不要跳過階段或將它們合併
- 每個階段都有嚴格的輸入/輸出契約

現在從階段 1 開始：需求規格。
