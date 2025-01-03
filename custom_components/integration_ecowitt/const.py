"""Constants used by ecowitt component."""

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION
from homeassistant.const import DEGREE
from homeassistant.const import UnitOfElectricPotential
from homeassistant.const import UnitOfLength
from homeassistant.const import PERCENTAGE
from homeassistant.const import UnitOfPower
from homeassistant.const import UnitOfPressure
from homeassistant.const import UnitOfSpeed
from homeassistant.const import UnitOfTemperature
from homeassistant.const import UnitOfTime
from homeassistant.const import UV_INDEX
from homeassistant.util.unit_system import METRIC_SYSTEM
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM

ECOWITT_PLATFORMS = ["sensor", "binary_sensor"]

TYPE_SENSOR = "sensor"
TYPE_BINARY_SENSOR = "binary_sensor"
DOMAIN = "integration_ecowitt"
DATA_CONFIG = "config"
DATA_OPTIONS = "options"
DATA_ECOWITT = "ecowitt_listener"
DATA_STATION = "station"
DATA_PASSKEY = "PASSKEY"
DATA_STATIONTYPE = "stationtype"
DATA_FREQ = "freq"
DATA_MODEL = "model"
DATA_READY = "ready"
REG_ENTITIES = "registered"

DEFAULT_PORT = 4199

SIGNAL_ADD_ENTITIES = "ecowitt_add_entities"
SIGNAL_REMOVE_ENTITIES = "ecowitt_remove_entities"

CONF_NAME = "component_name"
CONF_UNIT_BARO = "barounit"
CONF_UNIT_WIND = "windunit"
CONF_UNIT_RAIN = "rainunit"
CONF_UNIT_WINDCHILL = "windchillunit"
CONF_UNIT_LIGHTNING = "lightningunit"

