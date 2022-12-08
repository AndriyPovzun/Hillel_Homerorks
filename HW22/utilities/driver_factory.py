from selenium.webdriver import Chrome, Firefox, Edge
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.chrome.service import Service as Chrome_Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as Edge_Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_current_driver(driver_id: int):
        if int(driver_id) == 1:
            web_driver = Chrome(service=Chrome_Service(ChromeDriverManager().install()))
        elif int(driver_id) == 2:
            web_driver = Firefox(service=Firefox_Service(GeckoDriverManager().install()))
        elif int(driver_id) == 3:
            web_driver = Edge(service=Edge_Service(EdgeChromiumDriverManager().install()))
        else:
            web_driver = Chrome(service=Chrome_Service(ChromeDriverManager().install()))
        return web_driver
