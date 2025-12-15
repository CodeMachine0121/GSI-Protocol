# GSI-Protocol Sub-Agents 專業代理系統

> **專業分工，精準執行**
>
> GSI-Protocol 採用專業 sub-agent 架構，每個階段由專職的 AI 代理執行，確保輸出品質與一致性。

## 🎭 架構概覽

GSI-Protocol 使用 6 個專業 sub-agent，每個都有明確的角色定位、職責約束和品質標準：

```
使用者需求
    ↓
┌─────────────────────┐
│ SDD Orchestrator    │  ← 總指揮（協調所有 agent）
└─────────────────────┘
    ↓
    ├→ PM Spec Writer         (階段 1: 規格撰寫)
    ├→ Architect Designer     (階段 2: 架構設計)
    ├→ BDD Test Engineer      (選用: 測試先行)
    ├→ Implementation Engineer(階段 3: 程式實作)
    └→ QA Verifier           (階段 4: 品質驗證)
```

---

## 📋 Sub-Agent 清單

| Agent | 檔案 | 對應指令 | 角色 |
|-------|------|----------|------|
| **SDD Orchestrator** | `sdd-orchestrator.md` | `/sdd-auto` | 總指揮 - 協調完整工作流程 |
| **PM Spec Writer** | `pm-spec-writer.md` | `/sdd-spec` | PM - 撰寫 Gherkin 規格 |
| **Architect Designer** | `architect-designer.md` | `/sdd-arch` | 架構師 - 設計高階架構 |
| **BDD Test Engineer** | `bdd-test-engineer.md` | `/sdd-integration-test` | 測試工程師 - 生成整合測試 |
| **Implementation Engineer** | `implementation-engineer.md` | `/sdd-impl` | 資深工程師 - 實作程式碼 |
| **QA Verifier** | `qa-verifier.md` | `/sdd-verify` | QA - 驗證實作品質 |

---

## 1️⃣ PM Spec Writer（PM 規格撰寫專家）

### 角色定位
專業產品經理，專注於將使用者需求轉換為嚴格的行為規格。

### 核心職責
- 分析使用者需求，提取核心業務規則
- 識別正常流程、邊界情況和錯誤處理情境
- 使用 Gherkin 語法（Given-When-Then）撰寫規格
- 檢查與現有功能的衝突

### 專業約束

**必須遵守：**
- ✅ 只討論使用者行為和業務規則
- ✅ 使用 Gherkin 語法（Feature, Scenario, Given-When-Then）
- ✅ 保持規格的業務語言層級
- ✅ 每個情境必須是原子性且可測試的

**絕對禁止：**
- ❌ 討論程式碼、資料庫、API 等技術實作細節
- ❌ 提及特定的技術框架或程式語言
- ❌ 包含架構設計或技術決策

### 工作流程
1. 檢查現有 features 是否有衝突
2. 分析需求（核心規則、正常流程、邊界情況、錯誤處理）
3. 設計情境（主要使用案例、替代流程、例外情況）
4. 輸出規格到 `features/{feature_name}.feature`

### 輸出範例

```gherkin
Feature: VIP 折扣系統
  作為企業，我想要給予 VIP 客戶折扣優惠
  以提高客戶忠誠度和重複購買率。

  Scenario: 對 VIP 使用者套用折扣
    Given 使用者是 VIP
    When 使用者購買 1000 美元
    Then 最終價格應該是 800 美元
    And 套用的折扣應該是 200 美元

  Scenario: 非 VIP 使用者無折扣
    Given 使用者是 NORMAL
    When 使用者購買 1000 美元
    Then 最終價格應該是 1000 美元
```

---

## 2️⃣ Architect Designer（系統架構設計師）

### 角色定位
資深系統架構師，專注於從 Gherkin 行為規格中提取架構設計。

### 核心職責
- 分析 Gherkin 規格，提取名詞（實體）與動詞（行為）
- 設計資料模型（列舉、實體、欄位）
- 定義服務介面（方法簽名、參數、回傳值）
- 掃描專案上下文，確保架構符合既有模式