TYPE_BAROMABSHPA = "baromabshpa"
TYPE_BAROMRELHPA = "baromrelhpa"
TYPE_BAROMABSIN = "baromabsin"
TYPE_BAROMRELIN = "baromrelin"
TYPE_RAINRATEIN = "rainratein"
TYPE_EVENTRAININ = "eventrainin"
TYPE_HOURLYRAININ = "hourlyrainin"
TYPE_TOTALRAININ = "totalrainin"
TYPE_DAILYRAININ = "dailyrainin"
TYPE_WEEKLYRAININ = "weeklyrainin"
TYPE_MONTHLYRAININ = "monthlyrainin"
TYPE_YEARLYRAININ = "yearlyrainin"
TYPE_RAINRATEMM = "rainratemm"
TYPE_EVENTRAINMM = "eventrainmm"
TYPE_HOURLYRAINMM = "hourlyrainmm"
TYPE_TOTALRAINMM = "totalrainmm"
TYPE_DAILYRAINMM = "dailyrainmm"
TYPE_WEEKLYRAINMM = "weeklyrainmm"
TYPE_MONTHLYRAINMM = "monthlyrainmm"
TYPE_YEARLYRAINMM = "yearlyrainmm"
TYPE_HUMIDITY = "humidity"
TYPE_HUMIDITY1 = "humidity1"
TYPE_HUMIDITY2 = "humidity2"
TYPE_HUMIDITY3 = "humidity3"
TYPE_HUMIDITY4 = "humidity4"
TYPE_HUMIDITY5 = "humidity5"
TYPE_HUMIDITY6 = "humidity6"
TYPE_HUMIDITY7 = "humidity7"
TYPE_HUMIDITY8 = "humidity8"
TYPE_HUMIDITYIN = "humidityin"
TYPE_WINDDIR = "winddir"
TYPE_WINDDIR_A10 = "winddir_avg10m"
TYPE_WINDSPEEDKMH = "windspeedkmh"
TYPE_WINDSPEEDKMH_A10 = "windspdkmh_avg10m"
TYPE_WINDGUSTKMH = "windgustkmh"
TYPE_WINDSPEEDMPH = "windspeedmph"
TYPE_WINDSPEEDMPH_A10 = "windspdmph_avg10m"
TYPE_WINDGUSTMPH = "windgustmph"
TYPE_MAXDAILYGUST = "maxdailygust"
TYPE_MAXDAILYGUSTKMH = "maxdailygustkmh"
TYPE_WINDGUSTMS = "windgustms"
TYPE_WINDSPEEDMS = "windspeedms"
TYPE_WINDSPEEDMS_A10 = "windspdms_avg10m"
TYPE_MAXDAILYGUSTMS = "maxdailygustms"
TYPE_TEMPC = "tempc"
TYPE_TEMPINC = "tempinc"
TYPE_TEMP1C = "temp1c"
TYPE_TEMP2C = "temp2c"
TYPE_TEMP3C = "temp3c"
TYPE_TEMP4C = "temp4c"
TYPE_TEMP5C = "temp5c"
TYPE_TEMP6C = "temp6c"
TYPE_TEMP7C = "temp7c"
TYPE_TEMP8C = "temp8c"
TYPE_DEWPOINTC = "dewpointc"
TYPE_DEWPOINTINC = "dewpointinc"
TYPE_DEWPOINT1C = "dewpoint1c"
TYPE_DEWPOINT2C = "dewpoint2c"
TYPE_DEWPOINT3C = "dewpoint3c"
TYPE_DEWPOINT4C = "dewpoint4c"
TYPE_DEWPOINT5C = "dewpoint5c"
TYPE_DEWPOINT6C = "dewpoint6c"
TYPE_DEWPOINT7C = "dewpoint7c"
TYPE_DEWPOINT8C = "dewpoint8c"
TYPE_WINDCHILLC = "windchillc"
TYPE_SOLARRADIATION = "solarradiation"
TYPE_UV = "uv"
TYPE_SOILMOISTURE1 = "soilmoisture1"
TYPE_SOILMOISTURE2 = "soilmoisture2"
TYPE_SOILMOISTURE3 = "soilmoisture3"
TYPE_SOILMOISTURE4 = "soilmoisture4"
TYPE_SOILMOISTURE5 = "soilmoisture5"
TYPE_SOILMOISTURE6 = "soilmoisture6"
TYPE_SOILMOISTURE7 = "soilmoisture7"
TYPE_SOILMOISTURE8 = "soilmoisture8"
TYPE_PM25_CH1 = "pm25_ch1"
TYPE_PM25_CH2 = "pm25_ch2"
TYPE_PM25_CH3 = "pm25_ch3"
TYPE_PM25_CH4 = "pm25_ch4"
TYPE_PM25_AVG_24H_CH1 = "pm25_avg_24h_ch1"
TYPE_PM25_AVG_24H_CH2 = "pm25_avg_24h_ch2"
TYPE_PM25_AVG_24H_CH3 = "pm25_avg_24h_ch3"
TYPE_PM25_AVG_24H_CH4 = "pm25_avg_24h_ch4"
TYPE_LIGHTNING_TIME = "lightning_time"
TYPE_LIGHTNING_NUM = "lightning_num"
TYPE_LIGHTNING_KM = "lightning"
TYPE_LIGHTNING_MI = "lightning_mi"
TYPE_CO2_TEMP = "tf_co2"
TYPE_CO2_TEMPC = "tf_co2c"
TYPE_CO2_HUMIDITY = "humi_co2"
TYPE_CO2_PM25 = "pm25_co2"
TYPE_CO2_PM25_AVG_24H = "pm25_24h_co2"
TYPE_CO2_PM10 = "pm10_co2"
TYPE_CO2_PM10_AVG_24H = "pm10_24h_co2"
TYPE_CO2_CO2 = "co2"
TYPE_CO2_CO2_AVG_24H = "co2_24h"
TYPE_CO2_BATT = "co2_batt"
TYPE_LEAK_CH1 = "leak_ch1"
TYPE_LEAK_CH2 = "leak_ch2"
TYPE_LEAK_CH3 = "leak_ch3"
TYPE_LEAK_CH4 = "leak_ch4"
TYPE_WH25BATT = "wh25batt"
TYPE_WH26BATT = "wh26batt"
TYPE_WH40BATT = "wh40batt"
TYPE_WH57BATT = "wh57batt"
TYPE_WH68BATT = "wh68batt"
TYPE_WH65BATT = "wh65batt"
TYPE_WH80BATT = "wh80batt"
TYPE_SOILBATT1 = "soilbatt1"
TYPE_SOILBATT2 = "soilbatt2"
TYPE_SOILBATT3 = "soilbatt3"
TYPE_SOILBATT4 = "soilbatt4"
TYPE_SOILBATT5 = "soilbatt5"
TYPE_SOILBATT6 = "soilbatt6"
TYPE_SOILBATT7 = "soilbatt7"
TYPE_SOILBATT8 = "soilbatt8"
TYPE_BATTERY1 = "batt1"
TYPE_BATTERY2 = "batt2"
TYPE_BATTERY3 = "batt3"
TYPE_BATTERY4 = "batt4"
TYPE_BATTERY5 = "batt5"
TYPE_BATTERY6 = "batt6"
TYPE_BATTERY7 = "batt7"
TYPE_BATTERY8 = "batt8"
TYPE_PM25BATT1 = "pm25batt1"
TYPE_PM25BATT2 = "pm25batt2"
TYPE_PM25BATT3 = "pm25batt3"
TYPE_PM25BATT4 = "pm25batt4"
TYPE_PM25BATT5 = "pm25batt5"
TYPE_PM25BATT6 = "pm25batt6"
TYPE_PM25BATT7 = "pm25batt7"
TYPE_PM25BATT8 = "pm25batt8"
TYPE_LEAKBATT1 = "leakbatt1"
TYPE_LEAKBATT2 = "leakbatt2"
TYPE_LEAKBATT3 = "leakbatt3"
TYPE_LEAKBATT4 = "leakbatt4"
TYPE_LEAKBATT5 = "leakbatt5"
TYPE_LEAKBATT6 = "leakbatt6"
TYPE_LEAKBATT7 = "leakbatt7"
TYPE_LEAKBATT8 = "leakbatt8"
TYPE_WN34TEMP1C = "tf_ch1c"
TYPE_WN34TEMP2C = "tf_ch2c"
TYPE_WN34TEMP3C = "tf_ch3c"
TYPE_WN34TEMP4C = "tf_ch4c"
TYPE_WN34TEMP5C = "tf_ch5c"
TYPE_WN34TEMP6C = "tf_ch6c"
TYPE_WN34TEMP7C = "tf_ch7c"
TYPE_WN34TEMP8C = "tf_ch8c"
TYPE_WN34BATT1 = "tf_batt1"
TYPE_WN34BATT2 = "tf_batt2"
TYPE_WN34BATT3 = "tf_batt3"
TYPE_WN34BATT4 = "tf_batt4"
TYPE_WN34BATT5 = "tf_batt5"
TYPE_WN34BATT6 = "tf_batt6"
TYPE_WN34BATT7 = "tf_batt7"
TYPE_WN34BATT8 = "tf_batt8"

