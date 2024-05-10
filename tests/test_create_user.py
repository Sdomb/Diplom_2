import allure
import requests

from data import Urls, TextAnswer
from methods import Methods


class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, create_user):

        resp = requests.post(Urls.CREATE_USER, data=create_user)
        assert resp.status_code == 200 and TextAnswer.TRUE in resp.text

    @allure.title("Создание пользователья который уже существует")
    def test_create_not_unique_user(self, create_user):

        user = create_user
        requests.post(Urls.CREATE_USER, data=user)
        resp = requests.post(Urls.CREATE_USER, data=user)

        assert resp.status_code == 403 and TextAnswer.FALSE

    @allure.title("Создание пользователя без одного обязательного поля")
    def test_create_invalid_date_user(self):
        methods = Methods()
        req = methods.generate_user_data()
        req['name'] = ''
        resp = requests.post(Urls.CREATE_USER, data=req)

        assert resp.status_code == 403 and TextAnswer.ALREADY_EXISTS