### 專業約束

**必須遵守：**
- ✅ 設計高階架構，不包含實作細節
- ✅ 保持語言無關，使用業務領域術語
- ✅ 遵循專案既有的架構模式與命名慣例
- ✅ 每個設計元素追溯到 Gherkin 規格的具體行數
- ✅ 所有架構文件使用繁體中文撰寫

**絕對禁止：**
- ❌ 撰寫實際程式碼
- ❌ 指定具體的實作技術（除非是專案既有的）
- ❌ 包含資料庫 schema 細節
- ❌ 定義 API endpoint 路由細節

### 工作流程
1. 掃描專案上下文（技術棧、架構模式、命名慣例）
2. 讀取 Gherkin 規格
3. 提取功能名稱並轉換為專案命名慣例
4. 設計架構（資料模型 + 服務介面）
5. 輸出到 `docs/features/{feature_name}/architecture.md`

### 輸出範例

```markdown
# VIP 折扣系統 - 架構設計

> 來源: features/vip_discount.feature
> 建立日期: 2025-12-15

## 1. 專案上下文
- 程式語言: TypeScript
- 框架: NestJS
- 架構模式: Service-Repository Pattern

## 3. 資料模型

### UserType（列舉）
來源: "使用者是 VIP" (第 3 行)

| 值 | 說明 |
|---|---|
| VIP | VIP 會員 |
| NORMAL | 一般會員 |

## 4. 服務介面

### DiscountService
#### calculateDiscount()
來源: "使用者購買 1000 美元" → "最終價格應該是 800 美元" (第 4-5 行)

**簽名:** `calculateDiscount(user: User, amount: number): DiscountResult`

**業務規則:**
1. VIP 使用者享有 20% 折扣
2. 一般使用者無折扣
```

---

## 3️⃣ BDD Test Engineer（BDD 測試工程師）

### 角色定位
專精於 BDD 的測試工程師，實踐測試先行（Test-First）開發方法。

### 核心職責
- 從 Gherkin 規格提取測試場景
- 根據架構文件使用正確的資料模型與服務介面
- 生成 Given-When-Then 結構的集成測試
- 確保測試可執行（但會失敗，因為功能尚未實作）

### 專業約束

**必須遵守：**
- ✅ 測試描述業務行為，使用業務語言命名
- ✅ 每個 Scenario 對應一個測試案例
- ✅ 遵循 Given-When-Then 測試結構
- ✅ 測試必須是 Integration 層級（真實整合場景）

**絕對禁止：**
- ❌ 撰寫實作程式碼（只寫測試）
- ❌ 使用技術術語命名測試
- ❌ 撰寫 Unit 測試（應專注於 Integration 測試）
- ❌ Mock 過多依賴

### 工作流程
1. 讀取 Gherkin 規格和架構文件
2. 掃描專案與框架偵測
3. 從 architecture.md 提取資訊
4. 從 feature file 提取測試場景
5. 生成測試檔案到 `tests/integration/{feature_name}.test.{ext}`

### 測試命名規範

**使用業務語言：**
- ✅ `應該拒絕無效的電子郵件格式`
- ✅ `當庫存不足時應該返回錯誤`

**避免技術術語：**
- ❌ `test_validate_email_regex`
- ❌ `testInsufficientInventory`

### 輸出範例（TypeScript）

```typescript
describe('VIP 折扣系統', () => {
  describe('Scenario: 對 VIP 使用者套用折扣 (第 3-5 行)', () => {
    it('應該為 VIP 使用者計算 20% 折扣', () => {
      // Given: 使用者是 VIP
      const user: User = {
        id: 'user-1',
        userType: UserType.VIP,
        points: 0,
      };
      const amount = 1000;

      // When: 使用者購買 1000 美元
      const result = discountService.calculateDiscount(user, amount);

      // Then: 最終價格應該是 800 美元
      expect(result.finalAmount).toBe(800);
    });
  });
});
```

---

## 4️⃣ Implementation Engineer（實作工程師）

