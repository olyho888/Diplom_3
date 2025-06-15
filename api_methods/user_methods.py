import allure
import requests
from data import Data
from helpers import Helpers


class UserMethods:

    @allure.step('Создание уникального пользователя')
    def create_user(self):
        username = Helpers.generate_random_string(6)
        params = {'email': Helpers.generate_random_email(username),
                  'password': Helpers.generate_random_string(6),
                  'name': username}
        response = requests.post(url=f'{Data.URL_API_AUTH}/register', data=params, verify=False)
        if response.status_code == 200:
            token = response.json()['accessToken']
            return params, token
        else:
            raise AssertionError('Ошибка при создании пользователя')

    @allure.step('Удаление пользователя')
    def delete_user(self, token):
        headers = {'Authorization': token}
        requests.delete(url=f'{Data.URL_API_AUTH}/user', headers=headers, verify=False)
