from selenium.webdriver.common.by import By

class LoginPage():
    #Locators
    txtbox_username_name="username"
    txtbox_password_name="password"
    button_login_xpath="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.NAME,self.txtbox_username_name)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self,pwd):
        passwordtxt=self.driver.find_element(By.NAME,self.txtbox_password_name)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def setOldPassword(self):
        pass

    