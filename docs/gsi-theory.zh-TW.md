# GSI-Protocol 理論

**語言**: [English](./gsi-theory.md) | **繁體中文**

## 什麼是 GSI？

GSI-Protocol 是一種系統化的軟體開發方法，強調**規格驅動、架構優先的開發**。GSI 縮寫代表此方法論的三大核心支柱：

- **G** - Gherkin（規格）
- **S** - Structure（架構）
- **I** - Implement（實作）

此方法確保每個功能都建立在明確需求、良好架構設計和經過驗證的實作之上。

---

## 三大支柱

### G - Gherkin（規格）

**目的**：從業務角度定義系統「應該做什麼」。

Gherkin 是一種業務可讀的領域特定語言，描述軟體行為而不涉及實作細節。它使用 **Given-When-Then** 格式來指定情境。

#### 為什麼選擇 Gherkin？

1. **業務可讀**：非技術利害關係人也能理解和驗證需求
2. **明確無歧義**：清晰的結構化格式減少誤解
3. **可測試**：每個情境都可以直接驗證
4. **語言無關**：獨立於程式語言或框架

#### 結構

```gherkin
Feature: 使用者認證
  作為一個使用者
  我想要用電子郵件和密碼登入
  以便我可以存取我的帳戶

  Scenario: 成功登入
    Given 已註冊使用者的電子郵件是 "user@example.com"
    And 密碼是 "SecurePass123"
    When 使用者提交登入憑證
    Then 使用者通過認證
    And 生成 session token

  Scenario: 密碼錯誤
    Given 已註冊使用者的電子郵件是 "user@example.com"
    And 密碼是 "WrongPassword"
    When 使用者提交登入憑證
    Then 認證失敗
    And 顯示錯誤訊息
```

#### 關鍵組成

- **Feature**：功能的高階描述
- **Scenario**：功能運作方式的具體範例
- **Given**：前置條件和初始狀態
- **When**：動作或事件
- **Then**：預期結果

#### 最佳實踐

- 專注於業務價值，而非技術實作
- 從使用者角度撰寫
- 涵蓋正常路徑、邊界情況和錯誤情境
- 保持情境之間的獨立性
- 使用具體範例

---

### S - Structure（架構）

**目的**：在高階層面定義系統「應該如何組織」。

Structure 代表連接業務需求（Gherkin）和程式碼實作之間的架構設計。它是**語言無關的**，專注於模型、介面和系統組織。

#### 為什麼架構優先？

1. **關注點分離**：元件之間有清晰的界線
2. **技術獨立**：設計可以用任何語言實作
3. **團隊協作**：在開始編碼前建立共同理解
4. **變更管理**：修改設計比修改程式碼容易
5. **品質保證**：架構可以在實作前審查

#### 從 Gherkin 到 Structure

轉換遵循系統化方法：

**名詞 → 資料模型**

- 使用者 → `User` 模型
- Session token → `SessionToken` 模型
- 憑證 → `Credentials` 模型

**動詞 → 服務介面**

- "提交登入憑證" → `AuthService.login()`
- "通過認證" → `AuthService.authenticate()`
- "生成 token" → `TokenService.generate()`

#### 架構文件結構

```markdown
# 功能名稱 - 架構設計

## 1. 專案上下文

- 語言：TypeScript
- 框架：Express.js
- 架構：分層架構（Controller → Service → Repository）
- 資料庫：PostgreSQL

## 2. 功能概述

此功能的高階描述

## 3. 資料模型

### User

- id: string (UUID)
- email: string (唯一，已驗證)
- passwordHash: string (bcrypt)
- createdAt: timestamp

### SessionToken

- token: string (JWT)
- userId: string (外鍵)
- expiresAt: timestamp

## 4. 服務介面

### AuthService

- login(email: string, password: string) → SessionToken
  - 驗證憑證
  - 生成 session token
  - 處理錯誤（無效憑證、找不到使用者）

### TokenService

- generate(userId: string) → string
- validate(token: string) → boolean

## 5. 架構決策

- 使用 JWT 進行無狀態認證
- 使用 bcrypt 雜湊密碼（成本因子：10）
- Token 過期時間：24 小時

## 6. 情境對應

| 情境         | 模型               | 服務                      | 方法                |
| ------------ | ------------------ | ------------------------- | ------------------- |
| 成功登入     | User, SessionToken | AuthService, TokenService | login(), generate() |
| 密碼錯誤     | User               | AuthService               | login()             |

## 7. 檔案結構

src/
├── models/
│   ├── User.ts
│   └── SessionToken.ts
├── services/
│   ├── AuthService.ts
│   └── TokenService.ts
└── repositories/
    └── UserRepository.ts
```

