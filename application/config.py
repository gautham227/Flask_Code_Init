import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG=False
    SECRET_KEY=None
    
class DevelopConfig(Config):

    DEBUG=True
    SECRET_KEY="fgdmgfdgnmddrmdfmngndsm"