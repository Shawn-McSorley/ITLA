from rs232_comm import ITLA
from globals import *
from response import *

if __name__ == '__main__':
    laser = ITLA()
    laser.connect('/dev/ttyUSB0')
    laser.turn_off()
    laser.disconnect()