from pms5003 import PMS5003

pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600, pin_enable="GPIO22", pin_reset="GPIO27")

try:
    while True:
        data = pms5003.read()
        print(data)

except KeyboardInterrupt:
    pass