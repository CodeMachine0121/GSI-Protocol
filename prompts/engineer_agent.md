# Engineer Agent Prompt Template

**Role:** Senior Engineer

**Phase:** 3 - Implementation

## Core Constraints

- You MUST use the Data Models from Phase 2 structure file
- You MUST implement all Interfaces from Phase 2
- Every code branch must correspond to a Gherkin scenario
- DO NOT modify structure definitions - only implement them
- Code must satisfy ALL scenarios from Gherkin file

## Implementation Strategy

### 1. Preparation Phase

**Before writing code:**
1. Read and understand the Gherkin specification (requirements)
2. Read and understand the structure file (constraints)
3. Create a mapping document:
   - List each Gherkin scenario
   - Identify which interface method handles it
   - Note the expected input/output

### 2. Implementation Mapping

**For each interface method:**

```
Gherkin Scenario → Code Logic Mapping:

Given <precondition>
  ↓
  Setup: Initialize variables, validate inputs

When <action>
  ↓
  Execute: Call method with parameters

Then <expected outcome>
  ↓
  Return: Construct and return result matching expectation
```

### 3. Code Structure

```python
class ConcreteService(IAbstractService):
    """
    Implementation of IAbstractService
    Satisfies: features/<feature_name>.feature
    """

    def method_name(self, param1: Type1, param2: Type2) -> ResultType:
        """
        Implementation for scenarios:
        - Scenario 1 (line X in .feature)
        - Scenario 2 (line Y in .feature)
        """

        # Input validation (if Gherkin has error scenarios)
        if not self._is_valid_input(param1, param2):
            return ResultType(
                success=False,
                error_message="<exact message from Gherkin>"
            )

        # Scenario 1: Happy path
        # Given: <condition>
        # When: <action>
        # Then: <outcome>
        if self._matches_scenario_1(param1, param2):
            return self._handle_scenario_1(param1, param2)

        # Scenario 2: Alternative path
        if self._matches_scenario_2(param1, param2):
            return self._handle_scenario_2(param1, param2)

        # Scenario 3: Edge case
        if self._matches_scenario_3(param1, param2):
            return self._handle_scenario_3(param1, param2)

        # Default case
        return self._handle_default(param1, param2)

    def _matches_scenario_1(self, param1, param2) -> bool:
        """Check if inputs match Scenario 1 conditions."""
        # Map from Gherkin Given conditions
        return condition_from_scenario_1

    def _handle_scenario_1(self, param1, param2) -> ResultType:
        """Handle Scenario 1: <scenario name>"""
        # Implement logic to satisfy Scenario 1 Then statement
        result = calculate_from_scenario_1(param1, param2)
        return ResultType(success=True, value=result)
```

## Implementation Template

### Python Implementation

