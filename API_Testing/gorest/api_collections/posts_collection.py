from API_Testing.gorest.api_collections.base_api import BaseAPI
from API_Testing.gorest.data.post_data import PostData
import json
from faker import Faker


class PostsAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__env = env
        self.__posts_url = self.__env.post_url
        self.__fake = Faker()
        self.__fake_post = {"title": f'{self.__fake.text()}',
                            "body": f'{self.__fake.text()}'}

    def create_user_post(self, user_id, body=None):
        self.__posts_url = self.__posts_url.replace('user_id', str(user_id))
        if not body:
            body = self.__fake_post
        return self._post(url=self.__posts_url, body=body)

    def get_all_user_posts(self, user_id):
        self.create_user_post(user_id)
        return self._get(url=self.__posts_url)

    def get_post_data_after_create(self, user_id):
        response = self.create_user_post(user_id)
        response = json.loads(response)
        post_data = PostData.from_json(**response['data'])
        return post_data

    @staticmethod
    def get_post_from_list(data_list):
        for data in data_list['data']:
            return data
