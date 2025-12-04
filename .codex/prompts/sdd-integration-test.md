---
description: BDD - 從 feature file 和架構文件生成 integration tests（測試先行）
---

# SDD-INTEGRATION-TEST: BDD Integration Tests

**輸入：** {{prompt}}  
格式：`<feature_file_path>`  
範例：`features/shopping_cart.feature`

**角色：** 協助開發者實踐 BDD（行為驅動開發）測試先行

**目標：** 
1. 讀取 feature file 和對應的 architecture.md
2. 生成 integration tests（先寫測試，後寫實作）
3. 測試會失敗（紅燈），等待實作後轉為通過（綠燈）

## 核心原則
- **BDD**：測試描述業務行為，非技術實作
- **Integration**：測試真實整合場景（API/DB/Service）
- **Scenario-driven**：每個 Scenario 對應一個測試案例
- **測試先行**：先寫測試（紅燈）→ 再實作（綠燈）

## 執行步驟

### 1. 讀取輸入檔案
```bash
# 讀取 feature file
cat <feature_file_path>

# 讀取對應的架構文件
cat docs/features/<feature_name>/architecture.md
```

### 2. 掃描專案與框架偵測
```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -name "*test*" -o -name "*spec*" | head -3
```

**框架優先順序：** architecture.md 指定 > 專案既有 > 預設
- **TypeScript**: Jest/Vitest + Supertest
- **Python**: pytest + httpx
- **Go**: testing + testify

### 3. 從 architecture.md 提取資訊
- 程式語言與框架
- 資料模型（實體、列舉）
- 服務介面（方法簽名）
- 檔案結構與路徑

### 4. 從 feature file 提取測試場景
- 每個 Scenario 對應一個測試案例
- 從 Given-When-Then 轉換為測試邏輯
- 保持業務語言描述

### 5. 測試結構（BDD 風格）

每個測試遵循 **Given-When-Then** 模式：
- **Given**: 準備測試資料與環境
- **When**: 執行被測試的行為
- **Then**: 驗證預期結果

**測試命名：** 使用 Scenario 描述，保持業務語言
- ✅ `應該拒絕無效的電子郵件格式`
- ✅ `當庫存不足時應該返回錯誤`
- ❌ `test_validate_email_regex`

## 測試要求
- [ ] 根據 architecture.md 使用正確的資料模型與介面
- [ ] 根據 feature file 的所有 Scenario 生成測試
- [ ] Given-When-Then 結構清晰
- [ ] 適當的 setup/teardown（例如：資料庫連線、測試資料清理）
- [ ] 可編譯/可執行（但會失敗，因為功能未實作）

## 生成測試檔案

**檔案位置：**
- 依據 architecture.md 指定的測試目錄
- 或依專案既有測試結構
- 預設：`tests/integration/<feature_name>.test.<ext>`

**測試內容包含：**
1. Import 對應的資料模型與服務介面（從 architecture.md）
2. 測試 setup/teardown
3. 每個 Scenario 一個測試函數
4. Given-When-Then 結構註解標示
5. 呼叫尚未實作的服務（會導致測試失敗/紅燈）

## 驗證
```bash
# 執行測試（預期失敗/紅燈，因為功能尚未實作）
npm test / pytest -v / go test -v
```

**預期結果：** 測試會失敗（紅燈），這是正常的。

## BDD 工作流程（測試先行）

1. **規格階段**：定義 feature file（`/sdd-spec`）
2. **架構階段**：設計技術架構（`/sdd-arch`）
3. **測試階段**（本指令）：生成 integration tests（🔴 紅燈）
4. **實作階段**：實作功能（`/sdd-impl`）
5. **驗證階段**：確認測試通過（`/sdd-verify` → 🟢 綠燈）

## 使用範例

```bash
# 先執行 sdd-spec 和 sdd-arch
/sdd-spec Create a shopping cart with add, remove, checkout
/sdd-arch features/shopping_cart.feature

# 生成 integration tests（測試會失敗/紅燈）
/sdd-bds features/shopping_cart.feature

# 實作功能
/sdd-impl features/shopping_cart.feature

# 驗證（測試應該通過/綠燈）
/sdd-verify features/shopping_cart.feature
```

開始讀取檔案並生成 integration tests。
