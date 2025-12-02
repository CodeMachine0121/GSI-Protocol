# SDD Workflow Commands Reference

This document explains all available SDD workflow commands and when to use them.

## Command Overview

```
/sdd-auto           → Auto mode: Run all 4 phases automatically
/sdd-spec           → Phase 1: Generate Gherkin specification
/sdd-arch           → Phase 2: Design data models & interfaces
/sdd-impl           → Phase 3: Implement the logic
/sdd-verify         → Phase 4: Verify implementation
```

---

## `/sdd-auto` - Auto Mode

**Purpose:** Automatically execute all 4 phases of the SDD workflow from requirement to verified implementation.

**Usage:**
```bash
/sdd-auto <your complete requirement in any language>
```

**Examples:**
```bash
/sdd-auto Implement a VIP discount system in Python where VIP users get 20% off purchases over $100

/sdd-auto Create a referral bonus system in TypeScript. When an invited user makes a purchase over $50, the inviter gets 100 points

/sdd-auto Build a task manager in Go with create, update, delete, and list operations
```

**What it does:**
1. ✅ Generates Gherkin specification (Phase 1)
2. ✅ Designs data models and interfaces (Phase 2)
3. ✅ Implements the logic (Phase 3)
4. ✅ Verifies against specification (Phase 4)

**When to use:**
- ✅ Quick prototyping
- ✅ Simple, well-defined features
- ✅ Exploring ideas rapidly
- ✅ Learning the SDD methodology
- ✅ When you trust AI to handle the full flow

**When NOT to use:**
- ❌ Complex enterprise features requiring review
- ❌ Production-critical code
- ❌ When you need to manually adjust each phase
- ❌ When working with legacy code constraints

---

## `/sdd-spec` - Phase 1: Specification

**Purpose:** Generate a Gherkin specification from natural language requirements.

**Usage:**
```bash
/sdd-spec <your requirement description>
```

**Example:**
```bash
/sdd-spec I need a user authentication system with login, logout, and password reset
```

**Output:**
- Creates `features/<feature_name>.feature` with Gherkin scenarios
- Includes happy paths, edge cases, and error scenarios
- Pure behavioral specification (no technical details)

**When to use:**
- ✅ You want to define requirements clearly before coding
- ✅ You need stakeholder approval on behavior
- ✅ Starting with requirements documentation
- ✅ Want to review/refine specification before proceeding

---

## `/sdd-arch` - Phase 2: Architecture

**Purpose:** Design data models and service interfaces from Gherkin specification.

**Usage:**
```bash
/sdd-arch <path to .feature file>
```

**Example:**
```bash
/sdd-arch features/user_authentication.feature
```

**Output:**
- Creates `structure/<feature>_structure.<ext>` (language-specific)
- Defines data models (from nouns in Gherkin)
- Defines service interfaces (from verbs in Gherkin)
- No implementation logic, only structure

**When to use:**
- ✅ After Phase 1 completion
- ✅ You want to review the technical architecture
- ✅ Need to validate data models with team
- ✅ Want to ensure structure aligns with system design

---

## `/sdd-impl` - Phase 3: Implementation

**Purpose:** Implement the logic within the defined structure to satisfy Gherkin scenarios.

**Usage:**
```bash
/sdd-impl <path to .feature file> <path to structure file>
```

**Example:**
```bash
/sdd-impl features/user_authentication.feature structure/user_authentication_structure.py
```

**Output:**
- Creates `implementation/<feature>_impl.<ext>` (language-specific)
- Implements all interfaces from Phase 2
- Maps each Gherkin scenario to code logic
- Includes basic self-verification

**When to use:**
- ✅ After Phase 2 completion
- ✅ Structure has been reviewed and approved
- ✅ Ready to write actual business logic
- ✅ Want to see working code

---

## `/sdd-verify` - Phase 4: Verification

**Purpose:** Verify implementation against Gherkin specification.

**Usage:**
```bash
/sdd-verify <path to .feature file> <path to implementation file>
```

**Example:**
```bash
/sdd-verify features/user_authentication.feature implementation/user_authentication_impl.py
```

