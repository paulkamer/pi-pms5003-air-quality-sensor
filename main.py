import paho.mqtt.client as mqtt
from pms5003 import PMS5003
import time
import json

PIN_ENABLE = "GPIO22"
PIN_RESET = "GPIO27"

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/pms5003"

pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600, pin_enable=PIN_ENABLE, pin_reset=PIN_RESET)

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
        data = pms5003.read()
        
        pm_data = {
            "pm1_0_ug_m3": data.pm_ug_per_m3(1.0),
            "pm2_5_ug_m3": data.pm_ug_per_m3(2.5),
            "pm10_ug_m3": data.pm_ug_per_m3(10.0),
            "pm1_0_ug_m3_atmos_env": data.pm_ug_per_m3(1.0, atmospheric_environment=True),
            "pm2_5_ug_m3_atmos_env": data.pm_ug_per_m3(2.5, atmospheric_environment=True),    
            "pm10_ug_m3_atmos_env": data.pm_ug_per_m3(None, atmospheric_environment=True),
            "pm0_3_per_1l_air": data.pm_per_1l_air(0.3),
            "pm0_5_per_1l_air": data.pm_per_1l_air(0.5),
            "pm1_0_per_1l_air": data.pm_per_1l_air(1.0),
            "pm2_5_per_1l_air": data.pm_per_1l_air(2.5),
            "pm5_per_1l_air": data.pm_per_1l_air(5),
            "pm10_per_1l_air": data.pm_per_1l_air(10),
        }
        
        print(pm_data)
        mqtt_client.publish(MQTT_TOPIC, json.dumps(pm_data))
        
        time.sleep(15)


except KeyboardInterrupt:
    pass
