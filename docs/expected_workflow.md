# AI 驅動的 SDD 工作流程定義

> 用於新功能實作的規格驅動開發

## 1. 概覽

此工作流程為使用 AI 代理建立軟體功能定義了嚴格的**規格驅動開發（SDD）** 流程。核心理念是**「規格 → 架構 → 實作 → 驗證」**。

該流程將業務邏輯、技術架構、程式撰寫和品質保證隔離到四個不同 Phase，以最小化幻覺並最大化精確度。

## 2. 流程（文字描述）

```text
[ 使用者需求 ]
       │
       ▼
+=============================================+
|  Phase 1：規格（靈魂）                       |
|  角色：  PM 代理                            |
|  行動：  定義行為（BDD）                     |
|  輸出：  Gherkin (.feature)                 |
+=============================================+
       │
       │ (傳遞 Gherkin)
       ▼
+=============================================+
|  Phase 2：架構（骨架）                       |
|  角色：  架構師代理                          |
|  行動：  設計資料模型與服務介面（繁中）        |
|  輸入：  Gherkin                            |
|  輸出：  架構文件 (Markdown)                 |
+=============================================+
       │
       │ (傳遞 Gherkin + 架構文件)
       ▼
+=============================================+
|  Phase 3：實作（血肉）                       |
|  角色：  工程師代理                          |
|  行動：  撰寫程式碼 / 遵循架構                |
|  輸入：  Gherkin + 架構文件                  |
|  輸出：  可執行程式碼                         |
+=============================================+
       │
       ▼
+=============================================+
|  Phase 4：驗證（檢查）                       |
|  角色：  QA 代理                            |
|  行動：  對照規格與架構驗證程式碼              |
|  輸出：  驗證結論報告                         |
+=============================================+
       │
       ├───── < 失敗 > ────┐
       │                   │ (回饋循環)
       │                   │
       ▼                   │
( 功能完成 )               └────→ [ 重試 Phase 3 ]
```

## 3. 工作流程階段詳情

### 階段 1：需求規格（行為）

**角色：** 產品經理（PM）
**目標：** 使用 BDD 將模糊的使用者需求轉換為嚴格的行為規格。

- **輸入：** 使用者的自然語言請求（例如，「我需要 VIP 折扣系統」）。
- **行動：**
  1. 分析業務規則和邊界案例。
  2. 使用 `Given-When-Then` 語法定義情境。
- **輸出產出：** `feature_spec.gherkin`
  - **必須包含：** 正常路徑、邊界案例、錯誤處理。
  - **不得包含：** 資料庫結構描述、特定編碼實作細節。

### Phase 2：架構設計（骨架）

**角色：** 系統架構師
**目標：** 設計支援 Gherkin 情境所需的技術架構（語言無關）。

- **輸入：** `feature_spec.gherkin`（來自 Phase 1）
- **行動：**
  1. **掃描專案上下文：** 偵測技術棧、架構模式、命名慣例
  2. **名詞分析：** 從 Gherkin 提取名詞以建立資料模型設計
  3. **動詞分析：** 從 Gherkin 提取動詞以建立服務介面設計
  4. **生成繁體中文架構文件：** 語言無關的高階設計
- **輸出產出：** `docs/features/{feature}/architecture.md`
  - **內容：**
    - **專案上下文：** 技術棧、架構模式、命名慣例
    - **資料模型：** 列舉、實體（語言無關描述）
    - **服務介面：** 方法簽名、業務規則（語言無關描述）
    - **架構決策：** 設計理由與整合方式
    - **檔案結構規劃：** 實作檔案應放置的位置
  - **約束：** 此 Phase 不含實作細節，僅定義架構。

### Phase 3：實作（編碼）

**角色：** 資深工程師
**目標：** 依據架構文件實作程式碼以滿足 Gherkin 規格。

- **輸入：**
  - `feature_spec.gherkin`（測試/需求）
  - `docs/features/{feature}/architecture.md`（架構設計）
- **行動：**
  1. 依據專案技術棧實作資料模型
  2. 實作服務介面中定義的所有方法
  3. 確保程式碼中的每個邏輯分支對應 Gherkin 檔案中的情境
  4. 將檔案放置於 architecture.md 定義的位置
- **輸出產出：** 實作程式碼（依專案既有目錄結構）
  - **內容：** 完整功能的程式碼，遵循專案架構與命名慣例

### Phase 4：驗證（自我修正）

**角色：** QA 自動化
**目標：** 驗證 Phase 3 符合 Phase 1 的需求與 Phase 2 的架構。

- **輸入：** 
  - `feature_spec.gherkin`
  - `docs/features/{feature}/architecture.md`
  - 實作程式碼
- **行動：**
  - 驗證架構符合性（資料模型、服務介面、檔案位置）
  - 對照實作的程式碼執行 Gherkin 情境
