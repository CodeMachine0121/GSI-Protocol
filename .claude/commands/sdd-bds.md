---
description: BDD × TDD - 從 feature 生成紅燈 integration tests
---

# SDD-BDS: BDD × TDD 紅燈測試

**需求：** {{prompt}}

**角色：** 協助開發者實踐 BDD（行為驅動開發）× TDD（測試驅動開發）

**目標：** 
1. 從 feature 需求生成可編譯但會失敗的 integration tests（紅燈）
2. 驅動開發流程：紅燈 → 綠燈 → 重構

## 核心原則
- **BDD**：測試描述業務行為，非技術實作
- **TDD**：測試先行、可編譯、會失敗（紅燈）
- **Integration**：測試真實整合場景（API/DB/Service）

## 執行步驟

### 1. 掃描專案與框架偵測
```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -name "*test*" -o -name "*spec*" | head -3
```

**框架優先順序：** 使用者指定 > 專案既有 > 預設
- **TypeScript**: Jest/Vitest + Supertest
- **Python**: pytest + httpx
- **Go**: testing + testify

### 2. 測試場景（至少 3 個）
- 正常流程
- 邊界情況
- 錯誤處理

### 3. 測試結構（BDD 風格）

每個測試遵循 **Arrange-Act-Assert** 模式：
- **Arrange**: 準備測試資料與環境
- **Act**: 執行被測試的行為
- **Assert**: 驗證預期結果

**測試命名：** 描述業務行為，非技術細節
- ✅ `應該拒絕無效的電子郵件格式`
- ✅ `當庫存不足時應該返回錯誤`
- ❌ `test_validate_email_regex`

## 測試要求
- [ ] 可編譯通過
- [ ] 執行會失敗（功能未實作）
- [ ] 涵蓋正常/邊界/錯誤
- [ ] Arrange-Act-Assert 結構
- [ ] setup/teardown

## 驗證
```bash
# 編譯檢查
npx tsc --noEmit  # TS
python -m py_compile tests/**/*.py  # Python
go build ./...  # Go

# 執行測試（預期失敗/紅燈）
npm test / pytest -v / go test -v
```

## BDD × TDD 工作流程

1. **紅燈階段**（本指令）：生成描述業務行為的失敗測試
2. **綠燈階段**：實作最小程式碼讓測試通過（可用 `/sdd-impl`）
3. **重構階段**：優化程式碼，保持測試通過

## 輸出位置
`tests/integration/{feature}.test.{ext}` 或依專案既有結構

開始生成紅燈測試。
