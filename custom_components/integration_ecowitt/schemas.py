"""Schema definitions."""
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_PORT

from .const import CONF_NAME
from .const import CONF_UNIT_BARO
from .const import CONF_UNIT_LIGHTNING
from .const import CONF_UNIT_RAIN
from .const import CONF_UNIT_WIND
from .const import CONF_UNIT_WINDCHILL
from .const import DEFAULT_PORT
from .const import DOMAIN
from .const import W_TYPE_HYBRID

COMPONENT_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PORT): cv.port,
        vol.Optional(CONF_UNIT_BARO): cv.string,
        vol.Optional(CONF_UNIT_WIND): cv.string,
        vol.Optional(CONF_UNIT_RAIN): cv.string,
        vol.Optional(CONF_UNIT_LIGHTNING): cv.string,
        vol.Optional(CONF_UNIT_WINDCHILL, default=W_TYPE_HYBRID): cv.string,
    }
)

CONFIG_SCHEMA = vol.Schema({DOMAIN: COMPONENT_SCHEMA}, extra=vol.ALLOW_EXTRA)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_NAME, description={"suggested_value": "ecowitt"}): str,
    }
)
