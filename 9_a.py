#!/usr/bin/env python3

#server program to read gas values

#sudo pip3 install Adafruit_MCP3008

import socket
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import time

HOST = '169.254.185.235'  # Standard loopback interface address (localhost)
PORT = 4000        # Port to listen on (non-privileged ports are > 1023)


SPI_DEVICE = 0
SPI_PORT = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                value = mcp.read_adc(0)
                print("Gas Value ", value , "units")
                if(value >300):
                    data = "Alert".encode('utf-8')
                    conn.sendall(data)
                time.sleep(3)
except KeyboardInterrupt:
    s.close()
    GPIO.cleanup()
