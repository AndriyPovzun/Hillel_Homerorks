import time

from selenium.webdriver.common.by import By
from HW22.utilities.web_ui.base_page import BasePage
from random import randint


class BikeOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __select_bike_color_droptable = (By.XPATH, '//span[@data-callback="ShopStoreColorSelect"]/input')
    __select_bike_size_droptable = (By.XPATH, '//span[@data-build="ShopStoreSizeBuild"]/input')
    __bike_size_random_choice = (
        By.XPATH, f'//span[@data-build="ShopStoreSizeBuild"]/span/span[position()={randint(1, 2)}]')
    __buy_bike_button = (By.XPATH, '//*[@class="buy butt1"]')
    __add_bike_to_compare_button = (By.XPATH, '//div[@class="butts"]//span[position()=3]')
    __add_to_favorites_button = (By.XPATH, '//div[@class="butts"]//span[position()=4]')
    __phone_number_input_field = (By.XPATH, '//div[@class="fastbuy"]//input')
    __order_call_button = (By.XPATH, '//div[@class="fastbuy"]//span')
    __cart_button = (By.XPATH, '//*[@class="cart"]')
    __empty_cart = (By.XPATH, '//*[@data-howorder="0"]')
    __cart_have_one_item = (By.XPATH, '//*[@data-howorder="1"]')
    __bike_on_compare_page = (By.XPATH, '//th[@class="store"][position()=1]')
    __header_compare_button = (By.XPATH, '//div[@class="cmp"]//*[position()=1]//*')
    __header_favorite_button = (By.XPATH, '//div[@class="wl"]//*[position()=1]')
    __bike_on_favorite_page = (By.XPATH, '//div[@class="tr"]')
    __delete_bike_from_compare_button = (By.XPATH, '//div[@class="butts"]//*[@class="delete"]')
    __buy_bike_in_credit_button = (By.XPATH, '//div[@class="butts"]//*[@class="butt2 credit"]')
    __thanks_title = (By.XPATH, '//div[@class="senks-title"]')
    __select_random_bank_button = (By.XPATH, f'//ul/li[position() = {randint(1, 4)}]/*[@class="butt1"]')

    def select_random_bike_size(self):
        self._click(self.__select_bike_size_droptable)
        self._click(self.__bike_size_random_choice)
        return self

    def click_buy_button(self):
        self._click(self.__buy_bike_button)
        return self

    def click_on_cart(self):
        self._click(self.__cart_button)
        return self

    def order_bike_and_go_to_cart(self):
        self.select_random_bike_size().click_buy_button().click_on_cart()

    def is_cart_have_one_item(self):
        return self._is_located(self.__cart_have_one_item)

    def click_compare_button(self):
        self._click(self.__add_bike_to_compare_button)
        return self

    def click_header_compare_button(self):
        self._click(self.__header_compare_button)
        return self

    def add_bike_to_compare_page_and_transition_to_it(self):
        self.click_compare_button()
        time.sleep(1)
        self.click_header_compare_button()

    def is_displayed_bike_in_compare_page(self):
        return self._is_located(self.__bike_on_compare_page)

    def click_add_to_favorite(self):
        self._click(self.__add_to_favorites_button)
        return self

    def click_go_to_favorite_page(self):
        self._click(self.__header_favorite_button)

    def add_bike_to_favorite_page_and_transition_to_it(self):
        self.click_add_to_favorite()
        time.sleep(1)
        self.click_go_to_favorite_page()

    def is_displayed_bike_in_favorite_page(self):
        return self._is_located(self.__bike_on_favorite_page)

    def is_not_displayed_bike_in_compare_page(self):
        return self._is_not_located(self.__bike_on_compare_page)

    def delete_bike_from_compare(self):
        self._click(self.__delete_bike_from_compare_button)

    def click_buy_bike_in_credit(self):
        self._click(self.__buy_bike_in_credit_button)
        return self

    def select_random_bank_for_pay_credit(self):
        self._click(self.__select_random_bank_button)
        return self

    def is_displayed_thanks_title(self):
        return self._is_located(self.__thanks_title)