#### 核心原則

- **語言無關**：描述介面，而非實作
- **高階層次**：專注於元件，而非演算法
- **上下文感知**：適應現有專案結構
- **可追溯**：對應回 Gherkin 情境

---

### I - Implement（實作）

**目的**：基於架構建立實際程式碼。

Implementation 是將架構設計轉換為可執行程式碼的階段。工程師遵循架構文件以確保一致性和完整性。

#### 為什麼要架構驅動實作？

1. **清晰**：不需要猜測要建立什麼
2. **一致性**：遵循專案慣例
3. **完整性**：涵蓋所有情境
4. **可追溯性**：每個程式碼路徑都對應到 Gherkin 情境

#### 實作原則

**1. 遵循架構**

- 實作 architecture.md 中定義的內容
- 使用指定的資料模型和介面
- 將檔案放在指定位置

**2. 情境驅動程式碼**

每個 Gherkin 情境都應有對應的程式碼：

```typescript
// Scenario: 成功登入
async login(email: string, password: string): Promise<SessionToken> {
  // Given: 已註冊使用者
  const user = await this.userRepo.findByEmail(email);
  if (!user) {
    throw new Error('找不到使用者'); // 錯誤情境
  }

  // Given: 正確密碼
  const isValid = await bcrypt.compare(password, user.passwordHash);
  if (!isValid) {
    throw new Error('密碼無效'); // 密碼錯誤情境
  }

  // When: 提交憑證（呼叫此方法時已完成）

  // Then: 認證並生成 token
  const token = await this.tokenService.generate(user.id);
  return token;
}
```

**3. Given-When-Then 對應**

- **Given**：輸入驗證和前置條件檢查
- **When**：核心業務邏輯執行
- **Then**：返回值和副作用

**4. 處理所有情境**

確保程式碼涵蓋：

- 正常路徑（成功情境）
- 邊界情況（邊界條件）
- 錯誤情境（驗證失敗、例外）

#### 程式碼品質指南

- 遵循專案編碼標準
- 撰寫乾淨、可讀的程式碼
- 不要過度設計
- 只實作指定的內容
- 為所有情境添加錯誤處理

---

## GSI 工作流程

### 核心 4 階段流程

```
階段 1: Gherkin（PM 角色）
   ↓
階段 2: Structure（架構師角色）
   ↓
階段 3: Implement（工程師角色）
   ↓
階段 4: Verification（QA 角色）
```

### 階段細節

#### 階段 1: 規格（PM）

**輸入**：使用者需求
**輸出**：`features/{feature}.feature`
**角色**：產品經理

PM 將業務需求轉換為 Gherkin 情境，專注於：

- 功能應該做什麼
- 業務規則和限制
- 邊界情況和錯誤條件
- 使用者觀點和價值

#### 階段 2: 架構（架構師）

**輸入**：Gherkin 規格
**輸出**：`docs/features/{feature}/architecture.md`
**角色**：軟體架構師

架構師設計技術結構：

- 分析專案上下文（技術棧、模式）
- 從 Gherkin 名詞提取資料模型
- 從 Gherkin 動詞定義服務介面
- 建立語言無關的設計
- 規劃檔案結構

#### 階段 3: 實作（工程師）

**輸入**：架構設計 + Gherkin 規格
**輸出**：原始碼檔案
**角色**：軟體工程師

工程師實作設計：

- 精確遵循架構文件
- 確保涵蓋所有 Gherkin 情境
- 將檔案放在指定位置
- 撰寫乾淨、可投產的程式碼

#### 階段 4: 驗證（QA）

**輸入**：Gherkin + 架構 + 實作
**輸出**：`docs/features/{feature}/conclusion.md`
**角色**：品質保證

QA 驗證：

- 架構符合性（模型、介面、檔案）
- 情境覆蓋率（所有 Given-When-Then 路徑）
- 實作正確性
- 生成通過/失敗報告

---

## 選用：整合測試

### BDD 整合測試（選用階段）

**指令**：`/sdd-integration-test`
**使用時機**：測試驅動開發（TDD）工作流程

整合測試是**選用的**，但強烈建議用於：

- 關鍵業務邏輯
- 複雜情境
- 測試驅動開發
- 持續整合管線

#### 測試優先工作流程

```
/sdd-spec <需求>
   ↓
/sdd-arch features/feature.feature
   ↓
/sdd-integration-test features/feature.feature  ← 選用但建議
   ↓
/sdd-impl features/feature.feature
   ↓
/sdd-verify features/feature.feature
```

#### 生成的測試

