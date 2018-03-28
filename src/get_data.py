import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from fitbit_client import fitbit_client


class GetData(object):

    def __init__(self, value_type):
        self.fitbit_client = fitbit_client.fitbit_client
        self.value_type = value_type

    def get_json(self, base_date=None, detail_level='15min', start_time=None, end_time=None):
        base_date = datetime.date.today().strftime('%Y-%m-%d') if base_date is None else base_date
        json_data = self.fitbit_client.intraday_time_series(f'activities/{self.value_type}',
                                                            base_date=base_date, detail_level=detail_level,
                                                            start_time=start_time, end_time=end_time)
        return json_data

    def get_dic_list(self, base_date=None, detail_date='15min', start_time=None, end_time=None):
        json_data = self.get_json(base_date, detail_date, start_time, end_time)
        dic_list = json_data[f'activities-{self.value_type}-intraday']['dataset']
        return dic_list

    def main(self):
        return self.get_dic_list()


if __name__ == '__main__':
    get_data = GetData('steps')
    dic_list = get_data.main()
    print(dic_list)
