import os
from configparser import ConfigParser


def config_open(filename='db_config.ini', section='database'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


params = config_open()
user = params.get('user')
passwd = params.get('password')
localhost = params.get('host')
db = params.get('database')
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(user, passwd, localhost, db)
