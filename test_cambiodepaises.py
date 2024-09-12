# Generated by Selenium IDE
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

class TestCambiodepaises():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cambiodepaises(self):
    self.driver.get("https://www.avianca.com/es/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.CSS_SELECTOR, "#pointOfSaleSelectorId > .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_list_item:nth-child(10) .points-of-sale_list_item_label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_footer_action_button > .button_label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button_label:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_list_item:nth-child(5) .points-of-sale_list_item_label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".points-of-sale_footer_action_button > .button_label").click()
  
