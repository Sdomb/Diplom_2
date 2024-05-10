import allure
import requests

from data import Urls, TextAnswer
from methods import Methods


class TestChangingDataUsers:
    @allure.title("Изменение эмейла авторизованным пользаком")
    def test_auth_replacing_email_user(self):

        methods = Methods()
        user_data = methods.generate_user_data()
        req = requests.post(Urls.CREATE_USER, data=user_data)
        token = req.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_email_value = 'x' + user_data["email"][1:]
        new_email = {"email": new_email_value}
        replace = requests.patch(Urls.REPLACE_DATA, json=new_email, headers=headers)

        assert replace.status_code == 200 and replace.json()['user']['email'] == new_email['email']

    @allure.title("Изменение пароля авторизованным пользаком")
    def test_auth_replacing_password_user(self):
        methods = Methods()
        user_data = methods.generate_user_data()
        req = requests.post(Urls.CREATE_USER, data=user_data)
        token = req.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_password_value = 'x' + user_data["password"][1:]
        new_password = {"password": new_password_value}
        replace = requests.patch(Urls.REPLACE_DATA, json=new_password, headers=headers)

        assert replace.status_code == 200 and TextAnswer.TRUE in replace.text

    @allure.title("Изменение имени авторизованным пользаком")
    def test_auth_replacing_name_user(self):

        methods = Methods()
        user_data = methods.generate_user_data()
        req = requests.post(Urls.CREATE_USER, data=user_data)
        token = req.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_name_value = 'x' + user_data["name"][1:]
        new_name = {"name": new_name_value}
        replace = requests.patch(Urls.REPLACE_DATA, json=new_name, headers=headers)

        assert replace.status_code == 200 and replace.json()['user']['name'] == new_name['name']

    @allure.title("Изменение имени неавторизованным пользаком")
    def test_not_auth_replacing_date_user(self):

        methods = Methods()
        user_data = methods.generate_user_data()
        requests.post(Urls.CREATE_USER, data=user_data)
        headers = {"Content-type": "application/json"}
        new_name_value = 'x' + user_data["name"][1:]
        new_name = {"name": new_name_value}
        replace = requests.patch(Urls.REPLACE_DATA, json=new_name, headers=headers)

        assert replace.status_code == 401 and TextAnswer.UNAUTHORIZED in replace.text
