import pytest
from API_Testing.gorest.api_collections.user_collection import User
from API_Testing.gorest.data.user_data import UserData
from API_Testing.gorest.CONSTANTS import ROOT_DIR
from API_Testing.gorest.configurations.config_parser import Configuration
import json


@pytest.fixture()
def env():
    with open(
            f'{ROOT_DIR}/configurations/configurations.json') as file:
        env = json.loads(file.read())
        env = Configuration(**env)
    return env


@pytest.fixture()
def create_and_get_user_data(env):
    user = User(env)
    response = user.create_random_user()
    response = response.json()
    user_data = UserData.from_json(**response['data'])
    return user_data
