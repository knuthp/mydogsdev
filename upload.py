import dropbox
from datetime import datetime



class Upload:
    def __init__(self):
        self.access_token = 'shi-tgc4bbAAAAAAAAAACSjMfqh8m4VyEPOLlFQ3afajcWy4wuEg_P9nR35eR7-G'
        self.dbx = dropbox.Dropbox(self.access_token)
        
    def upload(self, image, imageTime):
        folder = imageTime.strftime('%Y-%m-%d')
        filename = imageTime.strftime('%H-%M-%S')
        self.dbx.files_upload(image, '/' + folder + '/' + filename + '_original.jpg')
        
if __name__ == '__main__':
    upload = Upload()
    f = open('filename.jpg')
    upload.upload(f, datetime.now())
