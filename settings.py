import os
from tornado.options import define, options

from utils.settings import parse_environment

# Constants

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG_PATH = os.path.join('/etc', 'jet.conf')

# Options

define('address', default='0.0.0.0', help='server address')
define('port', default=8888, help='server port', type=int)
define('config', default=DEFAULT_CONFIG_PATH, help='config file path')
define('debug', default=False, help='debug mode', type=bool)

define('web_base_url', default='https://app.jetadmin.io', help='Jet Admin frontend application base URL')
define('api_base_url', default='https://api.jetadmin.io/api', help='Jet Admin API base URL')

define('database_engine', help='database engine (postgresql, mysql, oracle, mssql, sqlite)')
define('database_host', help='database host')
define('database_port', help='database port', type=int)
define('database_user', help='database user')
define('database_password', help='database password')
define('database_name', help='database name or path')

required_options = [
    'address',
    'port',
    'database_engine',
    'database_name',
]

# Parse

options.parse_command_line(final=False)

if options.config:
    try:
        options.parse_config_file(options.config, final=False)
    except FileNotFoundError as e:
        if options.config != DEFAULT_CONFIG_PATH:
            raise e

parse_environment(options, final=True)

for option in required_options:
    if option not in options or options[option] is None:
        raise Exception('Required option {} is not specified'.format(option))

# Settings

ADDRESS = options.address
PORT = options.port
DEBUG = options.debug

WEB_BASE_URL = options.web_base_url
API_BASE_URL = options.api_base_url

DATABASE_ENGINE = options.database_engine
DATABASE_HOST = options.database_host
DATABASE_PORT = options.database_port
DATABASE_USER = options.database_user
DATABASE_PASSWORD = options.database_password
DATABASE_NAME = options.database_name