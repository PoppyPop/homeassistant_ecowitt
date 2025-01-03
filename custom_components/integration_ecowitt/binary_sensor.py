"""Support for Ecowitt Weather Stations."""

import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.const import STATE_OFF
from homeassistant.const import STATE_ON
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.dispatcher import async_dispatcher_connect

from . import async_add_ecowitt_entities
from . import EcowittEntity
from .const import DOMAIN
from .const import REG_ENTITIES
from .const import SIGNAL_ADD_ENTITIES
from .const import TYPE_BINARY_SENSOR

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Add sensors if new."""

    async def add_entities(discovery_info=None):
        await async_add_ecowitt_entities(
            hass,
            entry,
            EcowittBinarySensor,
            BINARY_SENSOR_DOMAIN,
            async_add_entities,
            discovery_info,
        )

    signal = f"{SIGNAL_ADD_ENTITIES}_{BINARY_SENSOR_DOMAIN}"
    async_dispatcher_connect(hass, signal, add_entities)
    await add_entities(
        hass.data[DOMAIN][entry.entry_id][REG_ENTITIES][TYPE_BINARY_SENSOR]
    )


class EcowittBinarySensor(EcowittEntity, BinarySensorEntity):
    """Definition of a binary sensor."""

    def __init__(self, hass, entry, key, name, dc, uom, icon, sc):
        """Initialize the sensor."""
        super().__init__(hass, entry, key, name)
        self._icon = icon
        self._uom = uom
        self._dc = dc

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        if self._key in self._ws.last_values:
            if self._ws.last_values[self._key] > 0:
                return True
        else:
            _LOGGER.warning(
                "Sensor %s not in last update, check range or battery", self._key
            )
            return None
        return False

    @property
    def state(self):
        """Return the state of the binary sensor."""
        # Don't claim a leak is cleared if the sensor is out of range
        if self.is_on is None:
            return STATE_UNKNOWN
        return STATE_ON if self.is_on else STATE_OFF

    @property
    def device_class(self):
        """Return the device class."""
        return self._dc
