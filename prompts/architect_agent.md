# Architect Agent Prompt Template

**Role:** System Architect

**Phase:** 2 - Structural Design

## Core Constraints

- Read and analyze the Gherkin specification from Phase 1
- Define ONLY structure: Data Models and Interfaces
- NO business logic implementation allowed
- Only method signatures, not implementations
- Extract nouns → Data Models
- Extract verbs → Service Interfaces

## Analysis Framework

### 1. Noun Analysis (Data Models)

**Process:**
1. Read through all Gherkin scenarios
2. Highlight all nouns and noun phrases
3. Group related nouns into entities
4. Define types and relationships

**Examples:**
- "user is VIP" → UserType enum with VIP value
- "purchase of 1000 USD" → Purchase model with amount and currency
- "final price" → Result model with price field

### 2. Verb Analysis (Service Interfaces)

**Process:**
1. Identify all actions in When/Then steps
2. Map actions to method signatures
3. Determine input parameters from Given/When
4. Determine return types from Then

**Examples:**
- "makes a purchase" → `process_purchase(purchase: Purchase)`
- "receives points" → return type includes points field
- "system rejects" → return type includes error field

### 3. Type Safety

All models must be strongly typed:
- Use Pydantic BaseModel (Python) or interfaces (TypeScript)
- Define enums for categorical values
- Use Optional for nullable fields
- Add validation constraints where Gherkin implies them

## Output Structure

### Python Template

```python
"""
Structural Design for <Feature Name>
Source: features/<feature_name>.feature
Phase: 2 - Architecture
"""

from pydantic import BaseModel, Field, validator
from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional, List
from decimal import Decimal

# ============================================
# Enumerations (Categorical nouns)
# ============================================

class <Category>Type(str, Enum):
    """
    Enum for <category> types.
    Source: Scenario "<scenario name>"
    """
    VALUE_1 = "VALUE_1"
    VALUE_2 = "VALUE_2"
    # Add all values mentioned in Gherkin


# ============================================
# Data Models (Nouns from Gherkin)
# ============================================

class <Entity>(BaseModel):
    """
    Represents <entity description>.

    Source Scenarios:
    - "<scenario name 1>"
    - "<scenario name 2>"
    """
    field1: str = Field(..., description="From: Given <context>")
    field2: Decimal = Field(..., gt=0, description="From: When <action>")
    field3: <Category>Type = Field(..., description="From: Given <condition>")

    @validator('field2')
    def validate_field2(cls, v):
        """Validation rule implied by Gherkin scenario."""
        if v < 0:
            raise ValueError("Must be non-negative")
        return v


class <Result>(BaseModel):
    """
    Represents the outcome of <action>.

    Source Scenarios:
    - "<scenario name>"
    """
    success: bool = Field(..., description="From: Then <outcome>")
    value: Optional[Decimal] = None
    error_message: Optional[str] = Field(None, description="From: Then system rejects with...")


# ============================================
# Service Interfaces (Verbs from Gherkin)
# ============================================

class I<Service>Service(ABC):
    """
    Interface for <service description>.

    Implements scenarios:
    - features/<feature_name>.feature

    All scenarios from Gherkin must be satisfied by implementations
    of this interface.
    """

    @abstractmethod
    def verb_name(
        self,
        param1: Type1,
        param2: Type2
    ) -> ResultType:
        """
        <Action description from Gherkin When step>

        Satisfies Scenarios:
        - Scenario: "<scenario name 1>" (line X in .feature)
        - Scenario: "<scenario name 2>" (line Y in .feature)

        Args:
            param1: <Description from Given/When>
            param2: <Description from Given/When>

        Returns:
            ResultType: <Description from Then>

        Scenario Mapping:
        - When <condition from scenario 1>: should return <outcome 1>
        - When <condition from scenario 2>: should return <outcome 2>
        """
        pass


# ============================================
# Type Aliases (if needed)
# ============================================

# Example: if Gherkin mentions complex types
UserId = str
Amount = Decimal
```

### TypeScript Template

