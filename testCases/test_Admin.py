from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPage
from pageObjects.AdminPageObjects import AdminPage
import os
from utilities.readProperties import ReadConfig

class TestAdminPage:
    def test_Admin_Page(self):
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
        self.ap = AdminPage(self.driver)
        self.ap.clickAdmin()
        self.driver.implicitly_wait(10)
        self.ap.name_displayed()
        self.ap.clickJob()
        self.ap.clickJobTitles()
        self.ap.clickAccount()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Login1.png")
        self.ap.clickChangePassword()
        self.driver.close()