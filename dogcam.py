from upload import Upload
from datetime import datetime
from time import sleep
import logging
import sys
from requests.exceptions import ConnectionError
import os
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


try:   
    from picamera import PiCamera
    logging.info('A Using PiCamera')
    from capturerpi import CaptureRaspberryPi
    capture = CaptureRaspberryPi()
except ImportError as e:
    logging.info('Using OpenCV camera')    
    from captureopencv import CaptureOpenCv
    capture = CaptureOpenCv()



logging.basicConfig(stream=sys.stdout, level=logging.INFO)

while True:
    try:
        captureTime = datetime.now()
        imgStr = capture.captureImage()
        access_key = os.environ.get('DROPBOX_ACCESS_KEY')
        upload = Upload(access_key)
        upload.upload(imgStr, captureTime)
        logging.info('Uploaded image %s', captureTime)
    except ConnectionError as e:
        logging.exception("Failed to upload file, %s", e)
    except Exception as e:
        logging.exception('Unexpected exception')
    
    sleep(60 * 5)
