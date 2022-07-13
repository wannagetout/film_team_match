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
     film_names = soup.find_all('a', class_='link link_inline link-holder link-holder_itemevent link-holder_itemevent_small')
     film_info = soup.find_all('div', class_='margin_top_5')
     film_link = soup.find_all('a', class_='link link_inline link-holder link-holder_itemevent link-holder_itemevent_small')
  
     film_names_list = []
     film_info_list = []
     film_link_list = []
     for name in film_names:
          name = name.get_text()
          film_names_list.append(name)
          
     for info in film_info:
          info = info.get_text()
          film_info_list.append(info)
         
     for link in film_link:
          link = link.get('href')
          film_link_list.append('https://kino.mail.ru/' + link)
              
     film_data = {
          'names': film_names_list,
          'info': film_info_list,

          'link': film_link_list
          }
     print(film_data)
    
     dframe_names = pd.DataFrame(data=film_data)

     dframe_names.to_csv('film_list.csv', encoding='utf-8', mode='a')
