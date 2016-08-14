from io import BytesIO
try :
    from picamera import PiCamera


    class CaptureRaspberryPi:
        def __init__(self):
            self.my_stream = BytesIO()
            self.camera = PiCamera
            self.camera.resolution = (1024, 768)
        
        def captureImage(self):
            self.camera.capture(self.my_stream, 'jpg', resize=(640, 480))
            return self.my_stream.getvalue()

            

except ImportError:
    pass
    