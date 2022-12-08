import configparser
from HW22.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app-info', 'base_url')

    @staticmethod
    def get_user_email():
        return config.get('user_info', 'user_email')

    @staticmethod
    def get_user_password():
        return config.get('user_info', 'user_password')

    @staticmethod
    def get_browser():
        return config.read('browser', 'browser_id')
