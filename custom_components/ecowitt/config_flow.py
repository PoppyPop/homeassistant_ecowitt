"""Config flow for ecowitt."""
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant import core
from homeassistant import exceptions
from homeassistant.const import CONF_PORT
from homeassistant.core import callback

from .const import CONF_UNIT_BARO
from .const import CONF_UNIT_LIGHTNING
from .const import CONF_UNIT_RAIN
from .const import CONF_UNIT_WIND
from .const import CONF_UNIT_WINDCHILL
from .const import DOMAIN
from .const import UNIT_BARO_OPTS
from .const import UNIT_LENGTH_OPTS
from .const import UNIT_PRECI_OPTS
from .const import UNIT_WIND_OPTS
from .const import W_TYPE_HYBRID
from .const import WINDCHILL_OPTS
from .schemas import (
    DATA_SCHEMA,
)


_LOGGER = logging.getLogger(__name__)


async def validate_input(hass: core.HomeAssistant, data):
    """Validate user input."""
    for entry in hass.config_entries.async_entries(DOMAIN):
        if entry.data[CONF_PORT] == data[CONF_PORT]:
            raise AlreadyConfigured
    return {"title": f"Ecowitt on port {data[CONF_PORT]}"}


class EcowittConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for the Ecowitt."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN

    async def async_step_import(self, device_config):
        """Import a configuration.yaml config, if any."""
        try:
            await validate_input(self.hass, device_config)
        except AlreadyConfigured:
            return self.async_abort(reason="already_configured")

        port = device_config[CONF_PORT]
        return self.async_create_entry(
            title=f"Ecowitt on port {port}", data=device_config
        )

    async def async_step_user(self, user_input=None):
        """Give initial instructions for setup."""
        if user_input is not None:
            return await self.async_step_initial_options()

        return self.async_show_form(step_id="user")

    async def async_step_initial_options(self, user_input=None):
        """Ask the user for the setup options."""
        errors = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                return self.async_create_entry(title=info["title"], data=user_input)
            except AlreadyConfigured:
                return self.async_abort(reason="already_configured")

        return self.async_show_form(
            step_id="initial_options", data_schema=DATA_SCHEMA, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Options flow."""
        return EcowittOptionsFlowHandler(config_entry)


class AlreadyConfigured(exceptions.HomeAssistantError):
    """Error to indicate this device is already configured."""


class EcowittOptionsFlowHandler(config_entries.OptionsFlow):
    """Ecowitt config flow options handler."""

    def __init__(self, config_entry):
        """Initialize HASS options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options_schema = vol.Schema(
            {
                vol.Optional(
                    CONF_UNIT_BARO,
                    default=self.config_entry.options.get(
                        CONF_UNIT_BARO,
                        self.hass.config.units.pressure_unit,
                    ),
                ): vol.In(UNIT_BARO_OPTS),
                vol.Optional(
                    CONF_UNIT_WIND,
                    default=self.config_entry.options.get(
                        CONF_UNIT_WIND,
                        self.hass.config.units.wind_speed_unit,
                    ),
                ): vol.In(UNIT_WIND_OPTS),
                vol.Optional(
                    CONF_UNIT_RAIN,
                    default=self.config_entry.options.get(
                        CONF_UNIT_RAIN,
                        self.hass.config.units.accumulated_precipitation_unit,
                    ),
                ): vol.In(UNIT_PRECI_OPTS),
                vol.Optional(
                    CONF_UNIT_LIGHTNING,
                    default=self.config_entry.options.get(
                        CONF_UNIT_LIGHTNING,
                        self.hass.config.units.length_unit,
                    ),
                ): vol.In(UNIT_LENGTH_OPTS),
                vol.Optional(
                    CONF_UNIT_WINDCHILL,
                    default=self.config_entry.options.get(
                        CONF_UNIT_WINDCHILL,
                        W_TYPE_HYBRID,
                    ),
                ): vol.In(WINDCHILL_OPTS),
            }
        )
        return self.async_show_form(step_id="init", data_schema=options_schema)
