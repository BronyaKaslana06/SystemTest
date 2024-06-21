# Generated by Selenium IDE
import unittest

import pytest
import time
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import BeautifulReport
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_loginRegister(self):
        """
        测试登录和注册功能
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(830, 816)
        self.driver.find_element(By.CSS_SELECTOR, ".change-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("LitaZ")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(4)").send_keys("2268920184@qq.com")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(6)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(6)").send_keys("15166217302")
        self.driver.find_element(By.CSS_SELECTOR, ".el-check-tag:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".tag-wrapper").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-check-tag:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-check-tag:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()


def click_element(driver, selector, by=By.CSS_SELECTOR, timeout=20):
    try:
        # 等待元素可点击
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        # 滚动到元素
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # 再次确认元素可点击
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        # 点击元素
        element.click()
    except TimeoutException:
        print(f"Element with selector {selector} could not be clicked within {timeout} seconds.")


def ensure_visibility_and_input(driver, selector, text, by=By.CSS_SELECTOR, timeout=10):
    try:
        # 等待元素可见
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        # 滚动到元素
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # 确保元素再次可见
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        # 发送文本到元素
        element.send_keys(text)
    except TimeoutException:
        print(f"Element with selector {selector} could not be interacted within {timeout} seconds.")


class TestClickInteract(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_clickInteract(self):
        """
        测试与帖子的互动
        """
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
        # self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input").click()
        # self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input").send_keys(
        #     "这是一条评论")
        time.sleep(3)
        click_element(self.driver, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input", By.XPATH)
        time.sleep(3)
        ensure_visibility_and_input(self.driver, "//div[@id=\'app\']/div/main/div[3]/div/div[2]/div/div/input","这是一条评论", By.XPATH)
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--large > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".one-comment:nth-child(2) a:nth-child(2)").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[5]/div[2]/div[2]/div/div/textarea").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/div/main/div[5]/div[2]/div[2]/div/div/textarea").send_keys(
            "这是评论的回复")
        self.driver.find_element(By.CSS_SELECTOR, ".reply_post_button span").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2)").click()
        pass


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_collection(self):
        """
        收藏功能测试
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".imgContainer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".card-list:nth-child(2) .card-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".interaction-button:nth-child(3) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".interaction-button:nth-child(3) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".interaction-button:nth-child(2) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".interaction-button:nth-child(2) img").click()
        pass


class TestFollowOthers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_followOthers(self):
        """
        关注他人功能测试
        """
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
        pass

class TestSearchJoinPlanet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_searchJoinPlanet(self):
        """
        搜索并加入星球测试
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(1)").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/section/section/main/section/header/div/div/div/input").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/section/section/main/section/header/div/div/div/input").send_keys(
            "原神")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(2) .planetNameContainer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--large").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--large")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, "//input").click()
        self.driver.find_element(By.XPATH, "//input").send_keys("111")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
        pass


class TestManageJoin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_manageJoin(self):
        """
        星主处理他人加入星球
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("Hane8ad")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Lll123456")
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .contentContainer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".all_button").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".all_button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//div[3]/div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--success:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2) > span").click()
        pass

class TestPostPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_postPost(self):
        """
        发送帖子
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .contentContainer").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
        # self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/main/div[2]/div/div[3]/div[2]/div/div/input").click()
        # self.driver.find_element(By.XPATH,
        #                          "//div[@id=\'app\']/div/main/div[2]/div/div[3]/div[2]/div/div/input").send_keys("111")
        # self.driver.switch_to.frame(0)
        # self.driver.find_element(By.CSS_SELECTOR, "p").click()
        # element = self.driver.find_element(By.ID, "tinymce")
        # self.driver.execute_script(
        #     "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>222</p>'}", element)
        # self.driver.switch_to.default_content()
        # self.driver.find_element(By.CSS_SELECTOR, ".save-journal span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(1) .planetNameContainer").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element(By.CSS_SELECTOR, ".el-card__body > div > .text-container .card-title").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1)").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--warning")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2) > span").click()
        pass

class TestManagePlanet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_managePlanet(self):
        """
        星主管理星球成员
        """
        self.driver.get("http://localhost:8080/")
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(1)").send_keys("ccr1")
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input-box:nth-child(2)").send_keys("Ccr030323!")
        self.driver.find_element(By.CSS_SELECTOR, ".button-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nav-menu-item:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-card:nth-child(2) .contentContainer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".card-title").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1)").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(1)")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        pass


class TestResource(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_resource(self):
        """
        资源管理操作
        """
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
        actions.move_to_element(element).perform()
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
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    print("TestLoginRegister")
    suite.addTests(loader.loadTestsFromTestCase(TestLoginRegister))
    print("TestClickInteract")
    suite.addTests(loader.loadTestsFromTestCase(TestClickInteract))
    print("TestSearchJoinPlanet")
    suite.addTests(loader.loadTestsFromTestCase(TestSearchJoinPlanet))
    print("TestManageJoin")
    suite.addTests(loader.loadTestsFromTestCase(TestManageJoin))
    print("TestCollection")
    suite.addTests(loader.loadTestsFromTestCase(TestCollection))
    print("TestManagePlanet")
    suite.addTests(loader.loadTestsFromTestCase(TestManagePlanet))
    print("TestPostPost")
    suite.addTests(loader.loadTestsFromTestCase(TestPostPost))
    print("TestFollowOthers")
    suite.addTests(loader.loadTestsFromTestCase(TestFollowOthers))
    print("TestResource")
    suite.addTests(loader.loadTestsFromTestCase(TestResource))

    # 你可以继续添加更多的测试类

    result = BeautifulReport.BeautifulReport(suite)
    result.report(filename='integrationReport.html', description='ClassmateGalaxy系统测试报告', log_path='.',report_dir='.')