**Output:**
- Creates `verification/<feature>_verification_report.md`
- Tests each Gherkin scenario
- Reports Pass/Fail with evidence
- Provides feedback for failures

**When to use:**
- ✅ After Phase 3 completion
- ✅ Before committing code
- ✅ Need formal verification report
- ✅ Want to ensure all scenarios are covered

---

## Workflow Comparison

### Auto Mode Flow
```
User Request
     ↓
/sdd-auto <requirement>
     ↓
[All 4 Phases Execute Automatically]
     ↓
Complete Feature
```

**Pros:**
- ⚡ Fastest way to working code
- 🎯 Single command
- 🔄 Good for iterations

**Cons:**
- 🚫 No manual review between phases
- 🚫 May need rework if complex

---

### Manual Mode Flow
```
User Request
     ↓
/sdd-spec <requirement>
     ↓
[Review Gherkin]
     ↓
/sdd-arch features/spec.feature
     ↓
[Review Structure]
     ↓
/sdd-impl features/spec.feature structure/struct.py
     ↓
[Review Implementation]
     ↓
/sdd-verify features/spec.feature implementation/impl.py
     ↓
Complete Feature
```

**Pros:**
- 🎯 Full control at each phase
- 📋 Manual review checkpoints
- 🔍 Better for complex features

**Cons:**
- ⏱️ More time-consuming
- 🔢 Multiple commands needed

---

## Decision Matrix

| Scenario | Recommended Command |
|----------|-------------------|
| "Quick prototype for demo" | `/sdd-auto` |
| "Production feature with team review" | Manual phases |
| "Learning SDD methodology" | `/sdd-auto` first, then try manual |
| "API contract design" | `/sdd-spec` + `/sdd-arch` |
| "Complex business logic" | Manual phases |
| "Testing an idea" | `/sdd-auto` |
| "Migrating existing code" | `/sdd-spec` first |
| "Need stakeholder approval" | Manual phases |

---

## Language Support

All commands are **language-agnostic**. Specify your target language in the requirement:

```bash
# Python
/sdd-auto Create a shopping cart in Python

# TypeScript
/sdd-auto Implement user profiles in TypeScript

# Go
/sdd-auto Build an API gateway in Go

# Rust
/sdd-auto Create a parser in Rust

# Or let it auto-detect from project context
/sdd-auto Add authentication
```

---

## Tips for Success

### For Auto Mode (`/sdd-auto`)
1. **Be specific:** "Create a VIP discount system with 20% off for purchases over $100"
2. **Include edge cases:** "...and reject negative amounts"
3. **Specify language:** "...in TypeScript" (or let it detect)
4. **Keep it focused:** One feature at a time

### For Manual Mode
1. **Review each output:** Don't blindly proceed to next phase
2. **Refine as needed:** Edit generated files before next phase
3. **Verify early:** Don't wait until Phase 4 to test
4. **Document changes:** If you modify structure, update Gherkin

---

## Common Pitfalls

❌ **Using `/sdd-auto` for production-critical code without review**
✅ Use manual phases for important features

❌ **Skipping Phase 4 verification**
✅ Always verify, even if Phase 3 looks correct

❌ **Not specifying language for multi-language projects**
✅ Explicitly state target language

❌ **Running phases out of order**
✅ Follow the sequence: Spec → Arch → Impl → Verify

---

## Getting Help

- See [QUICKSTART.md](QUICKSTART.md) for hands-on guide
- See [LANGUAGE_GUIDE.md](LANGUAGE_GUIDE.md) for language-specific patterns
- See [README.md](README.md) for full documentation

---

**Quick Reference Card:**

```
Fast Prototype    → /sdd-auto <requirement>
Production Code   → /sdd-spec → /sdd-arch → /sdd-impl → /sdd-verify
Just Spec        → /sdd-spec <requirement>
Just Structure   → /sdd-arch <spec.feature>
Just Code        → /sdd-impl <spec> <structure>
Just Verify      → /sdd-verify <spec> <impl>
```
