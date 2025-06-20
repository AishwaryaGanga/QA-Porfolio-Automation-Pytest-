from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.basepage import Page
from time import sleep

class OpenAmazonPage(Page):

    CONTINUE_BTN = (By.CSS_SELECTOR, ".a-button-text")
    LANGUAGE = (By.CSS_SELECTOR,".icp-nav-link-inner")
    CHANGE_COUNTRY =(By.CSS_SELECTOR,".icp-mkt-change-lnk")
    TITLE = (By.CSS_SELECTOR, "h3[class='a-spacing-extra-large']")
    GO_BACK = (By.CSS_SELECTOR, ".a-button-input")

    def open_amazon_homepage(self):
        self.open_url(self.base_url)

    def continue_shopping(self):
        self.click(*self.CONTINUE_BTN)

    def verify_homepage(self):
        self.verify_url("https://www.amazon.com/")

    def verify_language(self):
        hover_to_lang = self.find_element(*self.LANGUAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_to_lang).perform()
        self.wait_until_clickable_click(*self.CHANGE_COUNTRY)
        self.verify_text('Website (Country/Region)', *self.TITLE)
        self.click(*self.GO_BACK)
        sleep(3)



