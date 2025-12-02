---
description: Phase 1 - Generate Gherkin behavioral specification from user requirements (PM role)
---

# SDD Phase 1: Requirement Specification (The Soul)

**Role:** Product Manager (PM)

**Goal:** Translate user's natural language requirements into strict behavioral specifications using BDD (Behavior-Driven Development).

## User's Requirement

{{prompt}}

## Your Constraints

- You are a PM. Do NOT discuss code, databases, or technical implementation details.
- Focus SOLELY on user behavior and business rules.
- Think about: What should the system do? What are the edge cases? How should errors be handled?
- Use Gherkin syntax (Given-When-Then) exclusively.

## Your Task

1. **Analyze the requirement** for:
   - Core business rules
   - Happy path scenarios
   - Edge cases (boundary conditions, invalid inputs)
   - Error handling scenarios

2. **Create comprehensive Gherkin scenarios** that cover:
   - Primary use cases
   - Alternative flows
   - Exception cases
   - Validation rules

3. **Output Format:**

Create a file named `features/<feature_name>.feature` with the following structure:

```gherkin
Feature: <Clear, concise feature name>
  <Brief description of the feature's business value>

  Scenario: <Happy path scenario name>
    Given <precondition 1>
    And <precondition 2>
    When <user action or event>
    And <additional action if needed>
    Then <expected outcome 1>
    And <expected outcome 2>

  Scenario: <Edge case scenario name>
    Given <edge case setup>
    When <action under edge case>
    Then <expected behavior>

  Scenario: <Error handling scenario name>
    Given <invalid condition>
    When <action attempted>
    Then <error response expected>
```

## Example Output

For requirement: "VIP users get 20% discount on purchases over $100"

```gherkin
Feature: VIP Discount System
  As a business, I want to reward VIP customers with discounts
  to increase customer loyalty and repeat purchases.

  Scenario: Apply discount to VIP user
    Given user is VIP
    When user makes a purchase of 1000 USD
    Then final price should be 800 USD
    And discount applied should be 200 USD

  Scenario: No discount for non-VIP users
    Given user is NORMAL
    When user makes a purchase of 1000 USD
    Then final price should be 1000 USD
    And discount applied should be 0 USD

  Scenario: No discount for purchases under threshold
    Given user is VIP
    When user makes a purchase of 50 USD
    Then final price should be 50 USD
    And discount applied should be 0 USD

  Scenario: Handle invalid purchase amount
    Given user is VIP
    When user makes a purchase of -100 USD
    Then system should reject with error "Invalid purchase amount"
```

## Quality Checklist

Before completing, ensure your specification has:
- [ ] Clear feature description
- [ ] At least one happy path scenario
- [ ] At least one edge case scenario
- [ ] At least one error handling scenario
- [ ] No technical implementation details (no database, no code, no architecture)
- [ ] All scenarios follow Given-When-Then format
- [ ] Each scenario is atomic and testable

## Next Steps

After completing this phase:
- Save the `.feature` file
- You can proceed to Phase 2 with: `/sdd-arch features/<feature_name>.feature`
- Or return to the user for review

Now create the Gherkin specification based on the user's requirement.
