# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def wind(speed):
    """Define the wind speed routine"""
    from gpiozero import Button
    wind_speed_sensor = Button(5)
    wind_count = 0

    def spin():
        global wind_count
        wind_count =+ 1
        return wind_count

def thp():
    import bme280
    import smbus2
    from time import sleep

    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)
    bme280.load.calibration_params(bus,address)
    while True
        bme280_data = bme280.sample(bus, address)
        temperature = randrange(60, 110,0.3) # bme280_data.temperature
        humidity = randrange(0, 100.0.3) # bme280_data.humidity
        pressure = randrange(60, 100, 0.3) # bme280_data.pressure
        sleep(1)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    thp()
    wind(speed)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
