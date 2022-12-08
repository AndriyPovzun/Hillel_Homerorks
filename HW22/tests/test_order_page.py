def test_add_bike_to_cart(go_to_order_page):
    order_page = go_to_order_page
    order_page.order_bike_and_go_to_cart()
    assert order_page.is_cart_have_one_item() is True, 'Bike was not added in cart'
