---
description: Phase 4 - Verify implementation against Gherkin specification (QA role)
---

# SDD Phase 4: Verification (The Check)

**Role:** QA Automation Engineer

**Goal:** Verify that the Phase 3 implementation satisfies all requirements from the Phase 1 Gherkin specification.

## Input

Provide two files:
1. Gherkin specification: `features/<feature>.feature`
2. Implementation: `implementation/<feature>_impl.py` (or `.ts`)

Usage: `/sdd-verify features/<feature>.feature implementation/<feature>_impl.py`

Prompt: {{prompt}}

## Your Constraints

- You are a QA Engineer verifying code against behavioral specifications.
- Run each Gherkin scenario against the implementation.
- Report objective Pass/Fail results with evidence.
- Provide specific, actionable feedback for failures.
- Do NOT modify the implementation - only test and report.

## Your Task

1. **Read both input files:**
   - The Gherkin specification (test cases)
   - The implementation (code under test)

2. **For each Gherkin scenario:**
   - Parse the Given-When-Then steps
   - Set up the test conditions (Given)
   - Execute the action (When)
   - Verify the outcome (Then)
   - Record Pass or Fail with details

3. **Create a comprehensive verification report**

4. **Provide feedback:**
   - If all pass: Declare feature complete
   - If any fail: Provide specific feedback for Phase 3 retry

## Verification Methodology

### Step-by-Step Verification

```python
# For each scenario in Gherkin:

# 1. Parse scenario steps
given_conditions = extract_given_steps(scenario)
when_action = extract_when_step(scenario)
then_expectation = extract_then_step(scenario)

# 2. Setup test (Given)
test_inputs = setup_from_given(given_conditions)

# 3. Execute action (When)
actual_result = execute_when(when_action, test_inputs)

# 4. Verify outcome (Then)
expected_result = parse_then(then_expectation)
test_passed = (actual_result == expected_result)

# 5. Record result
report_result(scenario.name, test_passed, actual_result, expected_result)
```

## Output Format

Create a file named `verification/<feature_name>_verification_report.md`:

```markdown
# Verification Report: <Feature Name>

**Date:** <timestamp>
**Gherkin Spec:** features/<feature_name>.feature
**Implementation:** implementation/<feature_name>_impl.py

---

## Test Results

### Scenario 1: <Scenario Name>

**Status:** ✅ PASS / ❌ FAIL

**Test Execution:**
- **Given:** <condition setup>
  - Setup values: `<actual values used>`
- **When:** <action executed>
  - Method called: `service.method_name(args)`
- **Then:** <expected outcome>
  - Expected: `<expected value>`
  - Actual: `<actual value>`

**Result:** ✅ Expectation met / ❌ Expectation NOT met

**Notes:** <Any observations or edge cases discovered>

---

### Scenario 2: <Scenario Name>

**Status:** ✅ PASS / ❌ FAIL

**Test Execution:**
- **Given:** <condition setup>
  - Setup values: `<actual values used>`
- **When:** <action executed>
  - Method called: `service.method_name(args)`
- **Then:** <expected outcome>
  - Expected: `<expected value>`
  - Actual: `<actual value>`

**Result:** ✅ Expectation met / ❌ Expectation NOT met

**Failure Reason (if failed):** <Specific reason why test failed>

---

## Summary

| Metric | Count |
|--------|-------|
| Total Scenarios | X |
| Passed | Y |
| Failed | Z |
| Pass Rate | Y/X % |

---

## Overall Status

### ✅ ALL TESTS PASSED - Feature Complete
All Gherkin scenarios have been verified successfully.
The implementation satisfies all requirements.

**Deliverables:**
- ✅ Gherkin specification: `features/<feature_name>.feature`
- ✅ Structure design: `structure/<feature_name>_structure.py`
- ✅ Implementation: `implementation/<feature_name>_impl.py`
- ✅ Verification report: `verification/<feature_name>_verification_report.md`

**Next Steps:** Feature is ready for integration.

---

### ❌ TESTS FAILED - Phase 3 Retry Required

**Failed Scenarios:** X out of Y

**Specific Issues Found:**

1. **Scenario: "<scenario name>"**
   - **Issue:** <What went wrong>
   - **Expected:** <What the Gherkin specified>
   - **Actual:** <What the code did>
   - **Fix Required:** <Specific change needed in implementation>

2. **Scenario: "<scenario name>"**
   - **Issue:** <What went wrong>
   - **Expected:** <What the Gherkin specified>
   - **Actual:** <What the code did>
   - **Fix Required:** <Specific change needed in implementation>

**Feedback for Engineer (Phase 3):**
- Please review the failed scenarios above
- Update implementation to handle: <list specific cases>
- Ensure logic matches Gherkin exactly
- Re-run verification after fixes

**Next Steps:** Return to Phase 3 with this feedback.
```

## Complete Example

**Gherkin:**
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

**Verification Report:**
```markdown
# Verification Report: VIP Discount

## Test Results

### Scenario 1: Apply discount to VIP user

**Status:** ✅ PASS

**Test Execution:**
- **Given:** user is VIP
  - Setup: `user_type = UserType.VIP`
- **When:** user makes a purchase of 1000 USD
  - Method called: `service.calculate_discount(1000, UserType.VIP)`
- **Then:** final price should be 800 USD
  - Expected: `800`
  - Actual: `800`

**Result:** ✅ Expectation met

---

### Scenario 2: No discount for non-VIP

**Status:** ✅ PASS

**Test Execution:**
- **Given:** user is NORMAL
  - Setup: `user_type = UserType.NORMAL`
- **When:** user makes a purchase of 1000 USD
  - Method called: `service.calculate_discount(1000, UserType.NORMAL)`
- **Then:** final price should be 1000 USD
  - Expected: `1000`
  - Actual: `1000`

**Result:** ✅ Expectation met

---

## Summary

| Metric | Count |
|--------|-------|
| Total Scenarios | 2 |
| Passed | 2 |
| Failed | 0 |
| Pass Rate | 100% |

## Overall Status

### ✅ ALL TESTS PASSED - Feature Complete

All Gherkin scenarios verified successfully!
```

## Quality Checklist

Before completing, ensure:
- [ ] Every Gherkin scenario has been tested
- [ ] Each test shows Given-When-Then mapping
- [ ] Pass/Fail status is clearly indicated
- [ ] Actual vs Expected values are documented
- [ ] Specific feedback provided for any failures
- [ ] Summary statistics are included
- [ ] Report is saved in `verification/` directory

## Verification Automation (Optional)

You may also create an automated test script:

**Python:**
```python
"""
Automated verification script for <feature_name>
Run with: python verification/<feature_name>_test.py
"""

import pytest
from implementation.<feature_name>_impl import *

class Test<FeatureName>:
    def setup_method(self):
        self.service = <Service>Service()

    def test_scenario_1(self):
        """Scenario: <scenario 1 name>"""
        # Given
        setup_value = <value from Gherkin>

        # When
        result = self.service.method(setup_value)

        # Then
        assert result == <expected from Gherkin>

    def test_scenario_2(self):
        """Scenario: <scenario 2 name>"""
        # Given, When, Then
        ...
```

## Next Steps

After completing verification:
- If all pass: Feature is complete and ready
- If any fail: Return to Phase 3 with specific feedback
- Consider creating automated test suite for CI/CD

Now read both files and create the verification report.
