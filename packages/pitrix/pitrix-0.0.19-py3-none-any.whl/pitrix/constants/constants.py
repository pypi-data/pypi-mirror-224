# --coding:utf-8--
# import sys

class DataBase:
    DB_NAME = "pitrix.db"
    CONFIG_TABLE = 'config'
    CACHE_TABLE = 'cache'
    SCHEMA_TABLE = 'schema'
    CACHE_VAR_NAME = 'var_name'
    CACHE_RESPONSE = 'response'
    CACHE_WORKER = 'worker'
    CACHE_API_INFO = 'api_info'
    CONFIG_KEY = 'key'
    CONFIG_VALUE = 'value'
    SCHEMA_API_NAME = 'api_name'
    SCHEMA_SCHEMA = 'schema'

class LogConfig:
    DEFAULT_LOG_LEVEL = 'INFO'
    FILE_FMT = '%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
    CONSOLE_FMT = '%(log_color)s%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
    COLOR = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'purple',
        }

class Conf:
    CONF_NAME = "config.yaml"
    UTILS_CONF_NAME = "utils.yaml"
    CURRENT_ENV_KEY = 'env'
    CONF_DIR = "conf/"
    TEMPLATE_SUFFIX = '.temp'

class Allure:
    JSON_DIR = "reports/json"
    HTML_DIR = "reports/html"