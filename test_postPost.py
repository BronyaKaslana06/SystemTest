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

class TestPostPost():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_postPost(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
    self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .contentContainer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[2]/div/div[3]/div[2]/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[2]/div/div[3]/div[2]/div/div/input").send_keys("111")
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>222</p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".save-journal span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .planetNameContainer").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".el-card__body > div > .text-container .card-title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2) > span").click()
  
