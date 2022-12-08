def test_login(login):
    personal_cabinet_page = login
    assert personal_cabinet_page.is_logout_button_displayed() is True, 'User not logged-in'


# def test_subscribe_on_promotion(open_main_page, env):
#     main_page = open_main_page
#     main_page.subscribe_on_promotions(env.user_email)
#     assert main_page.subscribe_success_is_displayed() is True, 'User not was subscribed on promotions'


def test_change_language(open_main_page):
    main_page = open_main_page
    main_page.change_page_language()
    assert main_page.language_page_is_ru() is True, 'Page language was not changed'


def test_bike_recommendation_constructor(scroll_to_bike_constructor):
    main_page = scroll_to_bike_constructor
    bike_before_constructor = main_page.get_bike_name_in_constructor()
    main_page.fill_constructor()
    assert bike_before_constructor != main_page.get_bike_name_in_constructor(), 'Constructor does\'t work'

