import datetime
import fitbit
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from fitbit_client import fitbit_client
from path import MyPath
from settings import Settings


# Heart関連の処理をもっとできるようにする
class Heart(object):
    CLIENT_ID = Settings.CLIENT_ID
    CLIENT_SECRET = Settings.CLIENT_SECRET
    ACCESS_TOKEN = Settings.ACCESS_TOKEN
    REFRESH_TOKEN = Settings.REFRESH_TOKEN
    HEARTPATH = MyPath.HEARTPATH

    def __init__(self, date=None, detail_level='15min'):
        self.fitbit_client = fitbit_client.fitbit_client
        self.date = datetime.date.today().strftime('%Y-%m-%d') if date is None else date
        self.detail_level = detail_level

    def get_heart(self):
        # TODO: このあたりの処理はメソッドでどうにかうまく
        data = self.fitbit_client.intraday_time_series('activities/heart', self.date, detail_level=self.detail_level)
        heart_dic = data['activities-heart-intraday']['dataset']
        return heart_dic

    def convert_dic_to_dataframe(self, heart_dic):
        heart_df = pd.DataFrame.from_dict(heart_dic)
        return heart_df

    def save_heart_plot(self, heart_df):
        plt.figure(figsize=(20, 5))
        plt.title('Heart Rate')
        plt.xlabel('time')
        plt.ylabel('heart rate')
        plt.xticks(heart_df.index, heart_df.time)
        plt.plot(heart_df.index, heart_df.value)
        plt.savefig(self.HEARTPATH.joinpath(f'HR_{self.date}.png'))

    def main(self):
        heart_dic = self.get_heart()
        heart_df = self.convert_dic_to_dataframe(heart_dic)
        print(heart_df)
        self.save_heart_plot(heart_df)

if __name__ == '__main__':
    heart = Heart()
    heart.main()
