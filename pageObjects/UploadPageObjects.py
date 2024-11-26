from selenium.webdriver.common.by import By


class UploadPage():
    # Locators
    btn_upload_xpath = "/html/body/app-root/div/div[2]/div/div/app-timesheet/div/div[1]/div/div/div[2]/a/button/span[2]/span[1]"
    btn_choosefile_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-mat-dialog-box/div/div/div/button"

    # constructor
    def __init__(self,driver):
        self.driver=driver

    # action methods
    def clickUploadFile(self):
        self.driver.find_element(By.XPATH,self.btn_upload_xpath).click()

    def clickChooseFile(self):
        self.driver.find_element(By.XPATH,self.btn_choosefile_xpath).click()