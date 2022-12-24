from http import HTTPStatus
from API_Testing.gorest.api_collections.posts_collection import PostsAPI
from API_Testing.gorest.data.post_data import PostData


def test_create_user_post_201(create_and_get_user_data, env):
    post = PostsAPI(env)
    created_user = create_and_get_user_data
    response = post.create_user_post(user_id=created_user.id)
    json_response = response.json()
    post_response_data = PostData.from_json(**json_response['data'])
    assert response.status_code == HTTPStatus.CREATED, f"Unexpected status code\nExpected: {HTTPStatus.CREATED}" \
                                                       f"\nActual: {response.status_code}"
    assert post_response_data.is_valid_response() is True, "Post response data is not valid"


def test_get_all_user_posts_endpoint_200(create_and_get_user_data, env):
    post = PostsAPI(env)
    created_user = create_and_get_user_data
    response = post.get_all_user_posts(created_user.id)
    json_response = response.json()
    post_data = post.get_post_from_list(json_response)
    post_response_data = PostData.from_json(**post_data)
    assert response.status_code == HTTPStatus.OK, f'Unexpected status code\nExpected: {HTTPStatus.OK}' \
                                                  f'Actual: {response.status_code}'
    assert post_response_data.is_valid_response() is True, f'Response data is not valid'
    assert post_response_data.user_id == created_user.id, 'This post does not belong to this user' \
                                                          f'Expected user ID: {created_user.id}' \
                                                          f'Actual user ID: {post_response_data.user_id}'
