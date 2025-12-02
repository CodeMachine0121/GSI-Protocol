# SDD Workflow - Quick Start Guide

Get started with Specification-Driven Development in 5 minutes!

## Installation

### Option 1: Clone to Claude Code global directory
```bash
cd ~/.claude/workflows
git clone <repo-url> sdd-workflow
```

### Option 2: Clone to your project
```bash
cd your-project
git clone <repo-url> .sdd-workflow
# Or add as git submodule
git submodule add <repo-url> .sdd-workflow
```

### Option 3: Copy commands only
```bash
mkdir -p .claude/commands
cp path/to/sdd-workflow/.claude/commands/* .claude/commands/
```

### Install Dependencies

For Python examples:
```bash
pip install -r requirements.txt
```

For TypeScript examples (if available):
```bash
npm install
```

## Your First SDD Feature

### Step 1: Define Your Requirement

Think of a simple feature you want to implement. For example:
> "I need a discount system where VIP users get 20% off purchases over $100."

### Step 2: Run the Auto Workflow

In Claude Code, use the `/sdd-auto` command:

```
/sdd-auto I need a discount system where VIP users get 20% off purchases over $100
```

The agent will automatically:
1. Generate a Gherkin specification (`features/discount.feature`)
2. Design data models and interfaces (`structure/discount_structure.py`)
3. Implement the logic (`implementation/discount_impl.py`)
4. Verify against the specification

All in one go, without stopping between phases!

### Step 3: Review the Output

Check the generated files:
- `features/` - Your behavioral specifications
- `structure/` - Your data models and interfaces
- `implementation/` - Your working code

### Step 4: Run and Test

```bash
# For Python implementations
python implementation/discount_impl.py

# The built-in verification will run and show results
```

## Using Individual Phases

You can also run phases separately:

### Phase 1: Specification Only
```
/sdd-spec I need a user authentication system
```
This generates only the Gherkin `.feature` file.

### Phase 2: Structure Design
```
/sdd-arch features/authentication.feature
```
This reads your Gherkin and generates data models and interfaces.

### Phase 3: Implementation
```
/sdd-impl features/authentication.feature structure/authentication_structure.py
```
This generates the actual code implementation.

### Phase 4: Verification
```
/sdd-verify features/authentication.feature implementation/authentication_impl.py
```
This verifies your implementation against the specification.

## Examples Included

Check out the `examples/` directory:

### Referral Bonus System
```bash
cd examples/referral_bonus
python implementation.py
```

This shows a complete example with:
- 4 Gherkin scenarios (happy path, edge cases, errors)
- Fully typed data models
- Clean implementation
- Built-in verification

## Common Patterns

### Pattern 1: Quick Prototyping (Auto Mode)
```
/sdd-auto <entire requirement>
# Get everything generated at once - fastest way to test ideas
```

**Best for:** Exploring ideas, simple features, demos

### Pattern 2: Production Development (Manual Mode)
```
/sdd-spec <requirement>
# Review and refine the Gherkin
/sdd-arch features/<feature>.feature
# Review structure, adjust if needed
/sdd-impl features/<feature>.feature structure/<feature>_structure.py
# Review implementation carefully
/sdd-verify features/<feature>.feature implementation/<feature>_impl.py
```

**Best for:** Production code, complex features, team collaboration

### Pattern 3: Specification First
```
# Write your own .feature file manually
/sdd-arch features/my_feature.feature
/sdd-impl features/my_feature.feature structure/my_feature_structure.py
```

**Best for:** Well-defined requirements, API contracts, pre-existing specs

## Tips for Success

### Writing Good Requirements

✅ **Good:**
> "Users can search products by name. Results show product name, price, and stock status. If no results found, show 'No products found' message."

❌ **Too Vague:**
> "Add a search feature."

❌ **Too Technical:**
> "Create a REST API endpoint with pagination using PostgreSQL full-text search."

### Understanding the Output

Each phase builds on the previous:
- **Phase 1** = What (business behavior)
- **Phase 2** = Structure (data and interfaces)
- **Phase 3** = How (implementation logic)
- **Phase 4** = Verification (does it work?)

### When to Use Each Approach

**Use `/sdd-auto` (auto mode) when:**
- You have a clear, simple requirement
- You want to prototype quickly
- You trust the AI to handle all phases
- You need a working solution fast

**Use manual phases when:**
- You want to review each phase carefully
- The requirement is complex or ambiguous
- You want to write some phases manually
- You're learning the SDD methodology
- You're developing production code

## Troubleshooting

### Commands Not Found

Ensure Claude Code can see the commands:
```bash
ls .claude/commands/
# Should show: sdd-auto.md, sdd-spec.md, sdd-arch.md, etc.
```

### Import Errors in Python

Make sure you're in the right directory:
```bash
cd implementation/
python -c "import sys; sys.path.insert(0, '..'); from structure.feature_structure import *"
```

Or use absolute imports in your code.

### Gherkin Syntax Errors

Validate your Gherkin files:
- Each scenario needs Given-When-Then
- Indent with 2 spaces
- Start with Feature: declaration

## Next Steps

1. **Try the example:** Run `examples/referral_bonus/implementation.py`
2. **Read the workflow:** Check `expected_workflow.md` for detailed methodology
3. **Create your own:** Use `/sdd` with your own feature requirement
4. **Explore prompts:** Look at `prompts/` to understand each agent's role
5. **Contribute:** Add your examples to help others!

## Learning Resources

- `README.md` - Full project documentation
- `expected_workflow.md` - Detailed SDD methodology
- `prompts/` - Agent prompt templates
- `examples/` - Working examples
- `CONTRIBUTING.md` - How to contribute

## Getting Help

If you encounter issues:
1. Check the examples in `examples/`
2. Review the prompt templates in `prompts/`
3. Read the detailed workflow in `expected_workflow.md`
4. Open an issue on GitHub

---

**Ready to start?** Try it now:
```
/sdd-auto I need a simple todo list where users can add, complete, and delete tasks
```

Or step through manually:
```
/sdd-spec I need a simple todo list where users can add, complete, and delete tasks
```

Happy coding with SDD! 🚀