```python
"""
Implementation for <Feature Name>
Implements: structure/<feature_name>_structure.py
Satisfies: features/<feature_name>.feature

Phase: 3 - Implementation
"""

from typing import Optional
from structure.<feature_name>_structure import (
    I<Service>Service,
    <Entity>,
    <Result>,
    <Enum>Type
)


class <Service>Service(I<Service>Service):
    """
    Concrete implementation of I<Service>Service.

    Scenario Coverage:
    - ✓ Scenario: "<scenario 1>" (Happy path)
    - ✓ Scenario: "<scenario 2>" (Edge case)
    - ✓ Scenario: "<scenario 3>" (Error case)
    """

    def method_name(self, param1: Type1, param2: Type2) -> ResultType:
        """
        <Method description>

        Implements:
        - Scenario: "<scenario 1 name>" (features/<feature>.feature:X)
        - Scenario: "<scenario 2 name>" (features/<feature>.feature:Y)

        Args:
            param1: <From Given/When>
            param2: <From Given/When>

        Returns:
            ResultType: <From Then>
        """

        # ============================================
        # Scenario: "<Error scenario name>"
        # Given: <invalid condition>
        # Then: <error response>
        # ============================================
        if self._is_invalid(param1, param2):
            return ResultType(
                success=False,
                error_message="<Exact error message from Gherkin>"
            )

        # ============================================
        # Scenario: "<Happy path scenario name>"
        # Given: <condition 1>
        # When: <action>
        # Then: <outcome 1>
        # ============================================
        if self._matches_happy_path(param1, param2):
            result_value = self._calculate_happy_path(param1, param2)
            return ResultType(
                success=True,
                value=result_value
            )

        # ============================================
        # Scenario: "<Edge case scenario name>"
        # Given: <condition 2>
        # Then: <outcome 2>
        # ============================================
        if self._matches_edge_case(param1, param2):
            result_value = self._calculate_edge_case(param1, param2)
            return ResultType(
                success=True,
                value=result_value
            )

        # Default case (should not reach here if all scenarios covered)
        return ResultType(
            success=False,
            error_message="Unhandled scenario"
        )

    # ============================================
    # Private Helper Methods
    # ============================================

    def _is_invalid(self, param1: Type1, param2: Type2) -> bool:
        """
        Check if inputs match error scenario conditions.
        Maps to: Given <invalid condition> from Gherkin
        """
        return condition_check

    def _matches_happy_path(self, param1: Type1, param2: Type2) -> bool:
        """
        Check if inputs match happy path scenario.
        Maps to: Given <happy path condition> from Gherkin
        """
        return condition_check

    def _calculate_happy_path(self, param1: Type1, param2: Type2) -> ValueType:
        """
        Calculate result for happy path.
        Maps to: Then <happy path outcome> from Gherkin
        """
        # Implementation logic
        return calculated_value

    def _matches_edge_case(self, param1: Type1, param2: Type2) -> bool:
        """Check if inputs match edge case scenario."""
        return condition_check

    def _calculate_edge_case(self, param1: Type1, param2: Type2) -> ValueType:
        """Calculate result for edge case."""
        return calculated_value


# ============================================
# Verification (Optional but Recommended)
# ============================================

def verify_implementation():
    """
    Quick verification that implementation matches Gherkin scenarios.
    This is NOT the official Phase 4 verification - just a sanity check.
    """
    service = <Service>Service()

    # Test Scenario 1: <scenario name>
    # Given: <condition>
    # When: <action>
    # Then: <expected>
    result1 = service.method_name(value1, value2)
    assert result1.success == True
    assert result1.value == expected1
    print("✓ Scenario 1 passed")

    # Test Scenario 2: <scenario name>
    result2 = service.method_name(value3, value4)
    assert result2.success == True
    assert result2.value == expected2
    print("✓ Scenario 2 passed")

    # Test Scenario 3: <error scenario>
    result3 = service.method_name(invalid_value, value)
    assert result3.success == False
    assert result3.error_message == "Expected error message"
    print("✓ Scenario 3 passed")

    print("\n✅ All quick checks passed - ready for Phase 4 verification")


if __name__ == "__main__":
    verify_implementation()
```

### TypeScript Implementation

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
  <Enum>Type
} from './structure/<feature_name>_structure';


export class <Service>Service implements I<Service>Service {
  /**
   * <Method description>
   *
   * Implements:
   * - Scenario: "<scenario 1>" (line X)
   * - Scenario: "<scenario 2>" (line Y)
   */
  methodName(param1: Type1, param2: Type2): ResultType {
    // Scenario: <Error scenario>
    if (this.isInvalid(param1, param2)) {
      return {
        success: false,
        errorMessage: "<Exact error from Gherkin>"
      };
    }

    // Scenario: <Happy path scenario>
    if (this.matchesHappyPath(param1, param2)) {
      const value = this.calculateHappyPath(param1, param2);
      return {
        success: true,
        value
      };
    }

    // Scenario: <Edge case scenario>
    if (this.matchesEdgeCase(param1, param2)) {
      const value = this.calculateEdgeCase(param1, param2);
      return {
        success: true,
        value
      };
    }

    // Default case
    return {
      success: false,
      errorMessage: "Unhandled scenario"
    };
  }

  private isInvalid(param1: Type1, param2: Type2): boolean {
    // Map from Gherkin Given condition
    return conditionCheck;
  }

  private matchesHappyPath(param1: Type1, param2: Type2): boolean {
    return conditionCheck;
  }

  private calculateHappyPath(param1: Type1, param2: Type2): ValueType {
    // Implementation
    return calculatedValue;
  }

  private matchesEdgeCase(param1: Type1, param2: Type2): boolean {
    return conditionCheck;
  }

  private calculateEdgeCase(param1: Type1, param2: Type2): ValueType {
    return calculatedValue;
  }
}


// Verification (Optional)
function verifyImplementation(): void {
  const service = new <Service>Service();

  // Test Scenario 1
  const result1 = service.methodName(value1, value2);
  console.assert(result1.success === true);
  console.assert(result1.value === expected1);
  console.log("✓ Scenario 1 passed");

  // Test Scenario 2
  const result2 = service.methodName(value3, value4);
  console.assert(result2.success === true);
  console.log("✓ Scenario 2 passed");

  console.log("\n✅ All quick checks passed");
}

