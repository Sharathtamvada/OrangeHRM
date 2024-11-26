from selenium.webdriver.common.by import By


class HomePage():
    # Locators
    btn_timesheets_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[2]/div/div/h2"
    btn_employees_xpath = "/html/body/app-root/div/div[1]/ul[1]/a[2]/li/span[2]"
    btn_programs_xpath = "/html/body/app-root/div/div[1]/ul[1]/a[3]/li/span[2]"
    btn_collapse_xpath = "/html/body/app-root/div/div[1]/ul[2]/button/li"

    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def clickTimesheets(self):
        self.driver.find_element(By.XPATH,self.btn_timesheets_xpath).click()

    def clickEmployees(self):
        self.driver.find_element(By.XPATH,self.btn_employees_xpath).click()
    
    def clickPrograms(self):
        self.driver.find_element(By.XPATH,self.btn_programs_xpath).click()

    def clickCollapse(self):
        self.driver.find_element(By.XPATH,self.btn_collapse_xpath).click()
