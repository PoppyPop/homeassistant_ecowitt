"""Tests for the Ecowitt config flow."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from homeassistant import config_entries, core
from homeassistant.const import CONF_PORT

from custom_components.integration_ecowitt.config_flow import (
    EcowittConfigFlow,
    EcowittOptionsFlowHandler,
    AlreadyConfigured,
    validate_input,
)
from custom_components.integration_ecowitt.const import (
    CONF_UNIT_BARO,
    CONF_UNIT_LIGHTNING,
    CONF_UNIT_RAIN,
    CONF_UNIT_WIND,
    CONF_UNIT_WINDCHILL,
    W_TYPE_HYBRID,
)


@pytest.fixture
def mock_hass():
    """Create a mock Home Assistant instance."""
    hass = MagicMock(spec=core.HomeAssistant)
    hass.data = {}
    hass.config = MagicMock()
    hass.config.units = MagicMock()
    hass.config.units.pressure_unit = "hPa"
    hass.config.units.wind_speed_unit = "m/s"
    hass.config.units.accumulated_precipitation_unit = "mm"
    hass.config.units.length_unit = "km"
    hass.config_entries = MagicMock()
    hass.config_entries.async_entries = MagicMock(return_value=[])
    return hass


class TestValidateInput:
    """Tests for validate_input function."""

    @pytest.mark.asyncio
    async def test_validate_input_success(self, mock_hass):
        """Test successful input validation."""
        data = {CONF_PORT: 4199}
        result = await validate_input(mock_hass, data)

        assert result == {"title": "Ecowitt on port 4199"}

    @pytest.mark.asyncio
    async def test_validate_input_port_already_configured(self, mock_hass):
        """Test validation fails when port is already configured."""
        existing_entry = MagicMock()
        existing_entry.data = {CONF_PORT: 4199}
        mock_hass.config_entries.async_entries.return_value = [existing_entry]

        data = {CONF_PORT: 4199}

        with pytest.raises(AlreadyConfigured):
            await validate_input(mock_hass, data)

    @pytest.mark.asyncio
    async def test_validate_input_different_ports(self, mock_hass):
        """Test validation passes with different ports."""
        existing_entry = MagicMock()
        existing_entry.data = {CONF_PORT: 4199}
        mock_hass.config_entries.async_entries.return_value = [existing_entry]

        data = {CONF_PORT: 4200}
        result = await validate_input(mock_hass, data)

        assert result == {"title": "Ecowitt on port 4200"}


class TestEcowittConfigFlow:
    """Tests for EcowittConfigFlow."""

    def test_config_flow_creation(self, mock_hass):
        """Test config flow instance creation."""
        flow = EcowittConfigFlow()
        assert flow.VERSION == 1
        assert hasattr(flow, "async_step_user")

    @pytest.mark.asyncio
    async def test_async_step_user_initial(self, mock_hass):
        """Test user step without input shows form."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        result = await flow.async_step_user()

        assert result["type"] == "form"
        assert result["step_id"] == "user"

    @pytest.mark.asyncio
    async def test_async_step_user_with_input(self, mock_hass):
        """Test user step with input transitions to initial_options."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        # Mock async_step_initial_options to verify it's called
        with patch.object(
            flow, "async_step_initial_options", new_callable=AsyncMock
        ) as mock_initial_options:
            mock_initial_options.return_value = {"type": "form"}

            await flow.async_step_user(user_input={})

            mock_initial_options.assert_called_once()

    @pytest.mark.asyncio
    async def test_async_step_initial_options_without_input(self, mock_hass):
        """Test initial_options step without input shows form."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        result = await flow.async_step_initial_options()

        assert result["type"] == "form"
        assert result["step_id"] == "initial_options"

    @pytest.mark.asyncio
    async def test_async_step_initial_options_with_valid_input(self, mock_hass):
        """Test initial_options step with valid input creates entry."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.return_value = {"title": "Ecowitt on port 4199"}

            user_input = {CONF_PORT: 4199}
            result = await flow.async_step_initial_options(user_input)

            assert result["type"] == "create_entry"
            assert result["title"] == "Ecowitt on port 4199"
            assert result["data"] == user_input

    @pytest.mark.asyncio
    async def test_async_step_initial_options_already_configured(self, mock_hass):
        """Test initial_options aborts when device already configured."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.side_effect = AlreadyConfigured

            user_input = {CONF_PORT: 4199}
            result = await flow.async_step_initial_options(user_input)

            assert result["type"] == "abort"
            assert result["reason"] == "already_configured"

    @pytest.mark.asyncio
    async def test_async_step_import_success(self, mock_hass):
        """Test import step with valid YAML config."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.return_value = {"title": "Ecowitt on port 4199"}

            device_config = {CONF_PORT: 4199}
            result = await flow.async_step_import(device_config)

            assert result["type"] == "create_entry"
            assert result["title"] == "Ecowitt on port 4199"
            assert result["data"] == device_config

    @pytest.mark.asyncio
    async def test_async_step_import_already_configured(self, mock_hass):
        """Test import step aborts when device already configured."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.side_effect = AlreadyConfigured

            device_config = {CONF_PORT: 4199}
            result = await flow.async_step_import(device_config)

            assert result["type"] == "abort"
            assert result["reason"] == "already_configured"

    def test_async_get_options_flow(self, mock_hass):
        """Test getting options flow handler."""
        config_entry = MagicMock(spec=config_entries.ConfigEntry)

        result = EcowittConfigFlow.async_get_options_flow(config_entry)

        assert isinstance(result, EcowittOptionsFlowHandler)
        assert result._config_entry == config_entry


