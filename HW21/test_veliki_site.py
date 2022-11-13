import credentials
import locators
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    service = Service('chromedriver.exe')
    chrome_driver = Chrome(service=service)
    wait = WebDriverWait(chrome_driver, 10)
    chrome_driver.get(credentials.base_url)
    chrome_driver.fullscreen_window()
    login_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_button)))
    login_button_element.click()
    email_field_element = wait.until(EC.presence_of_element_located((By.XPATH, locators.email_login_field)))
    email_field_element.clear()
    email_field_element.send_keys(credentials.user_email)
    password_field_element = wait.until(EC.presence_of_element_located((By.XPATH, locators.password_login_field)))
    password_field_element.clear()
    password_field_element.send_keys(credentials.user_password)
    submit_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.submit_login_button)))
    submit_login_button.click()
    logout_button_element = wait.until(EC.presence_of_element_located((By.XPATH, locators.logout_button)))
    logout_is_on_the_page = logout_button_element.is_displayed()
    assert logout_is_on_the_page is True, 'User not logged-in'
