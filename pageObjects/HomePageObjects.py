from selenium.webdriver.common.by import By


class HomePage():
    # Locators
    btn_timesheets_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[2]/div/div/h2"
    btn_employees_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[3]/div/div/h2"
    btn_programs_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[3]/div/div/h2"
    btn_sliderright_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/button[2]"
    btn_sliderleft_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/button[1]"
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

    def clickSliderRight(self):
        self.driver.find_element(By.XPATH,self.btn_sliderright_xpath).click()

    def clickSliderLeft(self):
        self.driver.find_element(By.XPATH,self.btn_sliderleft_xpath).click()
