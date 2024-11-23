from selenium.webdriver.common.by import By


class AdminPage():
    #Locators
    btn_admin_xpath="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    name_admin_xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]"
    drpdwn_job_xpath="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
    btn_jobtitles_xpath="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a"
    drpdwn_account_xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p"
    btn_changepassword_xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[3]/a"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def clickAdmin(self):
        self.driver.find_element(By.XPATH,self.btn_admin_xpath).click()

    def name_displayed(self):
        self.driver.find_element(By.XPATH,self.name_admin_xpath).is_displayed()

    def clickJob(self):
        self.driver.find_element(By.XPATH,self.drpdwn_job_xpath).click()

    def clickJobTitles(self):
        self.driver.find_element(By.XPATH,self.btn_jobtitles_xpath).click()
        
    def clickAccount(self):
        self.driver.find_element(By.XPATH,self.drpdwn_account_xpath).click()
        
    def clickChangePassword(self):
        self.driver.find_element(By.XPATH,self.btn_changepassword_xpath).click()