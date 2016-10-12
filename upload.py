import dropbox
from datetime import datetime
import os



class Upload:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)
        
    def upload(self, image, imageTime):
        folder = imageTime.strftime('%Y-%m-%d')
        filename = imageTime.strftime('%H-%M-%S')
        self.dbx.files_upload(image, '/' + folder + '/' + filename + '_original.jpg')
        
if __name__ == '__main__':
    access_key = os.environ.get('DROPBOX_ACCESS_KEY')
    upload = Upload(access_key)
    f = open('filename.jpg')
    upload.upload(f, datetime.now())
