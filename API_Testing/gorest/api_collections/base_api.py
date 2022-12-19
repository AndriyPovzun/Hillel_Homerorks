import requests
import json
from API_Testing.gorest import conftest


class BaseAPI:
    def __init__(self, env):
        self.__env = env
        self.__base_url = self.__env.base_url
        self.__headers = {"Authorization": self.__env.authorization,
                          "Content-Type": self.__env.content_type}
        self.__request = requests

    def _get(self, url, params=None):
        response = self.__request.get(url=f'{self.__base_url}{url}', params=params, headers=self.__headers)
        return response

    def _post(self, url, body=None, params=None):
        json_body = json.dumps(body)
        response = self.__request.post(url=f'{self.__base_url}{url}', data=json_body, params=params,
                                       headers=self.__headers)
        return response

    def _delete(self, url, params=None):
        response = self.__request.delete(url=f'{self.__base_url}{url}', params=params, headers=self.__headers)
        return response

    def _put(self, url, body=None, params=None):
        json_body = json.dumps(body)
        response = self.__request.put(url=f'{self.__base_url}{url}', data=json_body, params=params,
                                      headers=self.__headers)
        return response