from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPage
from pageObjects.HomePageObjects import HomePage
import os
from utilities.readProperties import ReadConfig

class TestHomePage:
    def test_Home_Page(self):
        baseURL = ReadConfig.getApplicationURL()
        user = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.get(baseURL)
        self.driver.maximize_window()

        # Initialize the HomePage object
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(user)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        self.hp = HomePage(self.driver)
        self.hp.clickTimesheets()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "timesheets_page.png")
        self.driver.close()