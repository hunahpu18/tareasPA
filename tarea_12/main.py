"""
Download and store data for usd/mx currency
@author: Jesus Rivera
CDMX
"""

import re
import csv
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import schedule


def get_data_scrapping():
    """
        Retrieves the table of currencies in yahoo finance

    """
    url = "https://finance.yahoo.com/currencies"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table')
    heads = table.thead
    currency_index = None
    currency_value_index = None
    result = {}
    for i, head in enumerate(heads.findAll('th')):
        if "name" in str(head.contents).lower():
            currency_index = i
        if "price" in str(head.contents).lower():
            currency_value_index = i
    for row in table.tbody.findAll('tr'):
        columns = row.findAll('td')
        pattern = r"<[^<>]+>"
        currency = re.sub(pattern, '', str(columns[currency_index]))
        value = re.sub(pattern, '', str(columns[currency_value_index]))
        result[currency] = float(value.replace(',', ''))
    return result


def job():
    """
    Auxiliary function for scheduling the job

    """
    print('running data collection')
    data = get_data_scrapping()
    with open('currency.csv', 'a',  newline='', encoding='utf-8') as file:
        # create the csv writer
        writer = csv.writer(file)
        for key in data:
            if 'MX' in key:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                writer.writerow([key, data[key], dt_string])


schedule.every(2).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