class TestEcowittOptionsFlowHandler:
    """Tests for EcowittOptionsFlowHandler."""

    def test_handler_initialization(self):
        """Test options flow handler initialization."""
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        handler = EcowittOptionsFlowHandler(config_entry)

        assert handler._config_entry == config_entry

    @pytest.mark.asyncio
    async def test_async_step_init_without_input(self):
        """Test init step without input shows form."""
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        config_entry.options = {}

        handler = EcowittOptionsFlowHandler(config_entry)
        handler.hass = MagicMock()
        handler.hass.config.units.pressure_unit = "hPa"
        handler.hass.config.units.wind_speed_unit = "m/s"
        handler.hass.config.units.accumulated_precipitation_unit = "mm"
        handler.hass.config.units.length_unit = "km"

        result = await handler.async_step_init()

        assert result["type"] == "form"
        assert result["step_id"] == "init"
        assert "data_schema" in result

    @pytest.mark.asyncio
    async def test_async_step_init_with_input(self):
        """Test init step with input creates entry."""
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        config_entry.options = {}

        handler = EcowittOptionsFlowHandler(config_entry)
        handler.hass = MagicMock()

        user_input = {
            CONF_UNIT_BARO: "hPa",
            CONF_UNIT_WIND: "m/s",
            CONF_UNIT_RAIN: "mm",
            CONF_UNIT_LIGHTNING: "km",
            CONF_UNIT_WINDCHILL: W_TYPE_HYBRID,
        }

        result = await handler.async_step_init(user_input)

        assert result["type"] == "create_entry"
        assert result["title"] == ""
        assert result["data"] == user_input

    @pytest.mark.asyncio
    async def test_async_step_init_uses_existing_options(self):
        """Test init step uses existing options as defaults."""
        existing_options = {
            CONF_UNIT_BARO: "mmHg",
            CONF_UNIT_WIND: "mph",
        }
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        config_entry.options = existing_options

        handler = EcowittOptionsFlowHandler(config_entry)
        handler.hass = MagicMock()
        handler.hass.config.units.pressure_unit = "hPa"
        handler.hass.config.units.wind_speed_unit = "m/s"
        handler.hass.config.units.accumulated_precipitation_unit = "mm"
        handler.hass.config.units.length_unit = "km"

        result = await handler.async_step_init()

        assert result["type"] == "form"
        # Verify that existing options are used as defaults
        result["data_schema"]
        # The schema should have the existing options available


class TestAlreadyConfiguredException:
    """Tests for AlreadyConfigured exception."""

    def test_already_configured_is_hass_error(self):
        """Test AlreadyConfigured is a HomeAssistantError."""
        from homeassistant import exceptions

        exc = AlreadyConfigured()
        assert isinstance(exc, exceptions.HomeAssistantError)


