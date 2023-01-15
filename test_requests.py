from random import randint as rnd, choice
from datetime import date
from time import sleep
from tinydb import TinyDB
import string
import requests
import json

URL = 'http://localhost:5000/get_form'

def create_value(value_type):
    if value_type == 'phone':
        return f'+7 {rnd(100, 1000)} {rnd(100, 1000)} {rnd(10, 100)} {rnd(10, 100)}'

    elif value_type == 'date':
        start = date.today().replace(day=1, month=1).toordinal()
        end = date.today().toordinal()
        random_day = date.fromordinal(rnd(start, end))
        return random_day.strftime('%d.%m.%Y')

    elif value_type == 'text':
        words = ['я', 'ищу', 'работу', 'помогите']
        result_text = ''
        for sent in range(rnd(1, 5)):
            for i in range(rnd(2, len(words))):
                word = words[rnd(0, len(words) - 1)]
                if not i:
                    word = word.capitalize()
                result_text += ' ' + word
            result_text += '.'
        return result_text.lstrip()

    elif value_type == 'email':
        result = ''
        for i in range(rnd(5, 15)):
            result += choice(string.ascii_letters)
        return result + '@mail.ru'

    else:
        return None

def create_params():
    res = dict()
    db = TinyDB('db.json')
    data = db.all()
    random_temp = rnd(0, len(data) - 1)
    for item in data[random_temp]:
        if item == 'name':
            continue
        if rnd(0, len(data)):
            res[item] = create_value(data[random_temp][item])
    return res

def request():
    while True:
        params = create_params()
        print(f'Запрос:\n{json.dumps(params, indent=4)}')
        output = requests.post(URL, params=params).json()
        print(f'Ответ:\n{json.dumps(output, indent=4)}\n')
        sleep(5)

if __name__ == '__main__':
    request()
