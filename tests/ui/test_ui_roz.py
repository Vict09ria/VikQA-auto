import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



# Individual part of the project:
@pytest.mark.ui 
def test_check_incorrect_email():

# Creating an object to control the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page "https://rozetka.com.ua"
    driver.get("https://rozetka.com.ua")

# Find the search field in which we will enter the name of the product
    search_field = driver.find_element(By.NAME,"search")
# Enter the name of the product in the search field
    search_field.send_keys("Ноутбуки")
# Find the search activation button
    btn_elem = driver.find_element(By.XPATH, "/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/button")
# Emulate a click with the left mouse button
    btn_elem.click()
    time.sleep(3)
# Close the browser
    driver.close()