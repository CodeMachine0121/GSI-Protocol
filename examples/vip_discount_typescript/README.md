# Example: VIP Discount System (TypeScript)

This demonstrates the SDD workflow implemented in TypeScript, showing how the methodology works across different languages.

## Requirement

"Implement a VIP discount system where VIP users get 20% off purchases over $100."

## Phase Outputs

### Phase 1: Specification (`spec.feature`)
Gherkin scenarios defining:
- VIP users get 20% discount
- Normal users pay full price
- Minimum threshold of $100
- Invalid purchase rejection

### Phase 2: Structure (`structure.ts`)
TypeScript interfaces and types:
- `UserType` enum (VIP, NORMAL)
- `User`, `Purchase`, `DiscountResult` interfaces
- `IDiscountService` interface
- Business rule constants

### Phase 3: Implementation (`implementation.ts`)
Concrete `DiscountService` class implementing all scenarios with:
- Input validation
- Threshold checking
- Discount calculation
- Error handling

## Running the Example

### Prerequisites
```bash
# Install TypeScript and ts-node
npm install -g typescript ts-node

# Or use Node.js directly after compiling
```

### Option 1: Using ts-node
```bash
cd examples/vip_discount_typescript
ts-node implementation.ts
```

### Option 2: Compile and run
```bash
cd examples/vip_discount_typescript
tsc implementation.ts structure.ts
node implementation.js
```

## Expected Output

```
Running quick verification checks...

Test 1: Apply 20% discount to VIP user
✓ Scenario 1: VIP discount - PASSED

Test 2: No discount for normal users
✓ Scenario 2: No discount for normal users - PASSED

Test 3: No discount for purchases under threshold
✓ Scenario 3: No discount under threshold - PASSED

Test 4: Reject invalid purchase amount
✓ Scenario 4: Invalid purchase rejected - PASSED

============================================================
✅ All scenarios verified successfully!
============================================================

Ready for Phase 4: Formal Verification
```

## Key Observations

### Language-Specific Adaptations

**TypeScript vs Python:**
- TypeScript uses `interface` instead of Python's `ABC`
- TypeScript uses `enum` similar to Python
- Method naming: `camelCase` vs `snake_case`
- Type annotations: built-in vs imported from `typing`

**Core SDD Principles Remain:**
- Gherkin specification is identical
- Noun → Data Model mapping is the same
- Verb → Interface mapping is the same
- Implementation logic mirrors the structure

### Benefits of Type Safety

TypeScript's compile-time checking catches:
- Missing interface implementations
- Type mismatches in parameters
- Undefined properties
- Null/undefined handling

## Comparison with Python Example

| Aspect | Python | TypeScript |
|--------|--------|------------|
| Data Models | `@dataclass` or Pydantic | `interface` |
| Interfaces | `ABC` + `@abstractmethod` | `interface` |
| Enums | `str, Enum` | `enum` |
| Naming | `snake_case` | `camelCase` |
| Type System | Runtime (Pydantic) | Compile-time |
| Verification | Built-in assertions | Built-in assertions |

## Next Steps

- Add Jest tests for automated verification
- Integrate with a TypeScript project
- Try the same feature in Go or Rust
- Compare implementation complexity across languages

This example proves that SDD methodology transcends language boundaries!
