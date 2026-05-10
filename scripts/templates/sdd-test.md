---
description: ⚠️ 已由 SpecBridge 取代，不再是標準流程的一部分
---

# SDD-TEST（已棄用）

> **此階段已從標準 SDD 工作流程中移除。**
>
> Contract 驗證現在由 **SpecBridge** 負責：
> - Phase 1（sdd-spec）生成 `.gsi/{feature}/*.feature`（SpecBridge HTTP contract）
> - Phase 4（sdd-verify）執行 `specbridge verify` 驗證 live API
>
> Unit tests 在 Phase 3（sdd-impl）中以 TDD 方式隨 production code 一同產出。
