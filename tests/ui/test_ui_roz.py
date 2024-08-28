import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



# Індивідуальна частина проєкту:
@pytest.mark.ui 
def test_check_incorrect_email():

# Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Відкрити сторінку "https://rozetka.com.ua"
    driver.get("https://rozetka.com.ua")

# Знайти  пошукове поле, в яке будемо вводити назву товару
    search_field = driver.find_element(By.NAME,"search")
# Ввести в пошукове поле назву товару
    search_field.send_keys("Ноутбуки")
# Знайти кнопку активації пошуку
    btn_elem = driver.find_element(By.XPATH, "/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/button")
# Emulate a click with the left mouse button
    btn_elem.click()
    time.sleep(3)

# Закрити браузер
    driver.close()