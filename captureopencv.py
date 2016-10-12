import numpy as np
from cv2 import VideoCapture, imencode, imdecode, namedWindow,\
    WINDOW_AUTOSIZE, imshow, waitKey, destroyWindow, imwrite
    


class CaptureOpenCv:
    def __init__(self):
        self.cam = VideoCapture(0)
        
    def captureImage(self):
        rc, img = self.cam.read()
        if rc:    # frame captured without any errors
            buf = imencode('.jpg', img)[1]
            return buf.tostring()


if __name__ == '__main__':
    capture = CaptureOpenCv() 
    imgStr = capture.captureImage()
    image = np.fromstring(imgStr, dtype=np.uint8)
    npImg = imdecode(image, 4)
    namedWindow("cam-test", WINDOW_AUTOSIZE)
    imshow("cam-test",npImg)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg",npImg) #save image        
