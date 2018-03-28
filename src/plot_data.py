import matplotlib.pyplot as plt

from path import MyPath


class PlotData(object):

    def __init__(self, value_type):
        self.value_type = value_type
        self.RESULTSPATH = MyPath.RESULTSPATH.joinpath(self.value_type)

    def make_data_for_plot(self, dic_list):
        x = [i for i in range(len(dic_list))]
        time = [d['time'] for d in dic_list]
        value = [d['value'] for d in dic_list]
        return x, time, value

    def plot_data(self, dic_list, title=None, xlabel='time', ylabel='value'):
        titel = self.value_type if title is None else title
        x, time, value = self.make_data_for_plot(dic_list)
        plt.figure(figsize=(20, 5))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(x, time)
        plt.plot(x, value)

    def save_image(self, dic_list, filename=None, title=None, xlabel=None, ylabel=None):
        self.plot_data(dic_list, title, xlabel, ylabel)
        filename = self.value_type if filename is None else filename
        plt.savefig(self.RESULTSPATH.joinpath(f'{filename}.png'))


if __name__ == '__main__':

    from get_data import GetData

    value_type = 'heart'

    get_data = GetData(value_type)
    dic_list = get_data.get_dic_list()

    plot_data = PlotData(value_type)
    plot_data.save_image(dic_list)
