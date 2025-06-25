from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.basepage import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class OpenAmazonPage(Page):

    CONTINUE_BTN = (By.CSS_SELECTOR, ".a-button-text")
    LANGUAGE = (By.CSS_SELECTOR,".icp-nav-link-inner")
    CHANGE_COUNTRY =(By.CSS_SELECTOR,".icp-mkt-change-lnk")
    TITLE = (By.CSS_SELECTOR, "h3[class='a-spacing-extra-large']")
    CANCEL = (By.ID, "icp-cancel-button")

    def open_amazon_homepage(self):
        self.open_url(self.base_url)
        sleep(5)

    def continue_shopping(self):
        self.click(*self.CONTINUE_BTN)

    def verify_homepage(self):
        self.verify_url("https://www.amazon.com/")
        sleep(5)

    def verify_language(self):

        self.wait.until(EC.presence_of_element_located(self.LANGUAGE))
        hover_to_lang = self.find_element(*self.LANGUAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_to_lang).perform()
        sleep(10)
        self.wait_until_clickable_click(*self.CHANGE_COUNTRY)
        sleep(2)
        self.verify_text('Website (Country/Region)', *self.TITLE)
        self.click(*self.CANCEL)
        sleep(3)



