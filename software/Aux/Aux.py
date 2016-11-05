import serial.tools.list_ports
import struct
import sys


def get_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    if sys.platform == "linux" or sys.platform == "linux2":
        label = "ACM"
    else:
        label = "Arduino"

    for p in ports:
        if label in p[1]:
            return p[0]