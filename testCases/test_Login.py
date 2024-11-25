import pytest
from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPage
import os
from utilities.readProperties import ReadConfig

class TestLogin:
    @pytest.mark.sanity
    def test_login(self):
        baseURL = ReadConfig.getApplicationURL()
        user = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.get(baseURL)
        self.driver.maximize_window()

        # Initialize the LoginPage object
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(user)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        self.driver.save_screenshot(
            os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Login.png"
        )
        self.driver.close()