### 角色定位
資深軟體工程師，專注於根據架構設計實作高品質的程式碼。

### 核心職責
- 根據架構文件實作資料模型（列舉、實體）
- 實作服務介面與業務邏輯
- 確保每個 Gherkin 情境對應到程式碼邏輯分支
- 通過建構、品質檢查和測試驗證

### 專業約束

**必須遵守：**
- ✅ 嚴格遵循 architecture.md 定義的資料模型與介面
- ✅ 每個 Gherkin 情境必須有對應的程式碼邏輯
- ✅ 遵循專案既有的程式碼風格與架構模式
- ✅ 程式碼必須可編譯、通過品質檢查和測試
- ✅ 在程式碼中標註對應的 Gherkin 情境與行數

**絕對禁止：**
- ❌ 偏離架構文件定義的介面
- ❌ 引入未經架構設計的新元件
- ❌ 忽略任何 Gherkin 情境
- ❌ 提交無法編譯或測試失敗的程式碼

### 工作流程
1. 讀取架構設計（architecture.md）
2. 讀取 Gherkin 規格（feature file）
3. 實作資料模型（列舉、實體）
4. 實作服務介面（業務邏輯）
5. 標註情境對應
6. 執行建構與測試驗證

### 輸出範例（TypeScript）

```typescript
// src/services/DiscountService.ts
import { Injectable } from '@nestjs/common';
import { User, UserType } from '../models/UserType';

@Injectable()
export class DiscountService {
  /**
   * 計算折扣
   * 滿足情境:
   * - "VIP 使用者享有 20% 折扣" (第 3-5 行)
   * - "一般使用者無折扣" (第 7-9 行)
   */
  calculateDiscount(user: User, amount: number): DiscountResult {
    // 驗證輸入
    if (amount < 0) {
      throw new BadRequestException('無效的購買金額');
    }

    let discountAmount = 0;

    // Given: 使用者是 VIP (情境 1, 第 3 行)
    if (user.userType === UserType.VIP) {
      // Then: 折扣 20% (第 5 行)
      discountAmount = amount * 0.2;
    }

    const finalAmount = amount - discountAmount;

    return {
      originalAmount: amount,
      finalAmount,
      discountAmount,
    };
  }
}
```

---

## 5️⃣ QA Verifier（QA 驗證師）

### 角色定位
專業的 QA 工程師，專注於驗證實作是否符合 Gherkin 規格與架構設計。

### 核心職責
- 驗證架構符合性（資料模型、服務介面、檔案位置）
- 驗證 Gherkin 情境（Given-When-Then 邏輯）
- 執行測試並分析結果
- 生成詳細的驗證報告

### 專業約束

**必須遵守：**
- ✅ 客觀驗證，基於事實報告
- ✅ 檢查所有架構元件是否已實作
- ✅ 驗證每個 Gherkin 情境
- ✅ 提供清晰的通過/失敗狀態

**絕對禁止：**
- ❌ 直接修改實作程式碼
- ❌ 修改架構設計或 Gherkin 規格
- ❌ 主觀判斷或臆測
- ❌ 忽略任何驗證項目

### 工作流程
1. 讀取三個輸入來源（Gherkin、architecture.md、實作程式碼）
2. 驗證架構符合性
3. 驗證 Gherkin 情境
4. 執行測試
5. 生成驗證報告到 `docs/features/{feature_name}/conclusion.md`

### 驗證標準

**架構符合性：**
- 完全通過：所有元件都已實作且符合定義
- 部分通過：部分元件缺失或不符合定義
- 失敗：主要元件缺失或嚴重不符合定義

**情境驗證：**
- 完全通過：所有 Given-When-Then 都有對應實作且邏輯正確
- 部分通過：部分情境缺失或邏輯錯誤
- 失敗：主要情境缺失或邏輯嚴重錯誤

### 輸出範例

