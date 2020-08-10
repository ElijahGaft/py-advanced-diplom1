import datetime

# import json
# import sys
# import time
from urllib.parse import urlencode
import requests
# from pip._vendor.msgpack.fallback import xrange




APP_ID = 7058177  # ID моего приложения зарегестрированного на сайте VK
AUTH_URL = 'https://oauth.vk.com/authorize'
Auth_DATA = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'account, photos, friends', # какие конкретно права вы хотите запросить у пользователя
    'response_type': 'token'
}

# print('?'.join((AUTH_URL, urlencode(Auth_DATA)))) # выдаёт ссылку на страничку разрешений прав, так я могу узнать токен.

TOKEN = 'dba17757431762a04ef6647e31f5be242b0557e32712ad2d3076454d35caed914fc990fbe41f23720c799'  # токен моего пользователя через которого идут все запросы


class User:
    def __init__(self, user_id, token):  # При создании обьекта класса, мы должны передать имя или ID пользователя
        self.user_id = user_id
        self.token = token

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.61',
            'user_id': self.user_id
        }

    def request(self, method, params):  # Формирование запроса
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def get_friends(self):
        params = self.get_params()
        response = self.request(
            'friends.get',
            params=params
        )
        return response.json()['response']
    
    def getProfileInfo(self):
        params = self.get_params()
        response = self.request(
            'account.getProfileInfo',
            params=params
        )
        return response.json()['response']

        
#306008470
now = datetime.datetime.now()
def paser_user_data(id_input):
    Person = User(id_input, TOKEN)
    #friends =  Person.get_friends()  # метод класса для поиска друзей юзера, переменная хранит словарь (имя и id)
    #friends = friends.get('items')
    info = Person.getProfileInfo() 
    Percon_birth = birth(info)
    Percon_sex = sex(info)
    Percon_city = city(info)
    Percon_relation = relation(info)
    print('Adge: ', Percon_birth)
    print('Sex: ', Percon_sex)
    print('City: ', Percon_city)
    print('Relation: ', Percon_relation)
    
def relation(info):
    relation = info.get('relation')
    if sex in [2, 3, 4, 7, 8,]:
        print('Сорян, приложение работает только для свободных...') 
    return relation    
    
def birth(info):
    if info.get('bdate_visibility') == 1:
        birth = info.get('bdate')
        birth = now.year-int(birth[-4:])
    else:
        print('укажите Ваш возвраст:')
        birth = check_input()
    return birth
    
def sex(info):
    sex = info.get('sex')
    if sex == 0:
        print('укажите Ваш пол (м, ж)')
        sex = check_input()
    if sex == 'м':
        sex = 2
    if sex == 'ж':
        sex = 1 
    return sex

def city(info):
    city = info.get('city')
    city = city.get('title')
    if city == None:
        print('укажите Ваш город: ')
        city = check_input()
    return city
        
def check_input():
    while True:
        data_input = input('')
        if data_input == '':
            print('Неверный ввод, пробуй еще')
        else:
            return data_input
    
    
def verify_id(id_input):
    # Проверка ввода
    
    # ...
    
    # Выполняем работу над указаным ID
    paser_user_data(id_input)
    return

if __name__ == '__main__':
    #while True:
        id_input = input('\nимя или ID пользователя:')
        if id_input == "exit":
            print('Выхожу из программы')
            # return
        else:
            verify_id(id_input)
