"""The Ecowitt Weather Station Component."""
import asyncio
import logging
import time

from homeassistant.config_entries import ConfigEntry
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.const import CONF_PORT
from homeassistant.core import callback
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_registry import async_get
from homeassistant.util.unit_system import METRIC_SYSTEM
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM
from pyecowitt import EcoWittListener
from pyecowitt import WINDCHILL_HYBRID
from pyecowitt import WINDCHILL_NEW
from pyecowitt import WINDCHILL_OLD

from .const import CONF_NAME
from .const import CONF_UNIT_BARO
from .const import CONF_UNIT_LIGHTNING
from .const import CONF_UNIT_RAIN
from .const import CONF_UNIT_SYSTEM_METRIC_MS
from .const import CONF_UNIT_WIND
from .const import CONF_UNIT_WINDCHILL
from .const import DATA_ECOWITT
from .const import DATA_FREQ
from .const import DATA_MODEL
from .const import DATA_OPTIONS
from .const import DATA_PASSKEY
from .const import DATA_READY
from .const import DATA_STATION
from .const import DATA_STATIONTYPE
from .const import DOMAIN
from .const import ECOWITT_PLATFORMS
from .const import IGNORED_SENSORS
from .const import REG_ENTITIES
from .const import S_IMPERIAL
from .const import S_METRIC
from .const import S_METRIC_MS
from .const import SENSOR_TYPES
from .const import SIGNAL_ADD_ENTITIES
from .const import SIGNAL_REMOVE_ENTITIES
from .const import TYPE_BINARY_SENSOR
from .const import TYPE_SENSOR
from .const import W_TYPE_HYBRID
from .const import W_TYPE_NEW
from .const import W_TYPE_OLD

