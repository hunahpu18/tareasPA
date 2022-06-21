# -*- coding: utf-8 -*-
"""
Download world happiness time series from hedonometer project.
See https://hedonometer.org/timeseries/en_all/?from=2020-08-24&to=2022-02-23
Created on Tue Feb 24 15:35:23 2022

@author: Jesus Rivera
CDMX
"""

import datetime

import matplotlib.pyplot as plt
import requests


def download_happiness(start_date, records):
    """
    Download happiness records from the url below. Happiness records are stored
    into happiness database table.

    Parameters
    ----------
    start_date : datetime.pyi
        Initial downloading base_date.
    records : int
        Maximum number of records after start_date to download.
    """
    data_json = requests.get(
        'https://hedonometer.org/api/v1/happiness/?format=json&timeseries__'
        f'title=en_all&date__gte='
        f'{start_date.strftime("%Y-%m-%d")}&limit={records}')
    data = data_json.json()
    data = [[
        datetime.datetime.strptime(d['date'], "%Y-%m-%d"), d['frequency'],
        float(d['happiness'])
    ] for d in data['objects']]

    return data


def retrieve_happiness(start_date: datetime, end_date: datetime = datetime.date.max, step: int = 1):
    """
    Download happiness records from the url below, from start date to end date
    :param start_date: start date to download
    :param end_date: end date to download
    :param step: step taken between downloaded dates
    :return:
    """
    data = download_happiness(start_date, 5000)
    if end_date != datetime.date.max:
        if end_date < start_date.date():
            raise Exception('start_date must be before end_date')

        filtered_data = list(filter(lambda elto: elto[0] < end_date, data))
        filtered_data.sort(key=lambda elto: elto[0])
        indices = range(0, len(filtered_data) + 1, step)
        return [filtered_data[i] for i in indices]

    indices = range(0, len(data) // step)
    return [data[i * step] for i in indices]


def plot_data(data):
    """
    Plot time series of data
    :param data:
    :return: data to plot
    """
    data.sort(key=lambda elto: elto[0])
    x = [elto[0] for elto in data]
    y = [elto[2] for elto in data]
    plt.title("Promedio de la Felicidad en Twitter")
    plt.xlabel("Fecha")
    plt.ylabel("Felicidad")
    plt.plot(x, y, 'o-')
    plt.show()


if __name__ == "__main__":
    date = datetime.datetime(2022, 1, 1)
    downloaded_data = retrieve_happiness(date, step=3)
    plot_data(downloaded_data)

    print(f"{downloaded_data}")