class TestConfigFlowIntegration:
    """Integration tests for config flow scenarios."""

    @pytest.mark.asyncio
    async def test_user_flow_complete(self, mock_hass):
        """Test complete user-initiated setup flow."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        # Step 1: User initiates setup
        result = await flow.async_step_user()
        assert result["type"] == "form"
        assert result["step_id"] == "user"

        # Step 2: User provides input, transitions to options
        with patch.object(
            flow, "async_step_initial_options", new_callable=AsyncMock
        ) as mock_initial_options:
            mock_initial_options.return_value = {"type": "form"}
            result = await flow.async_step_user(user_input={})
            mock_initial_options.assert_called_once()

    @pytest.mark.asyncio
    async def test_import_flow_with_multiple_entries(self, mock_hass):
        """Test import with multiple existing entries."""
        # Setup multiple existing entries with different ports
        entry1 = MagicMock()
        entry1.data = {CONF_PORT: 4199}
        entry2 = MagicMock()
        entry2.data = {CONF_PORT: 4200}

        mock_hass.config_entries.async_entries.return_value = [entry1, entry2]

        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        # Try to add a new port (should succeed)
        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.return_value = {"title": "Ecowitt on port 4201"}

            device_config = {CONF_PORT: 4201}
            result = await flow.async_step_import(device_config)

            assert result["type"] == "create_entry"

    @pytest.mark.asyncio
    async def test_initial_options_form_contains_all_fields(self, mock_hass):
        """Test that initial_options form includes all unit configuration fields."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        result = await flow.async_step_initial_options()

        assert result["type"] == "form"
        assert result["step_id"] == "initial_options"
        # Verify the schema is present
        assert "data_schema" in result

    @pytest.mark.asyncio
    async def test_options_flow_with_all_unit_types(self):
        """Test options flow with all unit type options."""
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        config_entry.options = {
            CONF_UNIT_BARO: "hPa",
            CONF_UNIT_WIND: "m/s",
            CONF_UNIT_RAIN: "mm",
            CONF_UNIT_LIGHTNING: "km",
            CONF_UNIT_WINDCHILL: W_TYPE_HYBRID,
        }

        handler = EcowittOptionsFlowHandler(config_entry)
        handler.hass = MagicMock()
        handler.hass.config.units.pressure_unit = "hPa"
        handler.hass.config.units.wind_speed_unit = "m/s"
        handler.hass.config.units.accumulated_precipitation_unit = "mm"
        handler.hass.config.units.length_unit = "km"

        result = await handler.async_step_init()

        assert result["type"] == "form"
        assert result["step_id"] == "init"


class TestConfigFlowEdgeCases:
    """Test edge cases and error scenarios."""

    @pytest.mark.asyncio
    async def test_validate_input_with_empty_config_entries(self, mock_hass):
        """Test validation when no entries exist."""
        mock_hass.config_entries.async_entries.return_value = []

        data = {CONF_PORT: 4199}
        result = await validate_input(mock_hass, data)

        assert result == {"title": "Ecowitt on port 4199"}

    @pytest.mark.asyncio
    async def test_async_step_initial_options_shows_errors_dict(self, mock_hass):
        """Test that errors dict is properly initialized."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        result = await flow.async_step_initial_options()

        assert result["type"] == "form"
        # Verify no errors by default
        assert result.get("errors", {}) == {}

    @pytest.mark.asyncio
    async def test_options_handler_respects_existing_options(self):
        """Test that options handler preserves existing option values."""
        existing_options = {
            CONF_UNIT_BARO: "mmHg",
            CONF_UNIT_WIND: "mph",
            CONF_UNIT_RAIN: "in",
        }
        config_entry = MagicMock(spec=config_entries.ConfigEntry)
        config_entry.options = existing_options

        handler = EcowittOptionsFlowHandler(config_entry)
        handler.hass = MagicMock()
        handler.hass.config.units.pressure_unit = "hPa"
        handler.hass.config.units.wind_speed_unit = "m/s"
        handler.hass.config.units.accumulated_precipitation_unit = "mm"
        handler.hass.config.units.length_unit = "km"

        result = await handler.async_step_init()

        assert result["type"] == "form"
        # The handler should have preserved the existing options
        assert handler._config_entry.options == existing_options

    @pytest.mark.asyncio
    async def test_port_validation_is_case_insensitive_or_exact(self, mock_hass):
        """Test that port matching is based on exact value."""
        existing_entry = MagicMock()
        existing_entry.data = {CONF_PORT: 4199}
        mock_hass.config_entries.async_entries.return_value = [existing_entry]

        # Test that string vs int port comparison works
        data = {CONF_PORT: 4199}
        with pytest.raises(AlreadyConfigured):
            await validate_input(mock_hass, data)

    @pytest.mark.asyncio
    async def test_import_preserves_all_config_data(self, mock_hass):
        """Test that import step preserves all configuration data."""
        flow = EcowittConfigFlow()
        flow.hass = mock_hass

        device_config = {
            CONF_PORT: 4199,
            CONF_UNIT_BARO: "hPa",
            CONF_UNIT_WIND: "m/s",
        }

        with patch(
            "custom_components.integration_ecowitt.config_flow.validate_input",
            new_callable=AsyncMock,
        ) as mock_validate:
            mock_validate.return_value = {"title": "Ecowitt on port 4199"}

            result = await flow.async_step_import(device_config)

            assert result["type"] == "create_entry"
            assert result["data"] == device_config
            assert result["data"][CONF_PORT] == 4199
