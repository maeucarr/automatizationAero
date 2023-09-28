import configparser

from utilities.settings import BASE_DIR

# configuration director path
path = BASE_DIR / 'configurations/config.ini'

# initial the configparser
config = configparser.ConfigParser()

# read the config.ini
config.read(path)


class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_user_name():
        username = config.get('Auth', 'username')
        return username

    @staticmethod
    def get_user_password():
        password = config.get('Auth', 'password')
        return password





