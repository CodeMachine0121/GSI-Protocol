# GSI-Protocol Theory

**Language**: English | [繁體中文](./gsi-theory.zh-TW.md)

## What is GSI?

GSI-Protocol is a systematic approach to software development that emphasizes **specification-driven, architecture-first development**. The acronym GSI represents the three core pillars of this methodology:

- **G** - Gherkin (Specification)
- **S** - Structure (Architecture)
- **I** - Implement (Implementation)

This approach ensures that every feature is built on a solid foundation of clear requirements, well-designed architecture, and verified implementation.

---

## The Three Pillars

### G - Gherkin (Specification)

**Purpose**: Define "What" the system should do from a business perspective.

Gherkin is a business-readable, domain-specific language that describes software behavior without detailing how that behavior is implemented. It uses a **Given-When-Then** format to specify scenarios.

#### Why Gherkin?

1. **Business-Readable**: Non-technical stakeholders can understand and verify requirements
2. **Unambiguous**: Clear, structured format reduces misunderstandings
3. **Testable**: Each scenario can be directly verified
4. **Language-Agnostic**: Independent of programming language or framework

#### Structure

```gherkin
Feature: User Authentication
  As a user
  I want to log in with email and password
  So that I can access my account

  Scenario: Successful login
    Given a registered user with email "user@example.com"
    And the password is "SecurePass123"
    When the user submits login credentials
    Then the user is authenticated
    And a session token is generated

  Scenario: Invalid password
    Given a registered user with email "user@example.com"
    And the password is "WrongPassword"
    When the user submits login credentials
    Then authentication fails
    And an error message is displayed
```

#### Key Components

- **Feature**: High-level description of functionality
- **Scenario**: Specific example of how the feature works
- **Given**: Preconditions and initial state
- **When**: Action or event
- **Then**: Expected outcome

#### Best Practices

- Focus on business value, not technical implementation
- Write from the user's perspective
- Cover happy paths, edge cases, and error scenarios
- Keep scenarios independent of each other
- Use concrete examples

---

### S - Structure (Architecture)

**Purpose**: Define "How" the system should be organized at a high level.

Structure represents the architectural design that bridges the gap between business requirements (Gherkin) and code implementation. It's **language-agnostic** and focuses on models, interfaces, and system organization.

#### Why Architecture-First?

1. **Separation of Concerns**: Clear boundaries between components
2. **Technology Independence**: Design can be implemented in any language
3. **Team Alignment**: Shared understanding before coding begins
4. **Change Management**: Easier to modify design than code
5. **Quality Assurance**: Architecture can be reviewed before implementation

#### From Gherkin to Structure

The transformation follows a systematic approach:

**Nouns → Data Models**

- User → `User` model
- Session token → `SessionToken` model
- Credentials → `Credentials` model

**Verbs → Service Interfaces**

- "submits login credentials" → `AuthService.login()`
- "is authenticated" → `AuthService.authenticate()`
- "generates token" → `TokenService.generate()`

#### Architecture Document Structure

```markdown
# Feature Name - Architecture Design

## 1. Project Context

- Language: TypeScript
- Framework: Express.js
- Architecture: Layered (Controller → Service → Repository)
- Database: PostgreSQL

## 2. Feature Overview

High-level description of what this feature does

## 3. Data Models

### User

- id: string (UUID)
- email: string (unique, validated)
- passwordHash: string (bcrypt)
- createdAt: timestamp

### SessionToken

- token: string (JWT)
- userId: string (foreign key)
- expiresAt: timestamp

## 4. Service Interfaces

### AuthService

- login(email: string, password: string) → SessionToken
  - Validates credentials
  - Generates session token
  - Handles errors (invalid credentials, user not found)

### TokenService

- generate(userId: string) → string
- validate(token: string) → boolean

## 5. Architecture Decisions

- Use JWT for stateless authentication
- Hash passwords with bcrypt (cost factor: 10)
- Token expiration: 24 hours

## 6. Scenario Mapping

| Scenario         | Models             | Services                  | Methods             |
| ---------------- | ------------------ | ------------------------- | ------------------- |
| Successful login | User, SessionToken | AuthService, TokenService | login(), generate() |
| Invalid password | User               | AuthService               | login()             |

## 7. File Structure

src/
├── models/
│ ├── User.ts
│ └── SessionToken.ts
├── services/
│ ├── AuthService.ts
│ └── TokenService.ts
└── repositories/
└── UserRepository.ts
```

