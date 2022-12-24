from http import HTTPStatus
from API_Testing.gorest.data.user_data import UserData
from API_Testing.gorest.api_collections.user_collection import User


def test_get_user_200(create_and_get_user_data, env):
    user = User(env)
    expected_person = create_and_get_user_data
    response = user.get_person(expected_person.id)
    person_data = user.get_user_data(expected_person.id)
    actual_person = UserData.from_json(**person_data)
    assert response.status_code == HTTPStatus.OK, f"Unexpected status code\nExpected: {HTTPStatus.OK}\nActual:" \
                                                  f" {response.status_code}"
    assert actual_person == expected_person, "It's not the same user"


def test_get_user_404(env):
    user = User(env)
    response = user.get_person(0)
    assert response.status_code == HTTPStatus.NOT_FOUND, f"Unexpected status code\nExpected: {HTTPStatus.NOT_FOUND}\n" \
                                                         f"Actual: {response.status_code}"


def test_create_user_201(env):
    user = User(env)
    response = user.create_random_user()
    assert response.status_code == HTTPStatus.CREATED, 'User not created'


def test_delete_user_204(create_and_get_user_data, env):
    user = User(env)
    created_person = create_and_get_user_data
    response = user.delete_user(created_person.id)
    assert response.status_code == HTTPStatus.NO_CONTENT, f'User not deleted\nExpected status code: ' \
                                                          f'{HTTPStatus.NO_CONTENT}\nActual: {response.status_code}'


def test_delete_user_404(env):
    user = User(env)
    response = user.delete_user(person_id=0)
    assert response.status_code == HTTPStatus.NOT_FOUND, f'User cannot have id = 0, must be error: ' \
                                                         f'{HTTPStatus.NOT_FOUND} - not found'


def test_update_user_name(create_and_get_user_data, env):
    user = User(env)
    created_person = create_and_get_user_data
    updated_person = user.update_user_name(person_id=created_person.id)
    updated_person_data = user.get_user_data(created_person.id)
    changed_person = UserData.from_json(**updated_person_data)
    assert updated_person.status_code == HTTPStatus.OK, f"Status code not expected\nExpected: {HTTPStatus.OK}" \
                                                        f"\nActual: {updated_person.status_code}"
    assert changed_person != created_person, "User has the same name"


def test_get_all_users_200(env):
    # API Developers declare that users are regularly removed from the database, but at least 2000 records are stable
    user = User(env)
    response = user.get_all_users()
    users_data = response.json()
    quantity_users = user.get_quantity_users_from_response(users_data)
    assert response.status_code == HTTPStatus.OK, f'Unexpected status code\nExpected: {HTTPStatus.OK}' \
                                                  f'Actual: {response.status_code}'
    assert quantity_users > 2000, f'Quantity user cannot be less than 2000, Actual: {quantity_users}'
