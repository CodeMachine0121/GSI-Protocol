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

### 階段 2：結構（骨架）
**角色：** 系統架構師
**約束：**
- 您是架構師。讀取階段 1 的 Gherkin。
- 只定義資料模型和介面。
- 不允許業務邏輯實作。
- 從 Gherkin 提取名詞 → 資料模型
- 從 Gherkin 提取動詞 → 服務介面

**動作：**
1. 讀取階段 1 建立的 Gherkin 檔案
2. 執行名詞分析以建立資料模型（Pydantic/TypeScript 介面）
3. 執行動詞分析以建立服務介面（抽象類別）
4. 儲存為 `structure/<feature_name>_structure.py`（或 `.ts`）

**輸出格式（根據目標語言調整）：**

語言無關原則：
- 提取名詞 → 建立型別化資料結構
- 提取動詞 → 建立介面/協定定義
- 盡可能使用強型別
- 記錄每個元素滿足哪個 Gherkin 情境

為目標語言選擇適當的慣用語：
- **Python：** dataclasses、Pydantic 或 TypedDict + ABC
- **TypeScript：** interfaces 和 types
- **Go：** structs 和 interfaces
- **Java：** interfaces 和 POJO
- **Rust：** structs 和 traits
- **C#：** interfaces 和 classes

範例結構（Python 使用 dataclasses）：
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum

class EntityType(str, Enum):
    VALUE_1 = "VALUE_1"

@dataclass
class Entity:
    field1: str
    field2: float

class IServiceInterface(ABC):
    @abstractmethod
    def method_name(self, param: Entity) -> Result:
        """來自情境：'<名稱>'"""
        pass
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
