from selenium.webdriver.common.by import By

class LoginPage():
    # Locators
    txtbox_username_name = "Email Address"
    txtbox_password_name="Password"
    button_signin_id = "next"

    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.NAME,self.txtbox_username_name)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self,pwd):
        passwordtxt=self.driver.find_element(By.NAME,self.txtbox_password_name)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_signin_id).click()

    def setOldPassword(self):
        pass
