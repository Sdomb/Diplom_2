import pytest
import requests

from methods import Methods
from data import Urls


@pytest.fixture(scope='function')
def create_user():
    methods = Methods()
    data = methods.generate_user_data()
    auth_data = data.copy()  # сохраняю сюда данные для последующего удаления пользака
    yield data
    response_post = requests.post(Urls.LOGIN_USER, data={"email": auth_data['email'], "password": auth_data['password']})
    token = response_post.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    requests.delete(Urls.DELETE_USER, headers=headers)
