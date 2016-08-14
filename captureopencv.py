from cv2 import VideoCapture, namedWindow, CV_WINDOW_AUTOSIZE, imshow, waitKey, destroyWindow, imwrite, imencode, imdecode,\
    CV_LOAD_IMAGE_COLOR


class CaptureOpenCv:
    def __init__(self):
        self.cam = VideoCapture(0)
        
    def captureImage(self):
        s, img = self.cam.read()
        if s:    # frame captured without any errors
            buf = imencode('.jpg', img)[1]
            return buf.tostring()


if __name__ == '__main__':
        capture = CaptureOpenCv() 
        img = capture.captureImage()
#         npImg = imdecode(img, CV_LOAD_IMAGE_COLOR)
#         namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
#         imshow("cam-test",npImg)
#         waitKey(0)
#         destroyWindow("cam-test")
#         imwrite("filename.jpg",npImg) #save image        
