from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "localhost"  # You can also mention here the external IP for Modbus Recorder
SERVER_PORT = 502
c = ModbusClient()
# uncomment this line to see debug message
# c.debug(True)
# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)
while True:
    # open or reconnect TCP to server

    if not c.is_open():
        if not c.open():
            print("unable to connect to " + SERVER_HOST + ":" + str(SERVER_PORT))
    # if open() is ok, read register (Modbus function 0x03)
    if c.is_open():
        # read 10 registers at address 0, store result in regs list
        regs = c.read_holding_registers(0, 10)
        # if success display registers
        if regs:
            print("reg ad #0 to 9: " + str(regs))
            # print(regs)
    # sleep 2s before next polling
    time.sleep(2)
