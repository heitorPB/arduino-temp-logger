import argparse
import serial.tools.list_ports
from Aux.Aux import *
import time


def gui(interval, port):
    from GUI.gui import TempLogger

    app = TempLogger()
    app.master.title(u"ä")
    app.mainloop()


def cli(interval, port):
    from CLI.cli import TempLogger 

    sensor = TempLogger(port)

    print(u"# Temp\tHumidity")
    print(u"# ºC  \t %")
    while 1:
        # FIXME change here to something like try, catch
        t = sensor.getTemperature()
        h = sensor.getHumidity()

        if t != None and h != None:
            print(t, h, sep = '\t')

        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cli", action = "store_true", help = "Do not start GUI.")
    parser.add_argument("-p", "--port", type = str, default = None, help = "Serial port connected to Arduino board.")
    parser.add_argument("-i", "--interval", type = int, default = 2, help = "interval in seconds between measurements. Must be greater than 2.")
    # TODO get baudrate
    args = parser.parse_args()

    if args.interval < 2:
        args.interval = 2
        print("Interval between measurments must be 2 or more seconds.")
        print("Set to 2 seconds. \n")

    if args.port == None:
        port = get_arduino_port()
    else:
        port = args.port
    # FIXME add verbose flag for this shit
    print("Possible Arduino in ", port)


    if args.cli:
        cli(args.interval, port)
    else:
        gui(args.interval, port)