# coding: utf-8

# for ptvsd debug.
import ptvsd
import platform

import time
import picamera

# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture('foo.jpg')