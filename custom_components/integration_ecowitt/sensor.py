"""Support for Ecowitt Weather Stations."""

import logging

import homeassistant.util.dt as dt_util
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.dispatcher import async_dispatcher_connect

from . import async_add_ecowitt_entities
from . import EcowittEntity
from .const import DOMAIN
from .const import REG_ENTITIES
from .const import SIGNAL_ADD_ENTITIES
from .const import TYPE_SENSOR

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Add sensors if new."""

    async def add_entities(discovery_info=None):
        await async_add_ecowitt_entities(
            hass,
            entry,
            EcowittSensor,
            SENSOR_DOMAIN,
            async_add_entities,
            discovery_info,
        )

    signal = f"{SIGNAL_ADD_ENTITIES}_{SENSOR_DOMAIN}"
    async_dispatcher_connect(hass, signal, add_entities)
    await add_entities(hass.data[DOMAIN][entry.entry_id][REG_ENTITIES][TYPE_SENSOR])


class EcowittSensor(EcowittEntity, SensorEntity):
    """Definition of a sensor."""

    def __init__(self, hass, entry, key, name, dc, uom, icon, sc):
        """Initialize the sensor."""
        super().__init__(hass, entry, key, name)
        self._icon = icon
        self._uom = uom
        self._dc = dc
        self._sc = sc

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if self._key in self._ws.last_values:
            # The lightning time is reported in UTC, hooray.
            if self._dc == SensorDeviceClass.TIMESTAMP:
                if not isinstance(self._ws.last_values[self._key], int):
                    return STATE_UNKNOWN
                return dt_util.as_local(
                    dt_util.utc_from_timestamp(self._ws.last_values[self._key])
                ).isoformat()
            # Battery value is 0-5
            if self._dc == SensorDeviceClass.BATTERY and self._uom == PERCENTAGE:
                return self._ws.last_values[self._key] * 20.0
            return self._ws.last_values[self._key]
        _LOGGER.warning(
            "Sensor %s not in last update, check range or battery", self._key
        )
        return STATE_UNKNOWN

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._uom

    @property
    def icon(self):
        """Return the icon to use in the fronend."""
        return self._icon

    @property
    def device_class(self):
        """Return the device class."""
        return self._dc

    @property
    def state_class(self):
        """Return sensor state class."""
        return self._sc
