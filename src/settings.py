import os


class Settings(object):
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
