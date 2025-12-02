---
description: Run the complete SDD (Specification-Driven Development) workflow - all 4 phases from requirement to verification
---

# SDD Workflow - Complete 4-Phase Process

You are now executing the **Specification-Driven Development (SDD)** workflow. This is a strict 4-phase process that transforms user requirements into verified, production-ready code.

## Core Philosophy

**"Spec -> Structure -> Implementation"**

Isolate business logic, technical architecture, and coding into distinct phases to minimize hallucination and maximize precision.

**This workflow is language and framework agnostic.** The user may request implementation in any programming language (Python, TypeScript, Go, Java, Rust, etc.) and any framework. You should adapt the output format accordingly while maintaining the SDD principles.

## User's Requirement

The user has requested: {{prompt}}

## Language Detection

**IMPORTANT:** Before starting, determine the target language:

1. If the user explicitly specifies a language in their prompt (e.g., "in Python", "using TypeScript"), use that
2. If the project context suggests a language (check existing files), use that
3. If unclear, ask the user which language they prefer
4. Default to Python if no preference is expressed

Once determined, use that language consistently through all phases.

## Your Task

Execute all 4 phases sequentially:

### Phase 1: Specification (The Soul)

**Role:** Product Manager
**Constraints:**

- You are a PM. Do NOT discuss code, databases, or technical implementation.
- Focus SOLELY on user behavior and business rules.
- Use Gherkin syntax (Given-When-Then).
- Must include: Happy paths, Edge cases, Error handling.

**Action:**

1. Analyze the user's requirement for business rules and edge cases
2. Create a `.feature` file with comprehensive Gherkin scenarios
3. Save it as `features/<feature_name>.feature`

**Output Format:**

```gherkin
Feature: <Feature Name>
  Scenario: <Scenario Name>
    Given <precondition>
    When <action>
    Then <expected outcome>
```

### Phase 2: Structure (The Skeleton)

**Role:** System Architect
**Constraints:**

- You are an Architect. Read the Gherkin from Phase 1.
- Define ONLY data models and interfaces.
- NO business logic implementation allowed.
- Extract nouns from Gherkin → Data Models
- Extract verbs from Gherkin → Service Interfaces

**Action:**

1. Read the Gherkin file created in Phase 1
2. Perform noun analysis to create Data Models (Pydantic/TypeScript interfaces)
3. Perform verb analysis to create Service Interfaces (Abstract classes)
4. Save as `structure/<feature_name>_structure.py` (or `.ts`)

**Output Format (adapt to target language):**

Language-agnostic principles:

- Extract nouns → Create typed data structures
- Extract verbs → Create interface/protocol definitions
- Use strong typing wherever possible
- Document which Gherkin scenario each element satisfies

Choose the appropriate idiom for the target language:

- **Python:** dataclasses, Pydantic, or TypedDict + ABC
- **TypeScript:** interfaces and types
- **Go:** structs and interfaces
- **Java:** interfaces and POJOs
- **Rust:** structs and traits
- **C#:** interfaces and classes

Example structure (Python with dataclasses):

```python
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum

class EntityType(str, Enum):
    VALUE_1 = "VALUE_1"

@dataclass
class Entity:
    field1: str
    field2: float

class IServiceInterface(ABC):
    @abstractmethod
    def method_name(self, param: Entity) -> Result:
        """From Scenario: '<name>'"""
        pass
```

### Phase 3: Implementation (The Flesh)

**Role:** Senior Engineer
**Constraints:**

- You are an Engineer. You MUST use the Data Models from Phase 2.
- Implement the logic for the Interfaces from Phase 2.
- Every code branch must correspond to a Gherkin scenario.
- Your code MUST pass all scenarios from Phase 1.

**Action:**

1. Read the Gherkin file from Phase 1
2. Read the structure file from Phase 2
3. Implement the concrete classes that fulfill the interfaces
4. Ensure all Gherkin scenarios are satisfied
5. Save as `implementation/<feature_name>_impl.py` (or `.ts`)

**Output Format (adapt to target language):**

Implement the interfaces/traits defined in Phase 2 using the idioms of your target language:

- Map Gherkin `Given` → Setup/preconditions
- Map Gherkin `When` → Method execution
- Map Gherkin `Then` → Return values/outcomes

Example (Python):

```python
from structure import IServiceInterface, Entity, Result

class ServiceImpl(IServiceInterface):
    def method_name(self, param: Entity) -> Result:
        # Scenario 1: <name>
        if condition_from_scenario:
            return Result(value=expected)
        # Scenario 2: <name>
        return Result(value=other)
```

Example (TypeScript):

```typescript
import { IServiceInterface, Entity, Result } from "./structure";

export class ServiceImpl implements IServiceInterface {
  methodName(param: Entity): Result {
    // Scenario 1: <name>
    if (conditionFromScenario) {
      return { value: expected };
    }
    return { value: other };
  }
}
```

Example (Go):

```go
type ServiceImpl struct {}

func (s *ServiceImpl) MethodName(param Entity) Result {
    // Scenario 1: <name>
    if conditionFromScenario {
        return Result{Value: expected}
    }
    return Result{Value: other}
}
```

### Phase 4: Verification (The Check)

**Role:** QA Automation
**Constraints:**

- Verify that Phase 3 implementation meets Phase 1 requirements.
- Run each Gherkin scenario against the implementation.
- Report Pass/Fail with detailed feedback.

**Action:**

1. Read the Gherkin file from Phase 1
2. Read the implementation from Phase 3
3. For each Gherkin scenario:
   - Set up the Given conditions
   - Execute the When action
   - Verify the Then outcome
4. Create a verification report
5. If failures exist, provide specific feedback for Phase 3 retry

**Output Format:**

```markdown
# Verification Report

## Test Results

### Scenario: <Name>

- Status: ✅ PASS / ❌ FAIL
- Given: <condition setup>
- When: <action executed>
- Then: <expected vs actual>
- Notes: <any discrepancies>

## Summary

- Total Scenarios: X
- Passed: Y
- Failed: Z

## Next Steps

[If all pass]: ✅ Feature Complete
[If any fail]: Feedback for Phase 3 retry: <specific issues>
```

## Execution Instructions

1. **Start with Phase 1**: Create the Gherkin specification
2. **Wait for user confirmation** (optional, but recommended for complex features)
3. **Proceed to Phase 2**: Design the structure
4. **Proceed to Phase 3**: Implement the logic
5. **Complete with Phase 4**: Verify the implementation
6. **If Phase 4 fails**: Return to Phase 3 with specific feedback

## Important Reminders

- Create a todo list to track all 4 phases
- Mark each phase as completed before moving to the next
- Save all artifacts in the specified directory structure
- Do NOT skip phases or merge them together
- Each phase has strict input/output contracts

Now begin with Phase 1: Requirement Specification.
