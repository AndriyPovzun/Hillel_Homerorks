def test_add_bike_to_cart(go_to_order_page):
    order_page = go_to_order_page
    order_page.order_bike_and_go_to_cart()
    assert order_page.is_cart_have_one_item() is True, 'Bike was not added in cart'


def test_add_bike_to_compare(go_to_order_page):
    order_page = go_to_order_page
    order_page.add_bike_to_compare_page_and_transition_to_it()
    assert order_page.is_displayed_bike_in_compare_page() is True, 'Bike not was added to compare page'


def test_add_bike_to_favorite(go_to_order_page):
    order_page = go_to_order_page
    order_page.add_bike_to_favorite_page_and_transition_to_it()
    assert order_page.is_displayed_bike_in_favorite_page() is True, 'Bike not was added to favorite page'


def test_remove_bike_from_compare(go_to_order_page):
    order_page = go_to_order_page
    order_page.add_bike_to_compare_page_and_transition_to_it()
    assert order_page.is_displayed_bike_in_compare_page() is True, 'Bike was not added to favorite page'
    order_page.delete_bike_from_compare()
    assert order_page.is_not_displayed_bike_in_compare_page() is True, 'Bike was not deleted from compare page'


def test_buy_bike_in_credit(go_to_order_page):
    order_page = go_to_order_page
    order_page.click_buy_bike_in_credit().select_random_bank_for_pay_credit()
    assert order_page.is_displayed_thanks_title() is True, 'Buy in credit process was not completed successfully'
