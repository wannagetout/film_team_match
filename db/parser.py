import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy

def parse(url):
    HEADERS={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    film_names = soup.find_all('span', class_='link__text')
    film_info = soup.find_all('div', class_='margin_top_5')
    film_rate = soup.find_all('span', class_='p-rate-flag__text')
    film_names_list = []
    film_info_list = []
    film_rate_list = []
    for name in film_names:
         name = name.get_text()
         film_names_list.append(name)
         
    for info in film_info:
         info = info.get_text()
         film_info_list.append(info)
    
    for rate in film_rate:
         rate = rate.get_text()
         film_rate_list.append(rate)
    #print(type(film_names))
    #print(type(film_info))
    #print(type(film_rate))
    #print(film_names)
    #print(film_info)
    #print(film_rate)
    #film_state = (film_names + film_info + film_rate).get_text()
    #print(film_state)
    names_series = pd.Series(film_names_list)
    info_series = pd.Series(film_info_list)
    rate_series = pd.Series(film_rate_list)
    
    
    
    with open('film_list_by_pandas.csv', 'a', newline='') as films: #csv файл с добавлением данных из цикла
        field_names = ['film_name']
        fiesld_info =['film_imfo']
        film_rate = ['film_rate']
        film_names = pd.DataFrame(names_series, columns=field_names)
        film_info_data = pd.DataFrame(info_series, columns=fiesld_info)
        film_rate_data = pd.DataFrame(rate_series, columns=film_rate)
        print(film_names)
        print(film_info_data)
        print(film_rate_data)
    #    
    #    for info in film_info:
    #        data = pd.DataFrame(films, columns=field_names)


