import serial.tools.list_ports
import struct

def get_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    print("# FIXME not work on linux")
    for p in ports:
        if "Arduino" in p[1]:
            return p[0]