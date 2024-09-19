from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class TeTestCambiodeidioma(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_cambiodeidioma(self):
        self.driver.get("https://nuxqa6.avtest.ink/es/")
        time.sleep(6)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_4 .dropdown_trigger_value").click()
        time.sleep(5)
        # 4 | mouseOver | css=#languageListTriggerId_4 .dropdown_trigger_value |  | 
        element = self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_4 .dropdown_trigger_value")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 5 | mouseOut | css=#languageListTriggerId_4 .dropdown_trigger_value |  | 
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 6 | click | id=optionId_languageListOptionsLisId_40 |  | 
        self.driver.find_element(By.ID, "optionId_languageListOptionsLisId_40").click()
        time.sleep(5)
        # 7 | click | css=#languageListTriggerId_50 .dropdown_trigger_value |  | 
        self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_50 .dropdown_trigger_value").click()
        time.sleep(5)
        # 8 | mouseOver | css=#languageListTriggerId_50 .dropdown_trigger_value |  | 
        element = self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_50 .dropdown_trigger_value")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 9 | mouseOut | css=#languageListTriggerId_50 .dropdown_trigger_value |  | 
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 10 | click | css=#optionId_languageListOptionsLisId_131 > .button_label |  | 
        self.driver.find_element(By.CSS_SELECTOR, "#optionId_languageListOptionsLisId_131 > .button_label").click()
        time.sleep(5)
        # 11 | click | css=#languageListTriggerId_83 .dropdown_trigger_value |  | 
        self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_83 .dropdown_trigger_value").click()
        time.sleep(5)
        # 12 | click | css=#optionId_languageListOptionsLisId_392 > .button_label |  | 
        self.driver.find_element(By.CSS_SELECTOR, "#optionId_languageListOptionsLisId_392 > .button_label").click()
        time.sleep(5)
        # 13 | mouseOver | id=init-page-loader |  | 
        element = self.driver.find_element(By.ID, "init-page-loader")
        actions = ActionChains(self.driver)



if __name__ == "__main__":
    unittest.main()

  
