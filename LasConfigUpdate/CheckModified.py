import hashlib

from ConfigManagement import ConfigManager
from S3FileManagement import S3FileMgmt
from API_Call import CloudFile


class CheckModifiedFile:
    in_path = None
    hashVar = None
    config = None
    s3FileMgmt = None
    APICall = None

    def __init__(self):
        self.config = ConfigManager()
        self.s3FileMgmt = S3FileMgmt()
        self.APICall = CloudFile()
        self.in_path = self.config.get_config('file_path') + self.config.get_config('file_name')

    @staticmethod
    def hash_file(filename, block_size=2 ** 20):
        md5 = hashlib.md5()
        with open(filename, "rb") as f:
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
        return md5.digest()

    def schedule_check(self):
        tempHash = self.hash_file(self.in_path)
        if self.hashVar is None:
            self.hashVar = tempHash
            print("Initial")
            self.APICall.uploadFile(self.in_path)
        else:
            if self.hashVar != tempHash:
                self.hashVar = tempHash
                print("Modified")
                self.s3FileMgmt.upload_file(self.in_path, 'mylasconfigtest')
            else:
                print("Not Modified")
