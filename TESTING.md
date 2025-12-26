# Config Flow Test Suite Quick Reference

## Overview

Complete test suite for the Ecowitt integration's config flow with **26 tests**, **100% coverage** for the config_flow module.

## Files Created/Modified

### New Files

- `tests/test_config_flow.py` (467 lines) - Main test suite
- `tests/README.md` - Comprehensive testing documentation

### Modified Files

- `setup.cfg` - Updated pytest configuration to use correct module path

## Test Statistics

- **Total Tests**: 26
- **Passing**: 26 ✓
- **Coverage**: 100% (config_flow.py)
- **Execution Time**: ~0.86 seconds

## Test Structure

```
TestValidateInput (3 tests)
├── Input validation success
├── Port already configured error
└── Different ports handling

TestEcowittConfigFlow (9 tests)
├── Config flow creation
├── User step (initial)
├── User step (with input)
├── Initial options (no input)
├── Initial options (valid input)
├── Initial options (already configured)
├── Import (success)
├── Import (already configured)
└── Options flow retrieval

TestEcowittOptionsFlowHandler (4 tests)
├── Handler initialization
├── Init step (no input)
├── Init step (with input)
└── Init step (existing options)

TestConfigFlowIntegration (4 tests)
├── Complete user flow
├── Import with multiple entries
├── Form field validation
└── All unit types

TestConfigFlowEdgeCases (6 tests)
├── Empty config entries
├── Error dict initialization
├── Options preservation
├── Port validation
└── Config data preservation
```

## Quick Commands

```bash
# Run all config flow tests
pytest tests/test_config_flow.py -v

# Run with coverage report
pytest tests/ --cov=custom_components.integration_ecowitt

# Run specific test class
pytest tests/test_config_flow.py::TestEcowittConfigFlow -v

# Run specific test
pytest tests/test_config_flow.py::TestValidateInput::test_validate_input_success -v

# Run with short output
pytest tests/test_config_flow.py -q
```

## What's Tested

### Functions

- ✓ `validate_input()` - Port validation and collision detection

### Classes

- ✓ `EcowittConfigFlow` - User/import setup flows
- ✓ `EcowittOptionsFlowHandler` - Options management
- ✓ `AlreadyConfigured` - Exception handling

### Flows

- ✓ User-initiated setup (step_user → step_initial_options → create_entry)
- ✓ YAML import flow (step_import → create_entry)
- ✓ Options modification (step_init → create_entry)

### Error Cases

- ✓ Port already configured
- ✓ Duplicate entries
- ✓ Invalid input handling
- ✓ Options preservation

## Fixtures

### `mock_hass`

Provides a mocked Home Assistant instance with:

- Proper config units (pressure, wind speed, precipitation, length)
- Config entries system
- Default unit values for testing

## Test Approach

All tests use:

- `unittest.mock` for mocking (MagicMock, AsyncMock)
- `pytest` for test organization
- `@pytest.mark.asyncio` for async test support
- Descriptive docstrings for test documentation

## Coverage Report

When you run the tests, you'll see coverage like:

```
custom_components/integration_ecowitt/config_flow.py    61      0   100%
```

This means all 61 statements in config_flow.py are covered by tests.

## Next Steps

To expand testing:

1. Add tests for `sensor.py` and `binary_sensor.py`
2. Add tests for `__init__.py` (setup/unload)
3. Add integration tests with actual Home Assistant
4. Add tests for `diagnostics.py`

See `tests/README.md` for more details on test structure and best practices.
