from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class TestCambiodepaises(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def Test_cambiodepaises(self):
        self.driver.get("https://nuxqa6.avtest.ink/es/")
        time.sleep(6)
        self.driver.set_window_size(1936, 1056)
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#pointOfSaleSelectorId > .icon").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_list_item:nth-child(10) .points-of-sale_list_item_label").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_footer_action_button > .button_label").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".button_label:nth-child(2)").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_list_item:nth-child(5) .points-of-sale_list_item_label").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_footer_action_button > .button_label").click()
        time.sleep(5)
  
    

if __name__ == "__main__":
    unittest.main()
  
    