- **輸出產出：** `docs/features/{feature}/conclusion.md`
- **邏輯：**
  - 如果**通過**：工作流程結束
  - 如果**失敗**：將錯誤回饋給 **Phase 3（工程師代理）** 重試

## 4. 插件的提示策略

生成插件時，確保每個代理的提示遵循以下指令：

- **對於規格代理：** "您是 PM。不要討論程式碼。僅使用 Gherkin 專注於使用者行為和業務規則。"
- **對於架構師代理：** "您是架構師。讀取 Gherkin。掃描專案上下文。定義語言無關的資料模型和服務介面。輸出繁體中文 Markdown 文件。不要實作，只定義架構。"
- **對於工程師代理：** "您是工程師。您必須嚴格遵循 architecture.md 定義的架構。依據專案技術棧實作程式碼。您的程式碼必須通過所有 Gherkin 情境。將檔案放置於 architecture.md 定義的位置。"
- **對於 QA 代理：** "驗證實作符合 Gherkin 規格與 architecture.md 架構。檢查資料模型、服務介面、檔案位置。生成驗證結論報告。"

## 5. 產出範例

**Phase 1 輸出（Gherkin）：**

```gherkin
Feature: VIP 折扣
  Scenario: 套用折扣
    Given 使用者是 VIP
    When 購買金額是 1000
    Then 最終價格應該是 800
```

**Phase 2 輸出（架構文件 - 繁中）：**

```markdown
# VIP 折扣 - 架構設計

## 1. 專案上下文
- 程式語言：Python
- 架構模式：Service Layer
- 命名慣例：snake_case

## 3. 資料模型
### UserType（列舉）
- VIP
- NORMAL

### DiscountResult（實體）
- final_price: 浮點數
- discount: 浮點數

## 4. 服務介面
### calculate_discount()
- 輸入：amount（浮點數）, user_type（UserType）
- 回傳：DiscountResult

## 7. 檔案結構規劃
src/
├── models/
│   └── discount_model.py
└── services/
    └── discount_service.py
```

**Phase 3 輸出（實作）：**

```python
# src/models/discount_model.py
from enum import Enum
from dataclasses import dataclass

class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

@dataclass
class DiscountResult:
    final_price: float
    discount: float

# src/services/discount_service.py
def calculate_discount(amount: float, user_type: UserType) -> DiscountResult:
    if user_type == UserType.VIP:
        discount = amount * 0.2
        return DiscountResult(amount - discount, discount)
    return DiscountResult(amount, 0)
```

**Phase 4 輸出（驗證結論）：**

```markdown
# VIP 折扣 - 驗證結論

## 3. 摘要
- 架構：2/2 通過
- 情境：1/1 通過
- **狀態：** ✅ 完成
```

## 6. 範例使用情境

以下是使用者觸發此工作流程插件時實際互動的樣子。

**使用者：**

> "我需要實作推薦獎金系統。如果使用者邀請朋友，且朋友完成超過 $50 的購買，邀請者獲得 100 點數。"

**代理（PM 角色 - 階段 1）：**

> "了解。我已為您的推薦系統起草行為規格（Gherkin）。
>
> **檔案：`referral.feature`**
>
> ```gherkin
> Feature: 推薦獎金系統
>   Scenario: 成功推薦
>     Given 使用者 A 邀請使用者 B
>     When 使用者 B 購買 60.0 美元
>     Then 使用者 A 獲得 100 獎勵點數
>
>   Scenario: 購買金額太低
>     Given 使用者 A 邀請使用者 B
>     When 使用者 B 購買 30.0 美元
>     Then 使用者 A 獲得 0 獎勵點數
> ```
>
> _進入結構設計..._"

**代理（架構師角色 - 階段 2）：**

> "根據上述 Gherkin，我已定義必要的資料模型和介面。
>
> **檔案：`structure.py`**
>
> ```python
> class Purchase(BaseModel):
>     amount: float
>     currency: str
>
> class User(BaseModel):
>     id: str
>     points: int
>
> class IReferralService(ABC):
>     @abstractmethod
>     def process_purchase(self, inviter: User, purchase: Purchase) -> User:
>         """計算並更新邀請者的點數。"""
>         pass
> ```
>
> _進入實作..._"

**代理（工程師角色 - 階段 3）：**

> "我已嚴格遵循結構和情境實作邏輯。
>
> **檔案：`impl.py`**
>
> ```python
> class ReferralService(IReferralService):
>     def process_purchase(self, inviter: User, purchase: Purchase) -> User:
>         if purchase.amount > 50:
>             inviter.points += 100
>         return inviter
> ```
>
> _執行驗證..._"

**代理（QA 角色 - 階段 4）：**

> "✅ **驗證通過。** 所有 Gherkin 情境對照實作成功通過。
>
> 這是您的最終檔案：`referral.feature`、`structure.py`、`impl.py`。"
