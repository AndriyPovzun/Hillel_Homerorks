def test_change_surname(login):
    personal_page = login
    personal_page.change_surname()
    assert personal_page.is_changed_surname() is True, 'Surname was not changed'


def test_change_name(login):
    personal_page = login
    personal_page.change_name()
    assert personal_page.is_changed_name() is True, 'Name was not changed'


def test_change_middle_name(login):
    personal_page = login
    personal_page.change_middle_name()
    assert personal_page.is_changed_middle_name() is True, 'Middle name was not changed'


def test_change_phone_number(login):
    personal_page = login
    personal_page.change_phone_number()
    assert personal_page.is_changed_phone_number() is True, 'Phone number was not changed'


def test_change_city(login):
    personal_page = login
    personal_page.change_city()
    assert personal_page.is_changed_city() is True, 'City was not changed'
