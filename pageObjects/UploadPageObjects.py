from selenium.webdriver.common.by import By

class UploadPage():
    # Locators
    btn_upload_xpath = "/html/body/app-root/div/div[2]/div/div/app-timesheet/div/div[1]/div/div/div[2]/a/button/span[2]/span[2]"
    btn_choosefile_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-mat-dialog-box/div/div/div/button"
    file_input_selector = "input[type='file']"
    file_path = r"C:\Users\SharathRaoTamvada(Da\OneDrive - Intuitive Technology Partners, Inc\Azas_zoovee\azas_zoovee_test_cases.xlsx"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def clickUploadFile(self):
        self.driver.find_element(By.XPATH, self.btn_upload_xpath).click()

    def clickChooseFile(self):
        # Click the 'Choose File' button to open the file input dialog
        self.driver.find_element(By.XPATH, self.btn_choosefile_xpath).click()

        # Locate the file input element and upload the file
        file_input = self.driver.find_element(By.CSS_SELECTOR, self.file_input_selector)
        file_input.send_keys(self.file_path)