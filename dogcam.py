from upload import Upload
from datetime import datetime
from time import sleep
import logging
import sys
from requests.exceptions import ConnectionError
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


try:   
    from picamera import PiCamera
    logging.info("Using PiCamera")
#     import capturerpi.CaptureRaspberryPi
#     capture = CaptureRaspberryPi
except ImportError:
    logging.info("Using OpenCV camera")    
    from captureopencv import CaptureOpenCv
    capture = CaptureOpenCv()



logging.basicConfig(stream=sys.stdout, level=logging.INFO)

while True:
    try:
        captureTime = datetime.now()
        imgStr = capture.captureImage()
    
        upload = Upload()
        upload.upload(imgStr, captureTime)
        logging.info("Uploaded image {0}".format(captureTime))
    except ConnectionError as e:
        logging.exception("Failed to upload file", e)
    except Exception as e:
        logging.exception("Unexpected exception", e)
    
    sleep(60 * 5)