def test_login(login):
    personal_cabinet_page = login
    assert personal_cabinet_page.is_logout_button_displayed() is True, 'User not logged-in'


def test_change_language(open_main_page):
    main_page = open_main_page
    main_page.change_page_language()
    assert main_page.language_page_is_ru() is True, 'Page language was not changed'


def test_bike_recommendation_constructor(scroll_to_bike_constructor):
    main_page = scroll_to_bike_constructor
    bike_before_constructor = main_page.get_bike_name_in_constructor()
    main_page.fill_constructor()
    assert bike_before_constructor != main_page.get_bike_name_in_constructor(), 'Constructor does\'t work'


def test_check_store_number_droptable(open_main_page):
    main_page = open_main_page
    main_page.click_show_numbers()
    assert main_page.is_open_numbers_droptable() is True, 'Table was not opened'


def test_search_button(open_main_page):
    main_page = open_main_page
    assert main_page.is_search_field_closed() is True, 'Search field not closed'
    main_page.click_search_button()
    assert main_page.is_search_field_opened() is True, 'Search field not opened'
