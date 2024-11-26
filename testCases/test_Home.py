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
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "home_page.png")
        self.hp = HomePage(self.driver)
        self.hp.clickTimesheets()
        self.driver.back()
        self.hp.clickSliderRight()
        self.hp.clickEmployees()
        self.driver.back()
        self.hp.clickSliderLeft()
        self.hp.clickPrograms()
        self.hp.clickHome()
        self.driver.close()