NOTIFICATION_ID = DOMAIN
NOTIFICATION_TITLE = "Ecowitt config migrated"

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict):
    """Configure the Ecowitt component using YAML."""
    hass.data.setdefault(DOMAIN, {})

    if DOMAIN in config:
        data = {
            CONF_PORT: config[DOMAIN][CONF_PORT],
            CONF_NAME: None,
        }
        # set defaults if not set in conf
        if CONF_UNIT_BARO not in config[DOMAIN]:
            config[DOMAIN][CONF_UNIT_BARO] = hass.config.units.pressure_unit
        if CONF_UNIT_WIND not in config[DOMAIN]:
            config[DOMAIN][CONF_UNIT_WIND] = hass.config.units.wind_speed_unit
        if CONF_UNIT_RAIN not in config[DOMAIN]:
            config[DOMAIN][
                CONF_UNIT_RAIN
            ] = hass.config.units.accumulated_precipitation_unit
        if CONF_UNIT_LIGHTNING not in config[DOMAIN]:
            config[DOMAIN][CONF_UNIT_LIGHTNING] = hass.config.units.length_unit
        if CONF_UNIT_WINDCHILL not in config[DOMAIN]:
            config[DOMAIN][CONF_UNIT_WINDCHILL] = W_TYPE_HYBRID
        # set the options for migration
        hass.data[DOMAIN][DATA_OPTIONS] = {
            CONF_UNIT_BARO: config[DOMAIN][CONF_UNIT_BARO],
            CONF_UNIT_WIND: config[DOMAIN][CONF_UNIT_WIND],
            CONF_UNIT_RAIN: config[DOMAIN][CONF_UNIT_RAIN],
            CONF_UNIT_LIGHTNING: config[DOMAIN][CONF_UNIT_LIGHTNING],
            CONF_UNIT_WINDCHILL: config[DOMAIN][CONF_UNIT_WINDCHILL],
        }
        hass.components.persistent_notification.create(
            "Ecowitt configuration has been migrated from yaml format "
            "to a config_flow. Your options and settings should have been "
            "migrated automatically.  Verify them in the Configuration -> "
            "Integrations menu, and then delete the ecowitt section from "
            "your yaml file.",
            title=NOTIFICATION_TITLE,
            notification_id=NOTIFICATION_ID,
        )
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": SOURCE_IMPORT}, data=data
            )
        )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the Ecowitt component from UI."""

    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})

    # if options existed in the YAML but not in the config entry, add
    if (
        not entry.options
        and entry.source == SOURCE_IMPORT
        and hass.data.get(DOMAIN)
        and hass.data[DOMAIN].get(DATA_OPTIONS)
    ):
        hass.config_entries.async_update_entry(
            entry=entry,
            options=hass.data[DOMAIN][DATA_OPTIONS],
        )

    # Store config
    hass.data[DOMAIN][entry.entry_id] = {}
    ecowitt_data = hass.data[DOMAIN][entry.entry_id]
    ecowitt_data[DATA_STATION] = {}
    ecowitt_data[DATA_READY] = False
    ecowitt_data[REG_ENTITIES] = {}
    for pl in ECOWITT_PLATFORMS:
        ecowitt_data[REG_ENTITIES][pl] = []

    if not entry.options:
        entry.options = {
            CONF_UNIT_BARO: hass.config.units.pressure_unit,
            CONF_UNIT_WIND: hass.config.units.wind_speed_unit,
            CONF_UNIT_RAIN: hass.config.units.accumulated_precipitation_unit,
            CONF_UNIT_LIGHTNING: hass.config.units.length_unit,
            CONF_UNIT_WINDCHILL: W_TYPE_HYBRID,
        }

    # preload some model info
    stationinfo = ecowitt_data[DATA_STATION]
    stationinfo[DATA_STATIONTYPE] = "Unknown"
    stationinfo[DATA_FREQ] = "Unknown"
    stationinfo[DATA_MODEL] = "Unknown"

    # setup the base connection
    web_server = EcoWittListener(port=entry.data[CONF_PORT])
    ecowitt_data[DATA_ECOWITT] = web_server

    if entry.options[CONF_UNIT_WINDCHILL] == W_TYPE_OLD:
        web_server.set_windchill(WINDCHILL_OLD)
    if entry.options[CONF_UNIT_WINDCHILL] == W_TYPE_NEW:
        web_server.set_windchill(WINDCHILL_NEW)
    if entry.options[CONF_UNIT_WINDCHILL] == W_TYPE_HYBRID:
        web_server.set_windchill(WINDCHILL_HYBRID)

    hass.loop.create_task(web_server.listen())

    async def close_server(*args):
        """Close the ecowitt server."""
        await web_server.stop()

    def check_imp_metric_sensor(sensor):
        """Check if this is the wrong sensor for our config (imp/metric)."""
        # Is this a metric or imperial sensor, lookup and skip
        _, _, _, _, _, metric, _ = SENSOR_TYPES[sensor]
        if metric == 0:
            return True
        if "baro" in sensor:
            if (
                entry.options[CONF_UNIT_BARO] == US_CUSTOMARY_SYSTEM.pressure_unit
                and metric == S_METRIC
            ):
                return False
            if (
                entry.options[CONF_UNIT_BARO] == METRIC_SYSTEM.pressure_unit
                and metric == S_IMPERIAL
            ):
                return False
        if "rain" in sensor:
            if (
                entry.options[CONF_UNIT_RAIN]
                == US_CUSTOMARY_SYSTEM.accumulated_precipitation_unit
                and metric == S_METRIC
            ):
                return False
            if (
                entry.options[CONF_UNIT_RAIN]
                == METRIC_SYSTEM.accumulated_precipitation_unit
                and metric == S_IMPERIAL
            ):
                return False
        if "windchill" not in sensor and ("wind" in sensor or "gust" in sensor):
            if (
                entry.options[CONF_UNIT_WIND] == US_CUSTOMARY_SYSTEM.wind_speed_unit
                and metric != S_IMPERIAL
            ):
                return False
            if (
                entry.options[CONF_UNIT_WIND] == METRIC_SYSTEM.wind_speed_unit
                and metric != S_METRIC
            ):
                return False
            if (
                entry.options[CONF_UNIT_WIND] == CONF_UNIT_SYSTEM_METRIC_MS
                and metric != S_METRIC_MS
            ):
                return False
        if (
            sensor == "lightning"
            and entry.options[CONF_UNIT_LIGHTNING] == METRIC_SYSTEM.length_unit
        ):
            return False
        if (
            sensor == "lightning_mi"
            and entry.options[CONF_UNIT_LIGHTNING] == US_CUSTOMARY_SYSTEM.length_unit
        ):
            return False
        return True

    def check_and_append_sensor(sensor):
        """Check the sensor for validity, and append to new entitiy list."""
        if sensor not in SENSOR_TYPES:
            if sensor not in IGNORED_SENSORS:
                _LOGGER.warning("Unhandled sensor type %s", sensor)
            return None

        # Is this a metric or imperial sensor, lookup and skip
        if not check_imp_metric_sensor(sensor):
            return None

        _, _, kind, _, _, _, _ = SENSOR_TYPES[sensor]
        ecowitt_data[REG_ENTITIES][kind].append(sensor)
        return kind

    async def _first_data_rec():
        _LOGGER.info("First ecowitt data recd, setting up sensors.")
        # check if we have model info, etc.
        if DATA_PASSKEY in web_server.last_values:
            stationinfo[DATA_PASSKEY] = web_server.last_values[DATA_PASSKEY]
            web_server.last_values.pop(DATA_PASSKEY, None)
        else:
            _LOGGER.error("No passkey, cannot set unique id.")
            return False
        if DATA_STATIONTYPE in web_server.last_values:
            stationinfo[DATA_STATIONTYPE] = web_server.last_values[DATA_STATIONTYPE]
            web_server.last_values.pop(DATA_STATIONTYPE, None)
        if DATA_FREQ in web_server.last_values:
            stationinfo[DATA_FREQ] = web_server.last_values[DATA_FREQ]
            web_server.last_values.pop(DATA_FREQ, None)
        if DATA_MODEL in web_server.last_values:
            stationinfo[DATA_MODEL] = web_server.last_values[DATA_MODEL]
            web_server.last_values.pop(DATA_MODEL, None)

        # load the sensors we have
        for sensor in web_server.last_values:
            check_and_append_sensor(sensor)

        if (
            not ecowitt_data[REG_ENTITIES][TYPE_SENSOR]
            and not ecowitt_data[REG_ENTITIES][TYPE_BINARY_SENSOR]
        ):
            _LOGGER.error("No sensors found to monitor, check device config.")
            return False

        for component in ECOWITT_PLATFORMS:
            hass.async_create_task(
                hass.config_entries.async_forward_entry_setup(entry, component)
            )

        ecowitt_data[DATA_READY] = True

    async def _async_ecowitt_update_cb(weather_data):
        """Primary update callback called from pyecowitt."""
        _LOGGER.debug("Primary update callback triggered.")

        new_sensors = {}
        old_sensors = []
        for component in ECOWITT_PLATFORMS:
            new_sensors[component] = []

        if not hass.data[DOMAIN][entry.entry_id][DATA_READY]:
            await _first_data_rec()
            return
        for sensor in weather_data:
            if sensor not in SENSOR_TYPES:
                if sensor not in IGNORED_SENSORS:
                    _LOGGER.warning(
                        "Unhandled sensor type %s value %s, " + "file a PR.",
                        sensor,
                        weather_data[sensor],
                    )
            elif (
                sensor not in ecowitt_data[REG_ENTITIES][TYPE_SENSOR]
                and sensor not in ecowitt_data[REG_ENTITIES][TYPE_BINARY_SENSOR]
                and sensor not in IGNORED_SENSORS
                and check_imp_metric_sensor(sensor)
            ):
                _LOGGER.warning(
                    "Unregistered sensor type %s value %s received.",
                    sensor,
                    weather_data[sensor],
                )
                # try to register the sensor
                kind = check_and_append_sensor(sensor)
                if kind is not None:
                    new_sensors[kind].append(sensor)
            # It's a sensor we know, not ignored, and of the wrong metricness
            elif (
                (
                    sensor in ecowitt_data[REG_ENTITIES][TYPE_SENSOR]
                    or sensor in ecowitt_data[REG_ENTITIES][TYPE_BINARY_SENSOR]
                )
                and sensor not in IGNORED_SENSORS
                and not check_imp_metric_sensor(sensor)
            ):
                _LOGGER.warning("Removing sensor type %s.", sensor)
                old_sensors.append(sensor)

        # If we have old sensors, delete them.
        if old_sensors:
            await async_remove_ecowitt_entities(old_sensors, hass, ecowitt_data)

        # if we have new sensors, set them up.
        for component in ECOWITT_PLATFORMS:
            if new_sensors[component]:
                signal = f"{SIGNAL_ADD_ENTITIES}_{component}"
                async_dispatcher_send(hass, signal, new_sensors[component])
        async_dispatcher_send(hass, DOMAIN)

    # this is part of the base async_setup_entry
    web_server.register_listener(_async_ecowitt_update_cb)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""

    web_server = hass.data[DOMAIN][entry.entry_id][DATA_ECOWITT]
    await web_server.stop()

    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in ECOWITT_PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_remove_ecowitt_entities(entities, hass, ecowitt_data):
    """Remove a sensor if needed."""

    try:
        eventData = {}
        for entity in entities:
            _, _, kind, _, _, _, _ = SENSOR_TYPES[entity]

            eventData[entity] = kind
            ecowitt_data[REG_ENTITIES][kind].remove(entity)

        async_dispatcher_send(hass, SIGNAL_REMOVE_ENTITIES, eventData)

    except Exception as e:
        _LOGGER.error(e)


async def async_add_ecowitt_entities(
    hass, entry, entity_type, platform, async_add_entities, discovery_info
):
    """Add an ecowitt entities."""
    entities = []
    if discovery_info is None:
        return

    for new_entity in discovery_info:
        if new_entity not in hass.data[DOMAIN][entry.entry_id][REG_ENTITIES][platform]:
            hass.data[DOMAIN][entry.entry_id][REG_ENTITIES][platform].append(new_entity)
        name, uom, _, device_class, icon, _, state_class = SENSOR_TYPES[new_entity]

        new_hass_entity = entity_type(
            hass, entry, new_entity, name, device_class, uom, icon, state_class
        )

        async_dispatcher_connect(
            hass, SIGNAL_REMOVE_ENTITIES, new_hass_entity.remove_entity
        )

        entities.append(new_hass_entity)

    if entities:
        async_add_entities(entities, True)


class EcowittEntity(Entity):
    """Base class for Ecowitt Weather Station."""

    def __init__(self, hass, entry, key, name):
        """Construct the entity."""
        self.hass = hass
        self._key = key
        self._name = name
        self._stationinfo = hass.data[DOMAIN][entry.entry_id][DATA_STATION]
        self._ws = hass.data[DOMAIN][entry.entry_id][DATA_ECOWITT]
        self._entry = entry

    @property
    def should_poll(self):
        """Ecowitt is a push."""
        return False

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return f"{self._stationinfo[DATA_PASSKEY]}-{self._key}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def device_info(self):
        """Return device information for this sensor."""
        if (
            self._entry.data[CONF_NAME] != ""
            and self._entry.data[CONF_NAME] is not None
        ):
            dname = self._entry.data[CONF_NAME]
        else:
            dname = DOMAIN

        return {
            "identifiers": {(DOMAIN, self._stationinfo[DATA_PASSKEY])},
            "name": dname,
            "manufacturer": DOMAIN,
            "model": self._stationinfo[DATA_MODEL],
            "sw_version": self._stationinfo[DATA_STATIONTYPE],
            "via_device": (DOMAIN, self._stationinfo[DATA_STATIONTYPE]),
            # "frequency": self._stationinfo[DATA_FREQ],
        }

    async def async_added_to_hass(self):
        """Add an listener."""
        async_dispatcher_connect(self.hass, DOMAIN, self._update_callback)

    @callback
    async def remove_entity(self, discovery_info=None):
        """Remove an entity."""

        if self._key in discovery_info:
            registry = async_get(self.hass)

            entity_id = registry.async_get_entity_id(
                discovery_info[self._key], DOMAIN, self.unique_id
            )

            _LOGGER.debug(
                f"Found entity {entity_id} for key {self._key} -> Uniqueid: {self.unique_id}"
            )
            if entity_id:
                registry.async_remove(entity_id)

    @callback
    def _update_callback(self) -> None:
        """Call from dispatcher when state changes."""
        self.async_schedule_update_ha_state(force_refresh=True)

    @property
    def assumed_state(self) -> bool:
        """Return whether the state is based on actual reading from device."""
        if (self._ws.lastupd + 5 * 60) < time.time():
            return True
        return False
