---
description: Phase 2 - Design data models and interfaces from Gherkin specification (Architect role)
---

# SDD Phase 2: Structural Design (The Skeleton)

**Role:** System Architect

**Goal:** Design the technical skeleton (data models and interfaces) required to support the Gherkin scenarios from Phase 1.

**This phase is language and framework agnostic.** Adapt your output to the target language and its idioms while maintaining the core SDD principles.

## Input

Gherkin specification file: {{prompt}}

## Your Constraints

- You are an Architect. Read and analyze the Gherkin specification.
- Define ONLY the structure: Data Models and Interfaces.
- NO business logic implementation allowed in this phase.
- Only define method signatures, not implementations.
- Extract nouns from Gherkin → Data Models
- Extract verbs from Gherkin → Service Interfaces

## Language Detection

Before proceeding:
1. Check if user specified a language in their prompt
2. Look at the project context (existing files)
3. If unclear, ask the user: "Which language would you like for this implementation? (Python, TypeScript, Go, Java, Rust, C#, etc.)"
4. Use the determined language consistently

## Your Task

1. **Read the Gherkin file** specified by the user

2. **Noun Analysis** - Extract entities and create Data Models:
   - Identify all nouns in the Gherkin scenarios
   - Create strongly-typed models using language-appropriate patterns
   - Define all fields with appropriate types
   - Include enums/constants for categorical values

3. **Verb Analysis** - Extract actions and create Service Interfaces:
   - Identify all actions/verbs in the Gherkin scenarios
   - Create abstract interfaces/protocols/traits
   - Define method signatures with type hints
   - Add docstrings/comments that reference the Gherkin scenarios

4. **Choose appropriate idioms for your target language:**

   - **Python:** dataclasses, Pydantic models, or Protocol/ABC
   - **TypeScript:** interfaces and types
   - **Go:** structs and interfaces
   - **Java:** interfaces and POJOs
   - **Rust:** structs and traits
   - **C#:** interfaces and records/classes
   - **Ruby:** modules and duck typing
   - **Kotlin:** interfaces and data classes

## Output Examples by Language

### Python (dataclasses + ABC)

```python
"""
Structural design for <Feature Name>
Source: features/<feature>.feature
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

# Enums (from categorical nouns)
class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

# Data Models (from nouns)
@dataclass
class User:
    """From Scenario: '<scenario name>'"""
    id: str
    user_type: UserType
    points: int = 0

@dataclass
class Result:
    success: bool
    value: Optional[float] = None
    error: Optional[str] = None

# Interfaces (from verbs)
class IDiscountService(ABC):
    """Satisfies: features/<feature>.feature"""

    @abstractmethod
    def calculate_discount(self, user: User, amount: float) -> Result:
        """
        From Scenarios:
        - "Apply discount to VIP" (line X)
        - "No discount for normal" (line Y)
        """
        pass
```

### TypeScript

```typescript
/**
 * Structural design for <Feature Name>
 * Source: features/<feature>.feature
 */

// Enums (from categorical nouns)
export enum UserType {
  VIP = "VIP",
  NORMAL = "NORMAL"
}

// Data Models (from nouns)
export interface User {
  /** From Scenario: '<scenario name>' */
  id: string;
  userType: UserType;
  points: number;
}

export interface Result {
  success: boolean;
  value?: number;
  error?: string;
}

// Interfaces (from verbs)
export interface IDiscountService {
  /**
   * From Scenarios:
   * - "Apply discount to VIP" (line X)
   * - "No discount for normal" (line Y)
   */
  calculateDiscount(user: User, amount: number): Result;
}
```

### Go

```go
// Structural design for <Feature Name>
// Source: features/<feature>.feature

package discount

// Enums (from categorical nouns)
type UserType string

const (
    UserTypeVIP    UserType = "VIP"
    UserTypeNormal UserType = "NORMAL"
)

// Data Models (from nouns)
// From Scenario: '<scenario name>'
type User struct {
    ID        string
    UserType  UserType
    Points    int
}

type Result struct {
    Success bool
    Value   *float64
    Error   *string
}

// Interfaces (from verbs)
// Satisfies: features/<feature>.feature
type DiscountService interface {
    // From Scenarios:
    // - "Apply discount to VIP" (line X)
    // - "No discount for normal" (line Y)
    CalculateDiscount(user User, amount float64) Result
}
```

### Java

```java
/**
 * Structural design for <Feature Name>
 * Source: features/<feature>.feature
 */

// Enums (from categorical nouns)
public enum UserType {
    VIP,
    NORMAL
}

// Data Models (from nouns)
/** From Scenario: '<scenario name>' */
public class User {
    private String id;
    private UserType userType;
    private int points;

    // Constructor, getters, setters
}

public class Result {
    private boolean success;
    private Double value;
    private String error;

    // Constructor, getters, setters
}

// Interfaces (from verbs)
/** Satisfies: features/<feature>.feature */
public interface IDiscountService {
    /**
     * From Scenarios:
     * - "Apply discount to VIP" (line X)
     * - "No discount for normal" (line Y)
     */
    Result calculateDiscount(User user, double amount);
}
```

### Rust

```rust
//! Structural design for <Feature Name>
//! Source: features/<feature>.feature

// Enums (from categorical nouns)
#[derive(Debug, Clone, PartialEq)]
pub enum UserType {
    Vip,
    Normal,
}

// Data Models (from nouns)
/// From Scenario: '<scenario name>'
#[derive(Debug, Clone)]
pub struct User {
    pub id: String,
    pub user_type: UserType,
    pub points: i32,
}

#[derive(Debug, Clone)]
pub struct Result {
    pub success: bool,
    pub value: Option<f64>,
    pub error: Option<String>,
}

// Traits (from verbs)
/// Satisfies: features/<feature>.feature
pub trait DiscountService {
    /// From Scenarios:
    /// - "Apply discount to VIP" (line X)
    /// - "No discount for normal" (line Y)
    fn calculate_discount(&self, user: &User, amount: f64) -> Result;
}
```

## Language-Agnostic Principles

Regardless of the target language, your structure design must:

1. **Traceability:** Every model and interface references its source Gherkin scenario
2. **Strong Typing:** Use the strongest typing available in the language
3. **No Implementation:** Only signatures/definitions, no logic
4. **Completeness:** All nouns → models, all verbs → interfaces
5. **Documentation:** Comments/docstrings link to specific Gherkin lines

## Quality Checklist

Before completing, ensure:
- [ ] All nouns from Gherkin are represented as data structures
- [ ] All verbs from Gherkin are represented as interface methods
- [ ] All categorical values use enums/constants
- [ ] Types are as strict as the language allows
- [ ] Each element references its source Gherkin scenario
- [ ] NO implementation logic exists (only definitions)
- [ ] File uses appropriate extension for target language
- [ ] Follows language-specific naming conventions

## Naming Conventions by Language

- **Python:** `snake_case` for functions/variables, `PascalCase` for classes
- **TypeScript/JavaScript:** `camelCase` for functions/variables, `PascalCase` for types/interfaces
- **Go:** `PascalCase` for exported, `camelCase` for private
- **Java/C#:** `camelCase` for methods/variables, `PascalCase` for classes/interfaces
- **Rust:** `snake_case` for functions/variables, `PascalCase` for types

## Next Steps

After completing this phase:
- Save the structure file with appropriate extension
- Proceed to Phase 3: `/sdd-impl features/<feature>.feature structure/<feature>_structure.<ext>`
- Or return to user for architecture review

Now read the Gherkin file and create the structural design in the appropriate language.
