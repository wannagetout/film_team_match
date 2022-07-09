from msilib.schema import Error
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
     film_rate = ''
     film_names = soup.find_all('a', class_='link link_inline link-holder link-holder_itemevent link-holder_itemevent_small')
     film_info = soup.find_all('div', class_='margin_top_5')
     film_link = soup.find_all('a', class_='link link_inline link-holder link-holder_itemevent link-holder_itemevent_small')
     #film_rate_1 = (soup.find_all('span', class_='p-rate-flag__text')) 
     #film_rate_2 = (soup.find_all('span', class_='p-rate-flag__imdb-text'))
     
     film_names_list = []
     film_info_list = []
     #film_rate_list = []
     film_link_list = []
     for name in film_names:
          name = name.get_text()
          film_names_list.append(name)
          #print(name)
          
     for info in film_info:
          info = info.get_text()
          film_info_list.append(info)
          #print(info)
          
     for link in film_link:
          link = link.get('href')
          film_link_list.append('https://kino.mail.ru/' + link)
          
     #for rate in film_rate_1 and film_rate_2:
     #     if rate == str(rate):
     #          film_rate_list.append(rate)
     #     else:
     #          rate = rate.get_text()
     #          film_rate_list.append(rate)
     #    print(rate)
     #print(type(film_names))
     #print(type(film_info))
     #print(type(film_rate))
     #print(film_names)
     #print(film_info)
     #print(film_rate)
     #film_state = (film_names + film_info + film_rate).get_text()
     #print(film_state)
     #names_series = pd.Series(film_names_list)
     #info_series = pd.Series(film_info_list)
     #rate_series = pd.Series(film_rate_list)
     
     film_data = {
          'names': film_names_list,
          'info': film_info_list,
          #'rate': film_rate_list
          'link': film_link_list
          }
#----------------------------------------------------------------------------------------------------------------
     #field_names = ['film_name',
     #          'film_imfo',
     #          'film_rate']
     
     #film_names = pd.DataFrame(names_series, columns=field_names)
     #film_info_data = pd.DataFrame(info_series, columns=field_info)
     #film_rate_data = pd.DataFrame(rate_series, columns=film_rate)
     print(film_data)
     #data = [names_series + info_series + rate_series]
     
     dframe_names = pd.DataFrame(data=film_data)
     #dframe_info = pd.DataFrame(data=film_data['info'])
     #dframe_rate = pd.DataFrame(data=film_data['rate'])
     
     #film_info_data.to_csv('film_list_by_pandas', columns=fiesld_info)
     #film_rate_data.to_csv('film_list_by_pandas', columns=film_rate)
     
     dframe_names.to_csv('film_list.csv', encoding='utf-8', mode='a')
     #dframe_info.to_csv('film_list_by_pandas.csv', encoding='utf-8', mode='a')
     #dframe_rate.to_csv('film_list_by_pandas.csv', encoding='utf-8', mode='a')
     
     #print(dframe)
     #print(film_info_data)
     #print(film_rate_data)
     #    
     #    for info in film_info:
     #        data = pd.DataFrame(films, columns=field_names)