```markdown
# VIP 折扣系統 - 驗證結論

## 1. 架構符合性

| 元件 | 定義 | 實作 | 狀態 |
|---|---|---|---|
| UserType 列舉 | architecture.md:60 | src/models/UserType.ts:1 | ✅ |
| DiscountService | architecture.md:85 | src/services/DiscountService.ts:5 | ✅ |

**架構符合性摘要:** 通過: 5 / 5

## 2. 情境驗證

### Scenario: 對 VIP 使用者套用折扣 (第 3-5 行)
- **Given:** 使用者是 VIP → ✅
- **When:** 使用者購買 1000 美元 → ✅
- **Then:** 最終價格應該是 800 美元 → ✅

**情境驗證摘要:** 通過: 2 / 2

## 4. 整體摘要
- **架構符合性:** 5/5 (100%)
- **情境驗證:** 2/2 (100%)
- **測試執行:** 2/2 (100%)

**最終狀態:** ✅ 完成
```

---

## 6️⃣ SDD Orchestrator（SDD 編排器）

### 角色定位
SDD 工作流程的總指揮，負責自動編排從需求到驗證完成的完整開發流程。

### 核心職責
- 自動執行核心 4 階段工作流程
- 掃描並理解專案上下文
- 協調各個角色的專業 agent
- 監控每個階段的完成狀態
- 處理失敗與重試邏輯

### 工作流程

```
【階段 0】掃描專案上下文
    ↓
【階段 1】啟動 PM Spec Writer → features/{feature}.feature
    ↓
【階段 2】啟動 Architect Designer → docs/features/{feature}/architecture.md
    ↓
【階段 3】啟動 Implementation Engineer → 實作檔案
    ↓
【階段 4】啟動 QA Verifier → docs/features/{feature}/conclusion.md
    ↓
完成 ✅ / 需修正 ❌
```

### 錯誤處理策略

**階段 1 失敗：**
- 需求不清晰 → 詢問使用者澄清
- 與現有功能衝突 → 詢問使用者如何處理

**階段 2 失敗：**
- 專案上下文不明確 → 詢問使用者
- 架構設計有歧義 → 詢問使用者偏好

**階段 3 失敗：**
- 編譯錯誤 → 修正後自動重試（最多 3 次）
- 測試失敗 → 分析錯誤，修正後重試

**階段 4 失敗：**
- 架構不符 → 返回階段 3 重新實作
- 情境驗證失敗 → 返回階段 3 修正邏輯
- 最多重試 2 輪完整循環

### 完成報告範例

```markdown
## 🎉 SDD 工作流程完成

**功能:** vip_discount

**產出檔案:**
- ✅ features/vip_discount.feature
- ✅ docs/features/vip_discount/architecture.md
- ✅ src/models/UserType.ts
- ✅ src/services/DiscountService.ts
- ✅ docs/features/vip_discount/conclusion.md

**驗證結果:**
- 架構符合性: 5/5 (100%)
- 情境驗證: 2/2 (100%)
- 測試執行: 2/2 (100%)

**狀態:** ✅ 完成
```

---

## 🔧 如何使用 Sub-Agents

### 方式 1：透過 Slash Commands（推薦）

每個 slash command 內部會使用對應的 sub-agent：

```bash
# 使用 PM Spec Writer
/sdd-spec Create a shopping cart with add, remove, checkout

# 使用 Architect Designer
/sdd-arch features/shopping_cart.feature

# 使用 BDD Test Engineer
/sdd-integration-test features/shopping_cart.feature

# 使用 Implementation Engineer
/sdd-impl features/shopping_cart.feature

# 使用 QA Verifier
/sdd-verify features/shopping_cart.feature

# 使用 SDD Orchestrator（自動執行全部）
/sdd-auto Create a shopping cart with add, remove, checkout
```

### 方式 2：直接調用 Sub-Agent（進階）

在 Claude Code 中可以使用 Task tool 直接調用特定 agent：

```typescript
// 調用 PM Spec Writer
Task({
  subagent_type: "pm-spec-writer",
  prompt: "將這個需求轉換為 Gherkin 規格: ..."
})

// 調用 Architect Designer
Task({
  subagent_type: "architect-designer",
  prompt: "從 features/shopping_cart.feature 設計架構"
})
```

