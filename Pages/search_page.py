from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.basepage import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



class SearchFor(Page):

    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    STAR = (By.CSS_SELECTOR, ".a-star-medium-4")
    PRODUCT = (By.CSS_SELECTOR, 'h2[aria-label *= "Elephant, Blue"]')
    CHECK_BOX = (By.CSS_SELECTOR, 'a[aria-label= "Apply Dr. Brown\'s filter to narrow results"]')
    IMAGES = (By.CSS_SELECTOR, ".a-spacing-small.item.imageThumbnail.a-declarative")

    def search_for(self):

        self.wait.until(EC.visibility_of_element_located(self.SEARCH))
        self.input_text("Toddler Toothbrush" , *self.SEARCH)
        self.click(*self.SEARCH_BUTTON)
        sleep(3)
        #self.find_elements(*self.STAR).click()
        checkbox = self.find_element(*self.CHECK_BOX)
        actions = ActionChains(self.driver)
        actions.click(checkbox).perform()
        sleep(3)


    def hover_to_product(self):

        #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.PRODUCT)
        element = self.wait.until(EC.visibility_of_element_located(self.PRODUCT))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        sleep(3)
        element.click()

    def check_image(self):
        images = self.find_elements(*self.IMAGES)
        for image in images:
            actions = ActionChains(self.driver)
            actions.move_to_element(image).perform()
            self.driver.execute_script("arguments[0].style.border='3px solid red';", image)
            sleep(2)