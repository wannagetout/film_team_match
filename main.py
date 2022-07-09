from db import parser 
import time
import random

if __name__ == "__main__":
    for page in range(1, 1231):   #перебор номеров страниц по образцу page='num'
        u = 'https://kino.mail.ru/cinema/all/?order=name&page=' + str(page)
        parser.parse(u) #вызов парсера
        print(u) #чек-поинт считанной страницы
        time.sleep(float(random.randint(5, 15)))    #задержка между запросами для избежания капчи
