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

    for name in film_names:
         name = name.get_text()
         print(name)
    
    #print(type(film_names))
    #print(type(film_info))
    #print(type(film_rate))
    #print(film_names)
    #print(film_info)
    #print(film_rate)
    #film_state = (film_names + film_info + film_rate).get_text()
    #print(film_state)

        
    #with open('film_list_by_pandas.csv', 'w', newline='') as films: #csv файл с добавлением данных из цикла
    #    field_names = ['film_name',
    #                   'film_imfo',
    #                   'film_rate']
    #    data = pd.DataFrame(film_state, columns=field_names)
    #    
    #    for info in film_info:
    #        data = pd.DataFrame(films, columns=field_names)


