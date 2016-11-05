import argparse
import serial.tools.list_ports
from Aux.Aux import *
import time


def gui(interval):
    from GUI.gui import TempLogger

    app = TempLogger()
    app.master.title(u"ä")
    app.mainloop()


def cli(interval):
    from CLI.cli import TempLogger 
    # connect to arduino
    port = get_arduino_port()
    print(port)

    sensor = TempLogger()

    print(u"# Temp\tHumidity")
    print(u"# ºC  \t %")
    while 1:
        # FIXME change here to something like try, catch
        t = sensor.getTemperature()
        h = sensor.getHumidity()

        # FIXME needs some formating here to maintain everything always aligned
        print(t, h)

        time.sleep(interval)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cli", action = "store_true", help = "Do not start GUI.")
    parser.add_argument("-p", "--port", type = str, default = "/dev/ttyACM0", help = "Serial port connected to Arduino board.")
    parser.add_argument("-i", "--interval", type = int, default = 2, help = "interval in seconds between measurements. Must be greater than 2.")
    args = parser.parse_args()

    if args.interval <= 2:
        args.interval = 2
        print("Interval between measurments must be 2 or more seconds.")
        print("Set to 2 seconds. \n")

    if args.cli:
        cli(args.interval)
    else:
        gui(args.interval)