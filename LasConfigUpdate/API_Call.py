import requests
from ConfigManagement import ConfigManager


class CloudFile:

    config = ConfigManager()
    api_url = config.get_config('upload_url')
    site_id = config.get_config('upload_siteId')

    def __init__(self):
        self.config = ConfigManager()
        self.api_url = self.config.get_config('upload_url')

    @classmethod
    def uploadFile(cls, in_path):
        print(cls.api_url)
        print(cls.site_id)
        uplFile = open(in_path, "rb")

        response = requests.post(cls.api_url, files={"uploadFile": uplFile}, data={'siteId': cls.site_id})
        print(response.json())
