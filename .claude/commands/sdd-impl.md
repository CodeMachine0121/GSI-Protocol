---
description: 階段 3 - 在定義的結構內實作邏輯（工程師角色）
---

# SDD 階段 3：實作（血肉）

**角色：** 資深工程師

**目標：** 在定義的結構內實作業務邏輯，以滿足所有 Gherkin 情境。

## 輸入

提供兩個檔案：
1. Gherkin 規格：`features/<feature>.feature`
2. 結構定義：`structure/<feature>_structure.py`（或 `.ts`）

用法：`/sdd-impl features/<feature>.feature structure/<feature>_structure.py`

提示：{{prompt}}

## 您的職責約束

- 您是資深工程師，實作嚴格定義的規格。
- 您必須使用階段 2 的資料模型（結構檔案）。
- 您必須實作階段 2 的所有介面。
- 每個程式碼分支必須對應一個 Gherkin 情境。
- 您的程式碼必須滿足 Gherkin 檔案中的所有情境。
- 不要修改結構定義 - 只實作它們。

## 您的任務

1. **讀取兩個輸入檔案：**
   - Gherkin 檔案（需求/測試規格）
   - 結構檔案（資料模型和介面）

2. **建立具體實作：**
   - 將每個介面實作為具體類別
   - 使用提供的資料模型
   - 將每個 Gherkin 情境對應到程式碼邏輯

3. **實作對應：**
   - `Given` 陳述 → 設定/輸入參數
   - `When` 陳述 → 方法呼叫/動作
   - `Then` 陳述 → 回傳值/結果

4. **輸出格式：**

建立名為 `implementation/<feature_name>_impl.py`（或 `.ts`）的檔案：

**Python 範例：**
```python
"""
<功能名稱> 的實作
實作：structure/<feature_name>_structure.py
滿足：features/<feature_name>.feature

此模組包含結構模組中定義的
服務介面的具體實作。
"""

from structure.<feature_name>_structure import *

class <Service>Service(I<Service>Service):
    """
    I<Service>Service 的具體實作。
    實作 features/<feature_name>.feature 的所有情境
    """

    def action_name(self, param1: Type1, param2: Type2) -> ResultType:
        """
        實作滿足：
        - 情境："<情境 1 名稱>"
        - 情境："<情境 2 名稱>"
        """

        # 將 Gherkin Given 條件對應到程式碼邏輯
        if condition_from_scenario_1:
            # 將 Gherkin Then 對應到回傳值
            return result_for_scenario_1

        # 處理情境 2 的邊界情況
        elif condition_from_scenario_2:
            return result_for_scenario_2

        # 處理情境 3 的錯誤情況
        if invalid_condition:
            return ResultType(
                success=False,
                error_message="來自 Gherkin 的錯誤訊息"
            )

        # 預設/正常路徑
        return default_result

# 範例用法（可選，用於示範）
if __name__ == "__main__":
    service = <Service>Service()

    # 測試 Gherkin 的情境 1
    result = service.action_name(param1_value, param2_value)
    print(f"結果：{result}")
```

**TypeScript 範例：**
```typescript
/**
 * <功能名稱> 的實作
 * 實作：structure/<feature_name>_structure.ts
 * 滿足：features/<feature_name>.feature
 */

import {
  I<Service>Service,
  <Entity>,
  <Result>,
  <EntityType>
} from './structure/<feature_name>_structure';

export class <Service>Service implements I<Service>Service {
  /**
   * 實作滿足：
   * - 情境："<情境 1 名稱>"
   * - 情境："<情境 2 名稱>"
   */
  actionName(param1: Type1, param2: Type2): ResultType {
    // 將 Gherkin Given 條件對應到程式碼邏輯
    if (conditionFromScenario1) {
      // 將 Gherkin Then 對應到回傳值
      return resultForScenario1;
    }

    // 處理情境 2 的邊界情況
    if (conditionFromScenario2) {
      return resultForScenario2;
    }

    // 處理情境 3 的錯誤情況
    if (invalidCondition) {
      return {
        success: false,
        errorMessage: "來自 Gherkin 的錯誤訊息"
      };
    }

    // 預設/正常路徑
    return defaultResult;
  }
}
```

## 完整範例

**Gherkin（features/vip_discount.feature）：**
```gherkin
Feature: VIP 折扣
  Scenario: 對 VIP 使用者套用折扣
    Given 使用者是 VIP
    When 使用者購買 1000 美元
    Then 最終價格應該是 800 美元

  Scenario: 非 VIP 使用者無折扣
    Given 使用者是 NORMAL
    When 使用者購買 1000 美元
    Then 最終價格應該是 1000 美元
```

**結構（structure/vip_discount_structure.py）：**
```python
class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

class IDiscountService(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float, user_type: UserType) -> float:
        pass
```

**實作（implementation/vip_discount_impl.py）：**
```python
from structure.vip_discount_structure import *

class DiscountService(IDiscountService):
    """實作 VIP 折扣邏輯。"""

    def calculate_discount(self, amount: float, user_type: UserType) -> float:
        """
        滿足情境：
        - "對 VIP 使用者套用折扣"
        - "非 VIP 使用者無折扣"
        """
        # 情境 1：VIP 享 20% 折扣
        if user_type == UserType.VIP:
            return amount * 0.8

        # 情境 2：非 VIP 支付全額
        return amount

# 驗證
if __name__ == "__main__":
    service = DiscountService()

    # 測試情境 1
    assert service.calculate_discount(1000, UserType.VIP) == 800

    # 測試情境 2
    assert service.calculate_discount(1000, UserType.NORMAL) == 1000

    print("✅ 所有情境驗證成功")
```

## 品質檢查清單

完成前，確保：
- [ ] 結構檔案中的所有介面都已實作
- [ ] 結構檔案中的所有資料模型都已使用
- [ ] 每個 Gherkin 情境都有對應的程式碼邏輯
- [ ] 沒有修改結構定義
- [ ] 程式碼包含對應到 Gherkin 情境的註解
- [ ] 包含基本驗證/測試程式碼（可選但建議）
- [ ] 檔案已儲存在 `implementation/` 目錄

## 下一步

完成此階段後：
- 儲存實作檔案
- 使用以下指令進入階段 4：`/sdd-verify features/<feature>.feature implementation/<feature>_impl.py`
- 或在驗證前執行手動測試

現在讀取兩個輸入檔案並建立實作。
