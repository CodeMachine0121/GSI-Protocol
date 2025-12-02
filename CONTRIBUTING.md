# Contributing to SDD Workflow

Thank you for your interest in contributing to the SDD Workflow project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists in the issue tracker
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Example Gherkin/code if applicable

### Contributing Code

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit using descriptive commit messages
6. Push to your fork
7. Create a Pull Request

### Contributing Examples

We love new examples! To add an example:

1. Create a new directory under `examples/<your-feature>/`
2. Include all 4 phase outputs:
   - `spec.feature` - Gherkin specification
   - `structure.py` (or `.ts`) - Data models and interfaces
   - `implementation.py` (or `.ts`) - Concrete implementation
   - `README.md` - Explanation of the example
3. Ensure the example is complete and working
4. Test it with the SDD workflow commands

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add more examples or use cases
- Improve prompt templates
- Translate documentation (future)

### Improving Slash Commands

If you want to improve the slash commands:
1. Test your changes thoroughly
2. Ensure backward compatibility
3. Update documentation
4. Provide examples of the improved behavior

## Development Guidelines

### Prompt Writing

When writing or improving prompts:
- Be clear and specific about constraints
- Use examples to illustrate concepts
- Reference the expected_workflow.md for alignment
- Test prompts with various inputs

### Code Examples

When adding code examples:
- Use type hints (Python) or strict typing (TypeScript)
- Follow the SDD philosophy: Spec → Structure → Implementation
- Include comments mapping code to Gherkin
- Add verification/tests

### Gherkin Specifications

When writing Gherkin examples:
- Follow Given-When-Then format strictly
- Use concrete values, not variables
- Cover happy path, edge cases, and error cases
- Keep scenarios focused and atomic

## Code Style

### Python
- Follow PEP 8
- Use type hints
- Use Pydantic for data models
- Use ABC for interfaces

### TypeScript
- Use strict TypeScript
- Follow standard conventions
- Use interfaces for contracts

### Gherkin
- Feature: Sentence case
- Scenario: Sentence case
- Steps: Lowercase except proper nouns
- Indent: 2 spaces

## Testing

Before submitting:
1. Test slash commands work correctly
2. Verify examples run without errors
3. Check that all 4 phases work together
4. Validate Gherkin syntax

## Pull Request Process

1. Update documentation for any changed functionality
2. Add or update examples if applicable
3. Ensure all examples still work
4. Update CHANGELOG.md (if exists)
5. Request review from maintainers

## Code Review

Reviewers will check:
- Alignment with SDD philosophy
- Code quality and clarity
- Documentation completeness
- Example correctness
- Backward compatibility

## Community

- Be respectful and constructive
- Help others learn the SDD approach
- Share your success stories
- Report what works and what doesn't

## Questions?

If you have questions:
- Check the README.md
- Review existing examples
- Look at expected_workflow.md
- Open a discussion issue

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make SDD Workflow better!
