import configparser


class ConfigManager:
    parser = configparser.ConfigParser()
    parser.read('AWSLasUpload.ini')

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read('AWSLasUpload.ini')

    @classmethod
    def get_config(cls, key):
        temp = cls.parser.get('DEFAULT', key)
        return temp

    @classmethod
    def get_config_with_section(cls, section, key):
        temp = cls.parser.get(section, key)
        return temp
