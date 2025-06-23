from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.basepage import Page
from Pages.amazon_homepage import OpenAmazonPage
from Pages.search_page import SearchFor


class Application:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Required for GitHub Actions
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")


        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.page = Page(self.driver)
        self.open_amazon = OpenAmazonPage(self.driver)
        self.search_product = SearchFor(self.driver)