S_METRIC = 1
S_IMPERIAL = 2
S_METRIC_MS = 3

W_TYPE_NEW = "new"
W_TYPE_OLD = "old"
W_TYPE_HYBRID = "hybrid"
CONF_UNIT_SYSTEM_METRIC_MS = "metric_ms"

LEAK_DETECTED = "Leak Detected"

UNIT_PRECI_OPTS = [
    METRIC_SYSTEM.accumulated_precipitation_unit,
    US_CUSTOMARY_SYSTEM.accumulated_precipitation_unit,
]


UNIT_LENGTH_OPTS = [METRIC_SYSTEM.length_unit, US_CUSTOMARY_SYSTEM.length_unit]

UNIT_BARO_OPTS = [METRIC_SYSTEM.pressure_unit, US_CUSTOMARY_SYSTEM.pressure_unit]
UNIT_WIND_OPTS = [
    METRIC_SYSTEM.wind_speed_unit,
    US_CUSTOMARY_SYSTEM.wind_speed_unit,
    CONF_UNIT_SYSTEM_METRIC_MS,
]
WINDCHILL_OPTS = [W_TYPE_HYBRID, W_TYPE_NEW, W_TYPE_OLD]


# Name, unit_of_measure, type, device_class, icon, metric=1, state_class
# name, uom, kind, device_class, icon, metric, state_class = SENSOR_TYPES[x]
SENSOR_TYPES = {
    TYPE_BAROMABSHPA: (
        "Absolute Pressure",
        UnitOfPressure.HPA,
        TYPE_SENSOR,
        SensorDeviceClass.PRESSURE,
        "mdi:gauge",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_BAROMRELHPA: (
        "Relative Pressure",
        UnitOfPressure.HPA,
        TYPE_SENSOR,
        SensorDeviceClass.PRESSURE,
        "mdi:gauge",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_BAROMABSIN: (
        "Absolute Pressure",
        UnitOfPressure.INHG,
        TYPE_SENSOR,
        SensorDeviceClass.PRESSURE,
        "mdi:gauge",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_BAROMRELIN: (
        "Relative Pressure",
        UnitOfPressure.INHG,
        TYPE_SENSOR,
        SensorDeviceClass.PRESSURE,
        "mdi:gauge",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_RAINRATEIN: (
        "Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_EVENTRAININ: (
        "Event Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HOURLYRAININ: (
        "Hourly Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TOTALRAININ: (
        "Total Rain Rate",
        f"{UnitOfLength.INCHES}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.TOTAL_INCREASING,
    ),
    TYPE_DAILYRAININ: (
        "Daily Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.DAYS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WEEKLYRAININ: (
        "Weekly Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.WEEKS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_MONTHLYRAININ: (
        "Monthly Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.MONTHS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_YEARLYRAININ: (
        "Yearly Rain Rate",
        f"{UnitOfLength.INCHES}/{UnitOfTime.YEARS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_RAINRATEMM: (
        "Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_EVENTRAINMM: (
        "Event Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HOURLYRAINMM: (
        "Hourly Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.HOURS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TOTALRAINMM: (
        "Total Rain Rate",
        UnitOfLength.MILLIMETERS,
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION,
        "mdi:water",
        S_METRIC,
        SensorStateClass.TOTAL_INCREASING,
    ),
    TYPE_DAILYRAINMM: (
        "Daily Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.DAYS}",
        TYPE_SENSOR,
        SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WEEKLYRAINMM: (
        "Weekly Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.WEEKS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_MONTHLYRAINMM: (
        "Monthly Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.MONTHS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_YEARLYRAINMM: (
        "Yearly Rain Rate",
        f"{UnitOfLength.MILLIMETERS}/{UnitOfTime.YEARS}",
        TYPE_SENSOR,
        None,  # SensorDeviceClass.PRECIPITATION_INTENSITY,
        "mdi:water",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY: (
        "Humidity",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITYIN: (
        "Indoor Humidity",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY1: (
        "Humidity 1",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY2: (
        "Humidity 2",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY3: (
        "Humidity 3",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY4: (
        "Humidity 4",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY5: (
        "Humidity 5",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY6: (
        "Humidity 6",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY7: (
        "Humidity 7",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_HUMIDITY8: (
        "Humidity 8",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDDIR: (
        "Wind Direction",
        DEGREE,
        TYPE_SENSOR,
        None,
        "mdi:compass",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDDIR_A10: (
        "Wind Direction 10m Avg",
        DEGREE,
        TYPE_SENSOR,
        None,
        "mdi:compass",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDKMH: (
        "Wind Speed",
        UnitOfSpeed.KILOMETERS_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDKMH_A10: (
        "Wind Speed 10m Avg",
        UnitOfSpeed.KILOMETERS_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDGUSTKMH: (
        "Wind Gust",
        UnitOfSpeed.KILOMETERS_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDMPH: (
        "Wind Speed",
        UnitOfSpeed.MILES_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDMPH_A10: (
        "Wind Speed 10m Avg",
        UnitOfSpeed.MILES_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDGUSTMPH: (
        "Wind Gust",
        UnitOfSpeed.MILES_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_MAXDAILYGUST: (
        "Max Daily Wind Gust",
        UnitOfSpeed.MILES_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_MAXDAILYGUSTKMH: (
        "Max Daily Wind Gust",
        UnitOfSpeed.KILOMETERS_PER_HOUR,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDGUSTMS: (
        "Wind Gust",
        UnitOfSpeed.METERS_PER_SECOND,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC_MS,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDMS: (
        "Wind Speed",
        UnitOfSpeed.METERS_PER_SECOND,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC_MS,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDSPEEDMS_A10: (
        "Wind Speed",
        UnitOfSpeed.METERS_PER_SECOND,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC_MS,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_MAXDAILYGUSTMS: (
        "Max Daily Wind Gust",
        UnitOfSpeed.METERS_PER_SECOND,
        TYPE_SENSOR,
        SensorDeviceClass.WIND_SPEED,
        "mdi:weather-windy",
        S_METRIC_MS,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMPC: (
        "Outdoor Temperature",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP1C: (
        "Temperature 1",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP2C: (
        "Temperature 2",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP3C: (
        "Temperature 3",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP4C: (
        "Temperature 4",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP5C: (
        "Temperature 5",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP6C: (
        "Temperature 6",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP7C: (
        "Temperature 7",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMP8C: (
        "Temperature 8",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_TEMPINC: (
        "Indoor Temperature",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINTC: (
        "Dewpoint",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINTINC: (
        "Indoor Dewpoint",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT1C: (
        "Dewpoint 1",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT2C: (
        "Dewpoint 2",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT3C: (
        "Dewpoint 3",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT4C: (
        "Dewpoint 4",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT5C: (
        "Dewpoint 5",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT6C: (
        "Dewpoint 6",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT7C: (
        "Dewpoint 7",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_DEWPOINT8C: (
        "Dewpoint 8",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WINDCHILLC: (
        "Windchill",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOLARRADIATION: (
        "Solar Radiation",
        f"{UnitOfPower.WATT}/m²",
        TYPE_SENSOR,
        SensorDeviceClass.IRRADIANCE,
        "mdi:weather-sunny",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_UV: (
        "UV Index",
        UV_INDEX,
        TYPE_SENSOR,
        None,
        "mdi:sunglasses",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE1: (
        "Soil Moisture 1",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE2: (
        "Soil Moisture 2",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE3: (
        "Soil Moisture 3",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE4: (
        "Soil Moisture 4",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE5: (
        "Soil Moisture 5",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE6: (
        "Soil Moisture 6",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE7: (
        "Soil Moisture 7",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILMOISTURE8: (
        "Soil Moisture 8",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_CH1: (
        "PM2.5 1",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_CH2: (
        "PM2.5 2",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_CH3: (
        "PM2.5 3",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_CH4: (
        "PM2.5 4",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_AVG_24H_CH1: (
        "PM2.5 24h average 1",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_AVG_24H_CH2: (
        "PM2.5 24h average 2",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_AVG_24H_CH3: (
        "PM2.5 24h average 3",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25_AVG_24H_CH4: (
        "PM2.5 24h average 4",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LIGHTNING_TIME: (
        "Last Lightning strike",
        "",
        TYPE_SENSOR,
        SensorDeviceClass.TIMESTAMP,
        "mdi:clock",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LIGHTNING_NUM: (
        "Lightning strikes",
        f"strikes/{UnitOfTime.DAYS}",
        TYPE_SENSOR,
        None,
        "mdi:weather-lightning",
        0,
        SensorStateClass.TOTAL_INCREASING,
    ),
    TYPE_LIGHTNING_KM: (
        "Lightning strike distance",
        UnitOfLength.KILOMETERS,
        TYPE_SENSOR,
        None,
        "mdi:ruler",
        S_METRIC,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LIGHTNING_MI: (
        "Lightning strike distance",
        UnitOfLength.MILES,
        TYPE_SENSOR,
        None,
        "mdi:ruler",
        S_IMPERIAL,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAK_CH1: (
        "Leak Detection 1",
        LEAK_DETECTED,
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.MOISTURE,
        "mdi:leak",
        0,
        None,
    ),
    TYPE_LEAK_CH2: (
        "Leak Detection 2",
        LEAK_DETECTED,
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.MOISTURE,
        "mdi:leak",
        0,
        None,
    ),
    TYPE_LEAK_CH3: (
        "Leak Detection 3",
        LEAK_DETECTED,
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.MOISTURE,
        "mdi:leak",
        0,
        None,
    ),
    TYPE_LEAK_CH4: (
        "Leak Detection 4",
        LEAK_DETECTED,
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.MOISTURE,
        "mdi:leak",
        0,
        None,
    ),
    TYPE_CO2_PM25: (
        "WH45 PM2.5",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_PM25_AVG_24H: (
        "WH45 PM2.5 24h average",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM25,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_PM10: (
        "WH45 PM10",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM10,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_PM10_AVG_24H: (
        "WH45 PM10 24h average",
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        TYPE_SENSOR,
        SensorDeviceClass.PM10,
        "mdi:eye",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_HUMIDITY: (
        "WH45 Humidity",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.HUMIDITY,
        "mdi:water-percent",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_TEMPC: (
        "WH45 Temperature",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_CO2: (
        "WH45 CO2",
        CONCENTRATION_PARTS_PER_MILLION,
        TYPE_SENSOR,
        None,  # SensorDeviceClass.CARBON_DIOXIDE,
        "mdi:molecule-co2",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_CO2_AVG_24H: (
        "WH45 CO2 24h average",
        CONCENTRATION_PARTS_PER_MILLION,
        TYPE_SENSOR,
        None,  # SensorDeviceClass.CARBON_DIOXIDE,
        "mdi:molecule-co2",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_CO2_BATT: (
        "WH45 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WH25BATT: (
        "WH25 Battery",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_WH26BATT: (
        "WH26 Battery",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_WH40BATT: (
        "WH40 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WH57BATT: (
        "WH57 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WH65BATT: (
        "WH65 Battery",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_WH68BATT: (
        "WH68 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WH80BATT: (
        "WH80 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT1: (
        "Soil Moisture 1 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT2: (
        "Soil Moisture 2 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT3: (
        "Soil Moisture 3 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT4: (
        "Soil Moisture 4 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT5: (
        "Soil Moisture 5 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT6: (
        "Soil Moisture 6 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT7: (
        "Soil Moisture 7 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_SOILBATT8: (
        "Soil Moisture 8 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_BATTERY1: (
        "Battery 1",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY2: (
        "Battery 2",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY3: (
        "Battery 3",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY4: (
        "Battery 4",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY5: (
        "Battery 5",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY6: (
        "Battery 6",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY7: (
        "Battery 7",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_BATTERY8: (
        "Battery 8",
        "BATT",
        TYPE_BINARY_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        None,
    ),
    TYPE_PM25BATT1: (
        "PM2.5 1 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT2: (
        "PM2.5 2 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT3: (
        "PM2.5 3 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT4: (
        "PM2.5 4 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT5: (
        "PM2.5 5 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT6: (
        "PM2.5 6 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT7: (
        "PM2.5 7 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_PM25BATT8: (
        "PM2.5 8 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT1: (
        "Leak 1 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT2: (
        "Leak 2 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT3: (
        "Leak 3 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT4: (
        "Leak 4 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT5: (
        "Leak 5 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT6: (
        "Leak 6 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT7: (
        "Leak 7 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_LEAKBATT8: (
        "Leak 8 Battery",
        PERCENTAGE,
        TYPE_SENSOR,
        SensorDeviceClass.BATTERY,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP1C: (
        "Soil Temperature 1",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP2C: (
        "Soil Temperature 2",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP3C: (
        "Soil Temperature 3",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP4C: (
        "Soil Temperature 4",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP5C: (
        "Soil Temperature 5",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP6C: (
        "Soil Temperature 6",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP7C: (
        "Soil Temperature 7",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34TEMP8C: (
        "Soil Temperature 8",
        UnitOfTemperature.CELSIUS,
        TYPE_SENSOR,
        SensorDeviceClass.TEMPERATURE,
        "mdi:thermometer",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT1: (
        "Soil Temperature 1 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT2: (
        "Soil Temperature 2 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT3: (
        "Soil Temperature 3 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT4: (
        "Soil Temperature 4 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT5: (
        "Soil Temperature 5 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT6: (
        "Soil Temperature 6 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT7: (
        "Soil Temperature 7 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
    TYPE_WN34BATT8: (
        "Soil Temperature 8 Battery",
        UnitOfElectricPotential.VOLT,
        TYPE_SENSOR,
        SensorDeviceClass.VOLTAGE,
        "mdi:battery",
        0,
        SensorStateClass.MEASUREMENT,
    ),
}

IGNORED_SENSORS = [
    "tempinf",
    "tempf",
    "temp1f",
    "temp2f",
    "temp3f",
    "temp4f",
    "temp5f",
    "temp6f",
    "temp7f",
    "temp8f",
    "tf_co2",
    "tf_ch1",
    "tf_ch2",
    "tf_ch3",
    "tf_ch4",
    "tf_ch5",
    "tf_ch6",
    "tf_ch7",
    "tf_ch8",
    "dateutc",
    "windchillf",
    "dewpointf",
    "dewpointinf",
    "dewpoint1f",
    "dewpoint2f",
    "dewpoint3f",
    "dewpoint4f",
    "dewpoint5f",
    "dewpoint6f",
    "dewpoint7f",
    "dewpoint8f",
    "mac",
    "fields",
    DATA_PASSKEY,
    DATA_STATIONTYPE,
    DATA_FREQ,
    DATA_MODEL,
]
