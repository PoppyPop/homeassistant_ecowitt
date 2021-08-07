"""
A bone-simple fake client used to test the hass integration
"""
import http.client
import time
import urllib.parse
from datetime import datetime
from random import randrange

MY_PASSKEY = "34271334ED1FADA6D8B988B14267E55D"
# MY_PASSKEY = '35271334ED1FADA7D8B988B22222E22D'

paramset_a = {
    "PASSKEY": MY_PASSKEY,
    "stationtype": "EasyWeatherV1.4.9",
    "dateutc": "2020-11-13+17:10:24",
    "tempinc": 20.0,
    "humidityin": 40,
    "baromrelin": 28.760,
    "baromabsin": 28.760,
    "tempc": 20.0,
    "humidity": 64,
    "winddir": 319,
    "windspeedmph": 0.9,
    "windgustmph": 1.1,
    "rainratein": 0.000,
    "eventrainin": 0.000,
    "dailyrainin": 0.000,
    "weeklyrainin": 0.024,
    "monthlyrainin": 0.028,
    "yearlyrainin": 0.843,
    "solarradiation": 375.53,
    "uv": 3,
    "pm25_ch1": 8.0,
    "pm25_avg_24h_ch1": 5.2,
    "freq": "915M",
    "model": "HP3500_V1.6.2",
    "leak_ch1": 0,
    "leakbatt1": 5,
}

paramset_b = {
    "PASSKEY": MY_PASSKEY,
    "stationtype": "EasyWeatherV1.5.4",
    "dateutc": "2020-11-16+15:30:24",
    "tempinc": 20.7,
    "humidityin": 52,
    "baromrelin": 29.785,
    "baromabsin": 29.785,
    "tempc": 20.4,
    "humidity": 94,
    "winddir": 260,
    "winddir_avg10m": 260,
    "windspeedmph": 0.0,
    "windspdmph_avg10m": 0.0,
    "windgustmph": 0.0,
    "maxdailygust": 6.9,
    "rainratein": 0.000,
    "eventrainin": 0.118,
    "hourlyrainin": 0.000,
    "dailyrainin": 0.118,
    "weeklyrainin": 0.118,
    "monthlyrainin": 0.378,
    "yearlyrainin": 6.268,
    "solarradiation": 0.00,
    "uv": 0,
    "soilmoisture1": 0,
    "wh65batt": 1,
    "wh25batt": 0,
    "soilbatt1": 1.5,
    "leak_ch1": 0,
    "leakbatt1": 5,
    "leak_ch2": 1,
    "leakbatt2": 3,
    "tf_co2": 56.7,
    "humi_co2": 72,
    "pm25_co2": 24.7,
    "pm25_24h_co2": 29.4,
    "pm10_co2": 24.7,
    "pm10_24h_co2": 29.9,
    "co2": 455,
    "co2_24h": 464,
    "co2_batt": 6,
    "freq": "868M",
    "model": "HP1000SE-PRO_Pro_V1.6.0",
}

host = "localhost"
port = "4199"

while True:
    try:
        print("Connecting to host {0} on port {1}".format(host, port))
        conn = http.client.HTTPConnection(host, port)
        headers = {"Content-type": "application/x-www-form-urlencoded"}

        usedParam = paramset_a

        usedParam["dateutc"] = datetime.now().strftime("%Y-%m-%d+%H:%M:%S")
        usedParam["tempinc"] = 20 + randrange(10) / 10.0

        params = urllib.parse.urlencode(usedParam)
        print(params)
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
    except Exception as err:
        print(err)
    finally:
        time.sleep(5)
