import configparser
from os import path

ROOT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

_config_path = path.join(ROOT_PATH, "config_ui_test.ini")

_config = configparser.RawConfigParser()
_config.read(_config_path)


class ConfigManager:
    url = _config.get("app_data", "BASE_URL")
    user_name = _config.get("user_data", "BASE_USER")
    user_pass = _config.get("user_data", "BASE_PASSWORD")
    browser = _config.get("browser_data", "BROWSER")
