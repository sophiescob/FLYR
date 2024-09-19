from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://www.avianca.com/es/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.CSS_SELECTOR, "#languageListTriggerId_22 .dropdown_trigger_value").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, "#optionId_languageListOptionsLisId_753 > .button_label").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "journeytypeId_1").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "originStationSelected").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, "#originDiv > .control_field_input").send_keys("mani")
    self.driver.find_element(By.CSS_SELECTOR, "#MZL > .station-control-list_item_link-country").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, "#MZL > .station-control-list_item_link-country")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".control_field-inbound .control_field_input").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".control_field-inbound .control_field_input").send_keys("bogo")
    self.driver.find_element(By.ID, "BOG").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".ngb-dp-month:nth-child(1) .ngb-dp-week:nth-child(6) > .ngb-dp-day:nth-child(2) .custom-day_day").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, ".ui-overlay")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".pax-control_selector_item:nth-child(2) .plus").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".pax-control_selector_item:nth-child(3) .plus").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".pax-control_selector_item:nth-child(4) .plus").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".control_options_selector_action_button > .button_label").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, "ibe-page page-journey-selection has-summary").click()
    time.sleep(5)


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()

