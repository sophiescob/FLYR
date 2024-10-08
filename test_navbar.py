import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNavbar():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_navbar(self):
    self.driver.get("https://nuxqa6.avtest.ink/es/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.CSS_SELECTOR, ".main-header_nav-primary_item:nth-child(5) .button_label").click()
    time.sleep(5)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#primary-nav-sub-menu-4 .main-header_primary-nav_submenu_item:nth-child(3) .link_label").click()
    time.sleep(5)
    self.vars["win7059"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win7059"])
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, ".main-header_nav-primary_item--section-booking .button_label").click()
    time.sleep(5)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#primary-nav-sub-menu-2 .main-header_primary-nav_submenu_item:nth-child(1) .link_label").click()
    time.sleep(5)
    self.vars["win4830"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win4830"])
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, ".main-header_nav-primary_item--section-info .button_label").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".main-header_nav-primary_item--section-info .button_label").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, "#primary-nav-sub-menu-3 .main-header_primary-nav_submenu_item:nth-child(7) .link_label").click()
    time.sleep(5)
  
  
if __name__ == "__main__":
    unittest.main()

