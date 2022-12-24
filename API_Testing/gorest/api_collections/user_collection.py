from API_Testing.gorest.api_collections.base_api import BaseAPI
import random


class User(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__env = env
        self.__user_url = self.__env.user_url
        self.__gender = ['male', 'female']
        self.__status = ['active', 'inactive']

        __valid_email = f'{self._fake.name()}@gmail.com'.replace(' ', '_')
        self.__random_user = {"email": f"{__valid_email}",
                              "name": f"{self._fake.name()}",
                              "gender": f"{random.choice(self.__gender)}",
                              "status": f"{random.choice(self.__status)}"}

    def get_all_users(self):
        return self._get(f'{self.__user_url}')

    def get_person(self, person_id):
        return self._get(f'{self.__user_url}{person_id}')

    def create_user(self, user_data):
        return self._post(url=f'{self.__user_url}', body=user_data)

    def create_random_user(self):
        return self._post(url=f'{self.__user_url}', body=self.__random_user)

    def get_user_data(self, person_id):
        response = self._get(f'{self.__user_url}{person_id}')
        response = response.json()
        return response['data']

    def delete_user(self, person_id):
        return self._delete(url=f'{self.__user_url}{person_id}')

    def update_user_name(self, person_id, user_data=None):
        if not user_data:
            user_data = {"name": f"{self._fake.name()}"}
        return self._put(url=f'{self.__user_url}{person_id}', body=user_data)

    @staticmethod
    def get_quantity_users_from_response(data_list):
        total = data_list['meta']['pagination']['total']
        return total
