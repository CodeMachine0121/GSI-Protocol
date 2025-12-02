---
description: Phase 3 - 根據架構設計實作程式碼，滿足 Gherkin 規格
---

# SDD Phase 3: 實作

**角色：** 資深工程師  
**輸入：** Gherkin 規格檔案 {{prompt}}  
**前置條件：** 已完成 Phase 2，存在 `docs/features/{feature_name}/architecture.md`  
**輸出：** 實作程式碼於專案既有目錄結構

## 核心原則

- **遵循架構**：嚴格依照 architecture.md 定義的資料模型與服務介面
- **情境驅動**：每個 Gherkin 情境對應到程式碼邏輯分支
- **專案整合**：檔案放置於專案既有目錄結構
- **可測試性**：程式碼可直接用於驗證 Gherkin 情境

## 執行步驟

### 1. 讀取架構設計

從 `docs/features/{feature_name}/architecture.md` 讀取：
- 專案上下文（語言、框架、架構模式）
- 資料模型定義（列舉、實體）
- 服務介面定義（方法簽名、參數、回傳值）
- 情境對應關係

### 2. 實作元件

依據架構文件實作：

**資料模型：**
- 實作列舉/常數
- 實作核心實體
- 加入資料驗證（依框架）

**服務介面：**
- 實作服務類別/介面
- 實作所有方法
- 每個方法對應 Gherkin 情境

**情境對應：**
- `Given` → 設定/輸入參數
- `When` → 方法呼叫
- `Then` → 回傳值/驗證

### 3. 儲存檔案

依據 architecture.md 的「檔案結構」章節，將檔案放置於正確位置

## 實作範例

### TypeScript + NestJS

**資料模型 (src/models/UserType.ts):**
```typescript
export enum UserType {
  VIP = 'VIP',
  NORMAL = 'NORMAL',
}

export interface User {
  id: string;
  userType: UserType;
  points: number;
}
```

**服務實作 (src/services/DiscountService.ts):**
```typescript
import { Injectable } from '@nestjs/common';
import { User, UserType } from '../models/UserType';

@Injectable()
export class DiscountService {
  /**
   * 滿足情境：
   * - "VIP 使用者享有 20% 折扣" (第 5-8 行)
   * - "一般使用者無折扣" (第 10-13 行)
   */
  calculateDiscount(user: User, amount: number): number {
    // Given: 使用者是 VIP (情境 1)
    if (user.userType === UserType.VIP) {
      // Then: 折扣 20%
      return amount * 0.8;
    }

    // Given: 使用者是 NORMAL (情境 2)
    // Then: 無折扣
    return amount;
  }
}
```

### Python + FastAPI

**資料模型 (src/models/user.py):**
```python
from enum import Enum
from pydantic import BaseModel

class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

class User(BaseModel):
    id: str
    user_type: UserType
    points: int = 0
```

**服務實作 (src/services/discount_service.py):**
```python
from src.models.user import User, UserType

class DiscountService:
    """
    滿足情境：
    - "VIP 使用者享有 20% 折扣" (第 5-8 行)
    - "一般使用者無折扣" (第 10-13 行)
    """
    def calculate_discount(self, user: User, amount: float) -> float:
        # Given: 使用者是 VIP (情境 1)
        if user.user_type == UserType.VIP:
            # Then: 折扣 20%
            return amount * 0.8
        
        # Given: 使用者是 NORMAL (情境 2)
        # Then: 無折扣
        return amount
```

## 程式碼撰寫要求

### 註解標註
- 每個方法標註對應的 Gherkin 情境與行數
- 關鍵邏輯註明對應的 Given/When/Then

### 錯誤處理
依據專案既有模式處理異常：
```typescript
// TypeScript
if (!user) {
  throw new BadRequestException('使用者不存在');
}
```

```python
# Python
if not user:
    raise ValueError("使用者不存在")
```

### 驗證邏輯
依據框架加入資料驗證（如需要）

## 品質檢查

- [ ] 已讀取 `docs/features/{feature_name}/architecture.md`
- [ ] 所有資料模型已實作
- [ ] 所有服務介面已實作
- [ ] 每個 Gherkin 情境都有對應程式碼邏輯
- [ ] 程式碼符合專案既有命名慣例與架構模式
- [ ] 檔案儲存至正確位置（依 architecture.md）
- [ ] 包含 Gherkin 情境追溯註解

## 執行流程

1. 讀取 `docs/features/{feature_name}/architecture.md`
2. 讀取 `features/{feature_name}.feature`
3. 依據架構文件與專案上下文實作程式碼
4. 將檔案儲存至專案既有目錄結構
5. 回報已建立的檔案清單

## 下一步

完成後可進行：
- 執行專案既有測試框架驗證
- 進入 Phase 4：測試驗證（如有定義）
- 整合至專案主要程式碼
