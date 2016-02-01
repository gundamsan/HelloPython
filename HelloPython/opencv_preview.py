# coding: utf-8
import ptvsd
import platform

import picamera
import picamera.array
import cv2

ptvsd.enable_attach(secret = 'ptvsd')

os = platform.system()

print 'Waiting for attach...'

if os != 'Windows':
    ptvsd.wait_for_attach()

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)

            cv2.imshow('frame', stream.array)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()