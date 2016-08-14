from io import BytesIO
from time import sleep

try :
    from picamera import PiCamera
    print("OK Import")

    class CaptureRaspberryPi:
        def __init__(self):
            self.camera = PiCamera()
        
        def captureImage(self):
            my_stream = BytesIO()
            self.camera.start_preview()
            sleep(2)
            self.camera.capture(my_stream, 'jpeg')
            return my_stream.getvalue()

            

except ImportError:
    print("ERROR")
    pass


if __name__ == '__main__':
    capture = CaptureRaspberryPi()
    imgStr = capture.captureImage()    
    print(len(imgStr))
    imgFile = open('myImg.jpg', 'w')
    imgFile.write(imgStr)
    imgFile.close()
   
