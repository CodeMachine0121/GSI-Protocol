---
description: 自動執行完整 SDD 工作流程 (核心 4 階段)
---

# SDD 自動模式

**需求：** __PROMPT__

**目標：** 依序執行完整流程，從需求到驗證完成，無需手動介入

**核心理念：** 規格 → 架構 → Contract Tests → 實作（TDD）→ 驗證

---

## 開始前：掃描專案

```bash
ls -la | grep -E "package.json|requirements.txt|go.mod|pom.xml"
find . -type d -maxdepth 3 | grep -E "src|models|services" | head -10
```

**技術棧判斷優先順序：** Prompt 指定 > 專案既有 > 詢問使用者

---

## Phase 1: 規格（sdd-spec）

依照 `sdd-spec` skill 執行，輸出 `features/{feature_name}.feature`

---

## Phase 2: 架構（sdd-arch）

依照 `sdd-arch` skill 執行，輸出 `.gsi/{feature_name}/architecture.md`

---

## Phase 2.5: Contract Tests（sdd-test）

依照 `sdd-test` skill 執行，輸出 `{FeatureName}ContractTests.{ext}`

---

## Phase 3: 實作（sdd-impl）

依照 `sdd-impl` skill 執行，輸出 production code + unit tests

---

## Phase 4: 驗證（sdd-verify）

依照 `sdd-verify` skill 執行，輸出 `.gsi/{feature_name}/conclusion.md`

若 Phase 4 有失敗 → 返回 Phase 3 修正，再重新執行 Phase 4

---

## 輸出結構

```
project_root/
├── .gsi/{feature}/
│   ├── PRD.md                                    # Phase 1 (業務行為規格)
│   ├── {feature}.feature                         # Phase 1 (SpecBridge HTTP contract)
│   ├── architecture.md                           # Phase 2
│   └── conclusion.md                             # Phase 4
└── {專案目錄}/
    ├── {模型檔案}                                # Phase 3
    ├── {服務檔案}                                # Phase 3
    └── {unit test 檔案}                          # Phase 3 (TDD 產出)
```

開始執行 Phase 1。