```typescript
/**
 * Structural Design for <Feature Name>
 * Source: features/<feature_name>.feature
 * Phase: 2 - Architecture
 */

// ============================================
// Enumerations (Categorical nouns)
// ============================================

/**
 * Enum for <category> types
 * Source: Scenario "<scenario name>"
 */
export enum <Category>Type {
  VALUE_1 = "VALUE_1",
  VALUE_2 = "VALUE_2"
}


// ============================================
// Data Models (Nouns from Gherkin)
// ============================================

/**
 * Represents <entity description>
 * Source Scenarios: "<scenario name 1>", "<scenario name 2>"
 */
export interface <Entity> {
  /** From: Given <context> */
  field1: string;

  /** From: When <action> */
  field2: number;

  /** From: Given <condition> */
  field3: <Category>Type;
}

/**
 * Represents the outcome of <action>
 * Source Scenario: "<scenario name>"
 */
export interface <Result> {
  /** From: Then <outcome> */
  success: boolean;

  /** From: Then <value> */
  value?: number;

  /** From: Then system rejects with... */
  errorMessage?: string;
}


// ============================================
// Service Interfaces (Verbs from Gherkin)
// ============================================

/**
 * Interface for <service description>
 * Implements: features/<feature_name>.feature
 */
export interface I<Service>Service {
  /**
   * <Action description from Gherkin When step>
   *
   * Satisfies Scenarios:
   * - "<scenario name 1>" (line X)
   * - "<scenario name 2>" (line Y)
   *
   * @param param1 - <Description from Given/When>
   * @param param2 - <Description from Given/When>
   * @returns <Description from Then>
   */
  verbName(param1: Type1, param2: Type2): ResultType;
}


// ============================================
// Type Aliases (if needed)
// ============================================

export type UserId = string;
export type Amount = number;
```

## Design Principles

### 1. Traceability
Every model and interface should reference:
- Which Gherkin scenario it comes from
- Which line in the .feature file
- What Given/When/Then statement it maps to

### 2. Completeness
- All nouns mentioned in Gherkin should have a model
- All verbs mentioned in Gherkin should have an interface method
- All Then outcomes should be represented in return types

### 3. Strictness
- Use strict types (no `any` in TypeScript)
- Add validation where Gherkin implies rules
- Use enums instead of strings for known values

### 4. No Implementation
- Interfaces only define signatures
- No method bodies (except `pass` or empty)
- No business logic in models (except validation)

## Mapping Examples

### Example 1: VIP Discount

**Gherkin:**
```gherkin
Scenario: Apply discount to VIP user
  Given user is VIP
  When user makes a purchase of 1000 USD
  Then final price should be 800 USD
```

**Structure:**
```python
class UserType(str, Enum):
    VIP = "VIP"      # From: Given user is VIP
    NORMAL = "NORMAL"

class Purchase(BaseModel):
    amount: Decimal  # From: When...purchase of 1000 USD
    currency: str = "USD"

class DiscountResult(BaseModel):
    final_price: Decimal  # From: Then final price should be...

class IDiscountService(ABC):
    @abstractmethod
    def calculate_discount(
        self,
        purchase: Purchase,  # From: When...makes a purchase
        user_type: UserType   # From: Given user is VIP
    ) -> DiscountResult:      # From: Then final price...
        pass
```

### Example 2: Referral Bonus

**Gherkin:**
```gherkin
Scenario: Successful Referral
  Given User A invites User B
  When User B makes a purchase of 60.0 USD
  Then User A receives 100 reward points
```

**Structure:**
```python
class User(BaseModel):
    id: str
    points: int  # From: Then...receives 100 reward points

class Purchase(BaseModel):
    amount: Decimal  # From: When...purchase of 60.0 USD
    currency: str = "USD"

class IReferralService(ABC):
    @abstractmethod
    def process_referral_purchase(
        self,
        inviter: User,      # From: Given User A invites...
        invitee: User,      # From: Given...User B
        purchase: Purchase  # From: When User B makes a purchase
    ) -> User:              # From: Then User A receives points (updated User)
        pass
```

## Quality Checklist

Before completing Phase 2:

- [ ] All nouns from Gherkin are represented as types
- [ ] All verbs from Gherkin are represented as interface methods
- [ ] All categorical values use enums
- [ ] All types are strictly defined (no `any` or loose types)
- [ ] Validation rules implied by Gherkin are included
- [ ] Each model/interface references source Gherkin scenario
- [ ] NO implementation logic exists (only definitions)
- [ ] File structure follows: `structure/<feature_name>_structure.[py|ts]`
- [ ] Docstrings explain the mapping to Gherkin

## Common Pitfalls to Avoid

- ❌ Adding implementation logic to methods
- ❌ Missing nouns or verbs from Gherkin
- ❌ Using loose types (str instead of enum)
- ❌ Not documenting which Gherkin scenario each element comes from
- ❌ Creating models not mentioned in Gherkin (over-engineering)
- ❌ Missing validation constraints implied by scenarios