#### Key Principles

- **Language-Agnostic**: Describe interfaces, not implementations
- **High-Level**: Focus on components, not algorithms
- **Context-Aware**: Adapt to existing project structure
- **Traceable**: Map back to Gherkin scenarios

---

### I - Implement (Implementation)

**Purpose**: Build the actual code based on architecture.

Implementation is where the architecture design becomes executable code. The engineer follows the architecture document to ensure consistency and completeness.

#### Why Architecture-Driven Implementation?

1. **Clarity**: No guesswork about what to build
2. **Consistency**: Follows project conventions
3. **Completeness**: All scenarios are covered
4. **Traceability**: Each code path maps to a Gherkin scenario

#### Implementation Principles

**1. Follow the Architecture**

- Implement exactly what's defined in architecture.md
- Use specified data models and interfaces
- Place files in designated locations

**2. Scenario-Driven Code**
Each Gherkin scenario should have corresponding code:

```typescript
// Scenario: Successful login
async login(email: string, password: string): Promise<SessionToken> {
  // Given: registered user
  const user = await this.userRepo.findByEmail(email);
  if (!user) {
    throw new Error('User not found'); // Error scenario
  }

  // Given: correct password
  const isValid = await bcrypt.compare(password, user.passwordHash);
  if (!isValid) {
    throw new Error('Invalid password'); // Invalid password scenario
  }

  // When: submit credentials (already done by calling this method)

  // Then: authenticate and generate token
  const token = await this.tokenService.generate(user.id);
  return token;
}
```

**3. Given-When-Then Mapping**

- **Given**: Input validation and precondition checks
- **When**: Core business logic execution
- **Then**: Return values and side effects

**4. Handle All Scenarios**
Ensure code covers:

- Happy path (successful scenarios)
- Edge cases (boundary conditions)
- Error scenarios (validation failures, exceptions)

#### Code Quality Guidelines

- Follow project coding standards
- Write clean, readable code
- No over-engineering
- Implement only what's specified
- Add error handling for all scenarios

---

## The GSI Workflow

### Core 4-Phase Process

```
Phase 1: Gherkin (PM Role)
   ↓
Phase 2: Structure (Architect Role)
   ↓
Phase 3: Implement (Engineer Role)
   ↓
Phase 4: Verification (QA Role)
```

### Phase Details

#### Phase 1: Specification (PM)

**Input**: User requirement
**Output**: `features/{feature}.feature`
**Role**: Product Manager

The PM translates business requirements into Gherkin scenarios, focusing on:

- What the feature should do
- Business rules and constraints
- Edge cases and error conditions
- User perspective and value

#### Phase 2: Architecture (Architect)

**Input**: Gherkin specification
**Output**: `docs/features/{feature}/architecture.md`
**Role**: Software Architect

The architect designs the technical structure:

- Analyzes project context (tech stack, patterns)
- Extracts data models from Gherkin nouns
- Defines service interfaces from Gherkin verbs
- Creates language-agnostic design
- Plans file structure

#### Phase 3: Implementation (Engineer)

**Input**: Architecture design + Gherkin spec
**Output**: Source code files
**Role**: Software Engineer

The engineer implements the design:

- Follows architecture document exactly
- Ensures all Gherkin scenarios are covered
- Places files in specified locations
- Writes clean, production-ready code

#### Phase 4: Verification (QA)

**Input**: Gherkin + Architecture + Implementation
**Output**: `docs/features/{feature}/conclusion.md`
**Role**: Quality Assurance

The QA verifies:

- Architecture compliance (models, interfaces, files)
- Scenario coverage (all Given-When-Then paths)
- Implementation correctness
- Generates pass/fail report

---

## Optional: Integration Tests

### BDD Integration Testing (Optional Phase)

**Command**: `/sdd-integration-test`
**When to Use**: Test-Driven Development (TDD) workflow

Integration tests are **optional** but highly recommended for:

- Critical business logic
- Complex scenarios
- Test-driven development
- Continuous integration pipelines

#### Test-First Workflow

```
/sdd-spec <requirement>
   ↓
/sdd-arch features/feature.feature
   ↓
/sdd-integration-test features/feature.feature  ← Optional but recommended
   ↓
/sdd-impl features/feature.feature
   ↓
/sdd-verify features/feature.feature
```

#### Generated Tests

Integration tests are generated directly from Gherkin scenarios:

