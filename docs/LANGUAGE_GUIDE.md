# SDD 語言指南

本指南展示 SDD 工作流程如何適應不同的程式語言，同時維持相同的核心方法論。

## 核心原則

**SDD 工作流程是語言無關的。** 雖然 Gherkin 規格（階段 1）在所有語言中保持一致，階段 2-4 會適應使用語言特定的慣用語和最佳實踐。

## 語言支援

### 第一層：完整支援並附範例
- **Python** - 使用 dataclasses、Pydantic 和 ABC 的範例
- **TypeScript** - 使用介面和型別的範例

### 第二層：文件化模式
- **Go** - 結構體和介面
- **Java** - 介面和 POJO
- **Rust** - 結構體和特徵
- **C#** - 介面和記錄

### 第三層：任何語言
方法論適用於任何支援以下特性的語言：
- 資料結構（結構體、類別、記錄）
- 型別定義（明確或隱式）
- 函式/方法定義

## 語言特定模式

### Python

**優勢：**
- 多種選擇：dataclasses、Pydantic、TypedDict
- ABC 用於介面
- 動態型別與型別提示

**階段 2 - 結構：**
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

class Status(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

@dataclass
class User:
    id: str
    status: Status

class IUserService(ABC):
    @abstractmethod
    def activate(self, user_id: str) -> User:
        pass
```

**何時使用：**
- 快速原型製作
- 資料科學應用
- 後端服務
- 腳本

**依賴項：**
```bash
pip install pydantic  # 如果使用 Pydantic 進行驗證
```

---

### TypeScript

**優勢：**
- 強大的編譯時型別檢查
- 基於介面的設計
- 優秀的 IDE 支援

**階段 2 - 結構：**
```typescript
enum Status {
  ACTIVE = "ACTIVE",
  INACTIVE = "INACTIVE"
}

interface User {
  id: string;
  status: Status;
}

interface IUserService {
  activate(userId: string): User;
}
```

**何時使用：**
- 前端應用
- Node.js 後端
- 全端網頁開發
- 需要強型別的專案

**依賴項：**
```bash
npm install typescript --save-dev
```

---

### Go

**優勢：**
- 簡單、明確的介面
- 內建並行處理
- 快速編譯和執行

**階段 2 - 結構：**
```go
package user

type Status string

const (
    StatusActive   Status = "ACTIVE"
    StatusInactive Status = "INACTIVE"
)

type User struct {
    ID     string
    Status Status
}

type UserService interface {
    Activate(userID string) (User, error)
}
```

**何時使用：**
- 微服務
- 雲端基礎設施
- CLI 工具
- 高效能後端

**不需要外部依賴**

---

### Java

**優勢：**
- 企業級就緒
- 強大的 OOP 支援
- 豐富的生態系統

**階段 2 - 結構：**
```java
public enum Status {
    ACTIVE,
    INACTIVE
}

public class User {
    private String id;
    private Status status;

    // 建構子、getter、setter
}

public interface IUserService {
    User activate(String userId);
}
```

**何時使用：**
- 企業應用
- Android 開發
- 大規模系統
- 遺留系統整合

**依賴項（Maven）：**
```xml
<!-- 視需要新增驗證函式庫 -->
```

---

### Rust

**優勢：**
- 無垃圾回收的記憶體安全
- 強大的型別系統
- 零成本抽象

**階段 2 - 結構：**
```rust
#[derive(Debug, Clone, PartialEq)]
pub enum Status {
    Active,
    Inactive,
}

#[derive(Debug, Clone)]
pub struct User {
    pub id: String,
    pub status: Status,
}

pub trait UserService {
    fn activate(&self, user_id: &str) -> Result<User, Error>;
}
```

**何時使用：**
- 系統程式設計
- WebAssembly
- 高效能應用
- 安全關鍵軟體

**依賴項（Cargo.toml）：**
```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
```

---

### C#

**優勢：**
- .NET 生態系統
- 現代語言特性
- Unity 遊戲開發

**階段 2 - 結構：**
```csharp
public enum Status
{
    Active,
    Inactive
}

public record User(string Id, Status Status);

public interface IUserService
{
    User Activate(string userId);
}
```

**何時使用：**
- .NET 應用
- Windows 桌面應用
- Unity 遊戲
- Azure 雲端服務

---

## 選擇正確語言

### 要問的問題

1. **您現有的程式碼庫是什麼？**
   - 使用相同語言以保持一致性

2. **您的團隊熟悉什麼？**
   - 利用現有專業知識

3. **您的效能需求是什麼？**
   - Go、Rust：高效能
   - Python、TypeScript：開發者生產力

4. **您的部署目標是什麼？**
   - 前端：TypeScript
   - 後端：任何（Python、Go、Java 等）
   - 行動裝置：Kotlin、Swift
   - WebAssembly：Rust

5. **您的型別安全需求是什麼？**
   - 嚴格：TypeScript、Rust、Go
   - 彈性：Python、Ruby

## 跨語言的 SDD 工作流程

### 階段 1：規格（Gherkin）
**所有語言始終相同**

```gherkin
Feature: 使用者啟用
  Scenario: 啟用非活動使用者
    Given 使用者狀態是 INACTIVE
    When 使用者被啟用
    Then 使用者狀態應該是 ACTIVE
```

### 階段 2：結構
**適應語言慣用語：**

| 語言 | 資料模型 | 介面 | 列舉 |
|----------|------------|-----------|------|
| Python | dataclass/@dataclass | ABC | Enum |
| TypeScript | interface | interface | enum |
| Go | struct | interface | const |
| Java | class | interface | enum |
| Rust | struct | trait | enum |
| C# | record | interface | enum |

### 階段 3：實作
**使用語言特定模式：**

| 語言 | 模式 | 錯誤處理 |
|----------|---------|----------------|
| Python | 類別實作 | try/except、Optional |
| TypeScript | 類別實作 | try/catch、undefined |
| Go | 結構體方法 | 錯誤回傳值 |
| Java | 類別實作 | try/catch、例外 |
| Rust | 實作特徵 | Result<T, E> |
| C# | 類別實作 | try/catch、可空 |

### 階段 4：驗證
**使用語言測試框架：**

| 語言 | 測試框架 | 斷言函式庫 |
|----------|---------------|-------------------|
| Python | pytest、unittest | assert、pytest |
| TypeScript | Jest、Mocha | expect、assert |
| Go | testing | testing.T |
| Java | JUnit | JUnit 斷言 |
| Rust | cargo test | assert! 巨集 |
| C# | xUnit、NUnit | Assert |

## 最佳實踐

### 通用原則

1. **強型別**：使用語言中最強的型別
2. **清晰命名**：遵循語言慣例（camelCase、snake_case 等）
3. **文件**：在註解中將程式碼對應回 Gherkin 情境
4. **驗證**：在邊界驗證，信任內部程式碼
5. **簡單性**：不要過度設計，只實作 Gherkin 指定的內容

### 語言特定建議

**Python：**
- 即使是選用的也使用型別提示
- 優先使用 dataclasses 而非普通類別
- 對驗證密集的程式碼考慮使用 Pydantic

**TypeScript：**
- 在 tsconfig.json 中啟用 `strict` 模式
- 對契約使用 `interface` 而非 `type`
- 利用聯合型別進行錯誤處理

**Go：**
- 保持介面小而專注
- 明確回傳錯誤
- 謹慎使用結構體嵌入

**Java：**
- 盡可能使用不可變物件
- 使用記錄類別（Java 14+）
- 對可空值使用 Optional

**Rust：**
- 擁抱 Result<T, E> 進行錯誤處理
- 使用 derive 巨集獲得常見特徵
- 利用借用而非複製

**C#：**
- 對不可變資料使用記錄
- 利用可空參考型別
- 對 I/O 操作使用 async/await

## 語言間遷移

### 相同功能，不同語言

SDD 工作流程使跨語言遷移系統化：

1. **Gherkin 保持不變**（階段 1）
2. **將資料模型對應**到新語言（階段 2）
3. **將介面對應**到新語言（階段 2）
4. **翻譯實作邏輯**（階段 3）
5. **根據相同 Gherkin 驗證**（階段 4）

### 範例：Python → TypeScript

**Python：**
```python
@dataclass
class User:
    id: str
    points: int
```

**TypeScript：**
```typescript
interface User {
  id: string;
  points: number;
}
```

**Gherkin 和邏輯保持一致！**

## 獲取幫助

使用新語言使用 SDD 時：

1. 查看 `examples/` 目錄中的類似語言
2. 審查語言特定的型別系統文件
3. 詢問 AI："使用慣用模式在 [語言] 中實作這個"
4. 從階段 1（Gherkin）開始 - 它始終相同
5. 讓 AI 將階段 2-4 適應您的語言

## 貢獻

幫助擴展語言支援：

1. 建立新語言的範例
2. 記錄語言特定模式
3. 分享最佳實踐
4. 回報語言特定適應的問題

詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

**記住：** SDD 的力量在於方法論，而非語言。首先專注於清晰的規格，然後讓實作適應您選擇的語言。
