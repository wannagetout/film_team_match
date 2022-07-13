from db import parser
from db import take_link_from_csv
import time
import random

if __name__ == "__main__":
    while True:
        print('1 - parse, 2 - read_csv, 3 - exit')
        user_input = input()
        if user_input == '1':    
            for page in range(1, 1231):   #перебор номеров страниц по образцу page='num'
                u = 'https://kino.mail.ru/cinema/all/?order=name&page=' + str(page)
                parser.parse(u) #вызов парсера
                print('-----------------------------------------------------')
                print(u, 'done') #чек-поинт считанной страницы
                print('-----------------------------------------------------')
                time.sleep(float(random.randint(5, 15)))    #задержка между запросами для избежания капчи
        if user_input == '2':
            take_link_from_csv.read_from_csv()
            #take_link_from_csv.take_content_from_link()
        if user_input == '3':
            exit()