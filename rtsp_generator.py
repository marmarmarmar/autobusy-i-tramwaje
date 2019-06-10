import cv2
import time


class RTSP_WRAPPER:

    @classmethod
    def get_frames_generator(cls, rtsp_path):
        i = 0
        while True:
            grabbed = True
            vs = cv2.VideoCapture(rtsp_path)
            while grabbed:
                grabbed, frame = vs.read()
                if grabbed:
                    i += 1
                    print(i)
                    yield frame
                else:
                    print('RELOAD TUTEJ')
                    print(i)
                    grabbed = True
                    vs = cv2.VideoCapture(rtsp_path)

