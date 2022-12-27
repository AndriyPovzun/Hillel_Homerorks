import pytest
import json
import allure
from contextlib import suppress

from HW22.CONSTANTS import ROOT_DIR

from HW22.page_objects.main_page import MainPage
from HW22.utilities.driver_factory import DriverFactory
from HW22.utilities.configurations import Configuration
from HW22.page_objects.bike_order_page import BikeOrderPage
from HW22.page_objects.personal_cabinet_page import PersonalCabinetPage


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='session')
def env():
    with open(
            f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configuration(**env_dict)


@pytest.fixture()
def create_driver(env, request):
    driver = DriverFactory.create_current_driver(driver_id=env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture()
def scroll_to_bike_constructor(create_driver, open_main_page):
    main_page = open_main_page
    main_page.scroll_to_bike_constructor()
    return MainPage(create_driver)


@pytest.fixture()
def scroll_to_bottom(create_driver, open_main_page):
    main_page = open_main_page
    main_page.scroll_to_promotion_section()
    return MainPage(create_driver)


@pytest.fixture()
def login(env, open_main_page, create_driver):
    main_page = open_main_page
    main_page.login(email_value=env.user_email, password_value=env.user_password)
    return PersonalCabinetPage(create_driver)


@pytest.fixture()
def login_and_back_to_main(login, create_driver):
    personal_page = login
    personal_page.back_on_main_page()
    return MainPage(create_driver)


@pytest.fixture()
def go_to_order_page(login_and_back_to_main, create_driver):
    main_page = login_and_back_to_main
    main_page.scroll_to_bike_grid()
    main_page.select_bike_in_grid()
    return BikeOrderPage(create_driver)
