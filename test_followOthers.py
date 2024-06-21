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

class TestFollowOthers():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_followOthers(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
    self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".personal-page-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fol").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-avatar > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".follower-name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--small").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
  