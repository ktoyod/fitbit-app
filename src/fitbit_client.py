import fitbit

from path import MyPath
from settings import Settings


class FitbitClient(object):
    CLIENT_ID = Settings.CLIENT_ID
    CLIENT_SECRET = Settings.CLIENT_SECRET
    ACCESS_TOKEN = Settings.ACCESS_TOKEN
    REFRESH_TOKEN = Settings.REFRESH_TOKEN
    HEARTPATH = MyPath.HEARTPATH

    def __init__(self):
        self.fitbit_client = fitbit.Fitbit(self.CLIENT_ID, self.CLIENT_SECRET,
                                           access_token=self.ACCESS_TOKEN, refresh_token=self.REFRESH_TOKEN)


fitbit_client = FitbitClient()
