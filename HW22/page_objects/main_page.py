from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW22.utilities.web_ui.base_page import BasePage
from random import randint
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.XPATH, '//div[@class="client notentered"]')
    __email_login_field = (By.XPATH, '//div[@id="enter-layer"]//input[@name="email"]')
    __password_login_field = (By.XPATH, '//div[@id="enter-layer"]//input[@name="pass"]')
    __submit_login_button = (By.XPATH, '//div[@id="enter-layer"]//button')
    __category_bicycle = (By.XPATH, "//img[@alt='Велосипеди']")
    __menu_button = (By.XPATH, "//span[@class='butt-menu']")
    __search_category_field = (By.XPATH, '//div[@class="menu-search"]//label[@class="textinput"]')
    __gifts_button = (By.XPATH, '//li[@data-id="9021"]')
    __favorite_button = (By.XPATH, "//div[@class='wl']")
    __ukrainian_page_lang = (By.XPATH, '//html[@lang="uk"]')
    __orks_page_lang = (By.XPATH, '//html[@lang="ru"]')
    __change_lang_button = (By.XPATH, '//div[@class="lang"]//a')
    __bike_name_in_konstruktor = (By.XPATH, '//div[@class="info"]/strong/a')
    __height_konstruktor_field = (By.XPATH, '//*[@data-build="BikeSelectGrowthBuild"]/input')
    __weight_konstruktor_field = (By.XPATH, '//*[@data-build="BikeSelectWeightBuild"]/input')
    __i_will_ride_on_droptable = (By.XPATH, '//span[@data-callback="BikeSelectRaodSelect"]')
    __i_will_ride_on_choice = (
        By.XPATH, '//span[@data-callback="BikeSelectRaodSelect"]/span/span[@data-value="4"]')
    __bike_style_droptable = (By.XPATH, '//span[@data-callback="BikeSelectStyleSelect"]')
    __random_style_bike = (
        By.XPATH, f'//span[@data-callback="BikeSelectStyleSelect"]/span/span[position()={randint(1, 4)}]')
    __price_droptable = (By.XPATH, '//span[@class="selectinput price maked"]/input')
    __price_random_choice = (
        By.XPATH, f'//span[@data-callback="BikeSelectPriceSelect"]/span/span[position()={randint(1, 3)}]')
    __search_bike_button = (By.XPATH, '//div[@class="form"]/div[last()]')
    __random_bike_in_grid = (
        By.XPATH, f'//ul[@class="stores1"]/li[position()={randint(1, 3)}]//div[@class="icon maked"]')
    __bike_in_grid = (
        By.XPATH, f'//ul[@class="stores1"]/li[position()=1]//div[@class="icon maked"]')
    __show_numbers_button = (By.XPATH, '//div[@class="phone"]//*[position()=1]')
    __store_phones_table = (By.XPATH, '//div[@id="phones-layer"][@class="opened"]')
    __search_button = (By.XPATH, '//div[@class="butt-search"]')
    __search_field_closed = (By.XPATH, '//div[@class="search"]')
    __search_field_opened = (By.XPATH, '//div[@class="search opened"]')

    def click_search_button(self):
        self._click(self.__search_button)

    def is_search_field_closed(self):
        return self._is_located(self.__search_field_closed)

    def is_search_field_opened(self):
        return self._is_located(self.__search_field_opened)

    def click_show_numbers(self):
        self._click(self.__show_numbers_button)
        return self

    def is_open_numbers_droptable(self):
        return self._is_located(self.__store_phones_table)

    def click_login_button(self):
        self._click(self.__login_button)
        return self

    def set_email(self, email_value):
        self._send_keys(self.__email_login_field, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__password_login_field, password_value)
        return self

    def click_submit_login_button(self):
        self._click(self.__submit_login_button)
        return self

    def login(self, email_value, password_value):
        self.click_login_button().set_email(email_value).set_password(password_value).click_submit_login_button()

    def change_page_language(self):
        self._click(self.__change_lang_button)

    def language_page_is_ru(self):
        return self._is_located(self.__orks_page_lang)

    def language_page_is_ukrainian(self):
        return self._is_located(self.__ukrainian_page_lang)

    # For constructor testing
    def get_bike_name_in_constructor(self):
        result = self._get_attribute_value(locator=self.__bike_name_in_konstruktor, attribute='href')
        return result

    def fill_height_field(self):
        self._send_keys(self.__height_konstruktor_field, randint(150, 190))
        return self

    def fill_weight_field(self):
        self._send_keys(self.__weight_konstruktor_field, randint(60, 80))
        return self

    def select_i_will_ride_on(self):
        self._click(self.__i_will_ride_on_droptable)
        self._click(self.__i_will_ride_on_choice)
        return self

    def select_style_bike(self):
        self._click(self.__bike_style_droptable)
        self._click(self.__random_style_bike)
        return self

    def select_price_bike(self):
        self._click(self.__price_droptable)
        self._click(self.__price_random_choice)
        return self

    def click_find_bike_by_recommendations(self):
        self._click(self.__search_bike_button)

    def check_change_bike_in_constructor(self):
        expected = self.get_bike_name_in_constructor()
        actual = self.get_bike_name_in_constructor()
        retry = 0
        while expected == actual:
            if retry == 3:
                break
            actual = self.get_bike_name_in_constructor()
            time.sleep(1)
            retry += 1

    def fill_constructor(self):
        self.fill_height_field().fill_weight_field().select_i_will_ride_on().select_style_bike().select_price_bike()
        self.click_find_bike_by_recommendations()
        self.check_change_bike_in_constructor()

    def select_bike_in_grid(self):
        self._is_located(self.__random_bike_in_grid)
        self._click(self.__random_bike_in_grid)

    def scroll_to_bike_constructor(self):
        self._scroller(self.__bike_name_in_konstruktor)

    def scroll_to_bike_grid(self):
        self._scroller(self.__bike_in_grid)

    def scroll_to_promotion_section(self):
        self._scroll_to_bottom()
