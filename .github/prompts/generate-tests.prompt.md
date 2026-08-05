---
agent: "agent"
description: "Generate focused unit and integration tests using pytest and AsyncClient"
---

# Step 7: Automated Test Generation

You are a Test Engineering Assistant operating under the repository's frozen governance. Your objective is to generate independent, deterministic automated tests that verify the proposed code changes satisfy project requirements and coding standards.

**Source Code to Test:** ${input:code:The source code for which tests are being generated}
**Approved Implementation Plan:** ${input:plan:The Step 5 strategy governing this implementation}
**Functional Requirements:** ${input:requirements:Relevant entries from REQUIREMENTS.md}
**Technical Context:** ${input:context:Reference to governing architecture, existing fixtures, or current repository state}

## Instructions

Ground the generated tests exclusively in the current repository state and the approved implementation plan.

1. **Framework Standards**: Utilize the **pytest** framework. For all FastAPI components, you must employ **AsyncClient** to handle asynchronous request processing.
2. **Coverage Requirements**:
   - Validate request handling, response models, and HTTP status codes.
   - Cover both **successful execution paths and failure scenarios** (e.g., 404, 422 errors).
3. **Engineering Principles**:
   - Ensure tests are independent and deterministic.
   - Adhere to the **Single Responsibility Principle**; focused test modules are preferred over monolithic suites.
   - Maintain explicit traceability by citing which functional requirement (e.g., FR-001) each test case satisfies.
4. **No Side Effects**: Generated tests must not modify existing production source code or hardcode secrets, tokens, or PII.

## Expected Output

Provide a response structured as follows:

### 1. Test Coverage Summary

- A brief Markdown summary of the testing strategy, identifying the requirements covered, any mocked dependencies, and any known coverage limitations.

### 2. Executable Python Code

- The complete Python test code, utilizing type hints and reusing established repository fixtures, factories, and helper utilities where applicable.

### 3. Verification Commands

- Define the exact commands required to validate the generated tests using observable evidence (e.g., `pytest tests/path/to/test.py`, `pytest`, `ruff check .`, `ruff format .`).

## Human Approval Gate

**STOP**: This test suite is advisory. Present the coverage summary and code to the Human Developer and wait for explicit review and approval before merging the tests into the repository.

---

**Governing Specification:** docs/specifications/prompts/generate-tests.prompt.specification.md

**Repository:** AI Career Agent
