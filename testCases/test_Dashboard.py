from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPage
from pageObjects.DashboardPageObjects import DashboardPage
import os
from utilities.readProperties import ReadConfig

class TestDashboardPage:
    def test_Dashboard_Page(self):
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
        self.dp = DashboardPage(self.driver)
        self.dp.selectTimesheets()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "timesheets_page.png")
        self.dp.selectEmployees()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "employees_page.png")
        self.dp.selectPrograms()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "programs_page.png")
        self.driver.close()