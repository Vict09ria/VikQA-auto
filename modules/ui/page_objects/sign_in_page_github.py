from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username,password):
        # We know the field, in which we will enter incorrectly the name of the koristuvach or the mailing address
        login_elem = self.driver.find_element(By.ID, "login_field")

        # The accountant's name or mailing address is entered incorrectly
        login_elem.send_keys(username)

        # We know the field, in this case we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Entering the wrong password
        pass_elem.send_keys(password)

        # Know the sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # It is possible to click the left button of the bear
        btn_elem.click()

    def check_title(self,expected_title):
        return self.driver.title == expected_title