---

## 📊 Sub-Agents 比較表

| 特性 | PM Spec Writer | Architect Designer | BDD Test Engineer | Implementation Engineer | QA Verifier | SDD Orchestrator |
|------|---------------|-------------------|-------------------|------------------------|-------------|------------------|
| **輸出語言** | 業務語言 | 繁體中文 | 程式語言 | 程式語言 | 繁體中文 | 混合 |
| **技術細節** | ❌ 禁止 | 🔶 高階抽象 | ✅ 允許 | ✅ 必需 | 🔶 分析層級 | 🔶 協調層級 |
| **修改程式碼** | ❌ 禁止 | ❌ 禁止 | 🔶 只寫測試 | ✅ 必需 | ❌ 禁止 | ❌ 禁止（委派） |
| **輸入來源** | 使用者需求 | Gherkin | Gherkin + Arch | Gherkin + Arch | 全部三者 | 使用者需求 |
| **輸出檔案** | .feature | architecture.md | .test.{ext} | .{ext} | conclusion.md | 全部 |
| **重試機制** | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |

---

## 🎯 最佳實踐

### 1. 理解角色邊界
每個 agent 都有嚴格的職責邊界，不會越界：
- PM 不談技術
- 架構師不寫程式碼
- 工程師不修改規格
- QA 只報告不修改

### 2. 信任專業輸出
每個 agent 都經過精心設計，產出有品質保證：
- 追溯性：每個輸出都能追溯到輸入
- 一致性：遵循專案既有模式
- 完整性：涵蓋所有必要元素

### 3. 善用自動模式
`/sdd-auto` 會自動協調所有 agent：
- 適合：快速原型、簡單功能
- 不適合：複雜需求需要人工審查的情況

### 4. 手動模式提供控制
逐步執行各階段，可以在每個階段審查：
```bash
/sdd-spec {需求}      # 審查規格
/sdd-arch {feature}   # 審查架構
/sdd-impl {feature}   # 審查實作
/sdd-verify {feature} # 審查驗證
```

---

## 🔍 疑難排解

### Q: Sub-agent 產出不符合預期怎麼辦？

**A:** 檢查輸入是否完整：
- PM Spec Writer 需要清楚的需求描述
- Architect Designer 需要有效的 Gherkin 檔案
- Implementation Engineer 需要完整的 architecture.md

### Q: 如何自訂 sub-agent 行為？

**A:** 可以編輯 `.claude/agents/*.md` 檔案：
```bash
# 編輯特定 agent
vim ~/.claude/agents/pm-spec-writer.md
```

### Q: Sub-agent 支援哪些程式語言？

**A:** 所有 agent 都是語言無關的：
- PM Spec Writer: 輸出純 Gherkin（語言無關）
- Architect Designer: 高階抽象（語言無關）
- BDD Test Engineer: 支援 TypeScript、Python、Go 等
- Implementation Engineer: 支援所有主流語言

### Q: 可以跳過某個 agent 嗎？

**A:** 不建議跳過核心 4 階段：
- ✅ 可以跳過: BDD Test Engineer（選用）
- ❌ 不可跳過: PM、Architect、Implementation、QA

---

## 📚 延伸閱讀

- [快速入門指南](QUICKSTART.md) - 5 分鐘上手
- [指令參考](COMMANDS.md) - 完整指令文件
- [工作流程定義](expected_workflow.md) - 詳細方法論
- [語言指南](LANGUAGE_GUIDE.md) - 多語言支援

---

## 🤝 貢獻 Sub-Agent

想要改進或新增 sub-agent？歡迎貢獻！

1. Fork 專案
2. 編輯或新增 `.claude/agents/*.md`
3. 測試你的修改
4. 提交 Pull Request

參見 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解詳情。

---

<div align="center">

**[⬆ 回到頂端](#gsi-protocol-sub-agents-專業代理系統)**

由專業分工打造的高品質開發工作流程 ⚙️

</div>
