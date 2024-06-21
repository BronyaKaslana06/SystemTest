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

class TestResource():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_resource(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
    self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".imgSize").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-menu-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.XPATH, "//input").click()
    self.driver.find_element(By.XPATH, "//input").send_keys("这是111")
    self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer > .el-button--primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer > .el-button:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card-title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".downloadButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".main_resource_info").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--small > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--small > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
  