整合測試直接從 Gherkin 情境生成：

```typescript
describe("使用者認證", () => {
  describe("情境：成功登入", () => {
    it("應該認證使用者並生成 token", async () => {
      // Given: 已註冊使用者
      const user = await createTestUser({
        email: "user@example.com",
        password: "SecurePass123",
      });

      // When: 提交登入憑證
      const result = await authService.login(
        "user@example.com",
        "SecurePass123",
      );

      // Then: 通過認證並取得 token
      expect(result.token).toBeDefined();
      expect(result.userId).toBe(user.id);
    });
  });

  describe("情境：密碼錯誤", () => {
    it("應該認證失敗", async () => {
      // Given: 已註冊使用者
      await createTestUser({
        email: "user@example.com",
        password: "SecurePass123",
      });

      // When: 提交錯誤密碼
      const promise = authService.login("user@example.com", "WrongPassword");

      // Then: 認證失敗
      await expect(promise).rejects.toThrow("密碼無效");
    });
  });
});
```

#### 整合測試的好處

1. **可執行規格**：Gherkin 變成可執行測試
2. **防止迴歸**：偵測破壞性變更
3. **文件**：測試作為使用範例
4. **信心**：端到端驗證系統行為

#### 何時可以跳過整合測試

- 簡單的 CRUD 操作
- 概念驗證專案
- 快速原型開發
- 時間受限的情況

---

## GSI-Protocol 的核心優勢

### 1. **透過分離獲得清晰**

每個階段都有明確目的：

- Gherkin：業務需求
- Structure：技術設計
- Implementation：程式碼

### 2. **語言無關**

相同的 Gherkin 和架構可以用以下語言實作：

- TypeScript、Python、Go、Java、C# 等
- 任何框架或技術棧

### 3. **團隊協作**

- PM 專注於業務價值
- 架構師設計系統結構
- 工程師清晰地實作
- QA 驗證完整性

### 4. **品質保證**

- 規格可測試
- 架構可審查
- 實作可驗證
- 涵蓋所有情境

### 5. **可維護性**

- 清晰的文件（Gherkin + 架構）
- 可追溯的需求
- 一致的程式碼結構
- 新團隊成員容易上手

### 6. **靈活性**

- TDD 的選用整合測試
- 手動或自動工作流程
- 專案感知適應

---

## 與其他方法論的比較

### GSI vs 傳統開發

| 面向     | 傳統                   | GSI-Protocol          |
| -------- | ---------------------- | --------------------- |
| 需求     | 常常不清楚或變動       | 清晰的 Gherkin 情境   |
| 架構     | 有時跳過或非正式       | 明確、有文件的設計    |
| 實作     | 直接從需求開始         | 由架構引導            |
| 驗證     | 手動測試               | 自動化情境驗證        |
| 文件     | 事後撰寫（如果有的話） | 開發過程中生成        |

### GSI vs BDD（行為驅動開發）

| 面向   | BDD        | GSI-Protocol         |
| ------ | ---------- | -------------------- |
| Gherkin | 是         | 是（G）              |
| 架構   | 未強調     | 核心支柱（S）        |
| 實作   | 測試驅動   | 架構驅動             |
| 測試   | 必需       | 選用（整合測試）     |

GSI-Protocol 可以視為 **BDD + 架構優先設計**，其中架構階段連接需求和實作。

---

## 最佳實踐

### 1. 從 Gherkin 開始

在思考程式碼之前，始終從清晰的業務情境開始。

### 2. 審查架構

在實作前讓團隊審查架構。

### 3. 精確遵循架構

實作期間不要偏離設計。

### 4. 驗證每個情境

確保程式碼涵蓋所有 Given-When-Then 路徑。

### 5. 失敗時迭代

如果驗證失敗，修正並重新驗證直到所有情境通過。

### 6. 明智使用整合測試

為關鍵功能添加測試，但不要過度測試簡單操作。

### 7. 保持文件更新

Gherkin 和架構應始終反映當前實作。

---

## 結論

GSI-Protocol 提供了一個結構化、可重複的軟體建構流程：

- 從清晰的業務需求開始（Gherkin）
- 設計周詳的架構（Structure）
- 精確實作（Implement）
- 驗證完整性（Verification）
- 選擇性包含整合測試（TDD）

透過遵循 **G-S-I** 支柱，團隊可以建構高品質的軟體，從需求到程式碼具有清晰的可追溯性，同時保持適應任何技術棧的靈活性。

選用的整合測試階段為實踐測試驅動開發的團隊增強工作流程，但核心 4 階段流程仍然是 GSI-Protocol 的基礎。
