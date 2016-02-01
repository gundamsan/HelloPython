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

            # effect gaussian blur.
            blur = cv2.GaussianBlur(gray, (9,9), 0)
            
            # serching circle by hough conversion.
            circles = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT,
                                       dp=1, minDist=50, param1=120, param2=40,
                                       minRadius=5, maxRadius=100)

            # drawing circle.
            if circles is not None:
                for c in circles[0]:
                    cv2.circle(stream.array, (c[0], c[1]), c[2], (0,0,255), 2)

            # display result.
            cv2.imshow('frame', stream.array)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

            stream.seek(0)
            stream.truncate()

        # disposal.
        cv2.destroyAllWindows()