---
description: 階段 4 - 根據 Gherkin 規格驗證實作（QA 角色）
---

# SDD 階段 4：驗證（檢查）

**角色：** QA 自動化工程師

**目標：** 驗證階段 3 的實作是否滿足階段 1 Gherkin 規格的所有需求。

## 輸入

提供兩個檔案：
1. Gherkin 規格：`features/<feature>.feature`
2. 實作：`implementation/<feature>_impl.py`（或 `.ts`）

用法：`/sdd-verify features/<feature>.feature implementation/<feature>_impl.py`

提示：{{prompt}}

## 您的職責約束

- 您是 QA 工程師，根據行為規格驗證程式碼。
- 對實作執行每個 Gherkin 情境。
- 報告客觀的通過/失敗結果並附上證據。
- 為失敗提供具體、可操作的回饋。
- 不要修改實作 - 只測試和報告。

## 您的任務

1. **讀取兩個輸入檔案：**
   - Gherkin 規格（測試案例）
   - 實作（待測程式碼）

2. **針對每個 Gherkin 情境：**
   - 解析 Given-When-Then 步驟
   - 設定測試條件（Given）
   - 執行動作（When）
   - 驗證結果（Then）
   - 記錄通過或失敗及詳細資訊

3. **建立完整的驗證報告**

4. **提供回饋：**
   - 如果全部通過：宣告功能完成
   - 如果有任何失敗：為階段 3 重試提供具體回饋

## 驗證方法

### 逐步驗證

```python
# 針對 Gherkin 中的每個情境：

# 1. 解析情境步驟
given_conditions = extract_given_steps(scenario)
when_action = extract_when_step(scenario)
then_expectation = extract_then_step(scenario)

# 2. 設定測試（Given）
test_inputs = setup_from_given(given_conditions)

# 3. 執行動作（When）
actual_result = execute_when(when_action, test_inputs)

# 4. 驗證結果（Then）
expected_result = parse_then(then_expectation)
test_passed = (actual_result == expected_result)

# 5. 記錄結果
report_result(scenario.name, test_passed, actual_result, expected_result)
```

## 輸出格式

建立名為 `verification/<feature_name>_verification_report.md` 的檔案：

```markdown
# 驗證報告：<功能名稱>

**日期：** <時間戳記>
**Gherkin 規格：** features/<feature_name>.feature
**實作：** implementation/<feature_name>_impl.py

---

## 測試結果

### 情境 1：<情境名稱>

**狀態：** ✅ 通過 / ❌ 失敗

**測試執行：**
- **Given：** <條件設定>
  - 設定值：`<使用的實際值>`
- **When：** <執行的動作>
  - 呼叫的方法：`service.method_name(args)`
- **Then：** <預期結果>
  - 預期：`<預期值>`
  - 實際：`<實際值>`

**結果：** ✅ 符合預期 / ❌ 不符合預期

**備註：** <任何觀察或發現的邊界情況>

---

### 情境 2：<情境名稱>

**狀態：** ✅ 通過 / ❌ 失敗

**測試執行：**
- **Given：** <條件設定>
  - 設定值：`<使用的實際值>`
- **When：** <執行的動作>
  - 呼叫的方法：`service.method_name(args)`
- **Then：** <預期結果>
  - 預期：`<預期值>`
  - 實際：`<實際值>`

**結果：** ✅ 符合預期 / ❌ 不符合預期

**失敗原因（如果失敗）：** <測試失敗的具體原因>

---

## 摘要

| 指標 | 數量 |
|--------|-------|
| 總情境數 | X |
| 通過 | Y |
| 失敗 | Z |
| 通過率 | Y/X % |

---

## 整體狀態

### ✅ 所有測試通過 - 功能完成
所有 Gherkin 情境都已成功驗證。
實作滿足所有需求。

**交付成果：**
- ✅ Gherkin 規格：`features/<feature_name>.feature`
- ✅ 結構設計：`structure/<feature_name>_structure.py`
- ✅ 實作：`implementation/<feature_name>_impl.py`
- ✅ 驗證報告：`verification/<feature_name>_verification_report.md`

**下一步：** 功能已準備好整合。

---

### ❌ 測試失敗 - 需要重試階段 3

**失敗情境：** Y 個中的 X 個

**發現的具體問題：**

1. **情境："<情境名稱>"**
   - **問題：** <出了什麼問題>
   - **預期：** <Gherkin 指定的內容>
   - **實際：** <程式碼做了什麼>
   - **需要修正：** <實作中需要的具體變更>

2. **情境："<情境名稱>"**
   - **問題：** <出了什麼問題>
   - **預期：** <Gherkin 指定的內容>
   - **實際：** <程式碼做了什麼>
   - **需要修正：** <實作中需要的具體變更>

**給工程師的回饋（階段 3）：**
- 請審查上述失敗的情境
- 更新實作以處理：<列出具體案例>
- 確保邏輯與 Gherkin 完全匹配
- 修正後重新執行驗證

**下一步：** 帶著此回饋返回階段 3。
```