```typescript
describe("User Authentication", () => {
  describe("Scenario: Successful login", () => {
    it("should authenticate user and generate token", async () => {
      // Given: registered user
      const user = await createTestUser({
        email: "user@example.com",
        password: "SecurePass123",
      });

      // When: submit login credentials
      const result = await authService.login(
        "user@example.com",
        "SecurePass123",
      );

      // Then: authenticated with token
      expect(result.token).toBeDefined();
      expect(result.userId).toBe(user.id);
    });
  });

  describe("Scenario: Invalid password", () => {
    it("should fail authentication", async () => {
      // Given: registered user
      await createTestUser({
        email: "user@example.com",
        password: "SecurePass123",
      });

      // When: submit wrong password
      const promise = authService.login("user@example.com", "WrongPassword");

      // Then: authentication fails
      await expect(promise).rejects.toThrow("Invalid password");
    });
  });
});
```

#### Benefits of Integration Tests

1. **Executable Specifications**: Gherkin becomes runnable tests
2. **Regression Prevention**: Detect breaking changes
3. **Documentation**: Tests serve as usage examples
4. **Confidence**: Verify system behavior end-to-end

#### When to Skip Integration Tests

- Simple CRUD operations
- Proof of concept projects
- Rapid prototyping
- Time-constrained situations

---

## Key Benefits of GSI-Protocol

### 1. **Clarity Through Separation**

Each phase has a clear purpose:

- Gherkin: Business requirements
- Structure: Technical design
- Implementation: Code

### 2. **Language Agnostic**

The same Gherkin and architecture can be implemented in:

- TypeScript, Python, Go, Java, C#, etc.
- Any framework or tech stack

### 3. **Team Collaboration**

- PM focuses on business value
- Architect designs system structure
- Engineer implements with clarity
- QA verifies completeness

### 4. **Quality Assurance**

- Specifications are testable
- Architecture is reviewable
- Implementation is verifiable
- All scenarios are covered

### 5. **Maintainability**

- Clear documentation (Gherkin + Architecture)
- Traceable requirements
- Consistent code structure
- Easy onboarding for new team members

### 6. **Flexibility**

- Optional integration tests for TDD
- Manual or automatic workflow
- Project-aware adaptation

---

## Comparison with Other Methodologies

### GSI vs Traditional Development

| Aspect         | Traditional                   | GSI-Protocol                    |
| -------------- | ----------------------------- | ------------------------------- |
| Requirements   | Often unclear or changing     | Clear Gherkin scenarios         |
| Architecture   | Sometimes skipped or informal | Explicit, documented design     |
| Implementation | Direct from requirements      | Guided by architecture          |
| Verification   | Manual testing                | Automated scenario verification |
| Documentation  | Written after (if at all)     | Generated during development    |

### GSI vs BDD (Behavior-Driven Development)

| Aspect         | BDD            | GSI-Protocol                 |
| -------------- | -------------- | ---------------------------- |
| Gherkin        | Yes            | Yes (G)                      |
| Architecture   | Not emphasized | Core pillar (S)              |
| Implementation | Test-driven    | Architecture-driven          |
| Tests          | Required       | Optional (integration tests) |

GSI-Protocol can be seen as **BDD + Architecture-First Design**, where the architecture phase bridges requirements and implementation.

---

## Best Practices

### 1. Start with Gherkin

Always begin with clear business scenarios before thinking about code.

### 2. Review Architecture

Have architecture reviewed by team before implementation.

### 3. Follow Architecture Exactly

Don't deviate from the design during implementation.

### 4. Verify Every Scenario

Ensure all Given-When-Then paths are covered in code.

### 5. Iterate on Failures

If verification fails, fix and re-verify until all scenarios pass.

### 6. Use Integration Tests Wisely

Add them for critical features, but don't over-test simple operations.

### 7. Keep Documentation Updated

Gherkin and architecture should always reflect current implementation.

---

## Conclusion

GSI-Protocol provides a structured, repeatable process for building software that:

- Starts with clear business requirements (Gherkin)
- Designs thoughtful architecture (Structure)
- Implements with precision (Implement)
- Verifies completeness (Verification)
- Optionally includes integration tests (TDD)

By following the **G-S-I** pillars, teams can build high-quality software with clear traceability from requirements to code, while maintaining flexibility to adapt to any technology stack.

The optional integration test phase enhances the workflow for teams practicing test-driven development, but the core 4-phase process remains the foundation of GSI-Protocol.
