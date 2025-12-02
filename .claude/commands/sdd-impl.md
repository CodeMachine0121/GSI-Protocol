---
description: Phase 3 - Implement the logic within the defined structure (Engineer role)
---

# SDD Phase 3: Implementation (The Flesh)

**Role:** Senior Engineer

**Goal:** Implement the business logic within the defined structure to satisfy all Gherkin scenarios.

## Input

Provide two files:
1. Gherkin specification: `features/<feature>.feature`
2. Structure definition: `structure/<feature>_structure.py` (or `.ts`)

Usage: `/sdd-impl features/<feature>.feature structure/<feature>_structure.py`

Prompt: {{prompt}}

## Your Constraints

- You are a Senior Engineer implementing a strictly defined specification.
- You MUST use the Data Models from Phase 2 (structure file).
- You MUST implement all Interfaces from Phase 2.
- Every code branch must correspond to a Gherkin scenario.
- Your code MUST satisfy all scenarios from the Gherkin file.
- DO NOT modify the structure definitions - only implement them.

## Your Task

1. **Read both input files:**
   - The Gherkin file (requirements/test specification)
   - The structure file (data models and interfaces)

2. **Create concrete implementations:**
   - Implement each interface as a concrete class
   - Use the provided data models
   - Map each Gherkin scenario to code logic

3. **Implementation mapping:**
   - `Given` statements → Setup/input parameters
   - `When` statements → Method calls/actions
   - `Then` statements → Return values/outcomes

4. **Output Format:**

Create a file named `implementation/<feature_name>_impl.py` (or `.ts`):

**Python Example:**
```python
"""
Implementation for <Feature Name>
Implements: structure/<feature_name>_structure.py
Satisfies: features/<feature_name>.feature

This module contains the concrete implementation of the
service interfaces defined in the structure module.
"""

from structure.<feature_name>_structure import *

class <Service>Service(I<Service>Service):
    """
    Concrete implementation of I<Service>Service.
    Implements all scenarios from features/<feature_name>.feature
    """

    def action_name(self, param1: Type1, param2: Type2) -> ResultType:
        """
        Implementation satisfying:
        - Scenario: "<scenario 1 name>"
        - Scenario: "<scenario 2 name>"
        """

        # Map Gherkin Given conditions to code logic
        if condition_from_scenario_1:
            # Map Gherkin Then to return value
            return result_for_scenario_1

        # Handle edge case from Scenario 2
        elif condition_from_scenario_2:
            return result_for_scenario_2

        # Handle error case from Scenario 3
        if invalid_condition:
            return ResultType(
                success=False,
                error_message="Error message from Gherkin"
            )

        # Default/happy path
        return default_result

# Example usage (optional, for demonstration)
if __name__ == "__main__":
    service = <Service>Service()

    # Test scenario 1 from Gherkin
    result = service.action_name(param1_value, param2_value)
    print(f"Result: {result}")
```

**TypeScript Example:**
```typescript
/**
 * Implementation for <Feature Name>
 * Implements: structure/<feature_name>_structure.ts
 * Satisfies: features/<feature_name>.feature
 */

import {
  I<Service>Service,
  <Entity>,
  <Result>,
  <EntityType>
} from './structure/<feature_name>_structure';

export class <Service>Service implements I<Service>Service {
  /**
   * Implementation satisfying:
   * - Scenario: "<scenario 1 name>"
   * - Scenario: "<scenario 2 name>"
   */
  actionName(param1: Type1, param2: Type2): ResultType {
    // Map Gherkin Given conditions to code logic
    if (conditionFromScenario1) {
      // Map Gherkin Then to return value
      return resultForScenario1;
    }

    // Handle edge case from Scenario 2
    if (conditionFromScenario2) {
      return resultForScenario2;
    }

    // Handle error case from Scenario 3
    if (invalidCondition) {
      return {
        success: false,
        errorMessage: "Error message from Gherkin"
      };
    }

    // Default/happy path
    return defaultResult;
  }
}
```

## Complete Example

**Gherkin (features/vip_discount.feature):**
```gherkin
Feature: VIP Discount
  Scenario: Apply discount to VIP user
    Given user is VIP
    When user makes a purchase of 1000 USD
    Then final price should be 800 USD

  Scenario: No discount for non-VIP
    Given user is NORMAL
    When user makes a purchase of 1000 USD
    Then final price should be 1000 USD
```

**Structure (structure/vip_discount_structure.py):**
```python
class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

class IDiscountService(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float, user_type: UserType) -> float:
        pass
```

**Implementation (implementation/vip_discount_impl.py):**
```python
from structure.vip_discount_structure import *

class DiscountService(IDiscountService):
    """Implements VIP discount logic."""

    def calculate_discount(self, amount: float, user_type: UserType) -> float:
        """
        Satisfies scenarios:
        - "Apply discount to VIP user"
        - "No discount for non-VIP"
        """
        # Scenario 1: VIP gets 20% discount
        if user_type == UserType.VIP:
            return amount * 0.8

        # Scenario 2: Non-VIP pays full price
        return amount

# Verification
if __name__ == "__main__":
    service = DiscountService()

    # Test Scenario 1
    assert service.calculate_discount(1000, UserType.VIP) == 800

    # Test Scenario 2
    assert service.calculate_discount(1000, UserType.NORMAL) == 1000

    print("✅ All scenarios verified")
```

## Quality Checklist

Before completing, ensure:
- [ ] All interfaces from structure file are implemented
- [ ] All data models from structure file are used
- [ ] Every Gherkin scenario has corresponding code logic
- [ ] No structure definitions are modified
- [ ] Code includes comments mapping to Gherkin scenarios
- [ ] Basic verification/test code is included (optional but recommended)
- [ ] File is saved in `implementation/` directory

## Next Steps

After completing this phase:
- Save the implementation file
- Proceed to Phase 4 with: `/sdd-verify features/<feature>.feature implementation/<feature>_impl.py`
- Or run manual tests before verification

Now read both input files and create the implementation.
