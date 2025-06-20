from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

    # Open Amazon homepage
driver.get("https://www.amazon.com")
driver.maximize_window()
time.sleep(3)
    # You can add waits or other actions here if needed

    # Close the browser
driver.quit()