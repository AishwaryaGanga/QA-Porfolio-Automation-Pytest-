from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.basepage import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



class SearchFor(Page):

    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    STAR = (By.CSS_SELECTOR, ".a-star-medium-4")
    PRODUCT = (By.CSS_SELECTOR, 'h2[aria-label *= "Dr. Brown\'s Infant Toothbrush"]')
    CHECK_BOX = (By.CSS_SELECTOR, 'a[aria-label= "Apply Dr. Brown\'s filter to narrow results"]')
    IMAGES = (By.CSS_SELECTOR, ".a-spacing-small.item.imageThumbnail.a-declarative")

    def search_for(self):
        self.input_text("Toddler Toothbrush" , *self.SEARCH)
        self.click(*self.SEARCH_BUTTON)
        sleep(3)
        #self.find_elements(*self.STAR).click()
        checkbox = self.find_element(*self.CHECK_BOX)
        actions = ActionChains(self.driver)
        actions.click(checkbox).perform()


    def hover_to_product(self):
        # element = self.find_element(*self.PRODUCT)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        # sleep(3)
        # element.click()

        try:
            try:
                locator = (By.CSS_SELECTOR, 'h2[aria-label*="Elephant, Blue"]')

                # Wait until the search results container is loaded
                self.drive.until(EC.presence_of_element_located((By.ID, "search")))

                # Scroll to make sure product appears
                self.driver.execute_script("window.scrollBy(0, 1000);")
                sleep(1)

                # Wait until product element is present and clickable
                element = self.wait.until(EC.presence_of_element_located(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
                sleep(2)

                self.wait.until(EC.element_to_be_clickable(locator)).click()

        except Exception as e:
            self.driver.save_screenshot("hover_failure.png")
            raise e

    def check_image(self):
        images = self.find_elements(*self.IMAGES)
        for image in images:
            actions = ActionChains(self.driver)
            actions.move_to_element(image).perform()
            self.driver.execute_script("arguments[0].style.border='3px solid red';", image)
            sleep(2)