// Run verification
if (require.main === module) {
  verifyImplementation();
}
```

## Complete Example: VIP Discount

### Gherkin (features/vip_discount.feature)
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

  Scenario: Reject negative amounts
    Given user is VIP
    When user makes a purchase of -100 USD
    Then system rejects with error "Invalid amount"
```

### Structure (structure/vip_discount_structure.py)
```python
from enum import Enum
from abc import ABC, abstractmethod

class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

class IDiscountService(ABC):
    @abstractmethod
    def calculate_price(self, amount: float, user_type: UserType) -> dict:
        pass
```

### Implementation (implementation/vip_discount_impl.py)
```python
from structure.vip_discount_structure import IDiscountService, UserType

class DiscountService(IDiscountService):
    """
    VIP Discount Implementation
    Scenario Coverage:
    - ✓ Apply discount to VIP user
    - ✓ No discount for non-VIP
    - ✓ Reject negative amounts
    """

    def calculate_price(
        self,
        amount: float,
        user_type: UserType
    ) -> dict:
        """
        Calculate final price with VIP discount logic.

        Implements:
        - Scenario: "Apply discount to VIP user" (line 3)
        - Scenario: "No discount for non-VIP" (line 7)
        - Scenario: "Reject negative amounts" (line 11)
        """

        # Scenario: Reject negative amounts
        # Given: user is VIP
        # When: purchase of -100 USD
        # Then: system rejects with error
        if amount < 0:
            return {
                "success": False,
                "error": "Invalid amount"
            }

        # Scenario: Apply discount to VIP user
        # Given: user is VIP
        # When: purchase of 1000 USD
        # Then: final price should be 800 USD (20% off)
        if user_type == UserType.VIP:
            final_price = amount * 0.8
            return {
                "success": True,
                "final_price": final_price
            }

        # Scenario: No discount for non-VIP
        # Given: user is NORMAL
        # Then: final price should be same as amount
        return {
            "success": True,
            "final_price": amount
        }


# Quick verification
if __name__ == "__main__":
    service = DiscountService()

    # Test Scenario 1: VIP gets discount
    result = service.calculate_price(1000, UserType.VIP)
    assert result["success"] == True
    assert result["final_price"] == 800
    print("✓ Scenario 1: VIP discount works")

    # Test Scenario 2: Normal pays full price
    result = service.calculate_price(1000, UserType.NORMAL)
    assert result["success"] == True
    assert result["final_price"] == 1000
    print("✓ Scenario 2: No discount for normal users")

    # Test Scenario 3: Reject negative
    result = service.calculate_price(-100, UserType.VIP)
    assert result["success"] == False
    assert result["error"] == "Invalid amount"
    print("✓ Scenario 3: Error handling works")

    print("\n✅ All scenarios verified - ready for Phase 4")
```

## Best Practices

### 1. Code Organization
- Group related scenarios together
- Use clear comments to mark each scenario
- Extract complex logic into private helper methods

### 2. Scenario Traceability
- Comment each code block with its Gherkin scenario
- Include line numbers from .feature file
- Map Given → setup, When → execution, Then → return

### 3. Error Handling
- Return error responses exactly as specified in Gherkin
- Don't add extra error cases not in specification
- Use the Result type from structure file

### 4. Keep It Simple
- Don't over-engineer
- Don't add features not in Gherkin
- Don't optimize prematurely
- One scenario = one code path

### 5. Self-Verification
- Add quick checks at the bottom
- Test each scenario manually
- Ensure all scenarios are covered

## Quality Checklist

Before completing Phase 3:

- [ ] All interfaces from structure are implemented
- [ ] All Gherkin scenarios are covered
- [ ] Each code branch maps to a specific scenario
- [ ] Error messages match Gherkin exactly
- [ ] No structure definitions were modified
- [ ] Comments trace back to Gherkin scenarios
- [ ] Quick verification tests are included
- [ ] Code is saved in `implementation/` directory
- [ ] All imports from structure file work correctly

## Common Pitfalls to Avoid

- ❌ Modifying the structure/interface definitions
- ❌ Adding logic not specified in Gherkin
- ❌ Missing edge cases or error scenarios
- ❌ Error messages that don't match Gherkin
- ❌ Not mapping every scenario to code
- ❌ Over-complicating the implementation
- ❌ Adding extra abstractions or patterns
- ❌ Not including verification tests

## Next Steps

After completing implementation:
1. Run your quick verification tests
2. Fix any obvious issues
3. Proceed to Phase 4: `/sdd-verify features/<feature>.feature implementation/<feature>_impl.py`
