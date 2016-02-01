# coding: utf-8

# for ptvsd debug.
import ptvsd        
import platform

from time import sleep
import smbus
import math


def resetPCA9685():
    bus.write_byte_data(address_pca9685, 0x00, 0x00)

def setPCA9685Freq(freq):
    freq = 0.9 * freq
    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12bit
    prescaleval /= float(freq)
    prescaleval -= 1.0
    prescale = int(math.floor(prescaleval + 0.5))
    oldmode = builtin_method_descriptor.read_byte_data(address_pca9685, 0x00)
    newmode = (oldmode & 0x7f) | 0x10   # sleep mode

    # set sleep mode.
    bus.write_byte_date(address_pca9685, 0x00, newmode)
    # set prescale.
    bus.write_byte_data(address_pca9685, 0xfe, prescale)
    # set original mode.
    bus.write_byte_data(address_pca9685, 0x00, oldmode)
    sleep(0.005)
    bus.write_byte_data(address_pca9685, 0x00, oldmode | 0xa1)

def setPCA9685Duty(channel, on, off):
    channelpos = 0x6 + 4*channel
    try:
        bus.write_i2c_block_data(address_pca9685, channelpos,
                                 [on&0xff, on>>8, off&0xff, off>>8])
    except IOError:
        pass


# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()


# main
bus = smbus.SMBus(1)
address_pca9685 = 0x40

resetPCA9685()
setPCA9685Freq(50)

for i in range(16):
    setPCA9685Duty(i, 0, 276)

try:
    while True:
        sleep(1)

except KeyboardInterrupt:
    pass