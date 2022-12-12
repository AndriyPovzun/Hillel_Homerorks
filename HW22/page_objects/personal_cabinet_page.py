from selenium.webdriver.common.by import By
from faker import Faker
from random import randint

from HW22.utilities.web_ui.base_page import BasePage


class PersonalCabinetPage(BasePage):
    def __init__(self, driver):
        self.__fake = Faker()
        super().__init__(driver)

    __logout_button = (By.XPATH, '//div[@class="client entered"]')
    __back_on_main_page_button = (By.XPATH, '//a[@class="logo"]')
    __edit_data_button = (By.XPATH, '//div[@class="butt"]//button[@class="butt1"]')
    __surname_field = (By.XPATH, '//div[@data-id="-1"]//input[@id="field-1"]')
    __name_field = (By.XPATH, '//input[@id="field-2"]')
    __middle_name_field = (By.XPATH, '//input[@id="field-3"]')
    __phone_field = (By.XPATH, '//input[@id="field2"]')
    __city_field = (By.XPATH, '//input[@id="field6"]')
    __save_changes_button = (By.XPATH, '//div[@class="butt"]//*[@class="butt1 edit"]')

    __new_surname = None
    __new_name = None
    __new_middle_name = None
    __new_phone_number = None
    __new_city = None

    def __generate_new_city(self):
        self.__new_city = self.__fake.city()
        return self.__new_city

    def __generate_new_number(self):
        self.__new_phone_number = randint(0000000000, 9999999999)
        return self.__new_phone_number

    def __generate_new_middle_name(self):
        self.__new_middle_name = self.__fake.name()
        return self.__new_middle_name

    def __generate_new_name(self):
        self.__new_name = self.__fake.name()
        return self.__new_name

    def __generate_new_surname(self):
        self.__new_surname = self.__fake.name()
        return self.__new_surname

    def is_logout_button_displayed(self):
        return self._is_displayed(self.__logout_button)

    def back_on_main_page(self):
        self._click(self.__back_on_main_page_button)

    def _click_edit_data(self):
        self._click(self.__edit_data_button)
        return self

    def _save_changes(self):
        self._click(self.__save_changes_button)
        return self

    def _set_random_surname(self):
        self.__generate_new_surname()
        self._send_keys(self.__surname_field, self.__new_surname)
        return self

    def _set_random_name(self):
        self.__generate_new_name()
        self._send_keys(self.__name_field, self.__new_name)
        return self

    def _set_random_middle_name(self):
        self.__generate_new_middle_name()
        self._send_keys(self.__middle_name_field, self.__new_middle_name)
        return self

    def _set_random_phone_number(self):
        self.__generate_new_number()
        self._send_keys(self.__phone_field, self.__new_phone_number)
        return self

    def _set_random_city(self):
        self.__generate_new_city()
        self._send_keys(self.__city_field, self.__new_city)
        return self

    def change_surname(self):
        self._click_edit_data()._set_random_surname()._save_changes()

    def change_name(self):
        self._click_edit_data()._set_random_name()._save_changes()

    def change_middle_name(self):
        self._click_edit_data()._set_random_middle_name()._save_changes()

    def change_phone_number(self):
        self._click_edit_data()._set_random_phone_number()._save_changes()

    def change_city(self):
        self._click_edit_data()._set_random_city()._save_changes()

    def is_changed_surname(self):
        self._click_edit_data()
        return self._is_displayed((By.XPATH, f'//*[@data-oldvalue="{self.__new_surname}"]'))

    def is_changed_name(self):
        self._click_edit_data()
        return self._is_displayed((By.XPATH, f'//*[@data-oldvalue="{self.__new_name}"]'))

    def is_changed_middle_name(self):
        self._click_edit_data()
        return self._is_displayed((By.XPATH, f'//*[@data-oldvalue="{self.__new_middle_name}"]'))

    def is_changed_phone_number(self):
        self._click_edit_data()
        return self._is_displayed((By.XPATH, f'//*[@data-oldvalue="+38{self.__new_phone_number}"]'))

    def is_changed_city(self):
        self._click_edit_data()
        return self._is_displayed((By.XPATH, f'//*[@data-oldvalue="{self.__new_city}"]'))
