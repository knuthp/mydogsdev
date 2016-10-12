import unittest
import dropbox
import os

class Test(unittest.TestCase):


    def testName(self):
        client = dropbox.client.DropboxClient(self.access_key)
        print 'linked account: ', client.account_info()


    def testUpload(self):
        client = dropbox.client.DropboxClient(self.access_key)
        f = open('../filename.jpg', 'rb')
        response = client.put_file('/magnum-opus.txt', f)
        print 'uploaded:', response
        
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.access_key = os.environ.get('DROPBOX_ACCCESS_TOKEN')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()