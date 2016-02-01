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

# definition cascade classifier.
cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)

            # acquisition grayimage.
            gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            
            # detection pattern.
            facerect = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2,
                                                minSize=(30, 30), maxSize=(150, 150))

            # drawing rectangle on detected face.
            if len(facerect) > 0:
                for rect in facerect:
                    cv2.rectangle(stream.array, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]),
                                  (0, 0, 255), thickness=2)

            # display result.
            cv2.imshow('frame', stream.array)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

            stream.seek(0)
            stream.truncate()

        # disposal.
        cv2.destroyAllWindows()