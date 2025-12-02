# Example: Referral Bonus System

This is a complete example demonstrating the SDD workflow for implementing a referral bonus feature.

## Requirement

"I need to implement a Referral Bonus system. If a user invites a friend, and the friend completes a purchase over $50, the inviter gets 100 points."

## Phase 1: Specification

**File:** `spec.feature`

Contains 4 Gherkin scenarios:
1. Successful Referral Bonus - Happy path where invitee spends > $50
2. Purchase Amount Too Low - Edge case where invitee spends < $50
3. No Referral Relationship - Edge case where users aren't connected
4. Invalid Purchase Amount - Error case with negative amount

## Phase 2: Structure

**File:** `structure.py`

Defines:
- **Data Models:**
  - `User` - Represents users with ID and points balance
  - `Purchase` - Represents purchase transactions
  - `ReferralResult` - Represents operation outcome

- **Service Interface:**
  - `IReferralService` - Abstract interface with `process_referral_purchase` method

- **Constants:**
  - `REFERRAL_BONUS_POINTS = 100`
  - `MINIMUM_PURCHASE_AMOUNT = 50.0`

## Phase 3: Implementation

**File:** `implementation.py`

Implements `ReferralService` class that:
- Rejects negative purchase amounts
- Awards 0 points if no referral relationship exists
- Awards 0 points if purchase ≤ $50
- Awards 100 points if purchase > $50 and referral exists

Includes quick verification function that tests all 4 scenarios.

## Running the Example

```bash
cd examples/referral_bonus
python implementation.py
```

Expected output:
```
Running quick verification checks...

Test 1: Successful Referral Bonus
✓ Scenario 1: Successful referral bonus - PASSED

Test 2: Purchase Amount Too Low
✓ Scenario 2: Purchase too low - PASSED

Test 3: No Referral Relationship
✓ Scenario 3: No referral relationship - PASSED

Test 4: Invalid Purchase Amount
✓ Scenario 4: Invalid purchase amount - PASSED

============================================================
✅ All scenarios verified successfully!
============================================================

Ready for Phase 4: Formal Verification
```

## Phase 4: Verification

For formal verification, run:
```
/sdd-verify examples/referral_bonus/spec.feature examples/referral_bonus/implementation.py
```

This would generate a comprehensive verification report with:
- Detailed test execution for each scenario
- Pass/Fail status with evidence
- Summary statistics
- Next steps recommendation

## Key Learnings

1. **Clear Specifications**: The Gherkin scenarios make requirements unambiguous
2. **Type Safety**: Pydantic models catch invalid data early
3. **Traceability**: Each code block maps to a specific Gherkin scenario
4. **Testability**: Every scenario can be objectively verified
5. **No Hallucination**: Implementation strictly follows structure and spec

## Try It Yourself

1. Modify `spec.feature` to add a new scenario (e.g., "Multiple purchases by same invitee")
2. Update `structure.py` if needed (probably not)
3. Update `implementation.py` to handle the new scenario
4. Run verification to ensure all scenarios pass

This demonstrates how SDD makes feature development systematic and verifiable!