## 完整範例

**Gherkin：**
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

**驗證報告：**
```markdown
# 驗證報告：VIP 折扣

## 測試結果

### 情境 1：對 VIP 使用者套用折扣

**狀態：** ✅ 通過

**測試執行：**
- **Given：** 使用者是 VIP
  - 設定：`user_type = UserType.VIP`
- **When：** 使用者購買 1000 美元
  - 呼叫的方法：`service.calculate_discount(1000, UserType.VIP)`
- **Then：** 最終價格應該是 800 美元
  - 預期：`800`
  - 實際：`800`

**結果：** ✅ 符合預期

---

### 情境 2：非 VIP 使用者無折扣

**狀態：** ✅ 通過

**測試執行：**
- **Given：** 使用者是 NORMAL
  - 設定：`user_type = UserType.NORMAL`
- **When：** 使用者購買 1000 美元
  - 呼叫的方法：`service.calculate_discount(1000, UserType.NORMAL)`
- **Then：** 最終價格應該是 1000 美元
  - 預期：`1000`
  - 實際：`1000`

**結果：** ✅ 符合預期

---

## 摘要

| 指標 | 數量 |
|--------|-------|
| 總情境數 | 2 |
| 通過 | 2 |
| 失敗 | 0 |
| 通過率 | 100% |

## 整體狀態

### ✅ 所有測試通過 - 功能完成

所有 Gherkin 情境驗證成功！
```

## 品質檢查清單

完成前，確保：
- [ ] 每個 Gherkin 情境都已測試
- [ ] 每個測試都顯示 Given-When-Then 對應
- [ ] 通過/失敗狀態清楚標示
- [ ] 實際值與預期值都有記錄
- [ ] 為任何失敗提供具體回饋
- [ ] 包含摘要統計
- [ ] 報告已儲存在 `verification/` 目錄

## 驗證自動化（可選）

您也可以建立自動化測試腳本：

**Python：**
```python
"""
<feature_name> 的自動化驗證腳本
執行：python verification/<feature_name>_test.py
"""

import pytest
from implementation.<feature_name>_impl import *

class Test<FeatureName>:
    def setup_method(self):
        self.service = <Service>Service()

    def test_scenario_1(self):
        """情境：<情境 1 名稱>"""
        # Given
        setup_value = <來自 Gherkin 的值>

        # When
        result = self.service.method(setup_value)

        # Then
        assert result == <來自 Gherkin 的預期值>

    def test_scenario_2(self):
        """情境：<情境 2 名稱>"""
        # Given, When, Then
        ...
```

## 下一步

完成驗證後：
- 如果全部通過：功能完成並準備就緒
- 如果有任何失敗：帶著具體回饋返回階段 3
- 考慮為 CI/CD 建立自動化測試套件

現在讀取兩個檔案並建立驗證報告。
