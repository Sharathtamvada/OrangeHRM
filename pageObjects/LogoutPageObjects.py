from selenium.webdriver.common.by import By


class LogoutPage():
    # Locators
    drpdwn_accout_xpath = "/html/body/app-root/app-header/div/nav/div/div[2]/ul/button/span[2]"
    btn_logout_xpath = "/html/body/div[3]/div[2]/div/div/div/button/span"

    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def clickAccount(self):
        self.driver.find_element(By.XPATH,self.drpdwn_accout_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()