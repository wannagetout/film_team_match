from bs4 import BeautifulSoup
import requests
import csv



def parse(url):
    HEADERS={
        'USER_AGENT': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'
    }
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('span', class_='link__text')
    #names = []
    #print(soup.text)
    with open('films_1.csv', 'a', newline='') as films: #csv файл с добавлением данных из цикла
        writer = csv.writer(films)
        writer.writerows(items)



