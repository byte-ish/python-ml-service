# Testing the ML Microservice

This document provides a comprehensive guide to testing the ML microservice, including instructions for running tests, understanding test coverage, and adding new tests.

## Table of Contents
1. [Overview](#overview)
2. [Test Types](#test-types)
   - [Unit Tests](#unit-tests)
   - [Integration Tests](#integration-tests)
3. [Test Frameworks and Tools](#test-frameworks-and-tools)
4. [How to Run Tests](#how-to-run-tests)
5. [Test Coverage](#test-coverage)
6. [Adding New Tests](#adding-new-tests)
7. [Debugging Test Failures](#debugging-test-failures)

---

## Overview

Testing ensures the reliability and stability of the microservice by validating its components and functionality. The project uses `pytest` as the primary testing framework along with coverage analysis tools.

---

## Test Types

### Unit Tests
- **Purpose:** Test individual functions and methods in isolation.
- **Location:** `tests/unit/`
- **Examples:**
  - Testing the preprocessor and postprocessor logic.
  - Verifying the behavior of utility functions like JWT creation.

### Integration Tests
- **Purpose:** Validate the interaction between multiple components.
- **Location:** `tests/integration/`
- **Examples:**
  - Testing API endpoints with mocked models and preprocessor behavior.
  - Validating that the `/predict` endpoint handles inputs correctly.

---

## Test Frameworks and Tools

The following tools are used for testing:

1. **Pytest:** The core framework for writing and running tests.
2. **pytest-cov:** A plugin to measure code coverage during tests.
3. **Mocking Utilities:** Used to mock external dependencies like model loading or HTTP requests.
4. **FastAPI TestClient:** For testing FastAPI endpoints.

Install these tools using the command:
```bash
pip install pytest pytest-cov
```

---

## How to Run Tests

1. **Run All Tests**
   ```bash
   pytest
   ```

2. **Run Tests with Coverage**
   ```bash
   pytest --cov=app
   ```

3. **Run Specific Test Files**
   ```bash
   pytest tests/unit/test_preprocessor.py
   ```

4. **Run Tests with Detailed Output**
   ```bash
   pytest -v
   ```

---

## Test Coverage

Test coverage ensures that all critical code paths are tested.

### Viewing Coverage Report
1. Run tests with coverage:
   ```bash
   pytest --cov=app --cov-report=term-missing
   ```
2. Generate an HTML coverage report:
   ```bash
   pytest --cov=app --cov-report=html
   ```
   Open the report in a browser:
   ```bash
   open htmlcov/index.html
   ```

### Coverage Goals
- **Target Coverage:** 90% or higher.
- **Focus Areas for Improvement:**
  - Uncovered logic in `ModelRegistry`.
  - Error-handling paths in the prediction service.

---

## Adding New Tests

Follow these steps to add new tests:

### 1. Identify the Target Functionality
- Determine the specific functionality to be tested.
- Example: Add tests for a new preprocessing method.

### 2. Create Test Files
- Use the `tests/` directory to organize tests:
  - Unit tests: `tests/unit/`
  - Integration tests: `tests/integration/`

### 3. Write the Test
- Use `pytest` for writing test cases.
- Example test for a new numerical preprocessor:
  ```python
  from app.preprocessors.numerical_preprocessor import NumericalPreprocessor

  def test_numerical_preprocessor_valid_input():
      preprocessor = NumericalPreprocessor()
      input_data = {"input": [[1, 2], [3, 4]]}
      output = preprocessor.preprocess(input_data)
      assert output == {"features": [[1, 2], [3, 4]]}
  ```

### 4. Run and Validate
- Run the test and ensure it passes:
   ```bash
   pytest tests/unit/test_numerical_preprocessor.py
   ```

---

## Debugging Test Failures

### Common Issues
1. **Incorrect Test Setup:** Ensure the function or method being tested is properly mocked.
2. **Dependency Errors:** Verify all required dependencies are installed.
3. **Assertion Failures:** Check expected and actual outputs in test logs.

### Example Debugging Process
1. Run the failing test with verbose output:
   ```bash
   pytest -v tests/unit/test_prediction_service.py
   ```
2. Add debugging print statements or use a debugger:
   ```python
   import pdb; pdb.set_trace()
   ```

---

## Best Practices for Testing

1. **Isolate Tests:** Avoid dependencies between test cases.
2. **Mock External Dependencies:** Use `pytest-mock` or `unittest.mock` to isolate functionality.
3. **Test Edge Cases:** Cover various scenarios, including invalid inputs and boundary conditions.
4. **Automate Tests:** Integrate tests into CI/CD pipelines to ensure consistent validation.

---

## Conclusion

Testing is an essential part of maintaining a robust and reliable microservice. By following the guidelines in this document, you can ensure that the ML microservice meets high-quality standards.