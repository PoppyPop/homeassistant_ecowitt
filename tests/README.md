"""
Ecowitt Integration Tests

This directory contains the test suite for the Ecowitt Weather Station custom integration.

## Running Tests

### Run all tests:

```bash
pytest tests/
```

### Run specific test file:

```bash
pytest tests/test_config_flow.py -v
```

### Run with coverage report:

```bash
pytest tests/ --cov=custom_components.integration_ecowitt --cov-report=html
```

### Run specific test class:

```bash
pytest tests/test_config_flow.py::TestEcowittConfigFlow -v
```

### Run specific test method:

```bash
pytest tests/test_config_flow.py::TestEcowittConfigFlow::test_async_step_user_initial -v
```

## Test Structure

### test_config_flow.py

Tests for the configuration flow and options flow handlers:

- **TestValidateInput**: Tests for the `validate_input` function

  - Successful validation
  - Port already configured error handling
  - Different ports handling

- **TestEcowittConfigFlow**: Tests for `EcowittConfigFlow` class

  - Config flow instantiation
  - User step initialization and input handling
  - Initial options step with and without input
  - Import step for YAML migration
  - Already configured handling
  - Options flow retrieval

- **TestEcowittOptionsFlowHandler**: Tests for `EcowittOptionsFlowHandler` class

  - Options handler initialization
  - Init step form display
  - User input processing
  - Existing options preservation

- **TestConfigFlowIntegration**: Integration tests

  - Complete user-initiated setup flow
  - Import flow with multiple entries
  - Form field validation

- **TestConfigFlowEdgeCases**: Edge case and error scenario tests
  - Empty config entries handling
  - Error dictionary initialization
  - Existing options preservation
  - Port validation
  - Config data preservation during import

## Test Dependencies

The test suite requires:

- pytest
- pytest-asyncio
- pytest-cov
- pytest-homeassistant-custom-component

These are automatically installed when you run `pip install -r requirements.txt` in the dev environment.

## Coverage

The test suite aims for 100% coverage of the config_flow module. Current status:

- config_flow.py: **100% coverage**
- const.py: **100% coverage** (imported for tests)
- schemas.py: **100% coverage** (imported for tests)

## Adding New Tests

When adding new tests:

1. Follow the existing test naming conventions (test\__ for functions, Test_ for classes)
2. Use descriptive docstrings for each test
3. Use fixtures for common setup (see `mock_hass` fixture)
4. Use `@pytest.mark.asyncio` for async test functions
5. Patch external dependencies using `unittest.mock.patch`
6. Keep tests focused and independent

Example test structure:

```python
@pytest.mark.asyncio
async def test_new_feature(self, mock_hass):
    """Test description of what is being tested."""
    flow = EcowittConfigFlow()
    flow.hass = mock_hass

    result = await flow.async_step_new_feature()

    assert result["type"] == "form"
    assert result["step_id"] == "new_feature"
```

## Mocking

The test suite uses `unittest.mock` for creating mock objects:

- `MagicMock`: Generic mock object for most Home Assistant objects
- `AsyncMock`: For mocking async functions
- `patch`: For replacing imports and external calls

All tests mock `HomeAssistant` instance to avoid actual integrations.
"""
