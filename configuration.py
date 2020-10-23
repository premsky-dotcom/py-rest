import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db.sqllite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://local_dev_fid:password1@localhost/metadata_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
