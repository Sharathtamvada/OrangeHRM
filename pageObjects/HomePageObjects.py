from selenium.webdriver.common.by import By


class HomePage():
    # Locators
    btn_timesheets_xpath = "/html/body/app-root/div/div/div/div/app-home/div/div/div/div/ngx-slick-carousel/div/div/div[2]/div/div/h2"

    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def clickTimesheets(self):
        self.driver.find_element(By.XPATH,self.btn_timesheets_xpath).click()
