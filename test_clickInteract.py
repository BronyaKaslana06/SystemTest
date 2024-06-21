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

class TestClickInteract():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_clickInteract(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
    self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .planetNameContainer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card-title").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input").send_keys("这是一条评论")
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--large > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".one-comment:nth-child(2) a:nth-child(2)").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[5]/div[2]/div[2]/div/div/textarea").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[5]/div[2]/div[2]/div/div/textarea").send_keys("这是评论的回复")
    self.driver.find_element(By.CSS_SELECTOR, ".reply_post_button span").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2)").click()
  
