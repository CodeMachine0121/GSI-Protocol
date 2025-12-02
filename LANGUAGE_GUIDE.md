# SDD Language Guide

This guide shows how the SDD workflow adapts to different programming languages while maintaining the same core methodology.

## Core Principle

**The SDD workflow is language-agnostic.** While the Gherkin specification (Phase 1) remains identical across languages, Phases 2-4 adapt to use language-specific idioms and best practices.

## Language Support

### Tier 1: Full Support with Examples
- **Python** - Examples with dataclasses, Pydantic, and ABC
- **TypeScript** - Examples with interfaces and types

### Tier 2: Documented Patterns
- **Go** - Structs and interfaces
- **Java** - Interfaces and POJOs
- **Rust** - Structs and traits
- **C#** - Interfaces and records

### Tier 3: Any Language
The methodology works with any language that supports:
- Data structures (structs, classes, records)
- Type definitions (explicit or implicit)
- Function/method definitions

## Language-Specific Patterns

### Python

**Strengths:**
- Multiple options: dataclasses, Pydantic, TypedDict
- ABC for interfaces
- Dynamic typing with type hints

**Phase 2 - Structure:**
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

class Status(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

@dataclass
class User:
    id: str
    status: Status

class IUserService(ABC):
    @abstractmethod
    def activate(self, user_id: str) -> User:
        pass
```

**When to use:**
- Rapid prototyping
- Data science applications
- Backend services
- Scripting

**Dependencies:**
```bash
pip install pydantic  # If using Pydantic for validation
```

---

### TypeScript

**Strengths:**
- Strong compile-time type checking
- Interface-based design
- Excellent IDE support

**Phase 2 - Structure:**
```typescript
enum Status {
  ACTIVE = "ACTIVE",
  INACTIVE = "INACTIVE"
}

interface User {
  id: string;
  status: Status;
}

interface IUserService {
  activate(userId: string): User;
}
```

**When to use:**
- Frontend applications
- Node.js backends
- Full-stack web development
- Projects requiring strong typing

**Dependencies:**
```bash
npm install typescript --save-dev
```

---

### Go

**Strengths:**
- Simple, explicit interfaces
- Built-in concurrency
- Fast compilation and execution

**Phase 2 - Structure:**
```go
package user

type Status string

const (
    StatusActive   Status = "ACTIVE"
    StatusInactive Status = "INACTIVE"
)

type User struct {
    ID     string
    Status Status
}

type UserService interface {
    Activate(userID string) (User, error)
}
```

**When to use:**
- Microservices
- Cloud infrastructure
- CLI tools
- High-performance backends

**No external dependencies needed**

---

### Java

**Strengths:**
- Enterprise-ready
- Strong OOP support
- Rich ecosystem

**Phase 2 - Structure:**
```java
public enum Status {
    ACTIVE,
    INACTIVE
}

public class User {
    private String id;
    private Status status;

    // Constructor, getters, setters
}

public interface IUserService {
    User activate(String userId);
}
```

**When to use:**
- Enterprise applications
- Android development
- Large-scale systems
- Legacy system integration

**Dependencies (Maven):**
```xml
<!-- Add validation libraries if needed -->
```

---

### Rust

**Strengths:**
- Memory safety without garbage collection
- Powerful type system
- Zero-cost abstractions

**Phase 2 - Structure:**
```rust
#[derive(Debug, Clone, PartialEq)]
pub enum Status {
    Active,
    Inactive,
}

#[derive(Debug, Clone)]
pub struct User {
    pub id: String,
    pub status: Status,
}

pub trait UserService {
    fn activate(&self, user_id: &str) -> Result<User, Error>;
}
```

**When to use:**
- Systems programming
- WebAssembly
- High-performance applications
- Safety-critical software

**Dependencies (Cargo.toml):**
```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
```

---

### C#

**Strengths:**
- .NET ecosystem
- Modern language features
- Unity game development

**Phase 2 - Structure:**
```csharp
public enum Status
{
    Active,
    Inactive
}

public record User(string Id, Status Status);

public interface IUserService
{
    User Activate(string userId);
}
```

**When to use:**
- .NET applications
- Windows desktop apps
- Unity games
- Azure cloud services

---

## Choosing the Right Language

### Questions to Ask

1. **What is your existing codebase?**
   - Use the same language for consistency

2. **What is your team familiar with?**
   - Leverage existing expertise

3. **What are your performance requirements?**
   - Go, Rust: High performance
   - Python, TypeScript: Developer productivity

4. **What is your deployment target?**
   - Frontend: TypeScript
   - Backend: Any (Python, Go, Java, etc.)
   - Mobile: Kotlin, Swift
   - WebAssembly: Rust

5. **What is your type safety requirement?**
   - Strict: TypeScript, Rust, Go
   - Flexible: Python, Ruby

## SDD Workflow Across Languages

### Phase 1: Specification (Gherkin)
**Always the same across all languages**

```gherkin
Feature: User Activation
  Scenario: Activate inactive user
    Given user status is INACTIVE
    When user is activated
    Then user status should be ACTIVE
```

### Phase 2: Structure
**Adapts to language idioms:**

| Language | Data Model | Interface | Enum |
|----------|------------|-----------|------|
| Python | dataclass/@dataclass | ABC | Enum |
| TypeScript | interface | interface | enum |
| Go | struct | interface | const |
| Java | class | interface | enum |
| Rust | struct | trait | enum |
| C# | record | interface | enum |

### Phase 3: Implementation
**Uses language-specific patterns:**

| Language | Pattern | Error Handling |
|----------|---------|----------------|
| Python | class implementation | try/except, Optional |
| TypeScript | class implementation | try/catch, undefined |
| Go | struct methods | error return value |
| Java | class implementation | try/catch, Exceptions |
| Rust | impl for trait | Result<T, E> |
| C# | class implementation | try/catch, nullable |

### Phase 4: Verification
**Uses language testing frameworks:**

| Language | Test Framework | Assertion Library |
|----------|---------------|-------------------|
| Python | pytest, unittest | assert, pytest |
| TypeScript | Jest, Mocha | expect, assert |
| Go | testing | testing.T |
| Java | JUnit | JUnit assertions |
| Rust | cargo test | assert! macros |
| C# | xUnit, NUnit | Assert |

## Best Practices

### Universal Principles

1. **Strong Typing**: Use the strongest typing available in your language
2. **Clear Naming**: Follow language conventions (camelCase, snake_case, etc.)
3. **Documentation**: Map code back to Gherkin scenarios in comments
4. **Validation**: Validate at boundaries, trust internal code
5. **Simplicity**: Don't over-engineer, implement only what Gherkin specifies

### Language-Specific Tips

**Python:**
- Use type hints even though they're optional
- Prefer dataclasses over plain classes
- Consider Pydantic for validation-heavy code

**TypeScript:**
- Enable `strict` mode in tsconfig.json
- Use `interface` over `type` for contracts
- Leverage union types for error handling

**Go:**
- Keep interfaces small and focused
- Return errors explicitly
- Use struct embedding sparingly

**Java:**
- Prefer immutable objects where possible
- Use record classes (Java 14+)
- Leverage Optional for nullable values

**Rust:**
- Embrace Result<T, E> for error handling
- Use derive macros for common traits
- Leverage borrowing instead of cloning

**C#:**
- Use records for immutable data
- Leverage nullable reference types
- Use async/await for I/O operations

## Migration Between Languages

### Same Feature, Different Language

The SDD workflow makes cross-language migration systematic:

1. **Gherkin stays the same** (Phase 1)
2. **Map data models** to new language (Phase 2)
3. **Map interfaces** to new language (Phase 2)
4. **Translate implementation logic** (Phase 3)
5. **Verify against same Gherkin** (Phase 4)

### Example: Python → TypeScript

**Python:**
```python
@dataclass
class User:
    id: str
    points: int
```

**TypeScript:**
```typescript
interface User {
  id: string;
  points: number;
}
```

**The Gherkin and logic remain identical!**

## Getting Help

When using SDD with a new language:

1. Check the `examples/` directory for similar languages
2. Review language-specific documentation for type systems
3. Ask the AI: "Implement this in [language] using idiomatic patterns"
4. Start with Phase 1 (Gherkin) - it's always the same
5. Let the AI adapt Phases 2-4 to your language

## Contributing

Help expand language support:

1. Create examples in new languages
2. Document language-specific patterns
3. Share best practices
4. Report issues with language-specific adaptations

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

**Remember:** The power of SDD is in the methodology, not the language. Focus on clear specifications first, then let the implementation adapt to your chosen language.
