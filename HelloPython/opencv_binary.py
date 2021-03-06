# coding: utf-8

# for ptvsd debug.
import ptvsd
import platform

import picamera
import picamera.array
import cv2

# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()


with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            # Acquisition PiCamera's image.
            camera.capture(stream, 'bgr', use_video_port=True)

            # conversion to gray image.
            gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            
            # conversion to binary image.
            #(ret, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            (ret, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            print ret

            # display result.
            cv2.imshow('frame', binary)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

            stream.seek(0)
            stream.truncate()

        # disposal.
        cv2.destroyAllWindows()