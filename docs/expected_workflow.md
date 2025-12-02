# AI-Driven SDD Workflow Definition

> Specification-Driven Development for New Feature Implementation

## 1. Overview

This workflow defines a strict **Specification-Driven Development (SDD)** process for building new software features using AI Agents. The core philosophy is **"Spec -> Structure -> Implementation"**.

The process isolates business logic, technical architecture, and coding into three distinct phases to minimize hallucination and maximize precision.

## 2. Process Flow (Text-Based)

```text
[ User Requirement ]
       │
       ▼
+=============================================+
|  Phase 1: Specification (The Soul)          |
|  Role:   PM Agent                           |
|  Action: Define Behavior (BDD)              |
|  Output: Gherkin (.feature)                 |
+=============================================+
       │
       │ (Pass Gherkin)
       ▼
+=============================================+
|  Phase 2: Structure (The Skeleton)          |
|  Role:   Architect Agent                    |
|  Action: Define Data Models & Interfaces    |
|  Input:  Gherkin                            |
|  Output: Schema / Design Spec (Code)        |
+=============================================+
       │
       │ (Pass Gherkin + Schema)
       ▼
+=============================================+
|  Phase 3: Implementation (The Flesh)        |
|  Role:   Engineer Agent                     |
|  Action: Write Logic / Fill Interfaces      |
|  Input:  Gherkin + Schema                   |
|  Output: Executable Code                    |
+=============================================+
       │
       ▼
+=============================================+
|  Phase 4: Verification (The Check)          |
|  Role:   QA Agent / Automated Script        |
|  Action: Run Gherkin Scenarios vs Code      |
+=============================================+
       │
       ├───── < Fail > ────┐
       │                   │ (Feedback Loop)
       │                   │
       ▼                   │
( Feature Complete )       └────→ [ Retry Phase 3 ]
```

## 3. Workflow Phases Detail

### Phase 1: Requirement Specification (Behavior)

**Role:** Product Manager (PM)
**Goal:** Translate vague user requirements into strict behavioral specifications using BDD.

- **Input:** User's natural language request (e.g., "I need a discount system for VIPs").
- **Action:**
  1.  Analyze business rules and edge cases.
  2.  Define scenarios using `Given-When-Then` syntax.
- **Output Artifact:** `feature_spec.gherkin`
  - **Must contain:** Happy paths, Edge cases, Error handling.
  - **Must NOT contain:** Database schema, specific coding implementation details.

### Phase 2: Structural Design (Architecture)

**Role:** System Architect
**Goal:** Design the technical skeleton required to support the Gherkin scenarios.

- **Input:** `feature_spec.gherkin` (from Phase 1)
- **Action:**
  1.  **Noun Analysis:** Extract nouns from Gherkin to create Data Models (Schema).
  2.  **Verb Analysis:** Extract verbs from Gherkin to create Service Interfaces (Abstract Classes / Signatures).
- **Output Artifact:** `structure_design.py` (or `.ts`)
  - **Content:**
    - **Data Models:** (e.g., Pydantic Models, Type Definitions) strictly typing input/output fields.
    - **Interfaces:** (e.g., Abstract Base Classes) defining function signatures without implementation logic.
  - **Constraint:** No business logic implementation allowed in this phase. Only definitions.

### Phase 3: Implementation (Coding)

**Role:** Senior Engineer
**Goal:** Implement the logic within the defined structure to satisfy the Gherkin specs.

- **Input:**
  - `feature_spec.gherkin` (The Test/Requirement)
  - `structure_design.py` (The Constraint/Blueprint)
- **Action:**
  1.  Write the actual code logic inside the defined interfaces.
  2.  Ensure every logical branch in the code corresponds to a Scenario in the Gherkin file.
- **Output Artifact:** `implementation.py` (or `.ts`)
  - **Content:** Fully functional code that implements the interfaces from Phase 2.

### Phase 4: Verification (Self-Correction)

**Role:** QA Automation
**Goal:** Verify that Phase 3 meets the requirements of Phase 1.

- **Input:** `feature_spec.gherkin` + `implementation.py`
- **Action:**
  - Run the Gherkin scenarios against the implemented code.
- **Logic:**
  - If **Pass**: Workflow ends.
  - If **Fail**: Return error logs to **Phase 3 (Engineer Agent)** for retry.

## 4. Prompting Strategy for Plugin

When generating the plugin, ensure the prompts for each agent follow these directives:

- **For Spec Agent:** "You are a PM. Do not discuss code. Focus solely on user behavior and business rules using Gherkin."
- **For Architect Agent:** "You are an Architect. Read the Gherkin. Define the NECESSARY Pydantic models and Abstract Base Classes to support these scenarios. Do not implement the methods, only define signatures."
- **For Engineer Agent:** "You are an Engineer. You must strictly use the provided Data Models. Implement the logic for the provided Interfaces. Your code must pass all Gherkin scenarios."

## 5. Artifact Examples

**Phase 1 Output (Gherkin):**

```gherkin
Feature: VIP Discount
  Scenario: Apply discount
    Given User is VIP
    When Purchase amount is 1000
    Then Final price should be 800
```

**Phase 2 Output (Structure):**

```python
class UserType(str, Enum):
    VIP = "VIP"
    NORMAL = "NORMAL"

class ICouponService(ABC):
    @abstractmethod
    def calculate(self, amount: float, user_type: UserType) -> float:
        pass
```

## 6. Example Usage Scenario

Here is how a real-world interaction would look like when the User triggers this workflow plugin.

**User:**

> "I need to implement a Referral Bonus system. If a user invites a friend, and the friend completes a purchase over $50, the inviter gets 100 points."

**Agent (PM Role - Phase 1):**

> "Understood. I have drafted the behavioral specification (Gherkin) for your Referral System.
>
> **File: `referral.feature`**
>
> ```gherkin
> Feature: Referral Bonus System
>   Scenario: Successful Referral
>     Given User A invites User B
>     When User B makes a purchase of 60.0 USD
>     Then User A receives 100 reward points
>
>   Scenario: Purchase amount too low
>     Given User A invites User B
>     When User B makes a purchase of 30.0 USD
>     Then User A receives 0 reward points
> ```
>
> _Moving to Structural Design..._"

**Agent (Architect Role - Phase 2):**

> "Based on the Gherkin above, I have defined the necessary Data Models and Interfaces.
>
> **File: `structure.py`**
>
> ```python
> class Purchase(BaseModel):
>     amount: float
>     currency: str
>
> class User(BaseModel):
>     id: str
>     points: int
>
> class IReferralService(ABC):
>     @abstractmethod
>     def process_purchase(self, inviter: User, purchase: Purchase) -> User:
>         """Calculates and updates points for the inviter."""
>         pass
> ```
>
> _Moving to Implementation..._"

**Agent (Engineer Role - Phase 3):**

> "I have implemented the logic strictly following the structure and scenarios.
>
> **File: `impl.py`**
>
> ```python
> class ReferralService(IReferralService):
>     def process_purchase(self, inviter: User, purchase: Purchase) -> User:
>         if purchase.amount > 50:
>             inviter.points += 100
>         return inviter
> ```
>
> _Running Verification..._"

**Agent (QA Role - Phase 4):**

> "✅ **Verification Passed.** All Gherkin scenarios passed successfully against the implementation.
>
> Here are your final files: `referral.feature`, `structure.py`, `impl.py`."
