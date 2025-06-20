from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.basepage import Page
from Pages.amazon_homepage import OpenAmazonPage
from Pages.search_page import SearchFor


class Application:

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.page = Page(self.driver)
        self.open_amazon = OpenAmazonPage(self.driver)
        self.search_product = SearchFor(self.driver)

